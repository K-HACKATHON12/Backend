from sqlalchemy import *
from db_config import Base

# 아파트
class LocApartmentInfo(Base):
    __tablename__ = 'loc_apartment_info'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="아파트_ID")

    # 상권 관련 정보
    trdar_cd = Column(Integer, nullable=False, comment="상권_코드")
    trdar_cd_nm = Column(String, nullable=False, comment="상권_코드_명")
    trdar_se_cd = Column(String, nullable=False, comment="상권_구분_코드")
    trdar_se_cd_nm = Column(String, nullable=False, comment="상권_구분_코드_명")
    stdr_yyqu_cd = Column(Integer, nullable=False, comment="기준_년분기_코드")

    # 아파트 관련 정보
    apt_hsmp_co = Column(Integer, nullable=False, comment="아파트_단지_수")
    avrg_ae = Column(Integer, nullable=False, comment="아파트_평균_면적")
    avrg_mktc = Column(BigInteger, nullable=False, comment="아파트_평균_시가")

    # 아파트 가격대별 세대 수
    pc_1_hdlmil_belo_hshld_co = Column(Integer, nullable=False, comment="아파트_가격_1_억_미만_세대_수")
    pc_1_hdlmil_hshld_co = Column(Integer, nullable=False, comment="아파트_가격_1_억_세대_수")
    pc_2_hdlmil_hshld_co = Column(Integer, nullable=False, comment="아파트_가격_2_억_세대_수")
    pc_3_hdlmil_hshld_co = Column(Integer, nullable=False, comment="아파트_가격_3_억_세대_수")
    pc_4_hdlmil_hshld_co = Column(Integer, nullable=False, comment="아파트_가격_4_억_세대_수")
    pc_5_hdlmil_hshld_co = Column(Integer, nullable=False, comment="아파트_가격_5_억_세대_수")
    pc_6_hdlmil_above_hshld_co = Column(Integer, nullable=False, comment="아파트_가격_6_억_이상_세대_수")

    # 아파트 면적별 세대 수
    ae_66_sqmt_belo_hshld_co = Column(Integer, nullable=False, comment="아파트_면적_66_제곱미터_미만_세대_수")
    ae_66_sqmt_hshld_co = Column(Integer, nullable=False, comment="아파트_면적_66_제곱미터_세대_수")
    ae_99_sqmt_hshld_co = Column(Integer, nullable=False, comment="아파트_면적_99_제곱미터_세대_수")
    ae_132_sqmt_hshld_co = Column(Integer, nullable=False, comment="아파트_면적_132_제곱미터_세대_수")
    ae_165_sqmt_hshld_co = Column(Integer, nullable=False, comment="아파트_면적_165_제곱미터_세대_수")


# 상권 영역
class LocAdministrativeDistrict(Base):
    __tablename__ = 'loc_administrative_district'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="료이키_ID")

    # 상권 관련 정보
    trdar_cd = Column(Integer, nullable=False, comment="상권_코드")
    trdar_cd_nm = Column(String, nullable=False, comment="상권_코드_명")
    trdar_se_cd = Column(String, nullable=False, comment="상권_구분_코드")
    trdar_se_cd_nm = Column(String, nullable=False, comment="상권_구분_코드_명")

    # 행정동 관련 정보
    adstrd_cd = Column(String, nullable=False, comment="행정동_코드")
    adstrd_cd_nm = Column(String, nullable=False, comment="행정동_코드_명")

    # 자치구 관련 정보
    signgu_cd = Column(String, nullable=False, comment="자치구_코드")
    signgu_cd_nm = Column(String, nullable=False, comment="자치구_코드_명")

    # 좌표 값
    xcnts_value = Column(Integer, nullable=False, comment="엑스좌표_값")
    ycnts_value = Column(Integer, nullable=False, comment="와이좌표_값")

    relm_ar = Column(Integer, nullable=False, comment="영역_면적")