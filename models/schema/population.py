from pydantic import BaseModel

class PopulationStreetPydantic(BaseModel):
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

class PopulationResidentPydantic(BaseModel):
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

class PopulationWorkplacePydantic(BaseModel):
    ID: int
    TRDAR_CD: int
    TRDAR_CD_NM: str
    TRDAR_SE_CD: str
    TRDAR_SE_CD_NM: str
    STDR_YYQU_CD: int
    TOT_WRC_POPLTN_CO: int
    MAG_10_WRC_POPLTN_CO: int
    MAG_20_WRC_POPLTN_CO: int
    MAG_30_WRC_POPLTN_CO: int
    MAG_40_WRC_POPLTN_CO: int
    MAG_50_WRC_POPLTN_CO: int
    MAG_60_ABOVE_WRC_POPLTN_CO: int
    FAG_10_WRC_POPLTN_CO: int
    FAG_20_WRC_POPLTN_CO: int
    FAG_30_WRC_POPLTN_CO: int
    FAG_40_WRC_POPLTN_CO: int
    FAG_50_WRC_POPLTN_CO: int
    FAG_60_ABOVE_WRC_POPLTN_CO: int
    AGRDE_10_WRC_POPLTN_CO: int
    AGRDE_20_WRC_POPLTN_CO: int
    AGRDE_30_WRC_POPLTN_CO: int
    AGRDE_40_WRC_POPLTN_CO: int
    AGRDE_50_WRC_POPLTN_CO: int
    AGRDE_60_ABOVE_WRC_POPLTN_CO: int
    ML_WRC_POPLTN_CO: int
    FML_WRC_POPLTN_CO: int

    class Config:
        orm_mode = True