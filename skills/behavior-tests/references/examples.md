# Behavior Test Examples

Use these examples to preserve the intent of the skill across languages, frameworks, and test runners.

## Good Targets

- API handlers or endpoints that enforce business rules
- commands that trigger business workflows
- service or use-case entry points with domain meaning
- exported domain functions with business meaning
- repository contracts only when query semantics or persistence behavior are themselves business rules

## Weak Targets

- private helpers
- internal method-call sequences
- exact query-builder chains
- DTO or entity mapping with no business rule
- DOM structure when the real requirement is domain or workflow behavior

## Example 1: Service Behavior

```text
fixture pricing_service
fixture taxable_order

test("calculates tax for a taxable order"):
    result = pricing_service.calculate_total(taxable_order)

    assert result.total == 1200
    assert result.tax == 200
```

Why it is good:

- business rule is clear
- setup is outside the body
- one action
- two assertions that prove the rule

## Example 2: API Behavior

```text
fixture authenticated_client
fixture valid_discount_code

test("applies a discount for an eligible customer"):
    response = authenticated_client.apply_discount(valid_discount_code)

    assert response.status == 200
    assert response.body.discount_percent == 15
```

## Example 3: Contract Error

```text
fixture authenticated_client
fixture expired_coupon

test("rejects an expired coupon"):
    response = authenticated_client.apply_coupon(expired_coupon)

    assert response.status == 400
    assert response.body.error_code == "coupon_expired"
```

## Anti-Pattern: Testing Implementation

Avoid:

```text
test("calls repository.save once"):
    repository = mock()
    service = Service(repository)

    service.create_order(data)

    assert repository.save.called_once
```

Prefer:

```text
fixture order_service
fixture valid_order

test("creates an order from valid input"):
    result = order_service.create_order(valid_order)

    assert result.id is present
    assert result.status == "created"
```

## Anti-Pattern: Technical Mapping

Avoid:

```text
test("maps dto to entity correctly"):
    result = mapper.map(input)

    assert result.id == input.id
    assert result.name == input.name
```

Prefer a behavior test only if that mapping expresses a business rule or public contract that matters outside the implementation.

## Anti-Pattern: Overloaded Test Body

Avoid:

```text
test("full order flow"):
    user = create_user()
    client = make_client(user)
    create_response = client.create_order(valid_payload)
    invoice_response = client.generate_invoice(create_response.body.id)
    cancel_response = client.cancel_order(create_response.body.id)

    assert create_response.status == 201
    assert invoice_response.status == 200
    assert cancel_response.status == 204
```

Prefer separate tests, each with:

- setup in fixtures or helpers
- one action
- 1-2 assertions
