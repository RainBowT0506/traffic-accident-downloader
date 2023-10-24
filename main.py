import requests
import mysql.connector
import multiprocessing
from DataItem import DataItem

baseUrl = "https://datacenter.taichung.gov.tw/swagger/OpenData/"

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

datetime = [
    # DataItem(year_112 + month_07, baseUrl + "0b8821b0-da2f-4e9e-915d-3c4c809ece39"),
    # DataItem(year_112 + month_06, baseUrl + "a6185bb8-dd02-45bb-af75-588f218685e7"),
    # DataItem(year_112 + month_05, baseUrl + "f69ecfa4-dcb0-4bad-8973-9de4cdeeed74"),
    # DataItem(year_112 + month_04, baseUrl + "d93f538b-b567-45fc-a4ce-56edf4998381"),
    # DataItem(year_112 + month_03, baseUrl + "a4e4facb-ee44-477e-9f24-eb1385c6797e"),
    # DataItem(year_112 + month_02, baseUrl + "a38b78bf-ca29-4258-88ec-dbcc90e26808"),
    # DataItem(year_112 + month_01, baseUrl + "52f7c0a4-e160-404b-9b55-593d41f51753"),  # 112 年
    # DataItem(year_111 + month_12, baseUrl + "94aa0e00-3bd6-4b8e-96c3-06b0f2a5389b"),
    # DataItem(year_111 + month_11, baseUrl + "1612620b-0a18-4c57-8d5b-b3ca47554b2e"),
    # DataItem(year_111 + month_10, baseUrl + "e7081dd6-824c-4ae4-b4da-0089807dc2a9"),
    # DataItem(year_111 + month_09, baseUrl + "2bc64f35-187d-44a4-9a76-22ddd0434102"),
    # DataItem(year_111 + month_08, baseUrl + "1048d4fa-01b0-4e16-b26c-7d1d613661b9"),
    # DataItem(year_111 + month_07, baseUrl + "9aeafaf0-da61-4109-a73a-15a7b45c6421"),
    # DataItem(year_111 + month_06, baseUrl + "d30d182f-2cca-4649-b44d-dd2818ad5310"),
    # DataItem(year_111 + month_05, baseUrl + "3b6c0b91-3f33-4713-b6f0-9a237c75c437"),
    # DataItem(year_111 + month_04, baseUrl + "3e46c34a-b270-4b70-8ad5-b77a21c4eddc"),
    # DataItem(year_111 + month_03, baseUrl + "9372de93-3304-4066-b8a9-f2b6ba318487"),
    # DataItem(year_111 + month_02, baseUrl + "e971ee12-51ac-48d4-ab99-d4e6ef5261b0"),
    # DataItem(year_111 + month_01, baseUrl + "70a05607-86d4-4e55-ab32-9195a0df4fff"),  # 111 年
    # DataItem(year_110 + month_12, baseUrl + "67a71376-d2dc-4a77-838d-c5ac1916929f"),
    # DataItem(year_110 + month_11, baseUrl + "140dc2f1-84c1-4047-90e0-c23121b08e2b"),
    # DataItem(year_110 + month_10, baseUrl + "40e8a096-aae9-4f83-b18b-da5de59762ad"),
    # DataItem(year_110 + month_09, baseUrl + "a532cf27-39b7-4c22-8b3c-8413b3e59dc7"),
    # DataItem(year_110 + month_08, baseUrl + "8c5b5625-08df-4411-b652-211d27a54200"),
    # DataItem(year_110 + month_07, baseUrl + "3cad518b-23d6-4ac1-a6dc-4cf7ae8b52cb"),
    # DataItem(year_110 + month_06, baseUrl + "9f5ac0c3-c50f-4a06-8e20-782b29806efb"),
    # DataItem(year_110 + month_05, baseUrl + "2489b2c4-636d-4bf4-b5d5-e517abe0ef2d"),
    # DataItem(year_110 + month_04, baseUrl + "8f6d8461-fae5-45d5-a4c1-f5c76874a2ca"),
    # DataItem(year_110 + month_03, baseUrl + "46a860d7-9f8b-4017-90d9-a876d1b51eac"),
    # DataItem(year_110 + month_02, baseUrl + "37b58156-0e73-4f43-b82e-eaec1d41f8ed"),
    # DataItem(year_110 + month_01, baseUrl + "48369889-e8cf-4675-bd1d-bf8a5c098e5a"),  # 110 年
    # DataItem(year_109 + month_12, baseUrl + "c6c57073-c64f-48a2-b24f-78612e8cccb1"),
    # DataItem(year_109 + month_11, baseUrl + "f596bd5b-8fb5-4067-ac5c-2ed82dc9633a"),
    # DataItem(year_109 + month_10, baseUrl + "4a9589f6-5656-41fe-8e51-4c1fa9574715"),
    # DataItem(year_109 + month_09, baseUrl + "4a738a6f-9e1d-45ce-b713-b57457ef5ae0"),
    # DataItem(year_109 + month_08, baseUrl + "86c4dbfd-196d-49bc-a1c6-050166604eb7"),
    # DataItem(year_109 + month_07, baseUrl + "507820ed-a3c0-421f-a69a-594539a348c4"),
    # DataItem(year_109 + month_06, baseUrl + "6f35d0e2-bf0a-44dd-8e1d-b35eaf3ff8db"),
    # DataItem(year_109 + month_05, baseUrl + "9016e7c5-db64-435c-b742-d85a74ddb215"),
    # DataItem(year_109 + month_04, baseUrl + "9becd2ac-f939-4d06-8f64-096cb9b16be0"),
    # DataItem(year_109 + month_03, baseUrl + "874cb57f-6da0-469a-8b79-92d348846216"),
    # DataItem(year_109 + month_02, baseUrl + "ef52fc64-f6e2-4d1c-bf8b-76e968be7065"),
    # DataItem(year_109 + month_01, baseUrl + "35680ebe-dca8-4828-ba00-dbb252ff5134"),  # 109 年
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
    # DataItem(year_108 + month_01, baseUrl + "671b1270-d109-499c-bf1a-bfeab7c392d9"),  # 108 年
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
    # DataItem(year_107 + month_01, baseUrl + "973edef9-4bd9-4740-a1c0-a84e35780d18"),  # 107 年
    # DataItem(year_106 + month_12, baseUrl + "dd91951a-b9e3-4c6e-94f6-edf7cf05e26b"),
    # DataItem(year_106 + month_11, baseUrl + "4abd4dab-5ba4-4889-aad1-7ec5f815b573"),
    # DataItem(year_106 + month_10, baseUrl + "4eea79de-aa65-4618-9801-85ee15cc803e"),
    # DataItem(year_106 + month_09, baseUrl + "a4841c3b-5346-4445-b17b-22f0c3188f49"),
    # DataItem(year_106 + month_08, baseUrl + "7c70f7c4-0d05-40c7-823a-c8f21548cbef"),
    # DataItem(year_106 + month_07, baseUrl + "ec70599c-1e0c-400b-bb2f-cd3d42a637d5"),
    # DataItem(year_106 + month_06, baseUrl + "0f421f0d-3e18-4ced-a310-de12b3269113"),
    # DataItem(year_106 + month_05, baseUrl + "0f608cc3-c0ea-4a74-b0a2-831128d0b6ee"),
    # DataItem(year_106 + month_04, baseUrl + "4c54b79d-d0de-4cfe-ab37-a51b65e858df"),
    # DataItem(year_106 + month_03, baseUrl + "31ceea6e-b553-442b-8f13-852ca1663d33"),
    # DataItem(year_106 + month_02, baseUrl + "4dcdc412-084f-445d-8f75-c1ac42021aaf"),
    # DataItem(year_106 + month_01, baseUrl + "00c5da7f-f812-4af1-ac75-9010263ed1e3"),  # 106 年
    # DataItem(year_105 + month_12, baseUrl + "8fc1c251-7e30-421a-9161-3445db9b805b"),
    # DataItem(year_105 + month_11, baseUrl + "1014a789-a5d6-47c9-9354-1a0674e4daeb"),  # 105 年
]


