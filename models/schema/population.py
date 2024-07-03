from pydantic import BaseModel

class PopulationStreetPydantic(BaseModel):
    ID: int
    TRDAR_CD: int
    TRDAR_CD_NM: str
    TRDAR_SE_CD: str
    TRDAR_SE_CD_NM: str
    STDR_YYQU_CD: int

    # 남성 유동인구 수
    ML_FLPOP_CO: int

    # 여성 유동인구 수
    FML_FLPOP_CO: int

    # 요일별 유동인구 수
    SUN_FLPOP_CO: int
    MON_FLPOP_CO: int
    TUES_FLPOP_CO: int
    WED_FLPOP_CO: int
    THUR_FLPOP_CO: int
    FRI_FLPOP_CO: int
    SAT_FLPOP_CO: int

    # 연령별 유동인구 수
    AGRDE_10_FLPOP_CO: int
    AGRDE_20_FLPOP_CO: int
    AGRDE_30_FLPOP_CO: int
    AGRDE_40_FLPOP_CO: int
    AGRDE_50_FLPOP_CO: int
    AGRDE_60_ABOVE_FLPOP_CO: int

    # 시간대
    TOT_FLPOP_CO: int
    TMZON_00_06_FLPOP_CO: int
    TMZON_06_11_FLPOP_CO: int
    TMZON_11_14_FLPOP_CO: int
    TMZON_14_17_FLPOP_CO: int
    TMZON_17_21_FLPOP_CO: int
    TMZON_21_24_FLPOP_CO: int

    class Config:
        orm_mode = True

class PopulationResidentPydantic(BaseModel):
    ID: int
    TRDAR_CD: int
    TRDAR_CD_NM: str
    TRDAR_SE_CD: str
    TRDAR_SE_CD_NM: str
    STDR_YYQU_CD: int
    TOT_REPOP_CO: int

    # 남성 연령대별 상주인구 수
    MAG_10_REPOP_CO: int
    MAG_20_REPOP_CO: int
    MAG_30_REPOP_CO: int
    MAG_40_REPOP_CO: int
    MAG_50_REPOP_CO: int
    MAG_60_ABOVE_REPOP_CO: int

    # 여성 연령대별 상주인구 수
    FAG_10_REPOP_CO: int
    FAG_20_REPOP_CO: int
    FAG_30_REPOP_CO: int
    FAG_40_REPOP_CO: int
    FAG_50_REPOP_CO: int
    FAG_60_ABOVE_REPOP_CO: int

    # 연령대별 상주인구 수
    AGRDE_10_REPOP_CO: int
    AGRDE_20_REPOP_CO: int
    AGRDE_30_REPOP_CO: int
    AGRDE_40_REPOP_CO: int
    AGRDE_50_REPOP_CO: int
    AGRDE_60_ABOVE_REPOP_CO: int

    # 성별 상주인구 수
    ML_REPOP_CO: int
    FML_REPOP_CO: int

    # 가구수
    APT_HSHLD_CO: int
    NON_APT_HSHLD_CO: int
    TOT_HSHLD_CO: int


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