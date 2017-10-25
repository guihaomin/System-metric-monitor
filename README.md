# Run this metric collector
`sudo python logger.py`
> Intervals can be adjusted in logger.py
> Interface and disk name can be specified in logger.py

# Metric information include:
**CPU**
- System CPU Usage
- User CPU Usage
- Load Avg
- Run Queue Length

**Process/Threads**
- Total # Process
- Running Process
- Sleeping Process
- Threads
- Blocked Process

**Memory**
- Used Physical Memory
- Unused Pysical Memory
- swap-in
- swap-out
- page-in
- page-out
- Amount of Swap Space Allocated

**Disk**
- Pysical Disk Read
- Amount of Disk Physical Read
- Pysical Disk Write
- Amount of Disk Physical Write
- Disk Busy Time

**Network**
- Total # Incoming Packages
- Size of Incoming Packages
- Total # Outgoing Packages
- Size of outging packages
- Connections
- Disconnections

# Log 
- **format**
  ```python
  "%s %f %s %d %s %s %s %s" 
    % (name, value, unit, interval, isCumulative, transform, description, host_name)
  ```
- **Important things to know about Metrics Parsing**
  In log, we have a flag about whether a value is a cumulative value.
  For cumulative value, we will calculate the mean value during that `interval`.

# Referance:
package linux-metrics distribution by Corey Goldberg (http://goldb.org)
