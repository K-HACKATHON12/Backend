from pydantic import BaseModel

class LocApartmentInfoPydantic(BaseModel):
    id: int
    trdar_cd: int
    trdar_cd_nm: str
    trdar_se_cd: str
    trdar_se_cd_nm: str
    stdr_yyqu_cd: int

    # 아파트 관련 정보
    apt_hsmp_co: int
    avrg_ae: int
    avrg_mktc: int

    # 아파트 가격대별 세대 수
    pc_1_hdlmil_belo_hshld_co: int
    pc_1_hdlmil_hshld_co: int
    pc_2_hdlmil_hshld_co: int
    pc_3_hdlmil_hshld_co: int
    pc_4_hdlmil_hshld_co: int
    pc_5_hdlmil_hshld_co: int
    pc_6_hdlmil_above_hshld_co: int

    # 아파트 면적별 세대 수
    ae_66_sqmt_belo_hshld_co: int
    ae_66_sqmt_hshld_co: int
    ae_99_sqmt_hshld_co: int
    ae_132_sqmt_hshld_co: int
    ae_165_sqmt_hshld_co: int

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