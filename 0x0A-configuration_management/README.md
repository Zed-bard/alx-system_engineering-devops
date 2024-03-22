```markdown
# Skynet Auto-Remediation Tool

## Background Context

During my time at SlideShare, I developed Skynet, an auto-remediation tool designed to monitor, scale, and fix Cloud infrastructure issues. Skynet utilized a parallel job-execution system called MCollective, allowing me to execute commands across one or multiple servers simultaneously. With MCollective, I could apply actions to selected sets of servers based on criteria such as hostname or other metadata.

However, an unfortunate bug in the code caused unexpected behavior. Sending a nil argument to MCollective's filter method resulted in unintended consequences:
- MCollective interpreted nil as a directive to apply the action to all servers.
- The action I initiated was to terminate selected servers.

This bug led to a significant disruption in SlideShare's document conversion environment, with 75% of conversion infrastructure servers being shut down. This resulted in users being unable to convert their documents, including PDFs, PowerPoints, and videos.

Thanks to Puppet, we were able to swiftly restore our infrastructure within an hour. Puppet automated the process of launching servers, configuring them, importing application code, starting processes, and fixing bugs, significantly reducing downtime.

While writing Puppet code requires upfront investment, its benefits in automating and maintaining complex infrastructure are undeniable.

## Resources

Read or watch:
- [Intro to Configuration Management](https://en.wikipedia.org/wiki/Configuration_management)
- [Puppet resource type: file](https://puppet.com/docs/puppet/latest/types/file.html)
- [Puppet’s Declarative Language: Modeling Instead of Scripting](https://puppet.com/docs/puppet/latest/lang_intro.html)
- [Puppet lint](https://puppet.com/docs/puppet/latest/style_guide.html)
- [Puppet emacs mode](https://github.com/voxpupuli/puppet-emacs)

## Requirements

### General
- All files will be interpreted on Ubuntu 20.04 LTS.
- All files should end with a new line.
- A README.md file at the root of the project folder is mandatory.
- Puppet manifests must pass puppet-lint version 2.1.1 without any errors.
- Puppet manifests must run without error.
- Puppet manifests' first line must be a comment explaining what the Puppet manifest is about.
- Puppet manifest files must end with the extension .pp.
```