def process_data_item(dataItem):
    print(dataItem.url)
    # 連接到MySQL數據庫
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="traffic"  # 替換為您的資料庫名稱
    )

    # 創建游標
    cursor = db_connection.cursor()
    api_url = dataItem.url
    response = requests.get(api_url)
    data = response.json()
    # 遍歷API數據並插入到資料庫
    for item in data:
        serial_number = item.get("序號", 0)
        county_code = item.get("縣市別代碼", 0)
        agency_code = item.get("機關代碼", "")
        telephone = item.get("市話", "")
        fax = item.get("傳真", "")

        year = item.get("年", 0)
        month = item.get("月", 0)
        day = item.get("日", 0)
        hour = item.get("時", 0)
        minute = item.get("分", 0)
        county = item.get("縣市", "")
        district = item.get("區", "")

        if "死亡數量" in item:
            number_of_deaths = item["死亡數量"]
        elif "死" in item:
            number_of_deaths = item["死"]
        else:
            number_of_deaths = 0

        if "受傷數量" in item:
            number_of_injuries = item["受傷數量"]
        elif "受傷" in item:
            number_of_injuries = item["受傷"]
        else:
            number_of_injuries = 0

        if "2-30" in item:
            field_2_to_30 = item["2-30"]
        elif "2_30" in item:
            field_2_to_30 = item["2_30"]
        else:
            field_2_to_30 = 0

        weather = item.get("天候", 0)
        lighting = item.get("光線", "")
        road_type = item.get("道路類別", "")
        speed_limit = item.get("速限", 0)
        road_configuration = item.get("道路型態", "")
        accident_location = item.get("事故位置", "")
        road_surface = item.get("路面鋪裝", "")
        road_condition = item.get("路面狀態", "")
        road_defect = item.get("路面缺陷", "")
        obstacle = item.get("障礙物", "")
        visibility = item.get("視距", "")
        traffic_signal_type = item.get("號誌種類", "")
        traffic_signal_action = item.get("號誌動作", "")
        median_barrier = item.get("分向設施", "")
        lane_type = item.get("快車道或一般車道間", "")
        lane_gap_type = item.get("快慢車道間", "")
        road_edge_line = item.get("路面邊線", "")
        accident_type_and_pattern = item.get("事故類型及型態", "")
        primary_cause = item.get("主要肇因", 0)
        injury_severity = item.get("受傷程度", "")
        primary_injury_location = item.get("主要傷處", "")
        protective_equipment = item.get("保護裝備", "")
        mobile_phone_use = item.get("行動電話", "")

        if "當事者區分(類別)" in item:
            party_type = item["當事者區分(類別)"]
        elif "當事者區分" in item:
            party_type = item["當事者區分"]
        elif "當事者區分_類別" in item:
            party_type = item["當事者區分_類別"]
        else:
            party_type = ""

        vehicle_use = item.get("車輛用途", "")
        party_action_status = item.get("當事者行動狀態", "")
        driver_qualification = item.get("駕駛資格情形", 0)
        driver_license_type = item.get("駕駛執照種類", "")
        alcohol_use = item.get("飲酒情形", 0)
        initial_vehicle_impact = item.get("車輛撞擊部位最初", "")
        other_vehicle_impact = item.get("車輛撞擊部位其他", "")
        individual_contributing_factors = item.get("肇事因素個別", 0)
        primary_contributing_factors = item.get("肇事因素主要", "")
        hit_and_run = item.get("肇事逃逸", 0)
        occupation = item.get("職業", 0)
        travel_purpose = item.get("旅次目的", 0)
        vehicle_type = item.get("車種", "")

        if "GPS座標X" in item:
            gps_coordinate_x = item["GPS座標X"]
        elif "GPS座標緯度" in item:
            gps_coordinate_x = item["GPS座標緯度"]
        elif "GPS座標_緯度" in item:
            gps_coordinate_x = item["GPS座標_緯度"]
        elif "GPS緯度" in item:
            gps_coordinate_x = item["GPS緯度"]
        else:
            gps_coordinate_x = 0

        if "GPS座標Y" in item:
            gps_coordinate_y = item["GPS座標Y"]
        elif "GPS座標_經度" in item:
            gps_coordinate_y = item["GPS座標_經度"]
        elif "GPS座標經度" in item:
            gps_coordinate_y = item["GPS座標經度"]
        elif "GPS經度" in item:
            gps_coordinate_y = item["GPS經度"]
        else:
            gps_coordinate_y = 0

        accident_category = item.get("事故類別", 0)

        sql = """
        INSERT INTO AccidentData (SerialNumber, CountyCode, AgencyCode, Telephone, Fax, Year, Month, Day, Hour, Minute, County, District, NumberOfDeaths, NumberOfInjuries, Field2To30, Weather, Lighting, RoadType, SpeedLimit, RoadConfiguration, AccidentLocation, RoadSurface, RoadCondition, RoadDefect, Obstacle, Visibility, TrafficSignalType, TrafficSignalAction, MedianBarrier, LaneType, LaneGapType, RoadEdgeLine, AccidentTypeAndPattern, PrimaryCause, InjurySeverity, PrimaryInjuryLocation, ProtectiveEquipment, MobilePhoneUse, PartyType, VehicleUse, PartyActionStatus, DriverQualification, DriverLicenseType, AlcoholUse, InitialVehicleImpact, OtherVehicleImpact, IndividualContributingFactors, PrimaryContributingFactors, HitAndRun, Occupation, TravelPurpose, VehicleType, GPSCoordinateX, GPSCoordinateY, AccidentCategory)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            serial_number,
            county_code,
            agency_code,
            telephone,
            fax,
            year,
            month,
            day,
            hour,
            minute,
            county,
            district,
            number_of_deaths,
            number_of_injuries,
            field_2_to_30,
            weather,
            lighting,
            road_type,
            speed_limit,
            road_configuration,
            accident_location,
            road_surface,
            road_condition,
            road_defect,
            obstacle,
            visibility,
            traffic_signal_type,
            traffic_signal_action,
            median_barrier,
            lane_type,
            lane_gap_type,
            road_edge_line,
            accident_type_and_pattern,
            primary_cause,
            injury_severity,
            primary_injury_location,
            protective_equipment,
            mobile_phone_use,
            party_type,
            vehicle_use,
            party_action_status,
            driver_qualification,
            driver_license_type,
            alcohol_use,
            initial_vehicle_impact,
            other_vehicle_impact,
            individual_contributing_factors,
            primary_contributing_factors,
            hit_and_run,
            occupation,
            travel_purpose,
            vehicle_type,
            gps_coordinate_x,
            gps_coordinate_y,
            accident_category
        )

        print(item)

        cursor.execute(sql, values)
    # 提交更改並關閉連接
    db_connection.commit()
    db_connection.close()


# 使用多進程處理每個 DataItem
if __name__ == "__main__":
    num_processes = min(len(datetime), multiprocessing.cpu_count())
    pool = multiprocessing.Pool(processes=num_processes)

    # 使用map函數將不同的 DataItem 分配給多個進程處理，使用map_async來避免封裝問題
    result = pool.map_async(process_data_item, datetime)
    result.wait()
    pool.close()
    pool.join()
