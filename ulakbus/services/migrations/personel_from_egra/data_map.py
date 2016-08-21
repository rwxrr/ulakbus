"""

"""


def ad_soyad(s):
    pass
    # ADSOYAD


PERSONEL = [

    ("ACIKALKOD", ""),
    ("ACIKALAD", ""),
    ("ACIKHIZALKOD", ""),
    ("ACIKHIZALAD", ""),
    ("ACIKHUSUSKOD", ""),
    ("ACIKHUSUSAD", ""),
    ("ACIKIADEKOD", ""),
    ("ACIKIADEAD", ""),
    ("VATANDASLIKNO", "tckn"),
    ("ACIKALTAR", "aciga_alinma_tarih"),
    ("GOREVSONTAR", "goreve_son_tarih"),
    ("GOREVIADEISTAR", "goreve_iade_istem_tarih"),
    ("GOREVIADETAR", "goreve_iade_tarih"),
    ("SIKIYONKALTAR", "s_yonetim_kald_tarih"),
    ("ACIKATANTAR", "aciktan_atanma_tarih"),
    ("ACIKAYBASTAR", "acik_aylik_bas_tarih"),
    ("ACIKAYBITTAR", "acik_aylik_bit_tarih"),
    ("GOREVESONAYBASTAR", "goreve_son_aylik_bas_tarih"),
    ("GOREVESONAYBITTAR", "goreve_son_aylik_bit_tarih"),
    ("SONAYODETAR", ""),
    ("HUSUS", "husus"),
    ("GON", ""),
    ("HITAPID", ""),
    ("HITAPHATAKOD", ""),
    ("HITAPHATAMESAJ", ""),
    ("HITGONTAR", ""),
    (ad_soyad("ad"), "ad"),
    (ad_soyad("soyad"), "soyad"),
    ("ADRES1", "ikamet_adresi"),
    ("ADRES2", "adres_2"),
    ("AILKOD", "ikamet_il"),
    ("AILCEKOD", "ikamet_ilce"),
    ("TAG1", ""),
    ("TARIH", ""),
    ("UST", ""),
    ("BRM", ""),
    ("ALT", ""),
    ("EPOSTA", "e_posta"),
    ("BASTAR", "baslama_tarihi"),
    ("TERHISTAR", ""),
    ("YSOGIRTAR", ""),
    ("SEVKTAR", ""),
    ("ASTEGMEN", "astegmen_nasp_tarihi"),
    ("TEGMEN", "tegmen_nasp_tarihi"),
    ("GOREVYER", "gorev_yeri"),
    ("SAYILMAGUNSAY", "sayilmayan_gun_sayisi"),
    ("DONEMSICILNO", ""),
    ("ASKERLIKDURUMKOD", ""),
    ("P_HAREKET1", ""),
    ("P_HAREKET2", ""),
    ("P_HAREKET3", ""),
    ("FHZAM", "fhz_orani"),
    ("KURUMZAMAN", ""),
    ("ACIKLAMA", "aciklama"),
    ("IBRAZTAR", "ibraz_tarihi"),
    ("TEKLIFYAZISI", ""),
    ("MUAFNEDEN", "muafiyet_neden"),
    ("GECISTAR", ""),
    ("KITABASTAR", "kita_baslama_tarihi"),
    ("KITABITTAR", "kita_bitis_tarihi"),
    ("KADROKOD", ""),
    ("KADROADI", "kadro"),
    ("KANUN", ""),
    ("TCNO", "tckn"),
    ("TIP", "tip"),
    ("BITTAR", "bitis_tarihi"),
    ("PRIMGUN", ""),
    ("BAGKURSICILNO", ""),
    ("MEMURIYET", ""),
    ("PRIMAY", ""),
    ("PRIMYIL", ""),
    ("DEGERLENDIR", ""),
    ("YVATANDASLIKNO", ""),
    ("YAD", ""),
    ("YSOYAD", ""),
    ("YISDURUM", ""),
    ("YDOGUMTARIHI", ""),
    ("YDERECEKOD", ""),
    ("KARNESERI", ""),
    ("KARNENO", ""),
    ("PASIF", ""),
    ("SGK", ""),
    ("USERNO", ""),
    ("USTBIRIMNO", ""),
    ("BIRIMNO", ""),
    ("KANUNNO", "kanun_kod"),
    ("MIKTAR", ""),
    ("MIKTARBIRIM", ""),
    ("BORCKOD", ""),
    ("BORCAY", ""),
    ("BORCGUN", ""),
    ("BORCYIL", ""),
    ("DERECE", "derece"),
    ("KADEME", "kademe"),
    ("ODENEN", "odenen_miktar"),
    ("KURUMAD", "calistigi_kurum"),
    ("KURUMILKOD", "isyeri_il"),
    ("KURUMILCEKOD", "isyeri_ilce"),
    ("TAHAKKUKTAR", ""),
    ("ODEMETAR", "odeme_tarihi"),
    ("EKGOSTERGE", "ekgosterge"),
    ("BORCADI", ""),
    ("HITAPKOD", ""),
    ("SIRANO", "kayitli_oldugu_sira_no"),
    ("MUHBIRADSOYAD", ""),
    ("IHBARTAR", ""),
    ("SUCNEVI", ""),
    ("SORUSACILISTAR", ""),
    ("SORUSTURMACI1ADSOYAD", ""),
    ("SORUSTURMACI2ADSOYAD", ""),
    ("SORUSTURMACI3ADSOYAD", ""),
    ("SORUSTURMACI4ADSOYAD", ""),
    ("SORUSBASTAR", ""),
    ("SORUSBITTAR", ""),
    ("TEBLIGATTAR", ""),
    ("ITIRAZ", ""),
    ("DUSUNCELER", ""),
    ("DURUM", "durum"),
    ("TEKLIFCEZAKOD", ""),
    ("TAKDIRCEZAKOD", ""),
    ("P_HAREKET", ""),
    ("AFKAPSAMI", ""),
    ("CEZATIPKOD", ""),
    ("CEZATIPADI", ""),
    ("SEBEPKOD", "sebep_kod"),
    ("SEBEPAD", ""),
    ("ACK", ""),
    ("GOREVBIRIM", ""),
    ("UNVANKOD", "unvan_kod"),
    ("YEVMIYE", "yevmiye"),
    ("UCRET", "ucret"),
    ("HIZMETSINIFKOD", ""),
    ("KADRODERECE", "kadro_derece"),
    ("GADERECE", ""),
    ("GAKADEME", ""),
    ("GAGOSTERGE", ""),
    ("KHADERECE", ""),
    ("KHAKADEME", ""),
    ("KHAGOSTERGE", ""),
    ("EMDERECE", ""),
    ("EMKADEME", ""),
    ("EMGOSTERGE", ""),
    ("ONAYTAR", "kurum_onay_tarihi"),
    ("HAREKETTIP", ""),
    ("GONTAR", ""),
    ("TABLO", ""),
    ("SICILNO", "kurum_sicil_no_int"),
    ("SANDIKKOD", "banka_sandik_kod"),
    ("AD", "ad"),
    ("SOYAD", "soyad"),
    ("UNIVERSITEKOD", ""),
    ("ALTBIRIMNO", ""),
    ("GOREV", "gorev"),
    ("CINSIYET", "cinsiyet"),
    ("UYRUKULKEKOD", "ulke_kod"),
    ("DOGTAR", "dogum_tarihi"),
    ("DOGYER", "dogum_yeri"),
    ("TEL", "telefon"),
    ("EMKMUKKADEME", "emekli_muktesebat_kademe"),
    ("EMKMUKDERECE", "emekli_muktesebat_derece"),
    ("GORAYKADEME", ""),
    ("GORAYDERECE", ""),
    ("KAZHAKKADEME", "kazanilmis_hak_ayligi_kademe"),
    ("KAZHAKDERECE", "kazanilmis_hak_ayligi_derece"),
    ("SEBEP", "sebep"),
    ("VEKIL", "vekil"),
    ("EMKMUKGOS", "emekli_muktesebat_ekgosterge"),
    ("GORAYGOS", ""),
    ("KAZHAKGOS", "kazanilmis_hak_ayligi_ekgosterge"),
    ("ONAYTARIH", "onay_tarihi"),
    ("EMK_HAREKET", ""),
    ("UNIKOD", ""),
    ("BASLAMAKOD", ""),
    ("AYRILMAKOD", ""),
    ("EMKMUKTRFTARIH", "em_sonraki_terfi_tarihi"),
    ("GORAYTRFTARIH", "ga_sonraki_terfi_tarihi"),
    ("KAZHAKTRFTARIH", "kh_sonraki_terfi_tarihi"),
    ("TERFITARIHI", ""),
    ("GOREVLERKOD", ""),
    ("GOREVLERADI", ""),
    ("SICILTIP", ""),
    ("GOREVTIPKOD", ""),
    ("GOREVTIPADI", "gorev_tipi"),
    ("YETKI", "yetki_seviyesi"),
    ("KOD", ""),
    ("AYRILMADURUM", "ayrilma_nedeni"),
    ("CEKKAYSAY", ""),
    ("CEKTAR", ""),
    ("EKSAY", ""),
    ("GUNSAY", "gun_sayisi"),
    ("SILSAY", ""),
    ("DEGTAR", ""),
    ("EKGONSAY", ""),
    ("GUNGONSAY", ""),
    ("SILGONSAY", ""),
    ("ASILSEBEP", ""),
    ("DURUMKOD", ""),
    ("HARSEBEPKOD", ""),
    ("HARSEBEPACK", ""),
    ("DURUMACK", ""),
    ("AYRILTAR", ""),
    ("YETKIKOD", ""),
    ("YETKIACK", ""),
    ("SONUCKOD", ""),
    ("SONUCACK", ""),
    ("KAYITID", "kayit_no"),
    ("SILTARIH", ""),
    ("GON NUMBER(1)", ""),
    ("HITAPTABLO", ""),
    ("HIZMETKOLKOD", ""),
    ("HIZMETKOLAD", ""),
    ("HIZMETSINIFADI", "hizmet_sinifi"),
    ("KISAADI", ""),
    ("EMSKOD", ""),
    ("HITAPKOD2", ""),
    ("KADROCERECE", "kadro_derece"),
    ("UNVANTAR", "unvan_tarihi"),
    ("KADROTAR", ""),
    ("UNV", ""),
    ("ADSOY", ""),
    ("ISAYRILMADURUMKOD", ""),
    ("DOSYANO", ""),
    ("ISAYRILMADURUMADI", ""),
    ("ISAYRILMADURUMTIP", ""),
    ("OZLUKSEBEP", ""),
    ("ISBASLAMADURUMKOD", ""),
    ("ISBASLAMADURUMADI", ""),
    ("ISBASLAMADURUMTIP", ""),
    ("MECBURYIL", ""),
    ("MECBURAY", ""),
    ("MECBURGUN", ""),
    ("MECBURZAMAN", ""),
    ("ITIBARKOD", ""),
    ("ITIBARAD", ""),
    ("YIL1", ""),
    ("GUN1", ""),
    ("YIL2", ""),
    ("GUN2", ""),
    ("IZINTIPKOD", ""),
    ("ADRES", "adres"),
    ("IZIN_ID", ""),
    ("VEKALET_ADSOYAD", ""),
    ("VEKALET_UNVAN", ""),
    ("VEKALET_SICILNO", ""),
    ("IZINTIPADI", ""),
    ("ALTBIRIMKOD", ""),
    ("IZINTARIHI", ""),
    ("AKADEMIKIDARI", ""),
    ("KADRODURUM", ""),
    ("KADROID", ""),
    ("KADROAYRILTAR", ""),
    ("HSINIFHITAPKOD", ""),
    ("ASILVEKIL", "asil_vekil"),
    ("ATAMASEKIL", "atama_sekli"),
    ("ULKEKOD", "ulke_kod"),
    ("MAAS", "maas"),
    ("YOLLUK", "yolluk"),
    ("YAZITAR", "resmi_yazi_tarih"),
    ("YAZISAYI", "resmi_yazi_sayi"),
    ("DURUM", "hizmet_durum"),
    ("PERTIP", ""),
    ("LDAP_TARIH", ""),
    ("MAHKEMEAD", "mahkeme_ad"),
    ("KARARTAR", "karar_tarihi"),
    ("KARARSAY", "karar_sayisi"),
    ("KESINTAR", "kesinlesme_tarihi"),
    ("ASILDOGTAR", "asil_dogum_tarihi"),
    ("TASHIHTAR", "tashih_dogum_tarihi"),
    ("ASILAD", "asil_ad"),
    ("ASILSOYAD", "asil_soyad"),
    ("TASHIHAD", "tashih_ad"),
    ("TASHIHSOYAD", "tashih_soyad"),
    ("GECERLIDOGTAR", "gecerli_dogum_tarihi"),
    ("BABAADI", "baba_adi"),
    ("ANAADI", "ana_adi"),
    ("MEDENIHALI", "medeni_hali"),
    ("ONCEKISOYAD", "ilk_soy_ad"),
    ("ILKOD", ""),
    ("ILCEKOD", ""),
    ("MAHKOY", ""),
    ("CILTNO", "kayitli_oldugu_cilt_no"),
    ("AILESIRANO", "kayitli_oldugu_sira_nokayitli_oldugu_aile_sira_no"),
    ("KIMLIKSERI", "cuzdan_seri"),
    ("KIMLIKNO", "tckn"),
    ("KIMLIKVERYER", "kimlik_cuzdani_verildigi_yer"),
    ("KIMLIKVERNEDEN", "kimlik_cuzdani_verilis_nedeni"),
    ("KIMLIKKAYNO", "kimlik_cuzdani_kayit_no"),
    ("KIMLIKVERTARIH", "kimlik_cuzdani_verilis_tarihi"),
    ("TAG", ""),
    ("MUSTERI_ID", ""),
    ("VATANDASLIK_NO", "tckn"),
    ("DOGUM_TARIHI", "dogum_tarihi"),
    ("MAIL", ""),
    ("EV_TEL", ""),
    ("IS_TEL", ""),
    ("CEP_TEL", "cep_telefonu"),
    ("FAX", ""),
    ("WEB", "web_sitesi"),
    ("ADRESS", "adres"),
    ("SEMT", ""),
    ("KAYIT_TARIHI", ""),
    ("EVLILIK_YIL_DONUMU", ""),
    ("KULLANICI_AD", ""),
    ("ACENTA_ID", ""),
    ("AKTIF", ""),
    ("EMEKLILIK_SIS_GIR_TAR", ""),
    ("ANNE_KIZLIK_SOYAD", ""),
    ("KIMLIK_SERI_NO", "cuzdan_seri_no"),
    ("GERCEK_DOG_TAR", "asil_dogum_tarihi"),
    ("UYRUK", "uyruk"),
    ("ANNE_AD", "ana_adi"),
    ("BABA_AD", "baba_adi"),
    ("MEDENI_DURUM", "medeni_hali"),
    ("DOGUM_YER", "dogum_yeri"),
    ("MESLEK_ID", ""),
    ("OKULADI", "okul_ad"),
    ("HAZIRLIKSURE", "hazirlik"),
    ("OGRENIMTIPKOD", ""),
    ("DIPLOMANO", ""),
    ("UZMANLIKALAN", ""),
    ("BITIRMENOTU", ""),
    ("BRANS", "brans"),
    ("MEZTAR", "mezuniyet_tarihi"),
    ("ISBASOGR", ""),
    ("DENKLIK", ""),
    ("DENKLIKTAR", "denklik_tarihi"),
    ("ONCEDEG", ""),
    ("ONKURUMDEG", ""),
    ("DIPTESCILNO", ""),
    ("DENKOKUL", "denklik_okulu"),
    ("DENKBOLUM", "denklik_bolum"),
    ("KURUMIBRAZTAR", ""),
    ("OGRENIMTIPADI", ""),
    ("MINDERECE", ""),
    ("MINKADEME", ""),
    ("SURE", "ogrenim_suresi"),
    ("SIRA", ""),
    ("HITAPTIP", ""),
    ("ONKURUMDEG", ""),
    ("IPADRES", ""),
    ("KANGRUPKOD", ""),
    ("EVTEL", ""),
    ("ISTEL", ""),
    ("CEPTEL", ""),
    ("POSTAKOD", ""),
    ("EMAIL", ""),
    ("EMAIL2", ""),
    ("WEBSAYFA", ""),
    ("STATUKOD", ""),
    ("SAGLIKDURUMU", ""),
    ("OZURLUDERECESI", "engel_derecesi"),
    ("VERGINO", ""),
    ("SIFRE", ""),
    ("ARSIV", "arsiv"),
    ("EMEKLISICILNO", "emekli_sicil_no"),
    ("EMEKLIGIRISTAR", ""),
    ("ADAYLIK", ""),
    ("GORBASTAR", "goreve_baslama_tarihi"),
    ("GORBITTAR", ""),
    ("KONTROL", ""),
    ("TAG2", ""),
    ("TAG3", ""),
    ("PERSONELTIP", ""),
    ("TERFIACIKLAMA", ""),
    ("GORACIKLAMA", ""),
    ("TERFICEZA", ""),
    ("TERFIASKER", ""),
    ("TERFIUCRETSIZ", ""),
    ("TERFISICIL", ""),
    ("GORUZATMA", ""),
    ("TERFIBAKANLIKGELEN", ""),
    ("ISADRES", ""),
    ("NOTLAR", "notlar"),
    ("OZURGRUPKOD", ""),
    ("OZURORAN", "engel_orani"),
    ("ANKET", ""),
    ("HIGTONTAR", ""),
    ("HITACK", ""),
    ("CEPYIL", ""),
    ("DILSEVIYE", ""),
    ("DILTARIH", ""),
    ("DILSINAV", ""),
    ("DIL", ""),
    ("KANGRUBU", "kan_grubu"),
    ("EMKDERECE", "emekli_derece"),
    ("EMKKADEME", "emekli_kademe"),
    ("GORDERECE", ""),
    ("GORKADEME", ""),
    ("KAZDERECE", "kazanilmis_hak_derece"),
    ("KAZKADEME", "kazanilmis_hak_kademe"),
    ("EMKTERFITAR", ""),
    ("GORTERFITAR", ""),
    ("KAZTERFITAR", ""),
    ("KADRODER", ""),
    ("GOSTERGE", ""),
    ("GORAYDER", "gorev_ayligi_derece"),
    ("GORAYKAD", "gorev_ayligi_kademe"),
    ("GORAYTERTAR", ""),
    ("KAZDER", ""),
    ("KAZKAD", ""),
    ("KAZTERTAR", ""),
    ("EMKDER", ""),
    ("EMKKAD", ""),
    ("EMKTERTAR", ""),
    ("CIKTITAR", ""),
    ("CIKTIUSER", ""),
    ("PERSTIPKOD", ""),
    ("PERSTIPADI", "personel_turu"),
    ("NERDEN", "nereden"),
    ("ALINANILKOD", ""),
    ("GRUPKOD", ""),
    ("GRUPAD", ""),
    ("GRUPTAG", ""),
    ("SORGUKOD", ""),
    ("SORGUAD", ""),
    ("SORGUSQL", ""),
    ("SORGUTAG", ""),
    ("RESIM", ""),
    ("SANDIKAD", "banka_sandik_kod"),
    ("SENDIKAKOD", ""),
    ("SENDIKAUYENO", ""),
    ("UYELIKTAR", ""),
    ("KONFEDERASYON", ""),
    ("SENDIKAAD", ""),
    ("SENDIKAKISAAD", ""),
    ("YIL", ""),
    ("NOTU", ""),
    ("KURUMTIP", ""),
    ("SSKSICILNO", ""),
    ("SSKSICILNO2", ""),
    ("STATUADI", "statu"),
    ("MAKAMTAZ", ""),
    ("GOREVTAZ", ""),
    ("TEMSILTAZ", ""),
    ("TAZBASTAR", "tazminat_tarihi"),
    ("TAZBITTAR", "tazminat_bitis_tarihi"),
    ("UNVAN", "unvan"),
    ("TEKLIF", ""),
    ("GEREKCE", ""),
    ("UCRETSIZTIPKOD", ""),
    ("SUREYIL", ""),
    ("SUREAY", ""),
    ("SUREGUN", ""),
    ("UCRETSIZTIPAD", ""),
    ("CINS", ""),
    ("MESAJID", ""),
    ("GRUPID", ""),
    ("KAYITTAR", ""),
    ("KULLANICIADI", ""),
    ("KULLANICIIP", ""),
    ("MAKINEADI", ""),
    ("ILANBASTAR", ""),
    ("ILANBITTAR", ""),
    ("BASLIK", ""),
    ("ICERIK", ""),
    ("LINK", ""),
    ("ULASINID", ""),
    ("MENUID", ""),
    ("BILGI", ""),
    ("LOGTARIH", ""),
    ("WAJANDAID", ""),
    ("BILGI_EN", ""),
    ("BILIMSELTIP", ""),
    ("BILIMSELCALISMA", ""),
    ("AD_EN", ""),
    ("WBLOGID", ""),
    ("BASLIK_EN", ""),
    ("WGUNCELID", ""),
    ("SORGUADI", ""),
    ("SORGU", ""),
    ("SSSID", ""),
    ("SORU", ""),
    ("CEVAP", ""),
    ("MESAJKONU", ""),
    ("MESAJ", ""),
    ("YABANCIDILKOD", ""),
    ("SEVIYE", ""),
    ("KAYITILKOD", "kayitli_oldugu_il"),
    ("KAYITILCEKOD", "kayitli_oldugu_ilce"),
    ("KAYITMAHKOY", "kayitli_oldugu_mahalle_koy"),
    ("AYRILUNIKOD", ""),
    ("ATRILTAR", ""),
    ("EVRAKTAR", ""),
    ("EVRAKSAY", ""),
    ("KURUM", ""),
    ("YDERECEADI", ""),
    ("YDILSINAVKOD", ""),
    ("ESKI", ""),
    ("YENI", ""),
    ("ULKE", "ulke"),

    ("", "memuriyet_baslama_tarihi"),
    ("", "kurum_sicil"),
    ("", "maluliyet_kod"),
    ("", "kuruma_baslama_tarihi"),
    ("", "emekli_sicil_6495"),
    ("", "sync"),
    ("", "kurs_ogrenim_suresi"),
    ("", "kurs_nevi"),
    ("", "bolum_ad"),
    ("", "ogrenim_yeri"),
    ("", "ogrenim_durumu"),
    ("", "bolum"),
    ("", "sgk_nevi"),
    ("", "sgk_sicil_no"),
    ("", "sure"),
    ("", "ozel_isyeri_ad"),
    ("", "bag_kur_meslek"),
    ("", "kidem_tazminat_odeme_durumu"),
    ("", "kha_durum"),
    ("", "makam"),
    ("", "temsil"),
    ("", "kadrosuzluk"),
    ("", "unvan_bitis_tarihi"),
    ("", "acik_sekil"),
    ("", "iade_sekil"),
    ("", "husus_aciklama"),
    ("", "emekli_sicil"),
    ("", "borc_nevi"),
    ("", "toplam_tutar"),
    ("", "odenen_miktar"),
    ("", "borclanma_tarihi"),
    ("", "ihz_nevi"),
    ("", "istisnai_ilgi_nevi"),
    ("", "kha_durum"),
    ("", "odeme_kademe"),
    ("", "odeme_ekgosterge"),
    ("", "emekli_ekgosterge"),
    ("", "askerlik_nevi"),
    ("", "sinif_okulu_sicil"),
    ("", "subayliktan_erlige_gecis_tarihi"),
    ("", "subay_okulu_giris_tarihi"),

    ("", "oda_no"),
    ("", "oda_tel_no"),
    ("", "e_posta_2"),
    ("", "e_posta_3"),
    ("", "yayinlar"),
    ("", "projeler"),
    ("", "ehliyet"),
    ("", "verdigi_dersler"),
    ("", "biyografi"),
    ("", "engelli_durumu"),
    ("", "engel_grubu"),
    ("", "kazanilmis_hak_ekgosterge"),
    ("", "gorev_ayligi_ekgosterge"),
    ("", "emekli_muktesebat_ekgosterge"),

    ("", "birim"),
    ("", "emekli_giris_tarihi"),
    ("", "gorev_suresi_baslama"),
    ("", "gorev_suresi_bitis"),
    ("", "baslama_sebep"),
    ("", "mecburi_hizmet_suresi"),
    ("", "aday_memur"),
    ("", "kurum_ici_gorev_baslama_tarihi"),
    ("", "kurum_ici_gorev_bitis_tarihi"),
    ("", "kurum_disi_gorev_baslama_tarihi"),
    ("", "kurum_disi_gorev_bitis_tarihi"),
    ("", "kadro_no"),
    ("", "unvan_aciklama"),
    ("", "baslangic"),
    ("", "bitis"),
    ("", "onay"),
    ("", "personel"),

    ("", "donus_tarihi"),
    ("", "donus_tip"),
    ("", "atama_aciklama"),
]