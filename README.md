# SMARS
#Architecture
## Apache2 web server
* install mod_python. - this didn't work well because of python2 vs python3 problems.  As a result python cgi was REALLY slow.
* installed mod_php instead.

#Debug Settings

in file `/home/pi/.local/lib/python3.5/site-packages/pydevd_file_utils.py`

```python
PATHS_FROM_ECLIPSE_TO_PYTHON = [
  [r'/home/doug/rpi_eclipse/SMARS/cgi-bin', r'/usr/lib/cgi-bin'],
  [r'/home/doug/rpi_eclipse/SMARS/SMARS', r'/home/pi/SMARS']
 ]

