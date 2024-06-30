from sqlalchemy import *
from db_config import Base

# 길단위 인구
class PopulationStreet(Base):
    __tablename__ = 'population_street'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="길단위인구_ID")

    # 상권 코드
    trdar_cd = Column(Integer, nullable=False, comment="상권_코드")
    trdar_cd_nm = Column(String, nullable=False, comment="상권_코드_명")
    trdar_se_cd = Column(String, nullable=False, comment="상권_구분_코드")
    trdar_se_cd_nm = Column(String, nullable=False, comment="상권_구분_코드_명")
    stdr_yyqu_cd = Column(Integer, nullable=False, comment="기준_년분기_코드")

    # 남성 유동인구 수
    ml_flpop_co = Column(Integer, nullable=False, comment="남성_유동인구_수")

    # 여성 유동인구 수
    fml_flpop_co = Column(Integer, nullable=False, comment="여성_유동인구_수")

    # 요일별 유동인구 수
    sun_flpop_co = Column(Integer, nullable=False, comment="일요일_유동인구_수")
    mon_flpop_co = Column(Integer, nullable=False, comment="월요일_유동인구_수")
    tues_flpop_co = Column(Integer, nullable=False, comment="화요일_유동인구_수")
    wed_flpop_co = Column(Integer, nullable=False, comment="수요일_유동인구_수")
    thur_flpop_co = Column(Integer, nullable=False, comment="목요일_유동인구_수")
    fri_flpop_co = Column(Integer, nullable=False, comment="금요일_유동인구_수")
    sat_flpop_co = Column(Integer, nullable=False, comment="토요일_유동인구_수")

    # 연령별 유동인구 수
    agrde_10_flpop_co = Column(Integer, nullable=False, comment="연령대_10_유동인구_수")
    agrde_20_flpop_co = Column(Integer, nullable=False, comment="연령대_20_유동인구_수")
    agrde_30_flpop_co = Column(Integer, nullable=False, comment="연령대_30_유동인구_수")
    agrde_40_flpop_co = Column(Integer, nullable=False, comment="연령대_40_유동인구_수")
    agrde_50_flpop_co = Column(Integer, nullable=False, comment="연령대_50_유동인구_수")
    agrde_60_above_flpop_co = Column(Integer, nullable=False, comment="연령대_60_이상_유동인구_수")

    # 시간대
    tot_flpop_co = Column(Integer, nullable=False, comment="총_유동인구_수")
    tmzon_00_06_flpop_co = Column(Integer, nullable=False, comment="시간대_00_06_유동인구_수")
    tmzon_06_11_flpop_co = Column(Integer, nullable=False, comment="시간대_06_11_유동인구_수")
    tmzon_11_14_flpop_co = Column(Integer, nullable=False, comment="시간대_11_14_유동인구_수")
    tmzon_14_17_flpop_co = Column(Integer, nullable=False, comment="시간대_14_17_유동인구_수")
    tmzon_17_21_flpop_co = Column(Integer, nullable=False, comment="시간대_17_21_유동인구_수")
    tmzon_21_24_flpop_co = Column(Integer, nullable=False, comment="시간대_21_24_유동인구_수")

# 상주 인구
class PopulationResident(Base):
    __tablename__ = 'population_resident'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="상주인구_ID")

    # 상권 코드
    trdar_cd = Column(Integer, nullable=False, comment="상권_코드")
    trdar_cd_nm = Column(String, nullable=False, comment="상권_코드_명")
    trdar_se_cd = Column(String, nullable=False, comment="상권_구분_코드")
    trdar_se_cd_nm = Column(String, nullable=False, comment="상권_구분_코드_명")
    stdr_yyqu_cd = Column(Integer, nullable=False, comment="기준_년분기_코드")

    tot_repop_co = Column(Integer, nullable=False, comment="총_상주인구_수")

    # 남성 연령대별 상주인구 수
    mag_10_repop_co = Column(Integer, nullable=False, comment="남성연령대_10_상주인구_수")
    mag_20_repop_co = Column(Integer, nullable=False, comment="남성연령대_20_상주인구_수")
    mag_30_repop_co = Column(Integer, nullable=False, comment="남성연령대_30_상주인구_수")
    mag_40_repop_co = Column(Integer, nullable=False, comment="남성연령대_40_상주인구_수")
    mag_50_repop_co = Column(Integer, nullable=False, comment="남성연령대_50_상주인구_수")
    mag_60_above_repop_co = Column(Integer, nullable=False, comment="남성연령대_60_이상_상주인구_수")

    # 여성 연령대별 상주인구 수
    fag_10_repop_co = Column(Integer, nullable=False, comment="여성연령대_10_상주인구_수")
    fag_20_repop_co = Column(Integer, nullable=False, comment="여성연령대_20_상주인구_수")
    fag_30_repop_co = Column(Integer, nullable=False, comment="여성연령대_30_상주인구_수")
    fag_40_repop_co = Column(Integer, nullable=False, comment="여성연령대_40_상주인구_수")
    fag_50_repop_co = Column(Integer, nullable=False, comment="여성연령대_50_상주인구_수")
    fag_60_above_repop_co = Column(Integer, nullable=False, comment="여성연령대_60_이상_상주인구_수")

    # 연령대별 상주인구 수
    agrde_10_repop_co = Column(Integer, nullable=False, comment="연령대_10_상주인구_수")
    agrde_20_repop_co = Column(Integer, nullable=False, comment="연령대_20_상주인구_수")
    agrde_30_repop_co = Column(Integer, nullable=False, comment="연령대_30_상주인구_수")
    agrde_40_repop_co = Column(Integer, nullable=False, comment="연령대_40_상주인구_수")
    agrde_50_repop_co = Column(Integer, nullable=False, comment="연령대_50_상주인구_수")
    agrde_60_above_repop_co = Column(Integer, nullable=False, comment="연령대_60_이상_상주인구_수")

    # 성별 상주인구 수
    ml_repop_co = Column(Integer, nullable=False, comment="남성_상주인구_수")
    fml_repop_co = Column(Integer, nullable=False, comment="여성_상주인구_수")

    # 가구수
    apt_hshld_co = Column(Integer, nullable=False, comment="아파트_가구_수")
    non_apt_hshld_co = Column(Integer, nullable=False, comment="비_아파트_가구_수")
    tot_hshld_co = Column(Integer, nullable=False, comment="총_가구_수")

