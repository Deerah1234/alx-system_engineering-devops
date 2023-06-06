# Incident Analysis

![Conducting a retrospective](post-mortem-meetings.jpg)

## Summary

Following the release of a new feature on our Ruby on Rails site, we received multiple user complaints about login and sign-up issues. This came as a surprise since the feature had worked during testing. We received 127 emails reporting the problem, which highlighted the urgency to investigate and address the issue promptly. After cloning the site's repository from GitBug and following the installation instructions, we discovered that the site failed to start. Eventually, we identified the cause as an oversight in updating the project's requirements. The site experienced malfunctions from 9:55 AM GMT+1 to 11:20 AM GMT+1.

## Timeline

+ 05-02-2022 9:55 AM GMT+1 - Initial complaint received from a customer regarding login issues.
+ 05-02-2022 10:20 AM GMT+1 - Winus, one of our backend developers, encountered the same issue.
+ 05-02-2022 10:35 AM GMT+1 - Investigation conducted on controllers and views for inconsistencies.
+ 05-02-2022 10:40 AM GMT+1 - Suspected the bcrypt gem, a dependency, as the potential cause due to an error message involving an invalid hash.
+ 05-02-2022 10:42 AM GMT+1 - Checked the views for potential binding issues but found no evidence.
+ 05-02-2022 10:45 AM GMT+1 - Considered the possibility of the controllers generating a different hash for a valid admin password.
+ 05-02-2022 10:50 AM GMT+1 - Winus speculated that the problem could be related to incorrect password hashing.
+ 05-02-2022 11:00 AM GMT+1 - Incident escalated to the backend development team.
+ 05-02-2022 11:20 AM GMT+1 - Issue resolved by updating the backend server's requirements, specifically the bcrypt gem version.

## Root Cause and Resolution

The issue stemmed from using an outdated version of the bcrypt gem. This version raised an error despite the hash being valid and matching the database records. It is likely that the hash generated was not compatible with the installed bcrypt version. Winus resolved the problem by manually updating the bcrypt version in the Gemfile.lock file, followed by reinstalling the required gems. The solution proved effective.

## Corrective and Preventive Measures

+ Establish a continuous integration pipeline to conduct builds on each pull request branch. This ensures that builds pass in the pull request branch before merging with the deployment branch.
+ Implement a monitoring system for the database and application servers to promptly detect and address any issues.
+ Develop comprehensive tests for new features, ensuring they pass before merging with the deployment branch.
