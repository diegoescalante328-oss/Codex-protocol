# Security Rules

## Safe-by-Default Policy
Prefer designs and implementation choices that reduce blast radius, privilege, and irreversible side effects.

## No Secrets in Repository
- Never commit keys, tokens, passwords, certificates, or private keys.
- Use environment variables or approved secret managers.
- If secret exposure is suspected, stop and report immediately.

## Least Privilege Mindset
- Use minimum permissions required for each action.
- Avoid broad filesystem, shell, network, or auth access when narrower options exist.

## Sensitive Surface Handling
Apply extra care when touching:
- authentication/authorization flows
- token/session handling
- file operations (especially destructive actions)
- shell command execution and input interpolation
- network calls and external integrations
- data movement, storage, and retention

## External Input Rules
- Treat all external input as untrusted.
- Validate format, type, range, and allowed values.
- Sanitize output where user-controlled content is rendered.

## Final Handoff Security Note
When sensitive surfaces are changed, include a dedicated security note in Handoff covering:
- what changed
- risk assessment summary
- security-relevant validations performed
- remaining cautions and follow-up actions
