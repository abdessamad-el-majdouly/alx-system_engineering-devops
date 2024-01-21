Postmortem Report
Following the release of ALX's System Engineering & DevOps project 0x19 at approximately 06:00 GMT+1 in Morocco, an outage occurred on an isolated Ubuntu container running an Apache web server. GET requests on the server resulted in 500 Internal Server Errors, rather than the expected response of an HTML file defining a simple Holberton WordPress site.

Debugging Process
Bamidele, also known as Lexxyla (derived from actual initials), identified the issue at around 19:20 PST and promptly initiated the debugging process.

Checked running processes using ps aux. Confirmed that two apache2 processes - root and www-data - were running correctly.

Examined the sites-available folder in the /etc/apache2/ directory and determined that the web server was serving content from /var/www/html/.

Ran strace on the PID of the root Apache process in one terminal and curled the server in another. Unfortunately, strace yielded no useful information.

Repeated step 3 on the PID of the www-data process. This time, strace revealed an -1 ENOENT (No such file or directory) error when attempting to access the file /var/www/html/wp-includes/class-wp-locale.phpp.

Scanned files in the /var/www/html/ directory using Vim pattern matching to locate the erroneous .phpp file extension. Discovered it in the wp-settings.php file (Line 137, require_once( ABSPATH . WPINC . '/class-wp-locale.php' );).

Removed the trailing p from the line.

Tested another curl on the server. Success - received a 200 response.

Created a Puppet manifest to automate the fix for this error.

Summary
In essence, the issue stemmed from a typo. The WordPress app encountered a critical error in wp-settings.php when trying to load the file class-wp-locale.phpp. The correct file name, located in the wp-content directory of the application folder, was class-wp-locale.php. The fix involved removing the trailing p.

Prevention
This outage was not a web server error but an application error. To avoid similar outages in the future, consider the following:

Testing: Thoroughly test the application before deployment to catch errors early.

Status Monitoring: Implement an uptime-monitoring service, such as UptimeRobot, to receive instant alerts upon website outage.

Note: In response to this error, a Puppet manifest [0-strace_is_your_friend.pp] was created to automate fixing identical errors. The manifest replaces any phpp extensions in the file /var/www/html/wp-settings.php with php. However, the expectation is that such errors will not recur, given our commitment to error-free coding! :wink:
