# Nosq
A vanilla python library used in place of an available NoSQL service

## Why
Some deployment environments work under extremely rigid requirements. An application might not be able to use 
services such as Redis or MongoDB that would help resolve a lot of problems. Python 3.x, however, might be 
available for use.

This should serve as a naive solution for NoSQL operations in a restricted environment and not require a 
running service.

## Target
Nosq is targeted to work on Unix environments with Python 3.6. Windows functionality will be a nice-to-have or a happy accident.

## Requirements

- [ ] Strict CVE Monitoring and Resolution
- [ ] Vanilla Python libraries **only**
- [ ] Focused on optimization - a vanilla implementation **will** be slow. Performance issues must be remedied to the utmost extent. This might require strategies such as possible disk manipulation in order to keep blocked data adjacent
- [ ] Support for old versions of Python, probably 3.6. Restricted environments may be restricted to old OSs, old repos, or old python distributions.

## Wishlist

- [ ] 'Service Mode' - this will be designed to work as a standalone library. A main function to launch it as its own tiny service may help for more distributed applications
- [ ] Lock Management - distributed systems may need to share locks. A common locking mechanism (most likely through the above 'Service Mode') would help steer development from slow or brittle solutions such as file locking on NFS mounts
- [ ] Brokering - work distribution on restricted systems is extremely difficult and requires 'clever' workarounds or lengthy sychronous processing.
If the system already provides features like isolated queues, it may be able to help with passing jobs to interested parties
- [ ] Common Interfaces - interfaces that mimic services such as Redis or MongoDB may allow this library to be dropped in and out as needed.
If a program is expected to work in a restricted and unrestricted environment, being able to use the good tools in the less restricted environments
and this tool in the restricted environment would make it easier to incorporate into workflows with as little code as possible.

### Resources

Despite being targeted for Go, this [Medium article](https://betterprogramming.pub/build-a-nosql-database-from-the-scratch-in-1000-lines-of-code-8ed1c15ed924) might help with providing approaches and ideas for implementation.
