from pydantic import BaseModel

class PopulationStreet(BaseModel):
    id: int
    trdar_cd: int
    trdar_cd_nm: str
    trdar_se_cd: str
    trdar_se_cd_nm: str
    stdr_yyqu_cd: int

    # 남성 유동인구 수
    ml_flpop_co: int

    # 여성 유동인구 수
    fml_flpop_co: int

    # 요일별 유동인구 수
    sun_flpop_co: int
    mon_flpop_co: int
    tues_flpop_co: int
    wed_flpop_co: int
    thur_flpop_co: int
    fri_flpop_co: int
    sat_flpop_co: int

    # 연령별 유동인구 수
    agrde_10_flpop_co: int
    agrde_20_flpop_co: int
    agrde_30_flpop_co: int
    agrde_40_flpop_co: int
    agrde_50_flpop_co: int
    agrde_60_above_flpop_co: int

    # 시간대
    tot_flpop_co: int
    tmzon_00_06_flpop_co: int
    tmzon_06_11_flpop_co: int
    tmzon_11_14_flpop_co: int
    tmzon_14_17_flpop_co: int
    tmzon_17_21_flpop_co: int
    tmzon_21_24_flpop_co: int

    class Config:
        orm_mode = True

class PopulationResident(BaseModel):
    id: int
    trdar_cd: int
    trdar_cd_nm: str
    trdar_se_cd: str
    trdar_se_cd_nm: str
    stdr_yyqu_cd: int
    tot_repop_co: int

    # 남성 연령대별 상주인구 수
    mag_10_repop_co: int
    mag_20_repop_co: int
    mag_30_repop_co: int
    mag_40_repop_co: int
    mag_50_repop_co: int
    mag_60_above_repop_co: int

    # 여성 연령대별 상주인구 수
    fag_10_repop_co: int
    fag_20_repop_co: int
    fag_30_repop_co: int
    fag_40_repop_co: int
    fag_50_repop_co: int
    fag_60_above_repop_co: int

    # 연령대별 상주인구 수
    agrde_10_repop_co: int
    agrde_20_repop_co: int
    agrde_30_repop_co: int
    agrde_40_repop_co: int
    agrde_50_repop_co: int
    agrde_60_above_repop_co: int

    # 성별 상주인구 수
    ml_repop_co: int
    fml_repop_co: int

    # 가구수
    apt_hshld_co: int
    non_apt_hshld_co: int
    tot_hshld_co: int

    class Config:
        orm_mode = True

class PopulationWorkplace(BaseModel):
    id: int
    trdar_cd: int
    trdar_cd_nm: str
    trdar_se_cd: str
    trdar_se_cd_nm: str
    stdr_yyqu_cd: int
    tot_wrc_popltn_co: int

    # 남성 연령대별 직장 인구 수
    mag_10_wrc_popltn_co: int
    mag_20_wrc_popltn_co: int
    mag_30_wrc_popltn_co: int
    mag_40_wrc_popltn_co: int
    mag_50_wrc_popltn_co: int
    mag_60_above_wrc_popltn_co: int

    # 여성 연령대별 직장 인구 수
    fag_10_wrc_popltn_co: int
    fag_20_wrc_popltn_co: int
    fag_30_wrc_popltn_co: int
    fag_40_wrc_popltn_co: int
    fag_50_wrc_popltn_co: int
    fag_60_above_wrc_popltn_co: int

    # 연령대별 직장 인구 수
    agrde_10_wrc_popltn_co: int
    agrde_20_wrc_popltn_co: int
    agrde_30_wrc_popltn_co: int
    agrde_40_wrc_popltn_co: int
    agrde_50_wrc_popltn_co: int
    agrde_60_above_wrc_popltn_co: int

    # 성별 직장 인구 수
    ml_wrc_popltn_co: int
    fml_wrc_popltn_co: int

    class Config:
        orm_mode = True