# 직장 인구
class PopulationWorkplace(Base):
    __tablename__ = 'population_workplace'

    ID = Column(Integer, primary_key=True, autoincrement=True, comment="직장인구_ID")

    TRDAR_CD = Column(Integer, nullable=False, comment="상권_코드")
    TRDAR_CD_NM = Column(String, nullable=False, comment="상권_코드_명")
    TRDAR_SE_CD = Column(String, nullable=False, comment="상권_구분_코드")
    TRDAR_SE_CD_NM = Column(String, nullable=False, comment="상권_구분_코드_명")
    STDR_YYQU_CD = Column(Integer, nullable=False, comment="기준_년분기_코드")

    TOT_WRC_POPLTN_CO = Column(Integer, nullable=False, comment="총_직장_인구_수")
    MAG_10_WRC_POPLTN_CO = Column(Integer, nullable=False, comment="남성연령대_10_직장_인구_수")
    MAG_20_WRC_POPLTN_CO = Column(Integer, nullable=False, comment="남성연령대_20_직장_인구_수")
    MAG_30_WRC_POPLTN_CO = Column(Integer, nullable=False, comment="남성연령대_30_직장_인구_수")
    MAG_40_WRC_POPLTN_CO = Column(Integer, nullable=False, comment="남성연령대_40_직장_인구_수")
    MAG_50_WRC_POPLTN_CO = Column(Integer, nullable=False, comment="남성연령대_50_직장_인구_수")
    MAG_60_ABOVE_WRC_POPLTN_CO = Column(Integer, nullable=False, comment="남성연령대_60_이상_직장_인구_수")

    FAG_10_WRC_POPLTN_CO = Column(Integer, nullable=False, comment="여성연령대_10_직장_인구_수")
    FAG_20_WRC_POPLTN_CO = Column(Integer, nullable=False, comment="여성연령대_20_직장_인구_수")
    FAG_30_WRC_POPLTN_CO = Column(Integer, nullable=False, comment="여성연령대_30_직장_인구_수")
    FAG_40_WRC_POPLTN_CO = Column(Integer, nullable=False, comment="여성연령대_40_직장_인구_수")
    FAG_50_WRC_POPLTN_CO = Column(Integer, nullable=False, comment="여성연령대_50_직장_인구_수")
    FAG_60_ABOVE_WRC_POPLTN_CO = Column(Integer, nullable=False, comment="여성연령대_60_이상_직장_인구_수")

    AGRDE_10_WRC_POPLTN_CO = Column(Integer, nullable=False, comment="연령대_10_직장_인구_수")
    AGRDE_20_WRC_POPLTN_CO = Column(Integer, nullable=False, comment="연령대_20_직장_인구_수")
    AGRDE_30_WRC_POPLTN_CO = Column(Integer, nullable=False, comment="연령대_30_직장_인구_수")
    AGRDE_40_WRC_POPLTN_CO = Column(Integer, nullable=False, comment="연령대_40_직장_인구_수")
    AGRDE_50_WRC_POPLTN_CO = Column(Integer, nullable=False, comment="연령대_50_직장_인구_수")
    AGRDE_60_ABOVE_WRC_POPLTN_CO = Column(Integer, nullable=False, comment="연령대_60_이상_직장_인구_수")

    ML_WRC_POPLTN_CO = Column(Integer, nullable=False, comment="남성_직장_인구_수")
    FML_WRC_POPLTN_CO = Column(Integer, nullable=False, comment="여성_직장_인구_수")