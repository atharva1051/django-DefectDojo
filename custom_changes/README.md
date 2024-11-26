# Custom Changes Documentation

## 1. Product Type org_id Field Addition

### Description
Added an organization identifier field to the Product_Type model to support organization-specific product type tracking.

### Changes Made
1. **Model Change** (`dojo/models.py`):
```python
# Added to Product_Type model
org_id = models.IntegerField(
    null=True, 
    blank=True, 
    help_text=_("Organization identifier for the product type")
)
```

2. **Migration File** (`dojo/db_migrations/0219_product_type_org_id.py`):
- Adds the org_id field to the Product_Type model
- Migration is automatically created using `python manage.py makemigrations`

### API Impact
- The field is automatically available through the API due to `fields = "__all__"` in ProductTypeSerializer
- Can be used in API operations:
  - GET /api/v2/product_types/?org_id=12345
  - POST /api/v2/product_types/ with {"org_id": 12345}
  - PUT /api/v2/product_types/{id}/ with {"org_id": 12345}

### Upgrade Instructions
When upgrading DefectDojo to a newer version:

1. Backup your database
2. Before running migrations in the new version, either:
   
   **Option A: Using the patch file**
   ```bash
   # Navigate to the DefectDojo root directory
   cd path/to/defectdojo
   
   # Apply the patch
   git apply custom_changes/org_id_changes.patch
   ```
   
   **Option B: Manual changes**
   - Reapply the org_id field to models.py
   - Copy the migration file to the new installation's migrations directory

3. Proceed with the normal upgrade process

### Version Information
- Original Implementation Date: [Current Date]
- DefectDojo Version at Implementation: [Your Current Version]
