# AuthSessions

Types:

```python
from conductor.types import AuthSession
```

Methods:

- <code title="post /auth-sessions">client.auth_sessions.<a href="./src/conductor/resources/auth_sessions.py">create</a>(\*\*<a href="src/conductor/types/auth_session_create_params.py">params</a>) -> <a href="./src/conductor/types/auth_session.py">AuthSession</a></code>
- <code title="get /auth-sessions/:id">client.auth_sessions.<a href="./src/conductor/resources/auth_sessions.py">retrieve</a>() -> <a href="./src/conductor/types/auth_session.py">AuthSession</a></code>

# EndUsers

Types:

```python
from conductor.types import (
    EndUser,
    EndUserListResponse,
    EndUserPingResponse,
    EndUserRequestResponse,
)
```

Methods:

- <code title="post /end-users">client.end_users.<a href="./src/conductor/resources/end_users.py">create</a>(\*\*<a href="src/conductor/types/end_user_create_params.py">params</a>) -> <a href="./src/conductor/types/end_user.py">EndUser</a></code>
- <code title="get /end-users/:id">client.end_users.<a href="./src/conductor/resources/end_users.py">retrieve</a>() -> <a href="./src/conductor/types/end_user.py">EndUser</a></code>
- <code title="get /end-users">client.end_users.<a href="./src/conductor/resources/end_users.py">list</a>() -> <a href="./src/conductor/types/end_user_list_response.py">EndUserListResponse</a></code>
- <code title="get /end-users/:id/ping/:integrationSlug">client.end_users.<a href="./src/conductor/resources/end_users.py">ping</a>() -> <a href="./src/conductor/types/end_user_ping_response.py">EndUserPingResponse</a></code>
- <code title="post /end-users/:id/request/:integrationSlug">client.end_users.<a href="./src/conductor/resources/end_users.py">request</a>(\*\*<a href="src/conductor/types/end_user_request_params.py">params</a>) -> <a href="./src/conductor/types/end_user_request_response.py">object</a></code>

# IntegrationConnections

Types:

```python
from conductor.types import IntegrationConnection, IntegrationConnectionListResponse
```

Methods:

- <code title="get /integration-connections/:id">client.integration_connections.<a href="./src/conductor/resources/integration_connections.py">retrieve</a>() -> <a href="./src/conductor/types/integration_connection.py">IntegrationConnection</a></code>
- <code title="get /integration-connections">client.integration_connections.<a href="./src/conductor/resources/integration_connections.py">list</a>() -> <a href="./src/conductor/types/integration_connection_list_response.py">IntegrationConnectionListResponse</a></code>

# QuickbooksDesktop

## Accounts

Types:

```python
from conductor.types.quickbooks_desktop import QbdAccount, AccountListResponse
```

Methods:

- <code title="post /quickbooks-desktop/accounts">client.quickbooks_desktop.accounts.<a href="./src/conductor/resources/quickbooks_desktop/accounts.py">create</a>(\*\*<a href="src/conductor/types/quickbooks_desktop/account_create_params.py">params</a>) -> <a href="./src/conductor/types/quickbooks_desktop/qbd_account.py">QbdAccount</a></code>
- <code title="get /quickbooks-desktop/accounts">client.quickbooks_desktop.accounts.<a href="./src/conductor/resources/quickbooks_desktop/accounts.py">list</a>(\*\*<a href="src/conductor/types/quickbooks_desktop/account_list_params.py">params</a>) -> <a href="./src/conductor/types/quickbooks_desktop/account_list_response.py">AccountListResponse</a></code>

## Bills

Types:

```python
from conductor.types.quickbooks_desktop import QbdBill, BillListResponse
```

Methods:

- <code title="post /quickbooks-desktop/bills">client.quickbooks_desktop.bills.<a href="./src/conductor/resources/quickbooks_desktop/bills.py">create</a>(\*\*<a href="src/conductor/types/quickbooks_desktop/bill_create_params.py">params</a>) -> <a href="./src/conductor/types/quickbooks_desktop/qbd_bill.py">QbdBill</a></code>
- <code title="get /quickbooks-desktop/bills">client.quickbooks_desktop.bills.<a href="./src/conductor/resources/quickbooks_desktop/bills.py">list</a>(\*\*<a href="src/conductor/types/quickbooks_desktop/bill_list_params.py">params</a>) -> <a href="./src/conductor/types/quickbooks_desktop/bill_list_response.py">BillListResponse</a></code>

## Classes

Types:

```python
from conductor.types.quickbooks_desktop import QbdClass, ClassListResponse
```

Methods:

