# Fixture Mapping

Use the project's native setup abstraction. The goal is always the same: move meaningful setup out of the test body so the body stays close to pure Act and Assert.

## Common Mappings

- pytest: fixtures
- Vitest: `beforeEach`, factory helpers, custom test context, or `test.extend`
- Jest: `beforeEach`, helper factories, builders, or harness setup
- xUnit-style frameworks: setup methods, test fixtures, builders, or test data objects
- UI and browser testing tools: page objects or helpers only when they support business-level actions rather than leaking implementation detail

## Naming Guidance

Name setup by business context, not by implementation detail.

Prefer:

- `authenticated_admin`
- `expired_subscription`
- `valid_order`
- `missing_invoice_id`

Avoid:

- `mock_repo`
- `service_with_stubbed_gateway`
- `fake_controller_context`

## Translation Rule

Treat "fixture" in this skill as a generic concept:

- reusable setup
- reusable business context
- reusable test data
- reusable harness construction

The exact mechanism depends on the language and framework. The intent does not change.
