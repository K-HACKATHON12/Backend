from pydantic import BaseModel

class LocApartmentInfoPydantic(BaseModel):
    ID: int
    TRDAR_CD: int
    TRDAR_CD_NM: str
    TRDAR_SE_CD: str
    TRDAR_SE_CD_NM: str
    STDR_YYQU_CD: int

    # 아파트 관련 정보
    APT_HSMP_CO: int
    AVRG_AE: int
    AVRG_MKTC: int

    # 아파트 가격대별 세대 수
    PC_1_HDLMIL_BELO_HSHLD_CO: int
    PC_1_HDLMIL_HSHLD_CO: int
    PC_2_HDLMIL_HSHLD_CO: int
    PC_3_HDLMIL_HSHLD_CO: int
    PC_4_HDLMIL_HSHLD_CO: int
    PC_5_HDLMIL_HSHLD_CO: int
    PC_6_HDLMIL_ABOVE_HSHLD_CO: int

    # 아파트 면적별 세대 수
    AE_66_SQMT_BELO_HSHLD_CO: int
    AE_66_SQMT_HSHLD_CO: int
    AE_99_SQMT_HSHLD_CO: int
    AE_132_SQMT_HSHLD_CO: int
    AE_165_SQMT_HSHLD_CO: int

    class Config:
        orm_mode = True

class LocAdministrativeDistrictPydantic(BaseModel):
    id: int
    trdar_cd: int
    trdar_cd_nm: str
    trdar_se_cd: str
    trdar_se_cd_nm: str

    # 행정동 관련 정보
    adstrd_cd: str
    adstrd_cd_nm: str

    # 자치구 관련 정보
    signgu_cd: str
    signgu_cd_nm: str

    # 좌표 값
    xcnts_value: int
    ycnts_value: int

    relm_ar: int

    class Config:
        orm_mode = True