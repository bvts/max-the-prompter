# Security Policy

## Scope

Max Prompter is primarily a collection of Markdown-based agent skills and routing guidance. It does not require a network service, database, or production runtime by itself.

Security reports are still welcome for issues such as:

- instructions that could cause an agent to expose secrets or sensitive files;
- unsafe default automation behavior;
- malicious command execution patterns introduced into the skill pack;
- dependency or supply-chain problems in repository tooling;
- prompt-injection weaknesses in shipped reference material that could materially affect agent safety.

## Reporting

For a sensitive issue, contact the repository maintainers through the private security-reporting mechanism configured on the GitHub repository. Do not publish exploitable details in a public issue before maintainers have had a chance to assess them.

## Safe usage

Agents should verify workspace boundaries, avoid leaking secrets, respect permission systems, and never claim that an operation was completed without verification. Max Prompter intentionally treats source truth, explicit constraints, and verification as first-class requirements.
