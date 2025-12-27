J/AJ/151/68     Kepler Mission. VII. Eclipsing binaries in DR3     (Kirk+, 2016)
================================================================================
Kepler eclipsing binary stars. VII. The catalog of eclipsing binaries found in
the entire Kepler data set.
    Kirk B., Conroy K., Prsa A., Abdul-Masih M., Kochoska A., Matijevic G.,
    Hambleton K., Barclay T., Bloemen S., Boyajian T., Doyle L.R., Fulton B.J.,
    Hoekstra A.J., Jek K., Kane S.R., Kostov V., Latham D., Mazeh T.,
    Orosz J.A., Pepper J., Quarles B., Ragozzine D., Shporer A., Southworth J.,
    Stassun K., Thompson S.E., Welsh W.F., Agol E., Derekas A., Devor J.,
    Fischer D., Green G., Gropp J., Jacobs T., Johnston C., LaCourse D.M.,
    Saetre K., Schwengeler H., Toczyski J., Werner G., Garrett M., Gore J.,
    Martinez A.O., Spitzer I., Stevick J., Thomadis P.C., Vrijmoet E.H.,
    Yenawine M., Batalha N., Borucki W.
   <Astron. J., 151, 68 (2016)>
   =2016AJ....151...68K    (SIMBAD/NED BibCode)
================================================================================
ADC_Keywords: Binaries, eclipsing
Keywords: binaries: eclipsing - catalogs - methods: data analysis -
          methods: numerical - stars: fundamental parameters - stars: statistics

Abstract:
    The primary Kepler Mission provided nearly continuous monitoring of
    ~200000 objects with unprecedented photometric precision. We present
    the final catalog of eclipsing binary systems within the 105deg^2^
    Kepler field of view. This release incorporates the full extent of the
    data from the primary mission (Q0-Q17 Data Release). As a result, new
    systems have been added, additional false positives have been removed,
    ephemerides and principal parameters have been recomputed,
    classifications have been revised to rely on analytical models, and
    eclipse timing variations have been computed for each system. We
    identify several classes of systems including those that exhibit
    tertiary eclipse events, systems that show clear evidence of
    additional bodies, heartbeat systems, systems with changing eclipse
    depths, and systems exhibiting only one eclipse event over the
    duration of the mission. We have updated the period and galactic
    latitude distribution diagrams and included a catalog completeness
    evaluation. The total number of identified eclipsing and ellipsoidal
    binary systems in the Kepler field of view has increased to 2878, 1.3%
    of all observed Kepler targets. An online version of this catalog with
    downloadable content and visualization tools is maintained at
    https://keplerEBs.villanova.edu/.

Description:
    The Kepler Eclipsing Binary Catalog lists the stellar parameters from
    the Kepler Input Catalog (KIC) augmented by: primary and secondary
    eclipse depth, eclipse width, separation of eclipse, ephemeris,
    morphological classification parameter, and principal parameters
    determined by geometric analysis of the phased light curve.

    The previous release of the Catalog (Paper II; Slawson et al. 2011,
    cat. J/AJ/142/160) contained 2165 objects, through the second Kepler
    data release (Q0-Q2). In this release, 2878 objects are identified and
    analyzed from the entire data set of the primary Kepler mission
    (Q0-Q17). The online version of the Catalog is currently maintained at
    https://keplerEBs.villanova.edu/. A static version of the online
    Catalog associated with this paper is maintained at MAST
    https://archive.stsci.edu/kepler/eclipsing_binaries.html.

File Summary:
--------------------------------------------------------------------------------
 FileName  Lrecl  Records    Explanations
--------------------------------------------------------------------------------
ReadMe        80        .    This file
catalog.dat  102     2876    Kepler Eclipsing Binary Catalog - Third Revision
                             (downloaded on https://keplerebs.villanova.edu/
                             - 2016 Aug 18)
table1.dat    36      173    The heartbeat stars in the Kepler sample
table2.dat    36       24    The systems with tidally induced pulsations in
                             the Kepler sample
table3.dat    69       36    The reflection effect systems in the Kepler sample
table4.dat    69       32    The occultation pairs in the Kepler sample
table5.dat   105        8    The circumbinary planets in the Kepler sample
table6.dat    69       14    The systems exhibiting multiple ephemerides in the
                             Kepler sample
