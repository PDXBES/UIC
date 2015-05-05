<h2>Production Well Table Description</h2>

## Identification Information ##
_**file name:**_ well update.jrl<p>
<i><b>Written by:</b></i> Neil Revello<p>
<i><b>Purpose:</b></i> Well Update for Permit Renewal 2014<p>
<h2>Well Use</h2>
<table><thead><th>UseID</th><th>Description</th><th>Reported</th></thead><tbody>
<tr><td>00</td><td>No Data</td><td>No</td></tr>
<tr><td>10</td><td><i><b>Drinking Water Classification</b></i></td></tr>
<tr><td>11</td><td>Domestic</td><td>Yes</td></tr>
<tr><td>12</td><td>Domestic - Irrigation</td><td>Yes</td></tr>
<tr><td>13</td><td>Domestic - Commerical</td><td>Yes</td></tr>
<tr><td>14</td><td>Domestic - Irrigation - Commerical / Industrial</td><td>Yes</td></tr>
<tr><td>20</td><td><i><b>Irrigationrigation Classification</b></i></td></tr>
<tr><td>21</td><td>Irrigation</td><td>Yes</td></tr>
<tr><td>22</td><td>Irrigation - Commerical / Industrial</td><td>Yes</td></tr>
<tr><td>30</td><td><i><b>Commercial - Industrial</b></i></td></tr>
<tr><td>31</td><td>Commerical / Industrial</td><td>Yes</td></tr>
<tr><td>40</td><td><i><b>Well use is unknown</b></i></td></tr>
<tr><td>41</td><td>Unknown - None - No Use Marked (all Catagories)</td><td>Yes</td></tr>
<tr><td>50</td><td><i><b>Community - Municipal (Public)</b></i></td></tr>
<tr><td>51</td><td>Public Water Well</td><td>Yes</td></tr>
<tr><td>60</td><td><i><b>Non Used for reporting</b></i></td></tr>
<tr><td>61</td><td>piezometer (only)</td><td>No</td></tr>
<tr><td>62</td><td>Thermal (only)</td><td>No</td></tr>
<tr><td>63</td><td>Livestock (only)</td><td>No</td></tr>
<tr><td>64</td><td>Dewatering (only)</td><td>No</td></tr>
<tr><td>65</td><td>Injection</td><td>No</td></tr>
<tr><td>66</td><td>Other</td><td>No</td></tr></tbody></table>

<b>LUT Name:</b> Lookup_WellUse_Code<br>
<table><thead><th>UseID</th><th>Description</th><th>Reported</th></thead><tbody>
<tr><td>00</td><td>No Data</td><td>No</td></tr>
<tr><td><i>10</i></td><td><i><b>Drinking Water Classification</b></i></td></tr>
<tr><td>11</td><td>DW</td><td>Yes</td></tr>
<tr><td>12</td><td>DW - IR</td><td>Yes</td></tr>
<tr><td>13</td><td>DW - CM</td><td>Yes</td></tr>
<tr><td>14</td><td>DW - IR - CM</td><td>Yes</td></tr>
<tr><td>20</td><td><i><b>Irrigation Classification</b></i></td></tr>
<tr><td>21</td><td>IR</td><td>Yes</td></tr>
<tr><td>22</td><td>IR - CM</td><td>Yes</td></tr>
<tr><td>30</td><td><i><b>Commercial / Industrial</b></i></td></tr>
<tr><td>31</td><td>CM</td><td>Yes</td></tr>
<tr><td>40</td><td><i><b>Well use is unknown</b></i></td></tr>
<tr><td>41</td><td>Unknown - None - No Use Marked (all Catagories)</td><td>Yes</td></tr>
<tr><td>50</td><td><i><b>Community - Municipal (Public)</b></i></td></tr>
<tr><td>51</td><td>PW</td><td>Yes</td></tr>
<tr><td>60</td><td><i><b>Non Used for reporting</b></i></td></tr>
<tr><td>61</td><td>piezometer (only)</td><td>No</td></tr>
<tr><td>62</td><td>Thermal (only)</td><td>No</td></tr>
<tr><td>63</td><td>Livestock (only)</td><td>No</td></tr>
<tr><td>64</td><td>Dewatering (only)</td><td>No</td></tr>
<tr><td>65</td><td>Injection</td><td>No</td></tr>
<tr><td>66</td><td>Use_Other<div>Test - Observation - Monitoring<div>Extraction - Heat Pump - LTGT<div>Ground Bed - Dust control - Dry Well</td><td>No</td></tr></tbody></table>



<h2>Operation Status</h2>
<table><thead><th>StatusID</th><th>Description</th></thead><tbody>
<tr><td>00</td><td>No Data</td></tr>
<tr><td>10</td><td><i><b>ACT - Active</b></i></td></tr>
<tr><td>11</td><td>ACT - OWRD</td></tr>
<tr><td>12</td><td>ACT - PWB</td></tr>
<tr><td>20</td><td><i><b>ABN - Abondoned</b></i></td></tr>
<tr><td>21</td><td>ABN - OWRD</td></tr>
<tr><td>22</td><td>ABN - PWD</td></tr>
<tr><td>30</td><td><i><b>NIS - Not in Service (Reporting)</b></i></td></tr>
<tr><td>31</td><td>NIS - OWRD</td></tr>
<tr><td>32</td><td>NIS - PWB</td></tr>
<tr><td>40</td><td><i><b>NOR - Non reporting Use type (Status does not matter)</b></i></td></tr>
<tr><td>41</td><td>NOR - OWRD</td></tr>
<tr><td>42</td><td>NOR - PWB</td></tr></tbody></table>

<h2>CoordInfo</h2>
<table><thead><th>coordID</th><th>Description</th></thead><tbody>
<tr><td>00</td><td>No Data</td></tr>
<tr><td>01</td><td>Latitude & Longitude</td></tr>
<tr><td>02</td><td>Spatial Location</td></tr>
<tr><td>03</td><td>TRS</td></tr></tbody></table>



<b>LUT Name:</b> Lookup_WellUse_Code<br>
<table><thead><th> Code </th><th> Description         </th></thead><tbody>
<tr><td>  00  </td><td> Unknown             </td></tr>
<tr><td>  01  </td><td> Domestic            </td></tr>
<tr><td>  02  </td><td> Irrigation          </td></tr>
<tr><td>  03  </td><td> Public or Community </td></tr>
<tr><td>  04  </td><td> Industrial          </td></tr>
<tr><td>  05  </td><td> Injection           </td></tr>
<tr><td>  06  </td><td> Thermal             </td></tr>
<tr><td>  07  </td><td> Livestock           </td></tr>