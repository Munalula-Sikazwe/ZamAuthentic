PROVINCES = ['Central Province', 'Copperbelt Province', 'Eastern Province', 'Luapula Province', 'Lusaka Province',
             'Muchinga Province', 'Northern Province', 'North-Western Province', 'Southern Province',
             'Western Province']

DISTRICTS = {
    'Central Province': ['Chibombo', 'Kabwe', 'Kapiri Mposhi', 'Mkushi', 'Mumbwa', 'Serenje'],
    'Copperbelt Province': ['Chililabombwe', 'Chingola', 'Kalulushi', 'Kitwe', 'Luanshya', 'Lufwanyama', 'Masaiti',
                            'Mpongwe', 'Mufulira', 'Ndola'],
    'Eastern Province': ['Chadiza', 'Chipata', 'Katete', 'Lundazi', 'Mambwe', 'Nyimba', 'Petauke'],
    'Luapula Province': ['Chienge', 'Chiengi', 'Kawambwa', 'Mansa', 'Milenge', 'Mwansabombwe', 'Nchelenge', 'Samfya'],
    'Lusaka Province': ['Chilanga', 'Chirundu', 'Kafue', 'Luangwa', 'Lusaka', 'Mumbwa'],
    'Muchinga Province': ['Chama', 'Chinsali', 'Isoka', 'Mpika', 'Mafinga', 'Nakonde'],
    'Northern Province': ['Kasama', 'Luwingu', 'Mporokoso', 'Mpulungu', 'Mbala', 'Nchelenge'],
    'North-Western Province': ['Chavuma', 'Kabompo', 'Kasempa', 'Manyinga', 'Mufumbwe', 'Mwinilunga', 'Solwezi',
                               'Zambezi'],
    'Southern Province': ['Chikankata', 'Choma', 'Gwembe', 'Kalomo', 'Kazungula', 'Livingstone', 'Mazabuka', 'Monze',
                          'Namwala', 'Pemba', 'Siavonga'],
    'Western Province': ['Kalabo', 'Kaoma', 'Lukulu', 'Mongu', 'Senanga', 'Sesheke', 'Shangombo']
}

