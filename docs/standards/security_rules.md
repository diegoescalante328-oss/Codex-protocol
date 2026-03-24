# Security Rules

## No Secrets in Repository
- Never commit API keys, tokens, passwords, certificates, or private keys.
- Use environment variables or secure secret managers.
- If a secret exposure is detected, stop and report immediately.

## Least Privilege Mindset
- Request and use only minimum permissions required.
- Avoid broad access patterns when scoped access is possible.

## Sensitive Operation Discipline
- Auth flows: preserve principle-of-least-privilege and fail-closed behavior.
- File operations: avoid destructive actions without explicit safeguards.
- Shell commands: avoid unsafe interpolation and validate inputs.
- Network behavior: communicate only with required endpoints and protocols.

## External Input Validation
- Treat all external/user/system input as untrusted.
- Validate format, bounds, and allowed values before use.
- Sanitize output when rendering user-controlled content.

## Handoff Security Note Requirement
If sensitive areas are touched (auth, data handling, permissions, filesystem, network, secrets), include a dedicated security note in final handoff covering:
- what sensitive surface changed
- risk assessment summary
- validations performed
- remaining cautions or follow-up actions
