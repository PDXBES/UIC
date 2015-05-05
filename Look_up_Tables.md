**Waste Water Type Look Up Table**<div><b>LUT Name:</b>
Look_up_Waste_Type_Tbl {only used domain codes listed}<br>
<br>
<table><thead><th> Waste Key </th><th> Waste Description </th></thead><tbody>
<tr><td> 1 </td><td> Stormwater </td></tr>
<tr><td> 5 </td><td> Drinking Water </td></tr>
<tr><td> 17 </td><td> ASR (Aquifer storage and recovery) </td></tr></tbody></table>

<b>LUT Name:</b> Lookup_Type_Code  {only used domain codes listed}<br>
<table><thead><th> DEQ Code </th><th> Description </th></thead><tbody>
<tr><td> 5D2 </td><td> Stormwater </td></tr>
<tr><td> 5D3 </td><td> Storm Water Drill Holes/seepage Pits </td></tr>
<tr><td> 5D4 </td><td> Industrial Storm Water Drainage </td></tr>
<tr><td> 5G30 </td><td> Special Drainage Water </td></tr>
<tr><td> 5R21 </td><td> Aquifer Recharge </td></tr>
<tr><td> 5X27 </td><td> Other Wells </td></tr></tbody></table>

<b>LUT Name:</b> Lookup_Well_Status_Tbl<br>
<table><thead><th>Code </th><th> Hansen Description </th><th> Status </th></thead><tbody>
<tr><td> AC </td><td> IN </td><td> In Service </td><td> Active </td></tr>
<tr><td> AC </td><td> CNS </td><td> Constructed No Service </td><td> Active </td></tr>
<tr><td> AC </td><td> TBAB </td><td> To be Abandoned </td><td> Active </td></tr>
<tr><td> AC </td><td> PEND </td><td> In Service Action Pending </td><td> Active </td></tr>
<tr><td> PA </td><td> ABAN </td><td> Abandoned </td><td> Inactive </td></tr>
<tr><td> UC </td><td> NEW </td><td> Under Construction </td><td> Active </td></tr>
<tr><td> NB </td><td> DNE </td><td> Not Built / Does not Exist </td><td> Inactive </td></tr></tbody></table>

<b>LUT Name:</b> Lookup_WellUse_Code<br>
<table><thead><th> Code </th><th> Description         </th></thead><tbody>
<tr><td>   0  </td><td> Unknown             </td></tr>
<tr><td>   1  </td><td> Domestic            </td></tr>
<tr><td>   2  </td><td> Irrigation          </td></tr>
<tr><td>   3  </td><td> Public or Community </td></tr>
<tr><td>   4  </td><td> Industrial          </td></tr>
<tr><td>   5  </td><td> Injection           </td></tr>
<tr><td>   6  </td><td> Thermal             </td></tr>
<tr><td>   7  </td><td> Livestock           </td></tr></tbody></table>