CONSTITUENCIES = {
    'Chibombo': ['Chibombo Central', 'Kapiri Mposhi East', 'Kapiri Mposhi West'],
    'Kabwe': ['Bwacha', 'Kabwe Central', 'Kabwe North', 'Kabwe South', 'Makeni'],
    'Kapiri Mposhi': ['Chisamba', 'Kapiri Mposhi'],
    'Mkushi': ['Katuba', 'Mkushi North', 'Mkushi South', 'Mumbwa'],
    'Mumbwa': ['Itezhi Tezhi', 'Mumbwa', 'Namwala'],
    'Serenje': ['Chitambo', 'Serenje'],
    'Chililabombwe': ['Chingola Central', 'Kampamba', 'Lubengele', 'Lulamba', 'Lumwana', 'Mambilima', 'Musenga'],
    'Chingola': ['Buntungwa', 'Chikola', 'Kasompe', 'Lulumbula', 'Nchanga', 'Nchanga South', 'Nsobo', 'Tuntulu'],
    'Kalulushi': ['Buntungwa', 'Kantanshi', 'Kashitu', 'Kashoka', 'Muntipa', 'Nkana', 'Wusakile'],
    'Kitwe': ['Buchichi', 'Bulangililo', 'Chamboli', 'Chimwemwe', 'Chisokone', 'Garden', 'Kamfinsa', 'Kamitondo',
              'Mindolo', 'Ndeke', 'Parklands', 'Riverside'],
    'Luanshya': ['Fisenge', 'Kabundi', 'Kafubu', 'Kamakonde', 'Kantanshi', 'Mikomfwa', 'Mpatamatu', 'Roan'],
    'Lufwanyama': ['Chifubu', 'Kakoma', 'Kamfwesa', 'Kampumbu', 'Kapisha', 'Lufwanyama', 'Lumwana East', 'Lumwana West',
                   'Nkana East', 'Sofa'],
    'Masaiti': ['Chambishi', 'Chibuluma', 'Chichele', 'Chiwala', 'Kafulafuta', 'Masaiti', 'Mpongwe', 'Nsansa'],
    'Mpongwe': ['Fisengele', 'Kapiri', 'Mumbwa Chilumba', 'Nsenga', 'Tribal Authority'],
    'Mufulira': ['Bwana Mkubwa', 'Chifubu', 'Chikozya', 'Kantanshi', 'Kashinakazembe', 'Mupambe', 'Mushitala', 'Ndeke',
                 'Shinde', 'Tutwa'],
    'Ndola': ['Chifubu', 'Chimwemwe', 'Kabwe', 'Kafubu', 'Lubuto', 'Masala', 'Mukobeko', 'Nkwazi', 'Pamodzi', 'Tugela',
              'Twapia'],
    'Chadiza': ['Chadiza', 'Kazembe', 'Mwanya'],
    'Chama': ['Chama North', 'Chama South', 'Lumezi'],
    'Chipata': ['Chadiza', 'Chanjuzi', 'Chikuwe', 'Chipangali', 'Jumbe', 'Kapata', 'Kasenengwa', 'Lutembwe', 'Lwangazi',
                'Msanzala', 'Mwale', 'Nsefu', 'Nyimba', 'Petauke Central', 'Petauke', 'Sinda'],
    'Katete': ['Chieftainess Kawaza', 'Katete Central', 'Katete East', 'Mkaika'],
    'Lundazi': ['Chikoka', 'Chiweza', 'Kasenenga', 'Kundabwika', 'Lumezi', 'Lundazi Central', 'Mwase', 'Zozwe'],
    'Mambwe': ['Chiwuyu', 'Mambwe-Lungu', 'Nsenga', 'Nyamphande'],
    'Nyimba': ['Katawa', 'Khothakota', 'Lunzi', 'Nyimba'],
    'Petauke': ['Chitambo', 'Gwembe', 'Kalindawalo', 'Katena', 'Lukusuzi', 'Lusangazi', 'Lwanya', 'Mumbwa Lutzi',
                'Nyika'],

}
wards = {
    'Chibolya': ['Chibolya Ward', 'Chibolya West Ward', 'Kuku Compound'],
    'Chilenje': ['Chilenje Ward', 'Chilenje South Ward', 'Chilenje North Ward', 'Chawama Ward'],
    'Chimwemwe': ['Chimwemwe Ward', 'Helen Kaunda Ward', 'Kanyama Ward'],
    'Chudleigh': ['Chudleigh Ward', 'Munali Ward'],
    'Garden': ['Garden Ward', 'Woodlands Ward'],
    'George': ['George Ward', 'Kalingalinga Ward'],
    'Golf': ['Golf Club Ward', 'Matero Ward'],
    'Itawa': ['Itawa Ward', 'Lilanda Ward'],
    'John Howard': ['John Howard Ward', 'Makululu Ward'],
    'Kabulonga': ['Kabulonga Ward', 'Ibex Hill Ward', 'Kamwala Ward', 'Roma Ward'],
    'Kalingalinga': ['Kalingalinga Ward', "Ng'ombe Ward"],
    'Kamanga': ['Kamanga Ward', 'Ridge Way Ward'],
    'Kuku': ['Kuku Compound'],
    'Makeni': ['Makeni Ward', 'Meanwood Ward', 'Ndeke Village Ward'],
    'Malambo': ['Malambo Ward', 'Mtendere Ward', 'Misisi Ward'],
    'Mandevu': ['Mandevu Ward', 'Matero Ward', 'Mumbwa Road Ward'],
    'Matero': ['Matero Ward'],
    'Munali': ['Munali Ward', 'Vorna Valley Ward'],
    'Ngwerere': ['Ngwerere Ward', 'Chelstone Ward', 'Chibelo Ward'],
    'Northmead': ['Northmead Ward', 'Kabulonga Ward', 'Long Acres Ward'],
    'Nyumba Yanga': ['Nyumba Yanga Ward', 'Ridgeway Ward'],
    'Olympia': ['Olympia Park Ward', 'Olympia Extension Ward', 'Chilenje Ward'],
    'Pamodzi': ['Pamodzi Ward', 'Kabulonga Ward'],
    'Roma': ['Roma Ward', 'Salama Park Ward'],
    'Sosongo': ['Sosongo Ward', 'Lusaka East Ward'],
    'Thorn Park': ['Thorn Park Ward', 'Chelston Ward', 'Kabulonga Ward'],
    'Woodlands': ['Woodlands Ward']
}
towns = {
    'Chibombo': ['Chisamba', 'Chitambo', 'Ichengelo', 'Kabwe', 'Kapiri Mposhi', 'Mkushi', 'Ngabwe'],
    'Kabwe': ['Bwacha', 'Chimanimani', 'Kabwe Central', 'Kabwe East', 'Kabwe West', 'Katondo', 'Makululu'],
    'Kapiri Mposhi': ['Bwacha', 'Kapiri Mposhi', 'Kwamwena', 'Muma', 'Nkondashi', 'Nsenga', 'Tazara'],
    'Mkushi': ['Kanona', 'Lwitikila', 'Mkushi North', 'Mkushi South', 'Ntumbachushi', 'Serenje'],
    'Mumbwa': ['Chibombo', 'Chisamba', 'Munyumbwe', 'Mumbwa Central', 'Musakashi', 'Nangoma', 'Shimabala', 'Chitanda',
               'Mumbwa', 'Mwitwa'],
    'Serenje': ['Chisomo', 'Kanona', 'Kasunko', 'Kateshi', 'Kwika', 'Serenje'],
    'Chililabombwe': ['Chililabombwe Central', 'Hellen', 'Kawama', 'Mimbula', 'Mukulumpe', 'Nchanga'],
    'Chingola': ['Chikola', 'Chingola Central', 'Fisenge', 'Kapisha', 'Kasompe', 'Mukulumpe'],
    'Kalulushi': ['Buntungwa', 'Chambishi', 'Chilenga', 'Kalulushi Central', 'Kantanshi', 'Kashitu', 'Mokambo',
                  'Wusakile'],
    'Kitwe': ['Buchichi', 'Bulangililo', 'Chamboli', 'Chimwemwe', 'Chisokone', 'Chiwala', 'Garden', 'Kamfinsa',
              'Kantanshi', 'Mindolo', 'Nkana', 'Parklands', 'Race Course', 'Wusakile'],
    'Luanshya': ['Fisenge', 'Kamirenda', 'Kansengu', 'Luanshya Central', 'Mikomfwa', 'Milyashi', 'Roan', 'Zambezi'],
    'Lufwanyama': ['Kafubu', 'Kamfinsa', 'Kapalala', 'Lufwanyama Central', 'Lumwana', 'Milyashi', 'Mufuchani'],
    'Masaiti': ['Chambishi', 'Kansuswa', 'Masaiti', 'Masumbwe', 'Mpongwe', 'Nsansa', 'Sasambu'],
    'Mpongwe': ['Kabundi', 'Kasansa', 'Mpongwe Central', 'Musakambezi', 'Ndeke', 'Ndubulula', 'Nyoka', 'Samfya'],
    'Mufulira': ['Bondeni', 'Chantete', 'Kamuchanga', 'Kantanshi', 'Kashitu', 'Kokolwe', 'Luchenza', 'Mukuyu'],
    'Ndola': ['Buseko', 'Chifubu', 'Chipulukusu', 'Chisokone', 'Chitamba', 'Chitongo', 'Fisenge', 'Kabwe', 'Kafubu',
              'Kafulafuta', 'Kafue Estates', 'Kansenshi', 'Kansusu', 'Lubuto', 'Makeni', 'Masala', 'Mwamfuli',
              'Mwambashi', 'Ndola Central', 'Nkwazi', 'Nsoko', 'Pamodzi', 'Shimpenzwe', 'Twapia'],
    'Chadiza': ['Chadiza', 'Chikowa', 'Chipwepwete', 'Chiwuyu', 'Kazembe', 'Kapichila', 'Lukusuzi', 'Lumezi',
                'Lutembwe', 'M’nyenyembe', 'Makalulu', 'Mphamba', 'Mphomwa', 'Msipazi', 'Msolo', 'Muzoka', 'Nkhanga'],
    'Chipata': ['Chanida', 'Chanjuzi', 'Chasenga', 'Chikando', 'Chikowa', 'Chimutengo', 'Chinyunyu', 'Chipangali',
                'Chipata', 'Chitambala', 'Chitandika', 'Chitekwe', 'Chitungulu', 'Chiwuyu', 'Kapata', 'Kapichila',
                'Kazembe', 'Lundazi', "M'chini", 'Mkanda', 'Mphangwe', 'Msekera', 'Msoro', 'Mthope', 'Mundazi',
                'Mushili', 'Mwami', 'Nyimba', 'Sinda', 'Vubwi'],
    'Katete': ['Chindwale', 'Chinyunyu', 'Jumbe', 'Katete', 'Kumponda', 'Lukusuzi', 'Mbangala', 'Msoro',
               'Mwase Lundazi', 'Nyanje'],
    'Lundazi': ['Chikowa', 'Chinunda', 'Chipangali', 'Chisenga', 'Chitungulu', 'Chivwiku', 'Gaula', 'Jumbe', 'Kasalu',
                'Katazi', 'Kwenje', 'Lukusuzi', 'Lundazi Boma', 'Mkomba', 'Mphamba', 'Mphangwe', 'Msoro', 'Nakazwe',
                'Nkhanga', 'Nkhomwa', 'Nyamphande', 'Nyamphande Airstrip', 'Simwami', 'Thabwa'],
    'Mambwe': ['Chilongozi', 'Chiundaponde', 'Chiwambo', 'Jumbe', 'Kangwe', 'Kundabwika', 'Mafuta', 'Mambwe Boma',
               'Mphuka', 'Mphuka Boma', 'Msebe', 'Mupata', 'Mushili', 'Muyombe', 'Mwanya', 'Njame', 'Nyimba', 'Sosala'],
    'Nyimba': ['Bweemba', 'Chalimbana', 'Chibombo', 'Chibombo Airstrip', 'Chigwe', 'Chikowa', 'Chikweti', 'Chilonga',
               'Chisanga', 'Chita', 'Kanganda', 'Kasamanda', 'Katete', 'Lwimba', 'Mawere', 'Mbaika', 'Mchinga',
               'Mpanshya', 'Msekera', 'Mwenda', 'Nyimba', 'Nyimba Airstrip', 'Pitwe', 'Sinyama', 'Sithobela', 'Sulwe'],
    'Petauke': ['Chilizya', 'Chimwaza', 'Chipata', 'Gogo', 'Kapandula', 'Kapotwe', 'Kasenengwa', 'Katopola',
                'Luangwa Boma', 'Lutembwe', 'Mamfubwe', 'Mandevu', 'Mandevu Airstrip', 'Masenjere', 'Matonga', 'Mkomba',
                'Mnyami', 'Mumbi', 'Mwase', 'Nkhanga', 'Nyimba', 'Petauke Boma', 'Pikwe', 'Rupizo', 'St Pauls',
                'Zalimba'],
    'Chienge': ['Chienge', 'Chipili', 'Isoka', 'Kanyembo', 'Mofwe', 'Chiengi', 'Kopa', 'Looma', 'Lukupa', 'Mala',
                'Nakazombi'],
    'Kawambwa': ['Kabuta', 'Kawambwa', 'Lunkunyi', 'Lwela', 'Mushingashi', 'Mwansabombwe', 'Mwewa', 'Nkumbi'],
    'Mansa': ['Chibanga', 'Chiweza', 'Kabuta', 'Kalasa', 'Kashitu', 'Kavulamanja', 'Kawambwa', 'Kipushi', 'Kisasa',
              'Lubwe', 'Lukolongo', 'Mansa', 'Masumba', 'Mibenge', 'Milando', 'Miputu', 'Misakalenge', 'Munwa',
              'Muswishi', 'Mwabulambo', 'Mwense', 'Nsolwe', 'Pumpu', 'Samfya', 'Senga', 'Shimina', 'Singalamwe',
              'Sulwe', 'Zambezi'],
    'Milenge': ['Isoka', 'Milenge', 'Mwansabombwe'],
    'Mwansabombwe': ['Chibamba', 'Kashikishi', 'Kabuta', 'Mabumba', 'Ntambu', 'Mwansabombwe'],
    'Nchelenge': ['Kaputa', 'Mambilima', 'Kawaza', 'Chiengi', 'Kambilombilo', 'Mwepu', 'Nchelenge'],
    'Samfya': ['Chisenga', 'Munkonge', 'Mukupa Katongo', 'Mushota', 'Chifunabuli', 'Chibanga'],
    'Chilanga': ['Chilanga', 'Linda'],
    'Chirundu': ['Chirundu'],
    'Kafue': ['Kafue', 'Shimabala'],
    'Luangwa': ['Feira', 'Katondwe', 'Luangwa'],
    'Lusaka': ['Chongwe', 'Chelston', 'Ibex Hill', 'Kabulonga', 'Kalingalinga', 'Kalundu', 'Kamwala', 'Kaunda Square',
               'Lusaka Central', 'Mandevu', 'Mtendere', 'Northmead', 'Olympia Park', 'Roma', 'Woodlands'],
    'Chama': ['Chibomba', 'Chikwa', 'Chimbwe', 'Chinyanja', 'Chitimbwa', 'Gwabi'],
    'Chinsali': ['Chifunda', 'Chinsali', 'Isambilimba', 'Kambwili', 'Kapichila', 'Lukupa', 'Mamuna', 'Muyombe',
                 'Nsama'],
    'Isoka': ['Isoka', 'Muyombe', 'Salamanda'],
    'Mpika': ['Chalabesa', 'Chibwa', 'Chikupi', 'Chilonga', 'Chimfuti', 'Chitanda', 'Chitina', 'Ilondola', 'Itala',
              'Kabanda',
              'Kabundi', 'Kabwe', 'Kamalamba', 'Kasama', 'Kasama-Nkolemfumu', 'Kasama-Palabana', 'Kasongo-Lunda',
              'Katanshya',
              'Katubambo', 'Lubambala', 'Lubushi', 'Lukupa', 'Lukupa-Mwelwa', 'Lwimbo', 'Masansa', 'Matipa', 'Mfuwe',
              'Mibilima',
              'Mikomfwa', 'Miloso', 'Minga', 'Mpenzeni', 'Mpika', 'Mporokoso', 'Msolo', 'Mwika', 'Nachilongo',
              'Nakonde', 'Namwala',
              'Nkolemfumu', 'Nsansha', 'Nsolo', 'Nyimba', 'Senga', 'Serenje', 'Shalala', 'Shibuyunji', 'Shikwakala',
              'Shimufumbwe',
              "Shiwang'andu", 'Tazara', 'Thendele', 'Tungati', 'Wasa'],
    'Mafinga': ['Chilonga', 'Chitina', 'Kabanda',
                'Kambwali', 'Kapichila', 'Kapilimikwa',
                'Kapoka', 'Kasamanda',
                'Kasamanda-Isampazi',
                'Lukupa', 'Lupona', 'Mafinga',
                'Mambilima', 'Masansa', 'Mpulungu',
                'Mupamadzi', 'Muyombe', 'Nsalu',
                'Nsolo'],
    'Nakonde': ['Chinakila', 'Kasama', 'Kasama-Palabana', 'Kasama-Pondo', 'Kasama-Silungwe', 'Mafuta', 'Mbala',
                'Mbesuma',
                'Mpulungu', 'Nakonde', 'Nambwele', 'Ntindi', 'Ntumba', 'Nyimbili'],
    'Kasama': ['Chambeshi', 'Chibote', 'Chilongozi', 'Chitamba', 'Kasama', 'Kateshi', 'Lukashya', 'Lukupa', 'Mambilima',
               'Mbesuma', 'Mwenda', 'Nseluka', 'Nthongolo', 'Sumbu'],
    'Luwingu': ['Chaba', 'Chifunabuli', 'Chiundaponde', 'Kapanda', 'Kaputa', 'Kasanka', 'Lubwe', 'Lukulu', 'Luwingu',
                'Mporokoso'],
    'Mporokoso': ['Chimbwi', 'Chinsali Boma', 'Isokwe', 'Kalungwishi', 'Kapila', 'Lumangwe', 'Mporokoso', 'Mushota'],
    'Mpulungu': ['Chimbamilonga', 'Funde', 'Kasongole', 'Kazembe', 'Kilwa', 'Mpulungu', 'Nsomfwa', "Shiwa Ng'andu"],
    'Mbala': ['Bulilo', 'Chibesakunda', 'Chilubula', 'Chinakila-Lubwa', 'Chipili', 'Ilambo', 'Ipusukilo', 'Kapisha',
              'Kaputa', 'Kawambwa-Mporokoso', 'Mbala', 'Mbesuma', 'Mpande', 'Mpulungu', 'Nkomba', 'Ntindi', 'Senga',
              'Twikatane'],
    'Chavuma': ['Chavuma', 'Kashiba', 'Kanongo', 'Lukolwe', 'Munwa', 'Munyama', 'Munzhi', 'Ntumbachushi', 'Sakazimbe',
                'Sikongo'],
    'Kabompo': ['Jimbiza', 'Kabompo', 'Kalene Mission', 'Kangwena', 'Kapanda', 'Katambora', 'Mukinge', 'Nkeyema',
                'Sikwale', 'Sikweshi'],
    'Kasempa': ['Chinonge', 'Chisasa', 'Jifumpa', 'Kabwafu', 'Kasempa', 'Kasenseli', 'Luwingu-Lwa-Shiye', 'Lwawu',
                'Mukumbi', 'Munwa', 'Nkandabwe', 'Nkeyema', 'Shakwanki'],
    'Manyinga': ['Chibanga', 'Ikulwe', 'Imusho', 'Kamisenga', 'Kampanya', 'Kananga', 'Kanongo', 'Kapanda', 'Kapila',
                 'Kapoko', 'Katota', 'Kikuube', 'Kilumba', 'Kipulu', 'Luchele', 'Lukanga', 'Mufumba', 'Mukumbi',
                 'Mweme', 'Nkunzvi', 'Nyoka', 'Sasamwenje', 'Sialwindi', 'Sikwale', 'Sikweshi', 'Yuka'],
    'Mufumbwe': ['Chibwe', 'Kabuta', 'Kamafunda', 'Kanongesha', 'Kanyama', 'Kashima', 'Kashitu', 'Katota',
                 'Kikonkomene', 'Kilindashi', 'Lumasenga', 'Lumwana East', 'Lumwana West', 'Lutembwe', 'Matale',
                 'Milambo', 'Mitukutuku', 'Mize', 'Mufumbwe', 'Musonweji', 'Muyumbu', 'Shangombo', 'Tambalale',
                 'Tutembwe'],
    "Mwinilunga": ["Kamakonde", "Kanyama", "Mwinilunga", "Sikongo", "Sikwale", "Sipuma"],
    "Solwezi": ["Kabitaka", "Kakombe", "Kapijimpanga", "Kapilamwamba", "Kikombe", "Kimasala", "Kipushi", "Mabanga",
                "Mutanda", "Mwenda", "Solwezi", "Tumvwanganai"],
    "Zambezi": ["Chavuma", "Chitokoloki", "Kabompo", "Kaputa", "Kasempa", "Manyinga", "Mufumbwe", "Mwinilunga",
                "Zambezi"],
    'Chikankata': ['Chikankata', 'Chikobola', 'Chilanga', 'Kafue Gorge'],
    'Choma': ['Choma', 'Babulo', 'Bbondo', 'Bweengwa', 'Chisekesi', 'Gwembe', 'Mapanza', 'Namwala'],
    'Gwembe': ['Chipepo', 'Gwembe', 'Itezhi-Tezhi'],
    'Kalomo': ['Kalomo', 'Chaanga', 'Mazabuka', 'Mwandi', 'Pemba', 'Zimba'],
    'Kazungula': ['Kazungula', 'Kasaya', 'Kazungula Estates', 'Mosi-O-Tunya', 'Sesheke'],
    'Livingstone': ['Livingstone', 'Dambwa Central', 'Dambwa North', 'Dambwa South', 'Dr. Kenneth Kaunda', 'Maramba'],
    'Mazabuka': ['Mazabuka', 'Chivuna', 'Munali', 'Nega Nega', 'Ngwezi', 'Ndeke', 'Nkulumbo', 'Siavonga'],
    'Monze': ['Monze', 'Bweengwa', 'Chikuni', 'Gwembe', 'Hachipuka', 'Habaswe', 'Munjule', 'Mwanza East', 'Mwanza West',
              'Namwala', 'Sikalongo'],
    'Namwala': ['Namwala', 'Makapwa', 'Mungule', 'Nanzhila', 'Ngoma', 'Sinafala'],
    'Pemba': ['Pemba', 'Chikanta', 'Chisekesi', 'Namwala'],
    'Siavonga': ['Siavonga', 'Binza', 'Bolombo', 'Chiawa', 'Chirundu', 'Kabuyu', 'Luangwa', 'Mandevu'],
    'Kalabo': ['Kalabo', 'Makanga', 'Sikongo', 'Sikongo', 'Sioma'],
    'Kaoma': ['Kaoma', 'Kasempa', 'Kawambwa', 'Mumbwa'],
    'Lukulu': ['Lukulu', 'Kaleni', 'Kampango', 'Kanyonyomba', 'Mwandi', 'Sikongo'],
    'Mongu': ['Mongu', 'Kaoma', 'Liuwa', 'Senanga'],
    'Senanga': ['Senanga', 'Kalabo', 'Lukulu'],
    'Sesheke': ['Sesheke', 'Kazungula', 'Livingstone', 'Mulobezi', 'Mwandi'],
    'Shangombo': ['Shangombo', 'Kalabo', 'Senanga']

}
