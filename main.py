import requests
import mysql.connector
import multiprocessing

from DataSource import datetime


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
        INSERT INTO taichung_accident (SerialNumber, CountyCode, AgencyCode, Telephone, Fax, Year, Month, Day, Hour, Minute, County, District, NumberOfDeaths, NumberOfInjuries, Field2To30, Weather, Lighting, RoadType, SpeedLimit, RoadConfiguration, AccidentLocation, RoadSurface, RoadCondition, RoadDefect, Obstacle, Visibility, TrafficSignalType, TrafficSignalAction, MedianBarrier, LaneType, LaneGapType, RoadEdgeLine, AccidentTypeAndPattern, PrimaryCause, InjurySeverity, PrimaryInjuryLocation, ProtectiveEquipment, MobilePhoneUse, PartyType, VehicleUse, PartyActionStatus, DriverQualification, DriverLicenseType, AlcoholUse, InitialVehicleImpact, OtherVehicleImpact, IndividualContributingFactors, PrimaryContributingFactors, HitAndRun, Occupation, TravelPurpose, VehicleType, GPSCoordinateX, GPSCoordinateY, AccidentCategory)
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
    print("close")


# 使用多進程處理每個 DataItem
if __name__ == "__main__":
    num_processes = min(len(datetime), multiprocessing.cpu_count())
    pool = multiprocessing.Pool(processes=num_processes)

    # 使用map函數將不同的 DataItem 分配給多個進程處理，使用map_async來避免封裝問題
    result = pool.map_async(process_data_item, datetime)
    result.wait()
    pool.close()
    pool.join()
