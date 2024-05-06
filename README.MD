# Django REST-API Project

## Requirements

The requirements to run the projects are given inside `requirements.txt`. To install, run the following command inside the project directory:

```
pip install -r requirements.txt

```

## URL Patterns

The URL patterns are given below. Additionally, I've added the URL details in the `home.html` page, which will be visible at the URL `http://127.0.0.1:8000/` once the project is run.

### Vendor Management

- **List all vendors**: `/api/vendors/`
- **Create a new vendor**: `/api/vendors/create/`
- **Retrieve a specific vendor's details**: `/api/vendors/<vendor_id>/`
- **Update a vendor**: `/api/vendors/<vendor_id>/update/`
- **Delete a specific vendor**: `/api/vendors/<vendor_id>/delete/`

### Purchase Order Management

- **Create a purchase history**: `/api/purchase_orders/create/`
- **List Purchase orders**: `/api/purchase_orders/`
- **List purchase orders by vendor id**: `/api/purchase_orders/?vendor_id="id"`
- **Get specific purchase order based on po_number**: `/api/purchase_orders/<po_number>/`
- **Update purchase order based on po_number**: `/api/purchase_orders/<po_number>/update/`
- **Delete purchase order based on po_number**: `/api/purchase_orders/<po_number>/delete/`

### Vendor Performance

- **Get performance history by vendor id**: `/api/vendors/<vendor_id>/performance/`

## JSON Input Examples

### Create Vendor

```json
{
    "name": "XYZ Corporation",
    "contact_details": "987-654-3210",
    "address": "456 Oak Avenue, Town, Country",
    "vendor_code": "VENDOR002"
}
```

To create a new vendor, send a POST request to the URL `http://127.0.0.1:8000/api/vendors/create`.

### Create Purchase Order

```json
{
    "po_number": "P001",
    "vendor": "id of the vendor for which you are creating the order (e.g., 1)",
    "order_date": "2023-04-15T12:00:00Z",
    "delivery_date": "2023-04-30T12:00:00Z",
    "items": {
        "product1": {
            "name": "Product 1",
            "price": 10.99,
            "quantity": 2
        },
        "product2": {
            "name": "Product 2",
            "price": 15.50,
            "quantity": 1
        }
    },
    "quantity": 3,
    "status": "pending",
    "issue_date": "2023-04-15T12:00:00Z"
}
```

To create a new purchase order, send a POST request to the URL `http://127.0.0.1:8000/api/purchase_orders/create`.

### Update Purchase Order

```json
{
    "po_number": "P001",
    "vendor": "id of the vendor for which you are creating the order (e.g., 1)",
    "order_date": "2023-04-15T12:00:00Z",
    "delivery_date": "2023-04-30T12:00:00Z",
    "items": {
        "product1": {
            "name": "Product 1",
            "price": 10.99,
            "quantity": 2
        },
        "product2": {
            "name": "Product 2",
            "price": 15.50,
            "quantity": 1
        }
    },
    "quantity": 3,
    "status": "completed",
    "issue_date": "2023-04-15T12:00:00Z"
}
```

To update an existing purchase order, send a PUT request to the URL `http://127.0.0.1:8000/api/purchase_orders/PO1/update/`. Replace `P001` with the actual `po_number` of the purchase order you want to update.

## Vendor Performance Metrics

- **Average Response Time**: The average response time is calculated in seconds. To find the days, divide the average response time by 86400.

- **Fulfillment Rate**: The fulfillment rate is calculated by dividing the count of successfully fulfilled orders by the total count of orders. If there are no orders, the rate is set to 0.0. If all orders are fulfilled, the rate will be 1.00. If some of the orders are not fulfilled, the rate would be below 1.00.

- **On-Time Delivery Rate**: The on-time delivery rate is calculated by dividing the count of on-time completed orders by the total count of completed orders. If all the orders are delivered before the expected time, the rate would be set to 1.00.

- **Quality Rating Average**: The function filters the purchase orders to get the completed orders that have a non-null quality rating. It then calculates the average of the quality ratings for these completed orders using the `aggregate(Avg('quality_rating'))` method. If there are no quality ratings, the average is set to 0.00.
 
