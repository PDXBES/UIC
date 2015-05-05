Variance Table
| gDate | VarType | Document | ProjNumb |
|:------|:--------|:---------|:---------|

Variance Table Structure
| Field | gDate |
|:------|:------|
| Alias | Granted Date|
| Data Type | Date |
| Nulls | No |
| Unique | No |
| Index |  |
| Default Value | No |
| Domain | Real Dates, MMM-YYYY |
| Source |  |
| Description | Date Variance was granted |

| Field | VarType |
|:------|:--------|
| Alias | Variance Type |
| Data Type | int |
| Nulls | No |
| Unique | No |
| Index |  |
| Default Value | 0 |
| Domain | ID - Name     - Description

&lt;DIV&gt;

 1 - SD       - Separation Distance

&lt;DIV&gt;

11 - NSD-Well - Non Separation Distance Wells

&lt;DIV&gt;

12 - NSD-ECSI - Non Separation Distance ECSI

&lt;DIV&gt;

13 - NSD-Wetl - Non Separation Distance Wetland

&lt;DIV&gt;

14 - NSD-SWTR - Non Separation Distance Surface Water

&lt;DIV&gt;

15 - NSD-Traf - Non Separation Distance Traffic

&lt;DIV&gt;

16 - NSD-Zone - Non Separation Distance Zoning

&lt;DIV&gt;

17 - NSD-2TOT - Non Separation Distance Two Year Time of Travel

&lt;DIV&gt;

18 - NSD-NSED - Non Separation Distance Non-Sedimentation Manhole

&lt;DIV&gt;

21 - WTR-WHP  - Water Bureau Well Head Protection

&lt;DIV&gt;



&lt;hr&gt;



&lt;DIV&gt;

Group ID - Group Name - Description

&lt;DIV&gt;

00 - SD  - Separation Distance

&lt;DIV&gt;

10 - NSD - Non Separation Distance

&lt;DIV&gt;

20 - WTR - Water Bureau |
| Source |  |
| Description | Variance Type |

| Field | Document |
|:------|:---------|
| Alias | Document |
| Data Type | Link |
| Nulls | No |
| Unique | Yes |
| Index |  |
| Default Value |  |
| Domain | PDF Research Document WEB or File link |
| Source |  |
| Description | Active Link to Document granting Variance |

| Field | ProjNumb |
|:------|:---------|
| Alias | Project Number |
| Data Type | Number |
| Nulls | No |
| Unique | Yes |
| Index |  |
| Default Value |  |
| Domain | Numeric Project Numbers |
| Source |  |
| Description | BES Project Number |