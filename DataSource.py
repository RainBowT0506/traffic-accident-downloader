from DataItem import DataItem

baseUrl = "https://datacenter.taichung.gov.tw/swagger/OpenData/"

year_113 = "113"
year_112 = "112"
year_111 = "111"
year_110 = "110"
year_109 = "109"
year_108 = "108"
year_107 = "107"
year_106 = "106"
year_105 = "105"
year_104 = "104"
year_103 = "103"
year_102 = "102"
year_101 = "101"
year_100 = "100"

month_12 = "12"
month_11 = "11"
month_10 = "10"
month_09 = "09"
month_08 = "08"
month_07 = "07"
month_06 = "06"
month_05 = "05"
month_04 = "04"
month_03 = "03"
month_02 = "02"
month_01 = "01"

# 只能是 Json 檔
datetime = [
    # DataItem(year_113 + month_01, baseUrl + "59e41927-ef94-4af2-b818-545f7765ceed"),  # 113 年，2024
    # DataItem(year_112 + month_12, baseUrl + "9cfd2adc-2267-451d-ace3-248f1d157b23"),
    # DataItem(year_112 + month_11, baseUrl + "92979089-9aaf-4ba3-be97-85e857ec4fd5"),
    # DataItem(year_112 + month_10, baseUrl + "38916fbc-187e-48fc-a6fa-2b1de3d2412f"),
    # DataItem(year_112 + month_09, baseUrl + "509ef016-e338-496a-97d6-ae13d74449b6"),
    # DataItem(year_112 + month_08, baseUrl + "b6645324-551f-4ba0-9e8b-d2de43567319"),
    # DataItem(year_112 + month_07, baseUrl + "0b8821b0-da2f-4e9e-915d-3c4c809ece39"),
    # DataItem(year_112 + month_06, baseUrl + "a6185bb8-dd02-45bb-af75-588f218685e7"),
    # DataItem(year_112 + month_05, baseUrl + "3dc2cdf1-bb74-411f-ab2a-01cbdcb440cb"),
    # DataItem(year_112 + month_04, baseUrl + "11f0c135-10d4-4ba6-b0db-b439ced75fe2"),
    # DataItem(year_112 + month_03, baseUrl + "b704f90e-4d5d-403e-a765-53619769158f"),
    # DataItem(year_112 + month_02, baseUrl + "92fe1e01-c31c-4da3-a75b-165192770b07"),
    # DataItem(year_112 + month_01, baseUrl + "86aaa7e2-ace4-4572-bfbc-d84a876a8455"),  # 112 年，2023(聖嬰)
    # DataItem(year_111 + month_12, baseUrl + "0fc3126c-53e2-4a42-b4db-5cb2370f28ad"),
    # DataItem(year_111 + month_11, baseUrl + "df9d220f-8a1d-49d0-8b0b-625b1295ef0c"),
    # DataItem(year_111 + month_10, baseUrl + "a7e5f923-4167-4baa-986b-2288b82e770d"),
    # DataItem(year_111 + month_09, baseUrl + "ba55e625-fa4a-4953-87ad-280b7bf9c28e"),
    # DataItem(year_111 + month_08, baseUrl + "904b7a13-ae49-4929-be32-44757daf2541"),
    # DataItem(year_111 + month_07, baseUrl + "9aeafaf0-da61-4109-a73a-15a7b45c6421"),
    # DataItem(year_111 + month_06, baseUrl + "58917acc-6fa2-4855-8c44-1475698a9f75"),
    # DataItem(year_111 + month_05, baseUrl + "750c328c-2b93-4a84-b20c-b34da8fb072e"),
    # DataItem(year_111 + month_04, baseUrl + "eb644c8d-2eb3-4a2e-8369-84c14885d316"),
    # DataItem(year_111 + month_03, baseUrl + "2302c32a-1df4-4a26-9098-aab9a2275883"),
    # DataItem(year_111 + month_02, baseUrl + "d5cb855d-b7c2-4452-bb45-9c700b015f34"),
    # DataItem(year_111 + month_01, baseUrl + "e2976ea3-5951-4bf7-b1c9-eabea00dcb8d"),  # 111 年，2022
    # DataItem(year_110 + month_12, baseUrl + "25c65d7f-b55c-46e0-aaca-4ed21153a96a"),
    # DataItem(year_110 + month_11, baseUrl + "e3bad0b7-ebef-421c-bef9-f5da4d1ff1fb"),
    # DataItem(year_110 + month_10, baseUrl + "1be1eeda-b8d1-4d29-871b-4c068f386619"),
    # DataItem(year_110 + month_09, baseUrl + "444e4c9b-d75f-4c67-b068-cd95877e815b"),
    # DataItem(year_110 + month_08, baseUrl + "c8e6a198-7b7a-48ea-9eb9-b73ec5729e15"),
    # DataItem(year_110 + month_07, baseUrl + "77358544-30f5-4429-9e68-d9869e8216f9"),
    # DataItem(year_110 + month_06, baseUrl + "4b5bb6da-e51d-4ece-8126-8f5503190d9e"),
    # DataItem(year_110 + month_05, baseUrl + "269fc3f5-e370-4058-b88c-c232ab4681a9"),
    # DataItem(year_110 + month_04, baseUrl + "4a0a14b6-7403-4201-aa02-ae89442e2424"),
    # DataItem(year_110 + month_03, baseUrl + "a21f8474-dc39-4e25-a661-db8e56d88bfe"),
    # DataItem(year_110 + month_02, baseUrl + "65276bbf-6c3e-426a-b269-fbeaf1c8b3e8"),
    # DataItem(year_110 + month_01, baseUrl + "66369140-4c8c-4113-9101-8bfbd5725f4c"),  # 110 年，2021
    # DataItem(year_109 + month_12, baseUrl + "7d210f01-956b-4a65-9c92-76ab1e2b0c29"),
    # DataItem(year_109 + month_11, baseUrl + "34a0a6ba-50e0-4f47-bc21-d986ad7514b2"),
    # DataItem(year_109 + month_10, baseUrl + "f6de22be-ce8e-4f85-8290-751d6daccaa4"),
    # DataItem(year_109 + month_09, baseUrl + "e361f4a4-5625-4e1e-b695-6643850a6365"),
    # DataItem(year_109 + month_08, baseUrl + "eb5f97a6-889d-4d0a-a401-ab70c47dfeea"),
    # DataItem(year_109 + month_07, baseUrl + "3d3d3455-5b2d-4525-8dd9-5c9d7cf19180"),
    # DataItem(year_109 + month_06, baseUrl + "01111c63-5df4-46da-a16b-c642c98b42de"),
    # DataItem(year_109 + month_05, baseUrl + "302c3783-c7dc-499e-b5b7-8a37473ead02"),
    # DataItem(year_109 + month_04, baseUrl + "9becd2ac-f939-4d06-8f64-096cb9b16be0"),
    # DataItem(year_109 + month_03, baseUrl + "874cb57f-6da0-469a-8b79-92d348846216"),
    # DataItem(year_109 + month_02, baseUrl + "ef52fc64-f6e2-4d1c-bf8b-76e968be7065"),
    # DataItem(year_109 + month_01, baseUrl + "35680ebe-dca8-4828-ba00-dbb252ff5134"),  # 109 年，2020
    # DataItem(year_108 + month_12, baseUrl + "7546529b-e616-441b-a3c5-fdacf100f978"),
    # DataItem(year_108 + month_11, baseUrl + "9b3af096-7854-4f74-9b6b-1ea11ad48adb"),
    # DataItem(year_108 + month_10, baseUrl + "5695817e-4442-48b8-a92f-68011f6e9f59"),
    # DataItem(year_108 + month_09, baseUrl + "542695bc-6660-46b1-9e9f-8959bbb2c68a"),
    # DataItem(year_108 + month_08, baseUrl + "f2d46a29-c4b9-4aec-ae9f-8acfd4fdb0f1"),
    # DataItem(year_108 + month_07, baseUrl + "e28fb404-32c3-447a-ae11-a25223b9feb3"),
    # DataItem(year_108 + month_06, baseUrl + "66c8345c-d6ad-4b4a-aff8-08f657e2c7aa"),
    # DataItem(year_108 + month_05, baseUrl + "05741eb7-25ba-4563-ab94-9e2b77f1c590"),
    # DataItem(year_108 + month_04, baseUrl + "ce12c9e4-6c9a-4122-b3c4-9ee937b5a4cc"),
    # DataItem(year_108 + month_03, baseUrl + "40cf142b-baa1-4c49-a15b-b1938aed0e44"),
    # DataItem(year_108 + month_02, baseUrl + "ebd5453d-dc60-47f5-9a86-a363bca3aeee"),
    # DataItem(year_108 + month_01, baseUrl + "671b1270-d109-499c-bf1a-bfeab7c392d9"),  # 108 年，2019
    # DataItem(year_107 + month_12, baseUrl + "3d1f50da-2e5e-4d05-a2a6-f5f49ff2a5ea"),
    # DataItem(year_107 + month_11, baseUrl + "3a86f518-9ed5-4823-831b-a76ebbdcafc4"),
    # DataItem(year_107 + month_10, baseUrl + "1de0ce02-1485-4bb2-b759-f3face841f3e"),
    # DataItem(year_107 + month_09, baseUrl + "3ffbd338-8416-455b-b924-a2706db8ec21"),
    # DataItem(year_107 + month_08, baseUrl + "a4b1da0d-41b0-4100-9b80-c367a15222d5"),
    # DataItem(year_107 + month_07, baseUrl + "a6d26181-8ef1-478b-b4b8-0ab8e51e7959"),
    # DataItem(year_107 + month_06, baseUrl + "d8bee716-cf17-4ecd-be6d-c6af2bb9f79c"),
    # DataItem(year_107 + month_05, baseUrl + "b78df1ec-0f87-4598-a7ec-87d198cad445"),
    # DataItem(year_107 + month_04, baseUrl + "b85ff577-a3a3-4577-bb49-93109de0f40b"),
    # DataItem(year_107 + month_03, baseUrl + "53260b1c-31a9-429e-bd8e-760f580d2556"),
    # DataItem(year_107 + month_02, baseUrl + "253b599a-b681-4982-9b7b-a773512faeb4"),
    # DataItem(year_107 + month_01, baseUrl + "973edef9-4bd9-4740-a1c0-a84e35780d18"),  # 107 年，2018
    # DataItem(year_106 + month_12, baseUrl + "dd91951a-b9e3-4c6e-94f6-edf7cf05e26b"),
    # DataItem(year_106 + month_11, baseUrl + "4abd4dab-5ba4-4889-aad1-7ec5f815b573"),
    # DataItem(year_106 + month_10, baseUrl + "4eea79de-aa65-4618-9801-85ee15cc803e"),
    # DataItem(year_106 + month_09, baseUrl + "a4841c3b-5346-4445-b17b-22f0c3188f49"),
    # DataItem(year_106 + month_08, baseUrl + "7c70f7c4-0d05-40c7-823a-c8f21548cbef"),
    # DataItem(year_106 + month_07, baseUrl + "ec70599c-1e0c-400b-bb2f-cd3d42a637d5"),
    # DataItem(year_106 + month_06, baseUrl + "0f421f0d-3e18-4ced-a310-de12b3269113"),
    # DataItem(year_106 + month_05, baseUrl + "0f608cc3-c0ea-4a74-b0a2-831128d0b6ee"),
    # DataItem(year_106 + month_04, baseUrl + "4c54b79d-d0de-4cfe-ab37-a51b65e858df"),
    # DataItem(year_106 + month_03, baseUrl + "7951e827-2415-48f6-a86e-bc8c7e396375"),
    # DataItem(year_106 + month_02, baseUrl + "83f3e89b-0a76-4358-9a4f-63f47cb5b288"),
    # DataItem(year_106 + month_01, baseUrl + "883985fe-d721-4981-9270-21c91d6b396b"),  # 106 年，2017
    # DataItem(year_105 + month_12, baseUrl + "8fc1c251-7e30-421a-9161-3445db9b805b"),
    # DataItem(year_105 + month_11, baseUrl + "1014a789-a5d6-47c9-9354-1a0674e4daeb"),  # 105 年，2016
]