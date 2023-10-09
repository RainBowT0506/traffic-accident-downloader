import requests
import mysql.connector
import multiprocessing
from DataItem import DataItem

baseUrl = "https://datacenter.taichung.gov.tw/swagger/OpenData/"
datetime = [
    DataItem("11207", baseUrl + "0b8821b0-da2f-4e9e-915d-3c4c809ece39"),
    DataItem("11206", baseUrl + "a6185bb8-dd02-45bb-af75-588f218685e7"),  # 開始新增序號、縣市別代碼、機關代碼、市話、傳真欄位
    DataItem("11205", baseUrl + "f69ecfa4-dcb0-4bad-8973-9de4cdeeed74"),
    DataItem("11204", baseUrl + "d93f538b-b567-45fc-a4ce-56edf4998381"),
    DataItem("11203", baseUrl + "a4e4facb-ee44-477e-9f24-eb1385c6797e"),
    DataItem("11201", baseUrl + "52f7c0a4-e160-404b-9b55-593d41f51753"),
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
        sql = """
        INSERT INTO AccidentData (SerialNumber, CountyCode, AgencyCode, Telephone, Fax, Year, Month, Day, Hour, Minute, County, District, NumberOfDeaths, NumberOfInjuries, Field2To30, Weather, Lighting, RoadType, SpeedLimit, RoadConfiguration, AccidentLocation, RoadSurface, RoadCondition, RoadDefect, Obstacle, Visibility, TrafficSignalType, TrafficSignalAction, MedianBarrier, LaneType, LaneGapType, RoadEdgeLine, AccidentTypeAndPattern, PrimaryCause, InjurySeverity, PrimaryInjuryLocation, ProtectiveEquipment, MobilePhoneUse, PartyType, VehicleUse, PartyActionStatus, DriverQualification, DriverLicenseType, AlcoholUse, InitialVehicleImpact, OtherVehicleImpact, IndividualContributingFactors, PrimaryContributingFactors, HitAndRun, Occupation, TravelPurpose, VehicleType, GPSCoordinateX, GPSCoordinateY, AccidentCategory)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            item["序號"],
            item["縣市別代碼"],
            item["機關代碼"],
            item["市話"],
            item["傳真"],
            item["年"],
            item["月"],
            item["日"],
            item["時"],
            item["分"],
            item["縣市"],
            item["區"],
            item["死亡數量"],
            item["受傷數量"],
            item["2-30"],
            item["天候"],
            item["光線"],
            item["道路類別"],
            item["速限"],
            item["道路型態"],
            item["事故位置"],
            item["路面鋪裝"],
            item["路面狀態"],
            item["路面缺陷"],
            item["障礙物"],
            item["視距"],
            item["號誌種類"],
            item["號誌動作"],
            item["分向設施"],
            item["快車道或一般車道間"],
            item["快慢車道間"],
            item["路面邊線"],
            item["事故類型及型態"],
            item["主要肇因"],
            item["受傷程度"],
            item["主要傷處"],
            item["保護裝備"],
            item["行動電話"],
            item["當事者區分(類別)"],
            item["車輛用途"],
            item["當事者行動狀態"],
            item["駕駛資格情形"],
            item["駕駛執照種類"],
            item["飲酒情形"],
            item["車輛撞擊部位最初"],
            item["車輛撞擊部位其他"],
            item["肇事因素個別"],
            item["肇事因素主要"],
            item["肇事逃逸"],
            item["職業"],
            item["旅次目的"],
            item["車種"],
            item["GPS座標X"],
            item["GPS座標Y"],
            item["事故類別"]
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

    # 使用map函數將不同的 DataItem 分配給多個進程處理
    pool.map(process_data_item, datetime)
    pool.close()
    pool.join()