table7.dat    34        9    Properties of the extraneous events found in the
                             Kepler sample
table8.dat    69       43    The systems exhibiting eclipse depth variations in
                             the Kepler sample
table9.dat    44       32    The systems with no repeating events (long) in the
                             Kepler sample
--------------------------------------------------------------------------------

See also:
           B/gcvs : General Catalogue of Variable Stars (Samus+ 2007-2013)
           V/133  : Kepler Input Catalog (Kepler Mission Team, 2009)
 J/MNRAS/452/3561 : Kepler eclipsing binaries. K2 Campaign 0 (LaCourse+, 2015)
 J/ApJS/217/31    : Kepler planetary candidates. VI. Q1-Q16 (Mullally+, 2015)
 J/ApJS/211/2     : Revised properties of Q1-16 Kepler targets (Huber+, 2014)
 J/PASP/126/914   : Kepler eclipsing binary stars. V. (Conroy+, 2014)
 J/AJ/147/45      : Kepler. IV. Eclipse times for close binaries (Conroy+, 2014)
 J/AJ/143/137     : Minima of 41 EBs from a Kepler survey (Gies+, 2012)
 J/AJ/142/160     : Kepler Mission. II. DR2 eclipsing binaries (Slawson+, 2011)
 J/AJ/141/83      : Eclipsing binaries in Kepler DR1 (Prsa+, 2011)
 J/ApJ/736/19     : Kepler planetary candidates. II. (Borucki+, 2011)
 https://keplerEBs.villanova.edu/ : Kepler Eclipsing Binary Catalog

Byte-by-byte Description of file: catalog.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label Explanations
--------------------------------------------------------------------------------
   1-  8  I08   ---     KIC   [1026032/12785282] Kepler Input Catalog number
  10- 21  F12.7 d       Per   [0.07/1087.3]Period of the eclipsing binary signal
  23- 32  F10.7 d     e_Per   [0/0.0147]?=-1 Period error
  34- 45  F12.6 d       BJD0  [5487.3/56903.9]?=-1 Time of eclipse BJD_0_
                               (Barycentric Julian Date-2400000) (1)
  47- 55  F9.6  d     e_BJD0  [0.003/2.5]?=-1 BJD_0_ error
  57- 61  F5.2  ---     Morph [0/1]?=-1 Morphology value (between 0-1) (2)
  63- 69  F7.4  deg     GLON  ?=-1 Kepler galactic longitude
  71- 77  F7.4  deg     GLAT  ?=-1 Kepler galactic latitude
  79- 85  F7.4  mag     Kpmag [-1/19.742]?=-1 Kepler magnitude of the target
  87- 91  I5    K       Teff  ?=-1 Kepler effective temperature
  92- 96  F5.4  ---     ---   [.0000]
  98-102  A5    ---     SC    Short-Cadence data? (True or False)
--------------------------------------------------------------------------------
Note (1): With the convention such that the primary (deeper) eclipse occurs at
     phase 0.
Note (2): Locally Linear Embedding (LLE; see Matijevic et al.,
     2012AJ....143..123M) morphology value assigned to system to designate the
     class of the system.
--------------------------------------------------------------------------------

Byte-by-byte Description of file: table1.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label Explanations
--------------------------------------------------------------------------------
   1-  8  I08   ---     KIC   [1573836/12255108] Kepler Input Catalog number (1)
  10- 19  F10.6 d       Per   [0.9/671.8] Period
  21- 28  F8.4  deg     RAdeg Right Ascension in decimal degrees (J2000)
  30- 36  F7.4  deg     DEdeg Declination in decimal degrees (J2000)
--------------------------------------------------------------------------------
Note (1): Heartbeat stars are a subclass of eccentric ellipsoidal variables
     introduced by Thompson et al. (2012ApJ...753...86T). These systems are
     flagged with the "HB" flag in the Catalog. Please refer to Section 8.1 in
     the text for further details.
--------------------------------------------------------------------------------

Byte-by-byte Description of file: table2.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label Explanations
--------------------------------------------------------------------------------
   1-  8  I08   ---     KIC   [1573836/12255108] Kepler Input Catalog number (1)
  10- 19  F10.6 d       Per   [0.9/671.8] Period
  21- 28  F8.4  deg     RAdeg Right Ascension in decimal degrees (J2000)
  30- 36  F7.4  deg     DEdeg Declination in decimal degrees (J2000)
