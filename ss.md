```python
import pandas as pd
url = r"https://en.wikipedia.org/wiki/DC_Universe_Animated_Original_Movies"
tables = pd.read_html(url) # Returns list of all tables on page
for tab in tables: 
    if "Release date" in tab.columns:
        required_table = tab
        print(required_table)
```

                                                Title        Release date  \
    0                              Superman: Doomsday  September 21, 2007   
    1                Justice League: The New Frontier   February 26, 2008   
    2                           Batman: Gotham Knight        July 8, 2008   
    3                                    Wonder Woman       March 3, 2009   
    4                     Green Lantern: First Flight       July 28, 2009   
    5                 Superman/Batman: Public Enemies  September 29, 2009   
    6            Justice League: Crisis on Two Earths   February 23, 2010   
    7                      Batman: Under the Red Hood        July 7, 2010   
    8                     Superman/Batman: Apocalypse  September 28, 2010   
    9                               All-Star Superman   February 22, 2011   
    10                 Green Lantern: Emerald Knights        July 7, 2011   
    11                               Batman: Year One    October 18, 2011   
    12                           Justice League: Doom   February 28, 2012   
    13                         Superman vs. The Elite       June 12, 2012   
    14       Batman: The Dark Knight Returns – Part 1  September 25, 2012   
    15       Batman: The Dark Knight Returns – Part 2    January 29, 2013   
    16                              Superman: Unbound         May 7, 2013   
    17         Justice League: The Flashpoint Paradox       July 30, 2013   
    18                            Justice League: War    February 4, 2014   
    19                                  Son of Batman         May 6, 2014   
    20                      Batman: Assault on Arkham       July 29, 2014   
    21             Justice League: Throne of Atlantis    January 13, 2015   
    22                               Batman vs. Robin       April 7, 2015   
    23              Justice League: Gods and Monsters       July 28, 2015   
    24                              Batman: Bad Blood    January 20, 2016   
    25                 Justice League vs. Teen Titans      March 29, 2016   
    26                       Batman: The Killing Joke       July 22, 2016   
    27                            Justice League Dark    January 24, 2017   
    28                Teen Titans: The Judas Contract      March 31, 2017   
    29                        Batman and Harley Quinn     August 15, 2017   
    30                     Batman: Gotham by Gaslight    January 23, 2018   
    31                     Suicide Squad: Hell to Pay      March 27, 2018   
    32                          The Death of Superman       July 24, 2018   
    33                          Reign of the Supermen    January 15, 2019   
    34              Justice League vs. the Fatal Five      March 30, 2019   
    35                                   Batman: Hush       July 20, 2019   
    36                       Wonder Woman: Bloodlines     October 5, 2019   
    37                              Superman: Red Son   February 25, 2020   
    38             Justice League Dark: Apokolips War         May 5, 2020   
    39                      Superman: Man of Tomorrow     August 23, 2020   
    40                     Batman: Soul of the Dragon    January 12, 2021   
    41                  Justice Society: World War II      April 27, 2021   
    42           Batman: The Long Halloween, Part One       June 22, 2021   
    43           Batman: The Long Halloween, Part Two       July 27, 2021   
    44                                      Injustice    October 19, 2021   
    45                               Catwoman: Hunted    February 8, 2022   
    46                 Green Lantern: Beware My Power       July 26, 2022   
    47  Batman and Superman: Battle of the Super Sons    October 18, 2022   
    
                                  Continuity  \
    0                             Standalone   
    1                             Standalone   
    2             Nolanverse (unofficial)[2]   
    3                             Standalone   
    4                             Standalone   
    5                     Superman/Batman[3]   
    6            Crisis on Two Earths / Doom   
    7                             Standalone   
    8                     Superman/Batman[3]   
    9                             Standalone   
    10                            Standalone   
    11  Year One / Dark Knight Returns[4][5]   
    12           Crisis on Two Earths / Doom   
    13                            Standalone   
    14  Year One / Dark Knight Returns[4][5]   
    15  Year One / Dark Knight Returns[4][5]   
    16                            Standalone   
    17                              DCAMU[6]   
    18                                 DCAMU   
    19                                 DCAMU   
    20                        Arkhamverse[7]   
    21                                 DCAMU   
    22                                 DCAMU   
    23                            Standalone   
    24                                 DCAMU   
    25                                 DCAMU   
    26                            Standalone   
    27                                 DCAMU   
    28                                 DCAMU   
    29                                  DCAU   
    30                            Standalone   
    31                                 DCAMU   
    32                                 DCAMU   
    33                                 DCAMU   
    34                            DCAU[8][9]   
    35                                 DCAMU   
    36                                 DCAMU   
    37                            Standalone   
    38                                 DCAMU   
    39                         Tomorrowverse   
    40                            Standalone   
    41                         Tomorrowverse   
    42                         Tomorrowverse   
    43                         Tomorrowverse   
    44                            Standalone   
    45                            Standalone   
    46                         Tomorrowverse   
    47                            Standalone   
    
                                             Adapted from  
    0                             "The Death of Superman"  
    1                                DC: The New Frontier  
    2                   Batman: "The Batman Nobody Knows"  
    3                    Wonder Woman: "Gods and Mortals"  
    4                                                 NaN  
    5                   Superman/Batman: "Public Enemies"  
    6             "Crisis on Earth-Three!" / JLA: Earth 2  
    7                            Batman: "Under the Hood"  
    8       Superman/Batman: "The Supergirl from Krypton"  
    9                                   All-Star Superman  
    10  "New Blood" / "What Price Honor?" / "Mogo Does...  
    11                                   Batman: Year One  
    12                              JLA: "Tower of Babel"  
    13  "What's So Funny About Truth, Justice & the Am...  
    14                            The Dark Knight Returns  
    15                            The Dark Knight Returns  
    16                               Superman: "Brainiac"  
    17                                         Flashpoint  
    18                             Justice League: Origin  
    19                           Batman: "Batman and Son"  
    20                                                NaN  
    21                               "Throne of Atlantis"  
    22  Batman: Night of the Owls / Batman and Robin: ...  
    23                                                NaN  
    24                  Batman and Robin / "Batman, Inc."  
    25                                                NaN  
    26                           Batman: The Killing Joke  
    27                                                NaN  
    28                  Teen Titans: "The Judas Contract"  
    29                                                NaN  
    30                                 Gotham by Gaslight  
    31                                                NaN  
    32                            "The Death of Superman"  
    33                           "Reign of the Supermen!"  
    34                                                NaN  
    35                                     Batman: "Hush"  
    36  Wonder Woman: "Down to Earth" / "Bitter Rivals...  
    37                                  Superman: Red Son  
    38  Darkseid War / "Final Crisis" / The New 52: Fu...  
    39    Superman: Birthright / Superman: American Alien  
    40                                                NaN  
    41                                                NaN  
    42                         Batman: The Long Halloween  
    43                         Batman: The Long Halloween  
    44      Injustice: Gods Among Us (comic / video game)  
    45                                                NaN  
    46  Green Lantern/Green Arrow / "Emerald Twilight"...  
    47                                                NaN  
                                             Title        Release date  \
    0                           Superman: Doomsday  September 18, 2007   
    1             Justice League: The New Frontier   February 26, 2008   
    2                        Batman: Gotham Knight        July 8, 2008   
    3                                 Wonder Woman       March 3, 2009   
    4                  Green Lantern: First Flight       July 28, 2009   
    5              Superman/Batman: Public Enemies  September 29, 2009   
    6         Justice League: Crisis on Two Earths   February 23, 2010   
    7                   Batman: Under the Red Hood       July 27, 2010   
    8                  Superman/Batman: Apocalypse  September 28, 2010   
    9   Superman/Shazam!: The Return of Black Adam    November 9, 2010   
    10                           All-Star Superman   February 22, 2011   
    11              Green Lantern: Emerald Knights        June 8, 2011   
    12                            Batman: Year One    October 18, 2011   
    13                        Justice League: Doom   February 28, 2012   
    14                      Superman vs. The Elite       June 12, 2012   
    15    Batman: The Dark Knight Returns – Part 1  September 25, 2012   
    16    Batman: The Dark Knight Returns – Part 2    January 29, 2013   
    17                           Superman: Unbound         May 7, 2013   
    18      Justice League: The Flashpoint Paradox       July 30, 2013   
    19                         Justice League: War    February 4, 2014   
    20                               Son of Batman         May 6, 2014   
    21                   Batman: Assault on Arkham     August 12, 2014   
    22          Justice League: Throne of Atlantis    January 27, 2015   
    23                            Batman vs. Robin      April 14, 2015   
    24           Justice League: Gods and Monsters       July 21, 2015   
    25                           Batman: Bad Blood    February 2, 2016   
    26              Justice League vs. Teen Titans      March 26, 2016   
    27                    Batman: The Killing Joke    October 10, 2016   
    28                         Justice League Dark    January 24, 2017   
    29             Teen Titans: The Judas Contract      March 31, 2017   
    30                     Batman and Harley Quinn     August 15, 2017   
    31                  Batman: Gotham by Gaslight    January 23, 2018   
    32                  Suicide Squad: Hell to Pay      March 27, 2018   
    33                       The Death of Superman       July 24, 2018   
    34                       Reign of the Supermen    January 13, 2019   
    35           Justice League vs. the Fatal Five      April 16, 2019   
    36                                Batman: Hush       July 20, 2019   
    37                    Wonder Woman: Bloodlines     October 5, 2019   
    38                           Superman: Red Son   February 25, 2020   
    39          Justice League Dark: Apokolips War         May 5, 2020   
    40                   Superman: Man of Tomorrow     October 5, 2020   
    41                 Batman: Death in the Family    October 13, 2020   
    42                  Batman: Soul of the Dragon    January 12, 2021   
    43               Justice Society: World War II        May 10, 2021   
    44        Batman: The Long Halloween, Part One       June 22, 2021   
    45        Batman: The Long Halloween, Part Two       July 27, 2021   
    46                                   Injustice    October 29, 2021   
    47                            Catwoman: Hunted    February 8, 2022   
    48           Constantine: The House of Mystery         May 3, 2022   
    49                                       Total               Total   
    50                                     Average             Average   
    
               Gross  Ref.  
    0    $10,102,202  [49]  
    1     $5,735,377  [50]  
    2     $8,539,068  [51]  
    3     $9,904,313  [52]  
    4     $8,484,729  [53]  
    5    $11,014,346  [54]  
    6     $8,636,868  [55]  
    7    $12,411,958  [56]  
    8     $8,839,887  [57]  
    9     $5,983,521  [58]  
    10    $7,539,076  [59]  
    11    $5,749,225  [60]  
    12    $6,137,182  [61]  
    13    $7,539,282  [62]  
    14    $3,184,408  [63]  
    15    $6,006,141  [64]  
    16    $4,315,736  [65]  
    17    $3,523,760  [66]  
    18    $5,260,646  [67]  
    19    $5,802,728  [68]  
    20    $7,023,969  [69]  
    21    $5,946,258  [70]  
    22    $4,657,085  [71]  
    23    $4,657,085  [72]  
    24    $2,972,092  [73]  
    25    $4,865,442  [74]  
    26    $4,865,442  [75]  
    27    $8,994,247  [76]  
    28    $3,318,438  [77]  
    29    $3,272,927  [78]  
    30    $2,247,876  [79]  
    31    $4,697,126  [80]  
    32    $2,865,568  [81]  
    33    $6,546,576  [82]  
    34    $3,773,664  [83]  
    35    $2,185,458  [84]  
    36    $3,597,264  [85]  
    37    $1,718,374  [86]  
    38    $2,032,174  [87]  
    39    $5,513,095  [88]  
    40    $3,400,133  [89]  
    41    $3,675,151  [90]  
    42    $2,421,468  [91]  
    43    $3,617,118  [92]  
    44    $3,607,779  [93]  
    45    $2,551,203  [94]  
    46    $2,668,958  [95]  
    47      $397,129  [96]  
    48      $232,393  [97]  
    49  $253,031,945     —  
    50    $5,163,917     —  



```python

```
