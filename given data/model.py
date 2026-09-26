# first table

class ProductOffering(BaseModel, BaseModelUser, BaseModelValidity):
    id = models.CharField(primary_key=True, max_length=20)
    type = models.CharField(max_length=20)
    description = models.CharField(max_length=100, null=True, blank=True)
    is_bundle = models.BooleanField()
    is_sellable = models.BooleanField()
    version = models.IntegerField(unique=True, null=True, blank=True)
    external_identifier = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    life_cycle_status = models.CharField(max_length=20)
    status_reason = models.CharField(max_length=200, null=True, blank=True)
    place_ref = models.CharField(max_length=30, null=True, blank=True)
    sla_ref = models.CharField(max_length=30, null=True, blank=True)
    channel = models.CharField(max_length=30, null=True, blank=True)
    service_candidate_ref = models.CharField(max_length=30, null=True, blank=True)
    resource_candidate_ref = models.CharField(max_length=30, null=True, blank=True)
    product_offering_term_ref = models.CharField(max_length=30, null=True, blank=True)
    agreement_ref = models.CharField(max_length=30, null=True, blank=True)
    market_segment_ref = models.CharField(max_length=30, null=True, blank=True)
    policy_ref = models.CharField(max_length=30, null=True, blank=True)
    allowed_action_ref = models.CharField(max_length=30, null=True, blank=True)
    unit_type = models.CharField(max_length=20, null=True, blank=True)
    hsn_sac_code = models.ForeignKey(
        "HsnSacCodeMaster",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

# second table 

class ProductOfferingPrice(BaseModel, BaseModelUser, BaseModelValidity):
    id = models.CharField(primary_key=True, max_length=20)
    price_type = models.CharField(max_length=20)
    name = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    version = models.IntegerField()
    valid_start_datetime = models.DateTimeField(auto_now_add=True)
    valid_end_datetime = models.DateTimeField(blank=True, null=True)
    quantity_amount = models.IntegerField(blank=True, null=True)
    quantity_unit = models.CharField(max_length=20, blank=True, null=True)
    recurring_charge_period_type = models.ForeignKey(
        RecurringPeriodMaster,
        to_field="recurring_code",
        on_delete=models.CASCADE,
        related_name="recurring_charge_period_type",
    )
    recurring_charge_period_length = models.IntegerField()
    is_bundle = models.BooleanField()
    price_currency = models.ForeignKey("CurrencyMaster", on_delete=models.PROTECT)
    price_value = models.DecimalField(max_digits=13, decimal_places=3)
    percentage_alteration = models.DecimalField(
        max_digits=13, decimal_places=3, null=True, blank=True
    )
    product_offering_term_duration = models.IntegerField(blank=True, null=True)
    place_ref = models.CharField(max_length=20, blank=True, null=True)
    policy_ref = models.CharField(max_length=30, blank=True, null=True)
    pricing_logic_algorithm_ref = models.CharField(max_length=30, blank=True, null=True)
    external_identifier = models.CharField(max_length=30, blank=True, null=True)
    product_offering = models.ForeignKey(ProductOffering, on_delete=models.CASCADE)
    price_without_tax = models.DecimalField(
        max_digits=13, decimal_places=3, null=True, blank=True
    )
    is_price_include_tax = models.BooleanField()
    life_cycle_status = models.CharField(max_length=20)
    tax_scheme_code = models.ForeignKey(
        "TaxSchemeMaster",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        db_column="tax_scheme_code",
    )

# third table 

class ProductOfferingTaxItem(BaseModel, BaseModelUser, UUIDBaseModel):
    product_offering_price = models.ForeignKey(
        "ProductOfferingPrice", on_delete=models.CASCADE
    )
    tax_code = models.ForeignKey("TaxCodeMaster", on_delete=models.CASCADE)
    tax_rate = models.ForeignKey("TaxRateMaster", on_delete=models.CASCADE)
    tax_amount_currency = models.ForeignKey("CurrencyMaster", on_delete=models.PROTECT)
    tax_amount_value = models.DecimalField(max_digits=13, decimal_places=3)
    is_active = models.BooleanField()
 
    class Meta:
        db_table = "product_offering_tax_item"
        indexes = [
            models.Index(
                fields=["product_offering_price", "is_active"],
                name="potax_price_active_idx",
            ),
        ]
 
    def __str__(self):
        return f"price_id={self.product_offering_price})"
 

 # fourth table 


class ProductOfferingBalance(
    UUIDBaseModel, BaseModel, BaseModelUser, BaseModelValidity
):
    product_offering = models.ForeignKey(ProductOffering, on_delete=models.CASCADE)
    balance_type_code = models.ForeignKey(
        BalanceTypeMaster, on_delete=models.CASCADE, db_column="balance_type_code"
    )  # FK-like: BUSINESS/CUSTOMER/INVOICE
    balance_value = (
        models.FloatField()
    )  # Example: FREE plan sets balance_value=1 for BUSINESS, PAID plan sets balance_value=3 for BUSINESS
    balance_reset_period_type = models.CharField(max_length=10)
    balance_reset_period_length = models.IntegerField()  # e.g. 1, 6 — 0 if NONE

# fourth table 


class CharacteristicMaster(BaseModel, BaseModelUser):
    characteristic_code = models.CharField(primary_key=True, max_length=20)
    characteristic_name = models.CharField(max_length=100)
    entity_type = models.CharField(max_length=50)
    characteristic_type = models.CharField(max_length=50)
    characteristic_value_type = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    include_in_invoice = models.BooleanField(default=False)
 
    class Meta:
        db_table = "characteristic_master"
 
    def __str__(self):
        return f"{self.characteristic_code}"

 # sixth table 

 class CategoryMaster(BaseModel, BaseModelUser, BaseModelValidity, UUIDBaseModel):
    name = models.CharField(max_length=30)
    version = models.IntegerField()
    description = models.CharField(max_length=100, null=True, blank=True)
    is_root = models.BooleanField()
    parent_category_id = models.IntegerField(null=True, blank=True)
    life_cycle_status = models.CharField(max_length=20)
    entity_type = models.CharField(max_length=50)
 
    class Meta:
        db_table = "category_master"
 
    def __str__(self):
        return f"{self.name} (version{self.version}) - {self.life_cycle_status}"

    