--------------------------------------------------------------------------------
Note (1): The objects with tidally induced pulsations are flagged with the "TP"
     flag in the Catalog. Please refer to the Section 8.1.1 in the paper for
     additional details about these systems.
--------------------------------------------------------------------------------

Byte-by-byte Description of file: table3.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label Explanations
--------------------------------------------------------------------------------
   1-  8  I08   ---     KIC   [1722276/12216706] Kepler Input Catalog number (1)
  10- 20  F11.7 d       Per   [0.1/670.7] Period
  22- 30  F9.7  d     e_Per   [0/0.01] Period error
  32- 43  F12.6 d       BJD0  [54861/55295] Time of eclipse BJD_0_ (Barycentric
                               Julian Date-2400000)
  45- 52  F8.6  d     e_BJD0  [0.003/0.43]? BJD_0_ error (2)
  54- 61  F8.4  deg     RAdeg Right Ascension in decimal degrees (J2000)
  63- 69  F7.4  deg     DEdeg Declination in decimal degrees (J2000)
--------------------------------------------------------------------------------
Note (1): The reflection effect is the mutual irradiation of the facing
     hemispheres of two stars in the binary system. These systems are flagged
     with the "REF" flag in the Catalog. See additional details in Section 8.2.
Note (2): Those reported without BJD_0_ errors are also heartbeat stars.
--------------------------------------------------------------------------------

Byte-by-byte Description of file: table4.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label Explanations
--------------------------------------------------------------------------------
   1-  8  I08   ---     KIC   [1722276/12216706] Kepler Input Catalog number (1)
  10- 20  F11.7 d       Per   [0.1/670.7] Period
  22- 30  F9.7  d     e_Per   [0/0.01] Period error
  32- 43  F12.6 d       BJD0  [54861/55295] Time of eclipse BJD_0_ (Barycentric
                               Julian Date-2400000)
  45- 52  F8.6  d     e_BJD0  [0.003/0.43] BJD_0_ error
  54- 61  F8.4  deg     RAdeg Right Ascension in decimal degrees (J2000)
  63- 69  F7.4  deg     DEdeg Declination in decimal degrees (J2000)
--------------------------------------------------------------------------------
Note (1): The occultation pairs are flagged with the "OCC" flag in the Catalog.
     Please see Section 8.3 for details about these systems.
--------------------------------------------------------------------------------

Byte-by-byte Description of file: table5.dat
--------------------------------------------------------------------------------
   Bytes Format Units  Label  Explanations
--------------------------------------------------------------------------------
   1-  8  I08   ---    KIC    [4862625/12644769] Kepler Input Catalog number (1)
  10- 21  A12   ---    Kepler Kepler identifier
  23- 30  F8.5  d      Per    [7.4/41.1] Period
  32- 38  F7.5  d    e_Per    Period error
  40- 49  F10.6 deg    RAdeg  Right Ascension in decimal degrees (J2000)
  51- 59  F9.6  deg    DEdeg  Declination in decimal degrees (J2000)
  61-105  A45   ---    Ref    Citation
--------------------------------------------------------------------------------
Note (1): There are currently 14 of circumbinary planets. These systems are
     flagged with the "CBP" flag in the Catalog. See more details about
     circumbinary planets in Section 8.4.
--------------------------------------------------------------------------------

Byte-by-byte Description of file: table6.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label Explanations
--------------------------------------------------------------------------------
   1-  8  I08   ---     KIC   [1722276/12216706] Kepler Input Catalog number (1)
  10- 20  F11.7 d       Per   [0.1/670.7] Period
  22- 30  F9.7  d     e_Per   [0/0.01] Period error
  32- 43  F12.6 d       BJD0  [54861/55295] Time of eclipse BJD_0_ (Barycentric
                               Julian Date-2400000)
  45- 52  F8.6  d     e_BJD0  [0.003/0.43] BJD_0_ error
  54- 61  F8.4  deg     RAdeg Right Ascension in decimal degrees (J2000)
  63- 69  F7.4  deg     DEdeg Declination in decimal degrees (J2000)
