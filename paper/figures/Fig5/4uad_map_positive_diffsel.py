###### PREAMBLE

import pymol
from pymol import cmd
import sys

structure = '4uad'

cmd.reinitialize()
cmd.set('bg_rgb','[1,1,1]') # white
cmd.set('antialias','2')
cmd.set('ray_opaque_background','off')
cmd.set('depth_cue', 'off')

### Modify here
url ='https://files.rcsb.org/download/4UAD.pdb'
cmd.load(url, 'orig')

cmd.select('importin', 'chain A')
cmd.select('origPB2', 'chain E')

cmd.load('S009PB2_{0}.pdb'.format(structure, 'S009'))
cmd.super('S009', 'origPB2')

cmd.hide('everything')
cmd.show('cartoon')
# cmd.show('surface')
for c in ['importin', 'S009']:
	cmd.show('surface', '{0}'.format(c))
# cmd.remove('origPB2')
cmd.color('wheat', 'importin')
cmd.color('white', 'S009')

cmd.orient()


### To get PB2 only
cmd.hide('everything')
# cmd.hide('everything', 'origPB2')
# cmd.hide('surface', 'S009')
cmd.show('cartoon', 'importin')
cmd.show('surface', 'S009')

###### END PREAMBLE


metric = 'positive_diffsel'
cmd.alter('resi 1', 'b = 1.2914272758838403')
cmd.alter('resi 2', 'b = 6.3134417680130985')
cmd.alter('resi 3', 'b = 9.879473685798931')
cmd.alter('resi 4', 'b = 1.9688225921920035')
cmd.alter('resi 5', 'b = 4.350825379227277')
cmd.alter('resi 6', 'b = 2.9975767711138923')
cmd.alter('resi 7', 'b = 2.2208808264390374')
cmd.alter('resi 8', 'b = 7.171138282620458')
cmd.alter('resi 9', 'b = 10.987701225509095')
cmd.alter('resi 10', 'b = 0.0014446334729110073')
cmd.alter('resi 11', 'b = 0.2934892012909697')
cmd.alter('resi 12', 'b = 6.355344417665372')
cmd.alter('resi 13', 'b = 4.812472436255967')
cmd.alter('resi 14', 'b = 4.373630990834902')
cmd.alter('resi 15', 'b = 4.479211361741696')
cmd.alter('resi 16', 'b = 1.5670443019984224')
cmd.alter('resi 17', 'b = 3.7775272934861137')
cmd.alter('resi 18', 'b = 0.6582092318224498')
cmd.alter('resi 19', 'b = 0.3313049904669509')
cmd.alter('resi 20', 'b = 1.0271393261984283')
cmd.alter('resi 21', 'b = 1.3915501579484362')
cmd.alter('resi 22', 'b = 13.569849956447769')
cmd.alter('resi 23', 'b = 9.611357395406754')
cmd.alter('resi 24', 'b = 9.234063448642203')
cmd.alter('resi 25', 'b = 7.147304697641548')
cmd.alter('resi 26', 'b = 1.6496267066768338')
cmd.alter('resi 27', 'b = 3.816275146998103')
cmd.alter('resi 28', 'b = 4.18137380132864')
cmd.alter('resi 29', 'b = 5.974683092983375')
cmd.alter('resi 30', 'b = 9.038557487608877')
cmd.alter('resi 31', 'b = 3.5421497912223154')
cmd.alter('resi 32', 'b = 5.365467976544083')
cmd.alter('resi 33', 'b = 2.2247244572592146')
cmd.alter('resi 34', 'b = 0.3792853358784936')
cmd.alter('resi 35', 'b = 6.4800101268885655')
cmd.alter('resi 36', 'b = 4.9556257760032105')
cmd.alter('resi 37', 'b = 5.319012734121881')
cmd.alter('resi 38', 'b = 2.2303914120940465')
cmd.alter('resi 39', 'b = 2.127387871724669')
cmd.alter('resi 40', 'b = 7.464412394596598')
cmd.alter('resi 41', 'b = 4.309001292095663')
cmd.alter('resi 42', 'b = 0.8094762688585773')
cmd.alter('resi 43', 'b = 2.596709128829477')
cmd.alter('resi 44', 'b = 5.104530229488189')
cmd.alter('resi 45', 'b = 1.5377562344088764')
cmd.alter('resi 46', 'b = 1.692264269100633')
cmd.alter('resi 47', 'b = 2.928551441291986')
cmd.alter('resi 48', 'b = 4.374779625307049')
cmd.alter('resi 49', 'b = 3.006592488059678')
cmd.alter('resi 50', 'b = 4.799257522017612')
cmd.alter('resi 51', 'b = 1.3616125274485609')
cmd.alter('resi 52', 'b = 2.5802667126211905')
cmd.alter('resi 53', 'b = 2.7465430619873548')
cmd.alter('resi 54', 'b = 0.2700966827227678')
cmd.alter('resi 55', 'b = 1.8855862189571424')
cmd.alter('resi 56', 'b = 0.6961164293734314')
cmd.alter('resi 57', 'b = 2.406860126025938')
cmd.alter('resi 58', 'b = 1.8239317053294497')
cmd.alter('resi 59', 'b = 0.5633015304256898')
cmd.alter('resi 60', 'b = 4.70418305930079')
cmd.alter('resi 61', 'b = 3.1151361649745057')
cmd.alter('resi 62', 'b = 6.62884748281815')
cmd.alter('resi 63', 'b = 0.8499478605572834')
cmd.alter('resi 64', 'b = 7.58903386178208')
cmd.alter('resi 65', 'b = 2.166052864587225')
cmd.alter('resi 66', 'b = 2.1156994205504724')
cmd.alter('resi 67', 'b = 1.5584075215434745')
cmd.alter('resi 68', 'b = 0.6166874466615844')
cmd.alter('resi 69', 'b = 15.621492833118868')
cmd.alter('resi 70', 'b = 1.125291207100379')
cmd.alter('resi 71', 'b = 0.13024124428145334')
cmd.alter('resi 72', 'b = 0.7915639840071175')
cmd.alter('resi 73', 'b = 3.3119724592740085')
cmd.alter('resi 74', 'b = 0.8924741397394741')
cmd.alter('resi 75', 'b = 1.5692733738403908')
cmd.alter('resi 76', 'b = 3.2313731449196306')
cmd.alter('resi 77', 'b = 0.5582416660509151')
cmd.alter('resi 78', 'b = 0.5845938890043758')
cmd.alter('resi 79', 'b = 1.1311368612564856')
cmd.alter('resi 80', 'b = 1.787012156159559')
cmd.alter('resi 81', 'b = 1.6897558468914666')
cmd.alter('resi 82', 'b = 9.821372997877994')
cmd.alter('resi 83', 'b = 2.792996153025274')
cmd.alter('resi 84', 'b = 5.959873881051795')
cmd.alter('resi 85', 'b = 8.281068524411818')
cmd.alter('resi 86', 'b = 3.2350971141530973')
cmd.alter('resi 87', 'b = 0.9051516246506311')
cmd.alter('resi 88', 'b = 4.44300984275183')
cmd.alter('resi 89', 'b = 5.116541081744867')
cmd.alter('resi 90', 'b = 3.9455033518483726')
cmd.alter('resi 91', 'b = 1.189728352082827')
cmd.alter('resi 92', 'b = 0.4566733021103802')
cmd.alter('resi 93', 'b = 2.13995084643844')
cmd.alter('resi 94', 'b = 2.7975228313712863')
cmd.alter('resi 95', 'b = 1.6501980617350274')
cmd.alter('resi 96', 'b = 2.150741640538531')
cmd.alter('resi 97', 'b = 1.8009300460112243')
cmd.alter('resi 98', 'b = 0.23670966415924385')
cmd.alter('resi 99', 'b = 1.8108554376820825')
cmd.alter('resi 100', 'b = 0.8483021740617487')
cmd.alter('resi 101', 'b = 0.21954953965585444')
cmd.alter('resi 102', 'b = 0.8700583019599839')
cmd.alter('resi 103', 'b = 0.7969506244636421')
cmd.alter('resi 104', 'b = 1.7806031229591206')
cmd.alter('resi 105', 'b = 2.5964845881049547')
cmd.alter('resi 106', 'b = 3.983628016972921')
cmd.alter('resi 107', 'b = 1.0766344816196705')
cmd.alter('resi 108', 'b = 0.07621424597057525')
cmd.alter('resi 109', 'b = 5.401571960907682')
cmd.alter('resi 110', 'b = 2.168099695718269')
cmd.alter('resi 111', 'b = 2.909472836987168')
cmd.alter('resi 112', 'b = 1.804796062854157')
cmd.alter('resi 113', 'b = 0.9341509113143358')
cmd.alter('resi 114', 'b = 1.365846223625213')
cmd.alter('resi 115', 'b = 0.5593636557874977')
cmd.alter('resi 116', 'b = 0.7393919775417817')
cmd.alter('resi 117', 'b = 9.770653498512994')
cmd.alter('resi 118', 'b = 0.2829037622815724')
cmd.alter('resi 119', 'b = 0.8991618047551294')
cmd.alter('resi 120', 'b = 1.4295931479725048')
cmd.alter('resi 121', 'b = 3.337069432530239')
cmd.alter('resi 122', 'b = 1.8754008577862311')
cmd.alter('resi 123', 'b = 1.1541075024740106')
cmd.alter('resi 124', 'b = 1.6940346104848811')
cmd.alter('resi 125', 'b = 0.4394099754808688')
cmd.alter('resi 126', 'b = 1.8062635229398984')
cmd.alter('resi 127', 'b = 0.1848233569328496')
cmd.alter('resi 128', 'b = 1.9710695080113396')
cmd.alter('resi 129', 'b = 2.677597362523785')
cmd.alter('resi 130', 'b = 3.329794389141439')
cmd.alter('resi 131', 'b = 1.0485543993384168')
cmd.alter('resi 132', 'b = 0.12653430630026805')
cmd.alter('resi 133', 'b = 0.8518411244552725')
cmd.alter('resi 134', 'b = 0.4454619927609473')
cmd.alter('resi 135', 'b = 0.7779175781065274')
cmd.alter('resi 136', 'b = 9.891331392680641')
cmd.alter('resi 137', 'b = 3.8245438988031752')
cmd.alter('resi 138', 'b = 2.962781993043972')
cmd.alter('resi 139', 'b = 3.8887807474922536')
cmd.alter('resi 140', 'b = 3.972392780473684')
cmd.alter('resi 141', 'b = 2.5585977008823573')
cmd.alter('resi 142', 'b = 3.253138966457221')
cmd.alter('resi 143', 'b = 0.9740170753509289')
cmd.alter('resi 144', 'b = 9.598276898825503')
cmd.alter('resi 145', 'b = 3.287341907528202')
cmd.alter('resi 146', 'b = 11.086491275999458')
cmd.alter('resi 147', 'b = 17.721947046914337')
cmd.alter('resi 148', 'b = 1.7185568080662212')
cmd.alter('resi 149', 'b = 1.9957247071909452')
cmd.alter('resi 150', 'b = 17.345380056247098')
cmd.alter('resi 151', 'b = 2.5214006951432015')
cmd.alter('resi 152', 'b = 3.4853609472264684')
cmd.alter('resi 153', 'b = 3.897498043586688')
cmd.alter('resi 154', 'b = 6.917479537157465')
cmd.alter('resi 155', 'b = 3.842875799794203')
cmd.alter('resi 156', 'b = 8.081846587659932')
cmd.alter('resi 157', 'b = 0.5920234492323955')
cmd.alter('resi 158', 'b = 12.652284401623044')
cmd.alter('resi 159', 'b = 5.208914385872462')
cmd.alter('resi 160', 'b = 1.7574699588076403')
cmd.alter('resi 161', 'b = 8.218667071492625')
cmd.alter('resi 162', 'b = 7.117230015855362')
cmd.alter('resi 163', 'b = 11.509093270922609')
cmd.alter('resi 164', 'b = 2.0161972850237246')
cmd.alter('resi 165', 'b = 4.046559586572111')
cmd.alter('resi 166', 'b = 3.361109272867161')
cmd.alter('resi 167', 'b = 1.1020223449858273')
cmd.alter('resi 168', 'b = 2.5833493941528647')
cmd.alter('resi 169', 'b = 17.847212570362874')
cmd.alter('resi 170', 'b = 7.225301642065469')
cmd.alter('resi 171', 'b = 1.4945289788269767')
cmd.alter('resi 172', 'b = 4.412658392528269')
cmd.alter('resi 173', 'b = 10.794446747431653')
cmd.alter('resi 174', 'b = 3.906265202646676')
cmd.alter('resi 175', 'b = 12.219633568273673')
cmd.alter('resi 176', 'b = 9.823427543093842')
cmd.alter('resi 177', 'b = 2.667655622563562')
cmd.alter('resi 178', 'b = 6.062248984983124')
cmd.alter('resi 179', 'b = 7.528619281734804')
cmd.alter('resi 180', 'b = 0.2480204405677972')
cmd.alter('resi 181', 'b = 0.4971747461080662')
cmd.alter('resi 182', 'b = 18.00790220487858')
cmd.alter('resi 183', 'b = 17.79514586208516')
cmd.alter('resi 184', 'b = 6.548964570303018')
cmd.alter('resi 185', 'b = 6.749344056870758')
cmd.alter('resi 186', 'b = 6.693945764107583')
cmd.alter('resi 187', 'b = 4.329483885006739')
cmd.alter('resi 188', 'b = 4.963079085843704')
cmd.alter('resi 189', 'b = 4.220866224852982')
cmd.alter('resi 190', 'b = 6.655836897448022')
cmd.alter('resi 191', 'b = 2.8392884329651635')
cmd.alter('resi 192', 'b = 6.898806305132957')
cmd.alter('resi 193', 'b = 2.4749582325079755')
cmd.alter('resi 194', 'b = 2.5108049751966024')
cmd.alter('resi 195', 'b = 0.8838458225604928')
cmd.alter('resi 196', 'b = 0.19891416709916987')
cmd.alter('resi 197', 'b = 3.713086006554013')
cmd.alter('resi 198', 'b = 1.749374129680196')
cmd.alter('resi 199', 'b = 2.6613890205114483')
cmd.alter('resi 200', 'b = 0.0795449586412152')
cmd.alter('resi 201', 'b = 0.3125162238855929')
cmd.alter('resi 202', 'b = 0.0')
cmd.alter('resi 203', 'b = 2.8417982414624734')
cmd.alter('resi 204', 'b = 1.2474643039313251')
cmd.alter('resi 205', 'b = 2.7026526541175286')
cmd.alter('resi 206', 'b = 1.2029574786679378')
cmd.alter('resi 207', 'b = 6.71963594699419')
cmd.alter('resi 208', 'b = 0.4806216600133581')
cmd.alter('resi 209', 'b = 0.23603238849119626')
cmd.alter('resi 210', 'b = 2.8666017056600563')
cmd.alter('resi 211', 'b = 5.576053369179224')
cmd.alter('resi 212', 'b = 5.4634149940442285')
cmd.alter('resi 213', 'b = 1.7178317319974392')
cmd.alter('resi 214', 'b = 1.3345156635436728')
cmd.alter('resi 215', 'b = 14.832834404048267')
cmd.alter('resi 216', 'b = 7.182397548089299')
cmd.alter('resi 217', 'b = 2.5474685718235555')
cmd.alter('resi 218', 'b = 2.1480098304904462')
cmd.alter('resi 219', 'b = 3.0999890302979614')
cmd.alter('resi 220', 'b = 1.824416469987596')
cmd.alter('resi 221', 'b = 2.832764547249049')
cmd.alter('resi 222', 'b = 5.966438147579032')
cmd.alter('resi 223', 'b = 4.927312675866571')
cmd.alter('resi 224', 'b = 8.49738057701521')
cmd.alter('resi 225', 'b = 5.317403636726628')
cmd.alter('resi 226', 'b = 1.6279919504581648')
cmd.alter('resi 227', 'b = 1.0957869141353471')
cmd.alter('resi 228', 'b = 13.827680672088242')
cmd.alter('resi 229', 'b = 2.4269248345947627')
cmd.alter('resi 230', 'b = 3.1715813400812487')
cmd.alter('resi 231', 'b = 1.1130193148421446')
cmd.alter('resi 232', 'b = 4.3560683296282825')
cmd.alter('resi 233', 'b = 2.082477862924709')
cmd.alter('resi 234', 'b = 0.8278919046564751')
cmd.alter('resi 235', 'b = 10.253248826563684')
cmd.alter('resi 236', 'b = 4.583807726191057')
cmd.alter('resi 237', 'b = 1.4994155090033658')
cmd.alter('resi 238', 'b = 2.2084380022615475')
cmd.alter('resi 239', 'b = 3.0510658408533438')
cmd.alter('resi 240', 'b = 3.5579698938402413')
cmd.alter('resi 241', 'b = 3.0429526412851238')
cmd.alter('resi 242', 'b = 1.941112495225076')
cmd.alter('resi 243', 'b = 0.9088230148076066')
cmd.alter('resi 244', 'b = 0.755964826359494')
cmd.alter('resi 245', 'b = 2.649705788668434')
cmd.alter('resi 246', 'b = 4.628594604490731')
cmd.alter('resi 247', 'b = 0.8770035274801147')
cmd.alter('resi 248', 'b = 10.551711741968703')
cmd.alter('resi 249', 'b = 2.575197102660004')
cmd.alter('resi 250', 'b = 3.3584374057382096')
cmd.alter('resi 251', 'b = 5.1271522915604315')
cmd.alter('resi 252', 'b = 1.9393198739398851')
cmd.alter('resi 253', 'b = 1.2369427944512823')
cmd.alter('resi 254', 'b = 7.020528420760013')
cmd.alter('resi 255', 'b = 10.280544808428925')
cmd.alter('resi 256', 'b = 4.749987753105394')
cmd.alter('resi 257', 'b = 19.53610532288629')
cmd.alter('resi 258', 'b = 3.3031204784758788')
cmd.alter('resi 259', 'b = 1.1703684628412896')
cmd.alter('resi 260', 'b = 4.9401813916804125')
cmd.alter('resi 261', 'b = 6.715283791987598')
cmd.alter('resi 262', 'b = 1.224340441361454')
cmd.alter('resi 263', 'b = 1.6073980870984304')
cmd.alter('resi 264', 'b = 3.092440954309815')
cmd.alter('resi 265', 'b = 3.9294340087698867')
cmd.alter('resi 266', 'b = 3.3285695632256234')
cmd.alter('resi 267', 'b = 0.9453020452216236')
cmd.alter('resi 268', 'b = 1.162603840700944')
cmd.alter('resi 269', 'b = 1.3012129320625727')
cmd.alter('resi 270', 'b = 0.6117738881713721')
cmd.alter('resi 271', 'b = 12.01437517944813')
cmd.alter('resi 272', 'b = 3.7250608844442983')
cmd.alter('resi 273', 'b = 5.065309674641896')
cmd.alter('resi 274', 'b = 19.33306763782897')
cmd.alter('resi 275', 'b = 1.9835615641054256')
cmd.alter('resi 276', 'b = 1.9729750215514332')
cmd.alter('resi 277', 'b = 0.8909753322724336')
cmd.alter('resi 278', 'b = 1.3491611507185726')
cmd.alter('resi 279', 'b = 1.1028239013987862')
cmd.alter('resi 280', 'b = 0.896550016387211')
cmd.alter('resi 281', 'b = 3.497020329820613')
cmd.alter('resi 282', 'b = 0.4420550881045572')
cmd.alter('resi 283', 'b = 1.1932853073653913')
cmd.alter('resi 284', 'b = 4.959192290482187')
cmd.alter('resi 285', 'b = 0.8601160115493156')
cmd.alter('resi 286', 'b = 2.4670602467917826')
cmd.alter('resi 287', 'b = 1.2589192645413352')
cmd.alter('resi 288', 'b = 0.927605057844986')
cmd.alter('resi 289', 'b = 1.1389066485544523')
cmd.alter('resi 290', 'b = 0.3466744715298428')
cmd.alter('resi 291', 'b = 3.5215362720015735')
cmd.alter('resi 292', 'b = 4.995873956740889')
cmd.alter('resi 293', 'b = 3.865213559420765')
cmd.alter('resi 294', 'b = 1.8489750362499415')
cmd.alter('resi 295', 'b = 1.9325470546703134')
cmd.alter('resi 296', 'b = 0.1497209490666299')
cmd.alter('resi 297', 'b = 1.3612220608273016')
cmd.alter('resi 298', 'b = 1.2275659812633024')
cmd.alter('resi 299', 'b = 0.3193363189263873')
cmd.alter('resi 300', 'b = 3.52038675908196')
cmd.alter('resi 301', 'b = 1.8791843486957482')
cmd.alter('resi 302', 'b = 0.4390292830632512')
cmd.alter('resi 303', 'b = 7.834891921671085')
cmd.alter('resi 304', 'b = 7.079232420782912')
cmd.alter('resi 305', 'b = 1.2492768280462572')
cmd.alter('resi 306', 'b = 2.6276784387621857')
cmd.alter('resi 307', 'b = 1.3458939931052465')
cmd.alter('resi 308', 'b = 2.0544633168741018')
cmd.alter('resi 309', 'b = 19.326745099761172')
cmd.alter('resi 310', 'b = 2.0851823293539025')
cmd.alter('resi 311', 'b = 1.6583092594565565')
cmd.alter('resi 312', 'b = 2.1653054889702266')
cmd.alter('resi 313', 'b = 1.3849017480566357')
cmd.alter('resi 314', 'b = 0.9969674033472428')
cmd.alter('resi 315', 'b = 0.9967524160089264')
cmd.alter('resi 316', 'b = 2.4524518203035965')
cmd.alter('resi 317', 'b = 1.88075273431606')
cmd.alter('resi 318', 'b = 2.828814712543513')
cmd.alter('resi 319', 'b = 1.1558093617447014')
cmd.alter('resi 320', 'b = 1.4959250414198524')
cmd.alter('resi 321', 'b = 0.35258012900069263')
cmd.alter('resi 322', 'b = 5.150896246719887')
cmd.alter('resi 323', 'b = 19.96210034915012')
cmd.alter('resi 324', 'b = 0.5356129869540507')
cmd.alter('resi 325', 'b = 1.8127258330089804')
cmd.alter('resi 326', 'b = 2.5628852525067947')
cmd.alter('resi 327', 'b = 1.8785656138971127')
cmd.alter('resi 328', 'b = 4.762852120349003')
cmd.alter('resi 329', 'b = 2.845138977253156')
cmd.alter('resi 330', 'b = 1.1743051458850455')
cmd.alter('resi 331', 'b = 2.7573554619247886')
cmd.alter('resi 332', 'b = 3.801087008036989')
cmd.alter('resi 333', 'b = 2.565604434457834')
cmd.alter('resi 334', 'b = 1.2028723199168947')
cmd.alter('resi 335', 'b = 2.175781194956567')
cmd.alter('resi 336', 'b = 3.6166255402872416')
cmd.alter('resi 337', 'b = 1.700791453559914')
cmd.alter('resi 338', 'b = 2.552641725958058')
cmd.alter('resi 339', 'b = 12.896342602703946')
cmd.alter('resi 340', 'b = 1.1538573368298928')
cmd.alter('resi 341', 'b = 0.3532034391709825')
cmd.alter('resi 342', 'b = 1.5559159187832046')
cmd.alter('resi 343', 'b = 3.683941085703143')
cmd.alter('resi 344', 'b = 0.6731843419950958')
cmd.alter('resi 345', 'b = 1.2888536129271844')
cmd.alter('resi 346', 'b = 0.5364725344024333')
cmd.alter('resi 347', 'b = 1.6774379153893526')
cmd.alter('resi 348', 'b = 1.282893547689019')
cmd.alter('resi 349', 'b = 0.1170514748085278')
cmd.alter('resi 350', 'b = 0.5051748946812309')
cmd.alter('resi 351', 'b = 5.3161766839817455')
cmd.alter('resi 352', 'b = 0.34119402899755')
cmd.alter('resi 353', 'b = 0.10399178137459847')
cmd.alter('resi 354', 'b = 1.7142172712643862')
cmd.alter('resi 355', 'b = 8.762200599897655')
cmd.alter('resi 356', 'b = 1.7750607136470054')
cmd.alter('resi 357', 'b = 14.032147290913132')
cmd.alter('resi 358', 'b = 0.2927998511898382')
cmd.alter('resi 359', 'b = 2.1970441888935657')
cmd.alter('resi 360', 'b = 0.22443815374233453')
cmd.alter('resi 361', 'b = 4.545685851777739')
cmd.alter('resi 362', 'b = 11.315285821016293')
cmd.alter('resi 363', 'b = 2.39395802679473')
cmd.alter('resi 364', 'b = 1.7118100805535017')
cmd.alter('resi 365', 'b = 1.0611277880815')
cmd.alter('resi 366', 'b = 0.3627086013552475')
cmd.alter('resi 367', 'b = 2.6958390810553854')
cmd.alter('resi 368', 'b = 1.146300329638625')
cmd.alter('resi 369', 'b = 2.2503513090864344')
cmd.alter('resi 370', 'b = 2.4561713451061564')
cmd.alter('resi 371', 'b = 0.6638969765345518')
cmd.alter('resi 372', 'b = 1.1414761514094305')
cmd.alter('resi 373', 'b = 1.9695841355141923')
cmd.alter('resi 374', 'b = 5.560991682280985')
cmd.alter('resi 375', 'b = 5.282475960748216')
cmd.alter('resi 376', 'b = 11.358961105362544')
cmd.alter('resi 377', 'b = 0.0')
cmd.alter('resi 378', 'b = 0.09783127571662276')
cmd.alter('resi 379', 'b = 1.7814132660536612')
cmd.alter('resi 380', 'b = 0.4591533265005706')
cmd.alter('resi 381', 'b = 2.85649506337937')
cmd.alter('resi 382', 'b = 0.0')
cmd.alter('resi 383', 'b = 2.966408202316732')
cmd.alter('resi 384', 'b = 1.6289369078810063')
cmd.alter('resi 385', 'b = 2.3708095257306403')
cmd.alter('resi 386', 'b = 2.412307444628107')
cmd.alter('resi 387', 'b = 5.471589586853478')
cmd.alter('resi 388', 'b = 2.160213478784745')
cmd.alter('resi 389', 'b = 0.5162143183773968')
cmd.alter('resi 390', 'b = 2.101892057156475')
cmd.alter('resi 391', 'b = 5.282119494577539')
cmd.alter('resi 392', 'b = 5.355817855197891')
cmd.alter('resi 393', 'b = 1.066048027387548')
cmd.alter('resi 394', 'b = 0.5495143002475351')
cmd.alter('resi 395', 'b = 3.7105871763428864')
cmd.alter('resi 396', 'b = 3.304452394187828')
cmd.alter('resi 397', 'b = 1.040142558382962')
cmd.alter('resi 398', 'b = 2.0710130798014754')
cmd.alter('resi 399', 'b = 4.288292902155528')
cmd.alter('resi 400', 'b = 1.3407098422385104')
cmd.alter('resi 401', 'b = 3.44505627530591')
cmd.alter('resi 402', 'b = 1.9108465921042936')
cmd.alter('resi 403', 'b = 2.5367662570985066')
cmd.alter('resi 404', 'b = 5.463370790422004')
cmd.alter('resi 405', 'b = 1.4403787544620086')
cmd.alter('resi 406', 'b = 0.09845081985790974')
cmd.alter('resi 407', 'b = 1.1099556657071508')
cmd.alter('resi 408', 'b = 0.0')
cmd.alter('resi 409', 'b = 3.1988744729766925')
cmd.alter('resi 410', 'b = 0.4475266540516121')
cmd.alter('resi 411', 'b = 0.3492210621043739')
cmd.alter('resi 412', 'b = 1.288084571838065')
cmd.alter('resi 413', 'b = 0.1611552655573492')
cmd.alter('resi 414', 'b = 1.9628580598555645')
cmd.alter('resi 415', 'b = 0.16141286333713134')
cmd.alter('resi 416', 'b = 9.578694626300091')
cmd.alter('resi 417', 'b = 0.3755257909293266')
cmd.alter('resi 418', 'b = 0.947722725076056')
cmd.alter('resi 419', 'b = 0.5038138577995479')
cmd.alter('resi 420', 'b = 1.7734155024870255')
cmd.alter('resi 421', 'b = 2.7935368696667124')
cmd.alter('resi 422', 'b = 1.3408387724517412')
cmd.alter('resi 423', 'b = 1.9506036769129944')
cmd.alter('resi 424', 'b = 0.3896275582558165')
cmd.alter('resi 425', 'b = 1.6156691301704966')
cmd.alter('resi 426', 'b = 0.4304618239311304')
cmd.alter('resi 427', 'b = 0.5288512012734279')
cmd.alter('resi 428', 'b = 1.680072496590285')
cmd.alter('resi 429', 'b = 12.46324753992378')
cmd.alter('resi 430', 'b = 11.149771515964844')
cmd.alter('resi 431', 'b = 0.518602127530139')
cmd.alter('resi 432', 'b = 2.4904850058736403')
cmd.alter('resi 433', 'b = 1.0199033668215958')
cmd.alter('resi 434', 'b = 0.6894948441869281')
cmd.alter('resi 435', 'b = 1.0125346900233172')
cmd.alter('resi 436', 'b = 2.210149529411312')
cmd.alter('resi 437', 'b = 3.5942435011458147')
cmd.alter('resi 438', 'b = 1.450235762589384')
cmd.alter('resi 439', 'b = 0.7238817848574185')
cmd.alter('resi 440', 'b = 6.130829731718893')
cmd.alter('resi 441', 'b = 2.096958549665428')
cmd.alter('resi 442', 'b = 3.8293648325036527')
cmd.alter('resi 443', 'b = 1.1470180562063776')
cmd.alter('resi 444', 'b = 0.16128801360040995')
cmd.alter('resi 445', 'b = 1.8875255532029085')
cmd.alter('resi 446', 'b = 3.8888851025517215')
cmd.alter('resi 447', 'b = 1.4280963520494558')
cmd.alter('resi 448', 'b = 0.9715186870499164')
cmd.alter('resi 449', 'b = 2.8533458003257484')
cmd.alter('resi 450', 'b = 1.921366461205725')
cmd.alter('resi 451', 'b = 1.6013607449984826')
cmd.alter('resi 452', 'b = 2.4724380309303995')
cmd.alter('resi 453', 'b = 1.9846041210866427')
cmd.alter('resi 454', 'b = 2.1264249306246352')
cmd.alter('resi 455', 'b = 0.19110936985679106')
cmd.alter('resi 456', 'b = 3.1245411085150647')
cmd.alter('resi 457', 'b = 3.2199432194459')
cmd.alter('resi 458', 'b = 6.5741903872766905')
cmd.alter('resi 459', 'b = 4.1131951989340605')
cmd.alter('resi 460', 'b = 2.0660690641355144')
cmd.alter('resi 461', 'b = 0.3824453725096481')
cmd.alter('resi 462', 'b = 1.708176490490496')
cmd.alter('resi 463', 'b = 2.111264681631205')
cmd.alter('resi 464', 'b = 1.454257684708464')
cmd.alter('resi 465', 'b = 1.6665470161137843')
cmd.alter('resi 466', 'b = 0.3588295552785317')
cmd.alter('resi 467', 'b = 1.2752449564228918')
cmd.alter('resi 468', 'b = 2.4848402394043925')
cmd.alter('resi 469', 'b = 0.4593378734889837')
cmd.alter('resi 470', 'b = 0.3171668035592444')
cmd.alter('resi 471', 'b = 2.1205518854345646')
cmd.alter('resi 472', 'b = 0.3989780011865361')
cmd.alter('resi 473', 'b = 2.6171443430178245')
cmd.alter('resi 474', 'b = 1.9597281383453424')
cmd.alter('resi 475', 'b = 1.477687051027741')
cmd.alter('resi 476', 'b = 1.2082009686754451')
cmd.alter('resi 477', 'b = 0.8838993682466407')
cmd.alter('resi 478', 'b = 1.1917170229209728')
cmd.alter('resi 479', 'b = 0.21660785927439846')
cmd.alter('resi 480', 'b = 0.6391681342898466')
cmd.alter('resi 481', 'b = 0.6643649343249418')
cmd.alter('resi 482', 'b = 0.8137928690326994')
cmd.alter('resi 483', 'b = 5.482738011443006')
cmd.alter('resi 484', 'b = 1.1075776070012875')
cmd.alter('resi 485', 'b = 2.190789500901941')
cmd.alter('resi 486', 'b = 1.406711954540622')
cmd.alter('resi 487', 'b = 1.0700640430089432')
cmd.alter('resi 488', 'b = 4.8415060822770375')
cmd.alter('resi 489', 'b = 4.2890927716599085')
cmd.alter('resi 490', 'b = 1.5937007709585902')
cmd.alter('resi 491', 'b = 0.4513347144460042')
cmd.alter('resi 492', 'b = 0.3376941602011133')
cmd.alter('resi 493', 'b = 0.4364653783537511')
cmd.alter('resi 494', 'b = 0.6349599635309027')
cmd.alter('resi 495', 'b = 1.8955343247811591')
cmd.alter('resi 496', 'b = 2.043793181439284')
cmd.alter('resi 497', 'b = 1.4969010327436092')
cmd.alter('resi 498', 'b = 1.5881394435627247')
cmd.alter('resi 499', 'b = 0.7504989880699009')
cmd.alter('resi 500', 'b = 0.04157563352381394')
cmd.alter('resi 501', 'b = 0.8601353355485217')
cmd.alter('resi 502', 'b = 1.9095568577441144')
cmd.alter('resi 503', 'b = 0.13079765499915538')
cmd.alter('resi 504', 'b = 1.4334685411068149')
cmd.alter('resi 505', 'b = 0.2959870448793059')
cmd.alter('resi 506', 'b = 1.084425277171913')
cmd.alter('resi 507', 'b = 1.8223867154435087')
cmd.alter('resi 508', 'b = 0.6195282609297231')
cmd.alter('resi 509', 'b = 0.4563889694179837')
cmd.alter('resi 510', 'b = 1.380711882135608')
cmd.alter('resi 511', 'b = 0.6870053539923759')
cmd.alter('resi 512', 'b = 0.8020578455156336')
cmd.alter('resi 513', 'b = 2.646961192563268')
cmd.alter('resi 514', 'b = 5.02774146855924')
cmd.alter('resi 515', 'b = 0.4989023400657671')
cmd.alter('resi 516', 'b = 0.544825533766957')
cmd.alter('resi 517', 'b = 2.372519422893855')
cmd.alter('resi 518', 'b = 1.8948842502634275')
cmd.alter('resi 519', 'b = 3.748147548516312')
cmd.alter('resi 520', 'b = 0.9988890596832852')
cmd.alter('resi 521', 'b = 31.595969315283497')
cmd.alter('resi 522', 'b = 11.01594491475235')
cmd.alter('resi 523', 'b = 17.1360189496529')
cmd.alter('resi 524', 'b = 7.58359771357865')
cmd.alter('resi 525', 'b = 19.10965167312025')
cmd.alter('resi 526', 'b = 11.089069196525793')
cmd.alter('resi 527', 'b = 12.629158653269567')
cmd.alter('resi 528', 'b = 5.509629251227191')
cmd.alter('resi 529', 'b = 1.9327363492119891')
cmd.alter('resi 530', 'b = 1.5358495898388027')
cmd.alter('resi 531', 'b = 1.908422301857124')
cmd.alter('resi 532', 'b = 6.2621689596319925')
cmd.alter('resi 533', 'b = 2.9211928232186244')
cmd.alter('resi 534', 'b = 9.000136419213524')
cmd.alter('resi 535', 'b = 3.8441983962239616')
cmd.alter('resi 536', 'b = 2.0618780716359897')
cmd.alter('resi 537', 'b = 2.058940636904679')
cmd.alter('resi 538', 'b = 2.4414783482429074')
cmd.alter('resi 539', 'b = 1.176304296071301')
cmd.alter('resi 540', 'b = 0.06456825873934367')
cmd.alter('resi 541', 'b = 1.9065411159512928')
cmd.alter('resi 542', 'b = 9.032091242631116')
cmd.alter('resi 543', 'b = 22.707784424991264')
cmd.alter('resi 544', 'b = 0.9504440846036801')
cmd.alter('resi 545', 'b = 6.14652977452502')
cmd.alter('resi 546', 'b = 2.637729774640193')
cmd.alter('resi 547', 'b = 7.999609611181714')
cmd.alter('resi 548', 'b = 0.73405580807014')
cmd.alter('resi 549', 'b = 0.8951599911496779')
cmd.alter('resi 550', 'b = 3.631947636320848')
cmd.alter('resi 551', 'b = 7.475734726040182')
cmd.alter('resi 552', 'b = 0.9223690056674506')
cmd.alter('resi 553', 'b = 1.320487047062752')
cmd.alter('resi 554', 'b = 5.146357608109337')
cmd.alter('resi 555', 'b = 0.7623236035997555')
cmd.alter('resi 556', 'b = 5.367707417913842')
cmd.alter('resi 557', 'b = 1.9758780620916059')
cmd.alter('resi 558', 'b = 3.0745385498250646')
cmd.alter('resi 559', 'b = 1.1587906304956102')
cmd.alter('resi 560', 'b = 4.364159267355232')
cmd.alter('resi 561', 'b = 0.95648657496514')
cmd.alter('resi 562', 'b = 1.7979350550048192')
cmd.alter('resi 563', 'b = 3.0113969810632812')
cmd.alter('resi 564', 'b = 1.6169415180921487')
cmd.alter('resi 565', 'b = 4.252214143592642')
cmd.alter('resi 566', 'b = 3.6603293938870936')
cmd.alter('resi 567', 'b = 2.8265864955153632')
cmd.alter('resi 568', 'b = 2.511415854219014')
cmd.alter('resi 569', 'b = 3.4614302661481995')
cmd.alter('resi 570', 'b = 5.142833225710468')
cmd.alter('resi 571', 'b = 1.181134313477868')
cmd.alter('resi 572', 'b = 3.7869941456774634')
cmd.alter('resi 573', 'b = 7.6470926230365635')
cmd.alter('resi 574', 'b = 1.0451752301495827')
cmd.alter('resi 575', 'b = 0.14805111954121886')
cmd.alter('resi 576', 'b = 0.9092837223513154')
cmd.alter('resi 577', 'b = 0.7670674701786109')
cmd.alter('resi 578', 'b = 8.809672540117646')
cmd.alter('resi 579', 'b = 3.5706086260595296')
cmd.alter('resi 580', 'b = 1.8948328960199252')
cmd.alter('resi 581', 'b = 7.05841357022305')
cmd.alter('resi 582', 'b = 7.207799511284275')
cmd.alter('resi 583', 'b = 1.661442988748346')
cmd.alter('resi 584', 'b = 1.1466563732616024')
cmd.alter('resi 585', 'b = 0.8486712396418964')
cmd.alter('resi 586', 'b = 1.9996615381061045')
cmd.alter('resi 587', 'b = 1.3165858546228693')
cmd.alter('resi 588', 'b = 9.662928782649184')
cmd.alter('resi 589', 'b = 5.333835682937775')
cmd.alter('resi 590', 'b = 1.9182213827479009')
cmd.alter('resi 591', 'b = 3.6234443312101954')
cmd.alter('resi 592', 'b = 0.7897495516060452')
cmd.alter('resi 593', 'b = 2.1517440437403623')
cmd.alter('resi 594', 'b = 8.022727344991736')
cmd.alter('resi 595', 'b = 0.2296067533319371')
cmd.alter('resi 596', 'b = 4.550075040488919')
cmd.alter('resi 597', 'b = 4.105501849955216')
cmd.alter('resi 598', 'b = 9.376103655283927')
cmd.alter('resi 599', 'b = 1.0705622305295928')
cmd.alter('resi 600', 'b = 1.3552925935276687')
cmd.alter('resi 601', 'b = 3.500754382989349')
cmd.alter('resi 602', 'b = 0.29995164722413203')
cmd.alter('resi 603', 'b = 1.2127374936508577')
cmd.alter('resi 604', 'b = 1.9227132048386515')
cmd.alter('resi 605', 'b = 2.9081892275640424')
cmd.alter('resi 606', 'b = 7.940305852840552')
cmd.alter('resi 607', 'b = 9.027634087464195')
cmd.alter('resi 608', 'b = 4.147917582437722')
cmd.alter('resi 609', 'b = 1.5001508994547126')
cmd.alter('resi 610', 'b = 2.948892767269049')
cmd.alter('resi 611', 'b = 2.834169771446777')
cmd.alter('resi 612', 'b = 4.9665106640484815')
cmd.alter('resi 613', 'b = 3.5988434685524093')
cmd.alter('resi 614', 'b = 2.46838405276406')
cmd.alter('resi 615', 'b = 3.017885026852105')
cmd.alter('resi 616', 'b = 3.0070138297747144')
cmd.alter('resi 617', 'b = 1.1784351167238605')
cmd.alter('resi 618', 'b = 0.9677624962544844')
cmd.alter('resi 619', 'b = 1.5642797356750635')
cmd.alter('resi 620', 'b = 3.4123833592135115')
cmd.alter('resi 621', 'b = 4.003450090698839')
cmd.alter('resi 622', 'b = 3.9318313294281935')
cmd.alter('resi 623', 'b = 2.1083705362045633')
cmd.alter('resi 624', 'b = 4.315570589360371')
cmd.alter('resi 625', 'b = 5.774705868593421')
cmd.alter('resi 626', 'b = 4.5635826760538825')
cmd.alter('resi 627', 'b = 18.009501233861478')
cmd.alter('resi 628', 'b = 2.340185000210988')
cmd.alter('resi 629', 'b = 0.8704370840081254')
cmd.alter('resi 630', 'b = 1.0715157924801002')
cmd.alter('resi 631', 'b = 2.5552796683502668')
cmd.alter('resi 632', 'b = 1.4769494853558172')
cmd.alter('resi 633', 'b = 1.0871095134746')
cmd.alter('resi 634', 'b = 4.861039411204058')
cmd.alter('resi 635', 'b = 5.890011954778791')
cmd.alter('resi 636', 'b = 2.128291392817934')
cmd.alter('resi 637', 'b = 1.1654520683986205')
cmd.alter('resi 638', 'b = 1.0877107913308826')
cmd.alter('resi 639', 'b = 0.8267458759700019')
cmd.alter('resi 640', 'b = 4.815933716499134')
cmd.alter('resi 641', 'b = 2.217026132876419')
cmd.alter('resi 642', 'b = 1.6031886024490092')
cmd.alter('resi 643', 'b = 4.867777250752533')
cmd.alter('resi 644', 'b = 4.503377073820602')
cmd.alter('resi 645', 'b = 4.6446915255254435')
cmd.alter('resi 646', 'b = 1.8536383431921233')
cmd.alter('resi 647', 'b = 7.531475708596172')
cmd.alter('resi 648', 'b = 15.17262351440026')
cmd.alter('resi 649', 'b = 2.2667425245951964')
cmd.alter('resi 650', 'b = 2.5856388248492097')
cmd.alter('resi 651', 'b = 0.7837877669087341')
cmd.alter('resi 652', 'b = 8.895225483354489')
cmd.alter('resi 653', 'b = 1.6854644169495474')
cmd.alter('resi 654', 'b = 2.7944825504617263')
cmd.alter('resi 655', 'b = 5.064847635360943')
cmd.alter('resi 656', 'b = 1.8588981725704936')
cmd.alter('resi 657', 'b = 4.73372547041037')
cmd.alter('resi 658', 'b = 1.6973302672492443')
cmd.alter('resi 659', 'b = 5.2570068970392105')
cmd.alter('resi 660', 'b = 0.2402485254115593')
cmd.alter('resi 661', 'b = 2.342348449002037')
cmd.alter('resi 662', 'b = 7.573544442453174')
cmd.alter('resi 663', 'b = 0.6240242865170853')
cmd.alter('resi 664', 'b = 10.417300280248163')
cmd.alter('resi 665', 'b = 0.5027638024181741')
cmd.alter('resi 666', 'b = 7.682007613476901')
cmd.alter('resi 667', 'b = 1.4259077920907433')
cmd.alter('resi 668', 'b = 4.249656071561162')
cmd.alter('resi 669', 'b = 14.612706884874823')
cmd.alter('resi 670', 'b = 1.1668426282138071')
cmd.alter('resi 671', 'b = 7.1394369941202775')
cmd.alter('resi 672', 'b = 2.07449688820827')
cmd.alter('resi 673', 'b = 7.0782661585164055')
cmd.alter('resi 674', 'b = 10.589745340272009')
cmd.alter('resi 675', 'b = 3.1585365405334014')
cmd.alter('resi 676', 'b = 9.77449416022883')
cmd.alter('resi 677', 'b = 2.9359920640785084')
cmd.alter('resi 678', 'b = 2.982773473492276')
cmd.alter('resi 679', 'b = 6.373110604496367')
cmd.alter('resi 680', 'b = 4.997558427204095')
cmd.alter('resi 681', 'b = 7.042368510241582')
cmd.alter('resi 682', 'b = 2.8332020503457795')
cmd.alter('resi 683', 'b = 3.954692559275736')
cmd.alter('resi 684', 'b = 6.294073146558416')
cmd.alter('resi 685', 'b = 3.2039785750727434')
cmd.alter('resi 686', 'b = 2.469442421449753')
cmd.alter('resi 687', 'b = 3.152843283329785')
cmd.alter('resi 688', 'b = 1.0025258597937063')
cmd.alter('resi 689', 'b = 2.3322977531413622')
cmd.alter('resi 690', 'b = 0.9018904464979411')
cmd.alter('resi 691', 'b = 2.121533407204928')
cmd.alter('resi 692', 'b = 2.093362567790196')
cmd.alter('resi 693', 'b = 2.3841460742216567')
cmd.alter('resi 694', 'b = 0.6640216584989846')
cmd.alter('resi 695', 'b = 0.6839030063722937')
cmd.alter('resi 696', 'b = 2.180407044572128')
cmd.alter('resi 697', 'b = 8.291243869328817')
cmd.alter('resi 698', 'b = 5.413004334352076')
cmd.alter('resi 699', 'b = 0.9237940402944608')
cmd.alter('resi 700', 'b = 2.5615097412717907')
cmd.alter('resi 701', 'b = 17.946994170066016')
cmd.alter('resi 702', 'b = 0.6545422632258968')
cmd.alter('resi 703', 'b = 0.7154879692460727')
cmd.alter('resi 704', 'b = 2.163898106233778')
cmd.alter('resi 705', 'b = 0.5039564343281013')
cmd.alter('resi 706', 'b = 0.8912438319570894')
cmd.alter('resi 707', 'b = 1.410971673624249')
cmd.alter('resi 708', 'b = 4.271966131882323')
cmd.alter('resi 709', 'b = 3.6528191133944254')
cmd.alter('resi 710', 'b = 2.9763398660884963')
cmd.alter('resi 711', 'b = 4.708977993057127')
cmd.alter('resi 712', 'b = 2.61443015621225')
cmd.alter('resi 713', 'b = 1.4896152715422866')
cmd.alter('resi 714', 'b = 3.919763186373594')
cmd.alter('resi 715', 'b = 5.008079873636287')
cmd.alter('resi 716', 'b = 0.3648123963152882')
cmd.alter('resi 717', 'b = 0.18597374913731315')
cmd.alter('resi 718', 'b = 0.7712706683263607')
cmd.alter('resi 719', 'b = 1.7110417554855073')
cmd.alter('resi 720', 'b = 1.077882129819355')
cmd.alter('resi 721', 'b = 0.7273386866072591')
cmd.alter('resi 722', 'b = 0.23752808740339945')
cmd.alter('resi 723', 'b = 0.8039054433851052')
cmd.alter('resi 724', 'b = 3.6496632790212153')
cmd.alter('resi 725', 'b = 4.27965849390728')
cmd.alter('resi 726', 'b = 1.9426930770917243')
cmd.alter('resi 727', 'b = 3.7329333960302544')
cmd.alter('resi 728', 'b = 7.552893503631201')
cmd.alter('resi 729', 'b = 1.1477632251290033')
cmd.alter('resi 730', 'b = 0.4684981642358128')
cmd.alter('resi 731', 'b = 1.5802674106699526')
cmd.alter('resi 732', 'b = 2.047957157188419')
cmd.alter('resi 733', 'b = 3.3270991135870496')
cmd.alter('resi 734', 'b = 0.7537012231133965')
cmd.alter('resi 735', 'b = 3.397618410450604')
cmd.alter('resi 736', 'b = 3.4836133514673535')
cmd.alter('resi 737', 'b = 0.7294499916457851')
cmd.alter('resi 738', 'b = 1.3965744698777405')
cmd.alter('resi 739', 'b = 0.717289287847269')
cmd.alter('resi 740', 'b = 3.3164490562338567')
cmd.alter('resi 741', 'b = 1.738794366576634')
cmd.alter('resi 742', 'b = 2.9796776799384084')
cmd.alter('resi 743', 'b = 0.4207436088335482')
cmd.alter('resi 744', 'b = 0.7678436556876671')
cmd.alter('resi 745', 'b = 0.3423997278883776')
cmd.alter('resi 746', 'b = 1.099675856386528')
cmd.alter('resi 747', 'b = 2.2218990386527233')
cmd.alter('resi 748', 'b = 3.5860508860909475')
cmd.alter('resi 749', 'b = 0.7369871963559658')
cmd.alter('resi 750', 'b = 1.6061103711739986')
cmd.alter('resi 751', 'b = 3.9259868622994514')
cmd.alter('resi 752', 'b = 0.4032838548790168')
cmd.alter('resi 753', 'b = 3.905262313371594')
cmd.alter('resi 754', 'b = 2.541607835747872')
cmd.alter('resi 755', 'b = 2.527711014426134')
cmd.alter('resi 756', 'b = 6.500142836511759')
cmd.alter('resi 757', 'b = 8.246433092584747')
cmd.alter('resi 758', 'b = 5.813695418386327')
cmd.alter('resi 759', 'b = 5.238690662506715')

cmd.spectrum('b', 'white_red', 'S009')

###### SETVIEW

cmd.set_view ('\
    -0.632510662,   -0.737213850,   -0.237579703,\
     0.506035805,   -0.161099315,   -0.847335100,\
     0.586391509,   -0.656170785,    0.474955797,\
    -0.000148103,    0.000024185, -318.995605469,\
   -34.610126495,   13.929591179,   32.111713409,\
   251.499099731,  386.493469238,  -20.000000000 ')


###### POSTAMBLE

cmd.select(None)
cmd.set('specular', "off")
cmd.draw(width=1000, height=1000)
cmd.png('{0}_{1}.png'.format(structure, metric), ray=1)
cmd.rotate('y', angle=180)
cmd.draw(width=1000, height=1000)
cmd.png('{0}_{1}_y.png'.format(structure, metric), ray=1)
cmd.rotate('y', angle=180)
cmd.rotate('x', angle=90)
cmd.draw(width=1000, height=1000)
cmd.png('{0}_{1}_x.png'.format(structure, metric), ray=1)