<b><i>Metro Land Use</i></b><div><b>LUT Name:</b> Lookup_MetroZoneClass<div><b>Description:</b> 44 regional classifications into which the zoning is generalized.<div>
<table><thead><th> Code </th><th> Classification </th><th> Description </th></thead><tbody>
<tr><td> FF    </td><td> Agriculture or Forestry </td><td> Agriculture or Forestry activities suited to commercial scale agricultural production or forestry, typically with lot sizes of 10, 20 or 30 acres or more. </td></tr>
<tr><td> SFR9  </td><td> Single family </td><td> Single family detached housing with lot sizes around 4,000 sq. ft. </td></tr>
<tr><td> SFR1  </td><td> Single family </td><td> Single family detached housing with minimum lot size from 35,000 sq. ft. </td></tr>
<tr><td> SFR2  </td><td> Single family </td><td> Single family detached housing with minimum lot size from 15,000 sq. ft. to a net acre </td></tr>
<tr><td> SFR3  </td><td> Single family </td><td> Single family detached housing with lot sizes from about 10,000 sq. ft. to 15,000 sq. ft. </td></tr>
<tr><td> SFR4  </td><td> Single family </td><td> Single family detached housing with lot sizes around 9,000 sq. ft. </td></tr>
<tr><td> SFR5  </td><td> Single family </td><td> Single family detached housing with lot sizes around 7,000 sq. ft. </td></tr>
<tr><td> SFR6  </td><td> Single family </td><td> Single family detached housing with lot sizes around 6,000 sq. ft. </td></tr>
<tr><td> SFR7  </td><td> Single family </td><td> Single family detached housing with lot sizes around 5,000 sq. ft. </td></tr>
<tr><td> MFR1  </td><td> Multi-family </td><td> Multi-family single family, townhouses, row houses permitted outright. Max density permitted is 15 units / net acre. </td></tr>
<tr><td> MFR2  </td><td> Multi-family </td><td> Multi-family single family, townhouses, row houses permitted outright. Max density permitted is 20 units / net acre. </td></tr>
<tr><td> MFR3  </td><td> Multi-family </td><td> Multi-family single family, townhouses, row houses permitted outright. Max density permitted is 25 units / net acre. </td></tr>
<tr><td> MFR4  </td><td> Multi-family </td><td> Multi-family single family, townhouses, row houses permitted outright. Max density permitted is 30 units / net acre. </td></tr>
<tr><td> CN    </td><td> Neighborhood Commercial </td><td> Neighborhood Commercial small-scale commercial districts permitting retail and serice activities such as grocery stores and neighborhood service establishments that support the local residential community. Floor space and/or lot sizes are usually limited to between 5,000 to 10,000 square feet. </td></tr>
<tr><td> CG    </td><td> General Commercial </td><td> General Commercial larger scale commercial districts, often with a more regional orientation for providing goods and services. Businesses offering a wider variety of goods and services (including large format retailers) are permitted in this district and include mid-rise office buildings, and highway and strip commercial zones. </td></tr>
<tr><td> CC    </td><td> Central Commercial </td><td> Central Commercial allows a full range of commercial typically associated with CBD's and downtowns. More restrictive than general commercial in the case of large lot and highway-oriented uses. Encourages higher FAR uses including multi-story development. </td></tr>
<tr><td> CO    </td><td> Office Commercial </td><td> Office Commercial districts accommodating a range of low-rise offices; supports various community business establishments, professional and medical offices; typically as a buffer between residential areas and more intensive commercial districts. </td></tr>
<tr><td> IL    </td><td> Light Industrial </td><td> Light Industrial districts permit warehousing and distribution facilities, light manufacturing, processing, fabrication or assembly. May allow limited commercial activities such as retail and service functions that support the businesses and workers in the district. </td></tr>
<tr><td> IH    </td><td> Heavy Industrial </td><td> Heavy Industrial districts permit light industrial and intensive industrial activity such as bottling, chemical processing, heavy manufacturing and similar uses with noxious externalities. </td></tr>
<tr><td> POS   </td><td> Parks and Open Space </td><td>  </td></tr>
<tr><td> PF    </td><td> Public Facilities </td><td> Public Facilities allows government building, institutional and cultural uses such as museums. </td></tr>
<tr><td> SFR10 </td><td> Single family </td><td> Single family detached or attached housing with lot sizes around 3,500 sq. ft. </td></tr>
<tr><td> SFR11 </td><td> Single family </td><td> Single family detached or attached housing with lot sizes around 3,000 sq. ft. </td></tr>
<tr><td> SFR12 </td><td> Single family </td><td> Single family detached or attached housing with lot sizes around 2,900 sq. ft. </td></tr>
<tr><td> SFR13 </td><td> Single family </td><td> Single family detached or attached housing with lot sizes around 2,700 sq. ft. </td></tr>
<tr><td> SFR14 </td><td> Single family </td><td> Single family detached or attached housing with lot sizes around 2,500 sq. ft. </td></tr>
<tr><td> SFR15 </td><td> Single family </td><td> Single family detached or attached housing with lot sizes around 2,300 sq. ft. </td></tr>
<tr><td> SFR16 </td><td> Single family </td><td> Single family detached or attached housing with lot sizes around 2,000 sq. ft. </td></tr>
<tr><td> MUE   </td><td> Multiple Use Employment </td><td> an employment district that accommodates a broad range of users including offices, retail stores, warehouse distribution, and light industrial including manufacturing, fabrication, and assembly. </td></tr>
<tr><td> MFR5  </td><td> Multi-family </td><td> Multi-family single family, townhouses, row houses permitted outright. Max density permitted is 35 units / net acre. </td></tr>
<tr><td> MFR6  </td><td> Multi-family </td><td> Multi-family single family, townhouses, row houses permitted outright. Max density permitted is 40 units / net acre. </td></tr>
<tr><td> MUR10 </td><td> Mixed Use </td><td> Mixed Use Commercial & Residential with FAR maximum of about 12.5 </td></tr>
<tr><td> MFR7  </td><td> Multi-family </td><td> Multi-family single family, townhouses, row houses permitted outright. Max density permitted is 60 units / net acre. </td></tr>
<tr><td> SFR8  </td><td> Single family </td><td> Single family detached housing with lot sizes around 4,500 sq. ft. </td></tr>
<tr><td> MUR1  </td><td> Mixed Use </td><td> Mixed Use Commercial & Residential with FAR maximum of about 0.35 </td></tr>
<tr><td> MUR2  </td><td> Mixed Use </td><td> Mixed Use Commercial & Residential with FAR maximum of about 0.5 </td></tr>
<tr><td> MUR3  </td><td> Mixed Use </td><td> Mixed Use Commercial & Residential with FAR maximum of about 0.75 </td></tr>
<tr><td> MUR4  </td><td> Mixed Use </td><td> Mixed Use Commercial & Residential with FAR maximum of about 1.25 </td></tr>
<tr><td> MUR5  </td><td> Mixed Use </td><td> Mixed Use Commercial & Residential with FAR maximum of about 1.5 </td></tr>
<tr><td> MUR6  </td><td> Mixed Use </td><td> Mixed Use Commercial & Residential with FAR maximum of about 1.75 </td></tr>
<tr><td> MUR7  </td><td> Mixed Use </td><td> Mixed Use Commercial & Residential with FAR maximum of about 2 </td></tr>
<tr><td> MUR8  </td><td> Mixed Use </td><td> Mixed Use Commercial & Residential with FAR maximum of about 3 </td></tr>
<tr><td> MUR9  </td><td> Mixed Use </td><td> Mixed Use Commercial & Residential with FAR maximum of about 4 </td></tr>
<tr><td> RRFU  </td><td> Rural </td><td> Rural Residential or Future Urban - residential uses permitted on rural lands (1 dwelling unit per lot) or areas designated for future urban development, typically lots are 10 or more acres </td></tr></tbody></table>