--------------------------------------------------------------------------------
Note (1): Sources with additional features (see Section 8.4) can be another sign
     of a stellar triple or multiple system. In this case the depth of the event
     is too deep to be the transit of a planet but is instead an eclipse by, or
     occultation of a third stellar body. We have been looking for such features
     in the Catalog and have uncovered 14 systems exhibiting multiple,
     determinable periods. These systems are flagged with the "M" flag in the
     Catalog.
--------------------------------------------------------------------------------

Byte-by-byte Description of file: table7.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label Explanations
--------------------------------------------------------------------------------
   1-  8  I08   ---     KIC   [6543674/7670485] Kepler Input Catalog number (1)
  10- 14  F5.3  %       Depth [0.6/0.975] Event depth
  16- 18  F3.1  d       W     [0.2/2] Event width
  20- 26  F7.1  d       Time0 [55023/56303.7] Start time (Time-240000)
  28- 34  F7.1  d       Time1 [55025/56303.9] End time (Time-240000)
--------------------------------------------------------------------------------
Note (1): In some systems, extraneous events are observed whose ephemerides
     cannot be determined. In some cases the period is longer than the time
     baseline and two subsequent events have not been observed by Kepler. In
     other cases, eclipsing the inner-binary at different phases results in a
     nonlinear ephemeris with an indeterminable period. It is worth noting that
     without spectroscopy or Eclipse Timing Variations (ETVs) that are in
     agreement that additional eclipse event is indeed related, these cases are
     not guaranteed to be multiple objects-some could be the blend of two
     independent binaries on the same pixel.
--------------------------------------------------------------------------------

Byte-by-byte Description of file: table8.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label Explanations
--------------------------------------------------------------------------------
   1-  8  I08   ---     KIC   [1722276/12216706] Kepler Input Catalog number (1)
  10- 20  F11.7 d       Per   [0.1/670.7] Period
  22- 30  F9.7  d     e_Per   [0/0.01] Period error
  32- 43  F12.6 d       BJD0  [54861/55295] Time of eclipse BJD_0_ (Barycentric
                               Julian Date-2400000)
  45- 52  F8.6  d     e_BJD0  [0.003/0.43]? BJD_0_ error
  54- 61  F8.4  deg     RAdeg Right Ascension in decimal degrees (J2000)
  63- 69  F7.4  deg     DEdeg Declination in decimal degrees (J2000)
--------------------------------------------------------------------------------
Note (1): The Depth Variations are flagged by the "DV" flag in the Catalog. See
     Section 8.7 in the text for additional details about the eclipse depth
     changes.
--------------------------------------------------------------------------------

Byte-by-byte Description of file: table9.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label Explanations
--------------------------------------------------------------------------------
   1-  8  I08   ---     KIC   [2162635/11038446] Kepler Input Catalog number (1)
  10- 15  F6.4  %       Depth [0.6/0.9988] Event depth
  17- 21  F5.2  d       W     [0.2/35] Event width
  23- 27  I5    d       BJD0  [54969/56222] Time of eclipse BJD_0_ (Barycentric
                               Julian Date-2400000)
  29- 36  F8.4  deg     RAdeg Right Ascension in decimal degrees (J2000)
  38- 44  F7.4  deg     DEdeg Declination in decimal degrees (J2000)
--------------------------------------------------------------------------------
Note (1): Systems exhibiting a primary and/or secondary eclipse but lack a
     repeat of either one. These systems do not have periods. These systems are
     flagged with the "L" (long) flag and are available from the database under
     http://keplerEBs.villanova.edu/search but are not included in the Eclipsing
     Binary (EB) Catalog.
--------------------------------------------------------------------------------

History:
    From electronic version of the journal

References:
    Prsa et al.,        Paper I     2011AJ....141...83P,   Cat. J/AJ/141/83
    Slawson et al.,     Paper II    2011AJ....142..160S,   Cat. J/AJ/142/160
    Matijevic et al.,   Paper III   2012AJ....143..123M
    Conroy et al.,      Paper IV    2014AJ....147...45C,   Cat. J/AJ/147/45
    Conroy et al.,      Paper V     2014PASP..126..914C,   Cat. J/PASP/126/914
    LaCourse et al.,    Paper VI    2015MNRAS.452.3561L,   Cat. J/MNRAS/452/3561
    Abdul-Masih et al., Paper VIII  2016AJ....151..101A,   Cat. J/AJ/151/101

================================================================================
(End)                                    Sylvain Guehenneux [CDS]    26-Jul-2016