- <code title="post /quickbooks-desktop/classes">client.quickbooks_desktop.classes.<a href="./src/conductor/resources/quickbooks_desktop/classes.py">create</a>(\*\*<a href="src/conductor/types/quickbooks_desktop/class_create_params.py">params</a>) -> <a href="./src/conductor/types/quickbooks_desktop/qbd_class.py">QbdClass</a></code>
- <code title="get /quickbooks-desktop/classes">client.quickbooks_desktop.classes.<a href="./src/conductor/resources/quickbooks_desktop/classes.py">list</a>(\*\*<a href="src/conductor/types/quickbooks_desktop/class_list_params.py">params</a>) -> <a href="./src/conductor/types/quickbooks_desktop/class_list_response.py">ClassListResponse</a></code>

## CreditCardCharges

Types:

```python
from conductor.types.quickbooks_desktop import QbdCreditCardCharge, CreditCardChargeListResponse
```

Methods:

- <code title="post /quickbooks-desktop/credit-card-charges">client.quickbooks_desktop.credit_card_charges.<a href="./src/conductor/resources/quickbooks_desktop/credit_card_charges.py">create</a>(\*\*<a href="src/conductor/types/quickbooks_desktop/credit_card_charge_create_params.py">params</a>) -> <a href="./src/conductor/types/quickbooks_desktop/qbd_credit_card_charge.py">QbdCreditCardCharge</a></code>
- <code title="get /quickbooks-desktop/credit-card-charges">client.quickbooks_desktop.credit_card_charges.<a href="./src/conductor/resources/quickbooks_desktop/credit_card_charges.py">list</a>(\*\*<a href="src/conductor/types/quickbooks_desktop/credit_card_charge_list_params.py">params</a>) -> <a href="./src/conductor/types/quickbooks_desktop/credit_card_charge_list_response.py">CreditCardChargeListResponse</a></code>

## Customers

Types:

```python
from conductor.types.quickbooks_desktop import QbdCustomer, CustomerListResponse
```

Methods:

- <code title="post /quickbooks-desktop/customers">client.quickbooks_desktop.customers.<a href="./src/conductor/resources/quickbooks_desktop/customers.py">create</a>(\*\*<a href="src/conductor/types/quickbooks_desktop/customer_create_params.py">params</a>) -> <a href="./src/conductor/types/quickbooks_desktop/qbd_customer.py">QbdCustomer</a></code>
- <code title="get /quickbooks-desktop/customers">client.quickbooks_desktop.customers.<a href="./src/conductor/resources/quickbooks_desktop/customers.py">list</a>(\*\*<a href="src/conductor/types/quickbooks_desktop/customer_list_params.py">params</a>) -> <a href="./src/conductor/types/quickbooks_desktop/customer_list_response.py">CustomerListResponse</a></code>

## Invoices

Types:

```python
from conductor.types.quickbooks_desktop import QbdInvoice, InvoiceListResponse
```

Methods:

- <code title="post /quickbooks-desktop/invoices">client.quickbooks_desktop.invoices.<a href="./src/conductor/resources/quickbooks_desktop/invoices.py">create</a>(\*\*<a href="src/conductor/types/quickbooks_desktop/invoice_create_params.py">params</a>) -> <a href="./src/conductor/types/quickbooks_desktop/qbd_invoice.py">QbdInvoice</a></code>
- <code title="get /quickbooks-desktop/invoices">client.quickbooks_desktop.invoices.<a href="./src/conductor/resources/quickbooks_desktop/invoices.py">list</a>(\*\*<a href="src/conductor/types/quickbooks_desktop/invoice_list_params.py">params</a>) -> <a href="./src/conductor/types/quickbooks_desktop/invoice_list_response.py">InvoiceListResponse</a></code>

## Vendors

Types:

```python
from conductor.types.quickbooks_desktop import QbdVendor, VendorListResponse
```

Methods:

- <code title="post /quickbooks-desktop/vendors">client.quickbooks_desktop.vendors.<a href="./src/conductor/resources/quickbooks_desktop/vendors.py">create</a>(\*\*<a href="src/conductor/types/quickbooks_desktop/vendor_create_params.py">params</a>) -> <a href="./src/conductor/types/quickbooks_desktop/qbd_vendor.py">QbdVendor</a></code>
- <code title="get /quickbooks-desktop/vendors">client.quickbooks_desktop.vendors.<a href="./src/conductor/resources/quickbooks_desktop/vendors.py">list</a>(\*\*<a href="src/conductor/types/quickbooks_desktop/vendor_list_params.py">params</a>) -> <a href="./src/conductor/types/quickbooks_desktop/vendor_list_response.py">VendorListResponse</a></code>