<b>LUT Name:</b> Lookup_ZoneGen<div><b>Description:</b> Nine generalized classifications into which the zoning is generalized<div>
<table><thead><th> Code </th><th> Classifications </th></thead><tbody>
<tr><td> IND </td><td> Industrial </td></tr>
<tr><td> COM </td><td> Commercial </td></tr>
<tr><td> MFR </td><td> Multi-family residential </td></tr>
<tr><td> POS </td><td> Parks and open space </td></tr>
<tr><td> MUR </td><td> Mixed-use residential </td></tr>
<tr><td> SFR </td><td> Single family residential </td></tr>
<tr><td> MUE </td><td> Mixed-use employment </td></tr>
<tr><td> PF  </td><td> Public facilities </td></tr>
<tr><td> RUR </td><td> Rural </td></tr></tbody></table>

<b>LUT Name:</b> Lookup_SIC<br>
<table><thead><th> 1799 </th><th> CONSTRUCTION, SPEC TRADE CONT. </th></thead><tbody>
<tr><td> 2011 </td><td> MEAT PACKING PLANTS </td></tr>
<tr><td> 2013 </td><td> SAUSAGES & OTHER PREPARED MEAT </td></tr>
<tr><td> 2026 </td><td> FLUID MILK </td></tr>
<tr><td> 2035 </td><td> PICKLES, SAUCES, & SALAD DRESS </td></tr>
<tr><td> 2038 </td><td> FROZEN SPECIALTIES, NEC </td></tr>
<tr><td> 2052 </td><td> COOKIES AND CRACKERS </td></tr>
<tr><td> 2076 </td><td> VEGETABLE OIL MILLS, NEC </td></tr>
<tr><td> 2079 </td><td> EDIBLE FATS AND OILS, ETC </td></tr>
<tr><td> 2082 </td><td> MALT BEVERAGES </td></tr>
<tr><td> 2086 </td><td> BOTTLED & CANNED SOFT DRINKS </td></tr>
<tr><td> 2087 </td><td> FLAVORING EXTRACTS AND SYRUPS </td></tr>
<tr><td> 2099 </td><td> FOOD PREPARATIONS, NEC </td></tr>
<tr><td> 2299 </td><td> TEXTILE GOODS, NEC </td></tr>
<tr><td> 2431 </td><td> PAPERBOARD MILLS </td></tr>
<tr><td> 2436 </td><td> SOFTWOOD VENEER AND PLYWOOD </td></tr>
<tr><td> 2672 </td><td> PAPER COATED AND LAMINATED,NEC </td></tr>
<tr><td> 2721 </td><td> PERIODICALS </td></tr>
<tr><td> 2812 </td><td> ALKALIES AND CHLORINE </td></tr>
<tr><td> 2816 </td><td> INORGANIC PIGMENTS </td></tr>
<tr><td> 2833 </td><td> MEDICINALS & BOTANICALS </td></tr>
<tr><td> 2834 </td><td> PHARMACEUTICAL PREPARATIONS </td></tr>
<tr><td> 2841 </td><td> SOAP AND OTHER DETERGENTS </td></tr>
<tr><td> 2851 </td><td> PAINTS AND ALLIED PRODUCTS </td></tr>
<tr><td> 2879 </td><td> AGRICULTURAL CHEMICALS, NEC </td></tr>
<tr><td> 2893 </td><td> PRINTING INK </td></tr>
<tr><td> 2899 </td><td> CHEMICAL PREPARATIONS, NEC </td></tr>
<tr><td> 2911 </td><td> PETROLEUM REFINING </td></tr>
<tr><td> 2952 </td><td> ASPHALT FELTS AND COATINGS </td></tr>
<tr><td> 2992 </td><td> LUBRICATING OILS & GREASES </td></tr>
<tr><td> 2999 </td><td> PETRO AND COAL PRODUCTS </td></tr>
<tr><td> 3295 </td><td> MINERALS, GROUND OR TREATED </td></tr>
<tr><td> 3312 </td><td> BLAST FURNACES & STEEL MILLS </td></tr>
<tr><td> 3321 </td><td> GRAY & DUCTILE IRON FOUNDRIES </td></tr>
<tr><td> 3324 </td><td> STEEL INVESTMENT FOUNDRIES </td></tr>
<tr><td> 3339 </td><td> PRIMARY NONFERROUS METALS, NEC </td></tr>
<tr><td> 3356 </td><td> NONFERROUS METALS EXCEPT CU,AL </td></tr>
<tr><td> 3365 </td><td> ALUMINUM FOUNDRIES </td></tr>
<tr><td> 3366 </td><td> COPPER FOUNDRIES </td></tr>
<tr><td> 3411 </td><td> METAL CANS </td></tr>
<tr><td> 3471 </td><td> PLATING AND POLISHING </td></tr>
<tr><td> 3479 </td><td> METAL COATING AND ALLIED SERV. </td></tr>
<tr><td> 3498 </td><td> FABRICATED PIPE AND FITTINGS </td></tr>
<tr><td> 3691 </td><td> STORAGE BATTERIES </td></tr>
<tr><td> 3714 </td><td> MOTOR VEHICLES PARTS & ACCESS </td></tr>
<tr><td> 3731 </td><td> SHIP BUILDING AND REPAIRING </td></tr>
<tr><td> 3769 </td><td> SPACE VEHICLE EQUIPMENT, NEC </td></tr>
<tr><td> 3914 </td><td> SILVERWARE AND PLATED WARE </td></tr>
<tr><td> 4013 </td><td> RR, SWITCHING & TERMINAL SERV. </td></tr>
<tr><td> 4212 </td><td> LOCAL TRUCKING, W/O STORAGE </td></tr>
<tr><td> 4213 </td><td> TRUCKING, EXCEPT LOCAL </td></tr>
<tr><td> 4214 </td><td> LOCAL TRUCKING WITH STORAGE </td></tr>
<tr><td> 4231 </td><td> TRUCKING TERMINAL FACILITIES </td></tr>
<tr><td> 4491 </td><td> MARINE CARGO HANDLING </td></tr>
<tr><td> 4499 </td><td> WATER TRANSPORTATION SERVICES </td></tr>
<tr><td> 4953 </td><td> REFUSE SYSTEMS </td></tr>
<tr><td> 5063 </td><td> ELECTRICAL APPARATUS & EQPMNT </td></tr>
<tr><td> 5085 </td><td> INDUSTRIAL SUPPLIES </td></tr>
<tr><td> 5143 </td><td> DIARY PRODUCTS, EXC DRIED/CAND </td></tr>
<tr><td> 5149 </td><td> GROCERIES AND RELATED PRODUCTS </td></tr>
<tr><td> 5161 </td><td> CHEMICAL AND ALLIED PRODUCTS </td></tr>
<tr><td> 5169 </td><td> CHEMICAL & ALLIED PRODUCTS </td></tr>
<tr><td> 5171 </td><td> PETRO BULK STATIONS & TERMINAL </td></tr>
<tr><td> 5198 </td><td> PAINTS, VARNISHES AND SUPPPLIE </td></tr>
<tr><td> 5500 </td><td> GENERAL AUTO. DEALERS, ETC. </td></tr>
<tr><td> 5541 </td><td> GASOLINE SERVICE STATIONS </td></tr>
<tr><td> 5699 </td><td> MISC. APPAREL & ACCES. STORES </td></tr>
<tr><td> 5983 </td><td> FUEL OIL DEALERS </td></tr>
<tr><td> 5990 </td><td> HEAVY EQUIPMENT, RETAIL </td></tr>
<tr><td> 7211 </td><td> POWER LAUNDRIES, FAMILY & COMM </td></tr>
<tr><td> 7213 </td><td> LINEN SUPPLY </td></tr>
<tr><td> 7218 </td><td> INDUSTRIAL LAUNDERERS </td></tr>
<tr><td> 7219 </td><td> LAUNDRY AND GARMENT SERVICES </td></tr>
<tr><td> 7353 </td><td> HEAVY CONSTRUCTION EQUIP, MTL </td></tr>
<tr><td> 7384 </td><td> PHOTOFINISHING LABORATORIES </td></tr>
<tr><td> 7513 </td><td> TRUCK RENTAL & LEASING NO DRVR </td></tr>
<tr><td> 7532 </td><td> TOP & BODY REPAIR & PAINT SHOP </td></tr>
<tr><td> 7538 </td><td> GEN. AUTO. REPAIR SHOPS </td></tr>
<tr><td> 7542 </td><td> CARWASHES </td></tr>
<tr><td> 7699 </td><td> REPAIR SERVICES, NEC </td></tr>
<tr><td> 8731 </td><td> COMMERCIAL PHYSICAL RESEARCH </td></tr>
<tr><td> 8734 </td><td> TESTING LABORATORIES </td></tr>