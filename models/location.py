from sqlalchemy import *
from db_config import Base

# 아파트
class LocApartmentInfo(Base):
    __tablename__ = 'loc_apartment_info'

    ID = Column(Integer, primary_key=True, autoincrement=True, comment="아파트_ID")

    # 상권 관련 정보
    TRDAR_CD = Column(Integer, nullable=False, comment="상권_코드")
    TRDAR_CD_NM = Column(String, nullable=False, comment="상권_코드_명")
    TRDAR_SE_CD = Column(String, nullable=False, comment="상권_구분_코드")
    TRDAR_SE_CD_NM = Column(String, nullable=False, comment="상권_구분_코드_명")
    STDR_YYQU_CD = Column(Integer, nullable=False, comment="기준_년분기_코드")

    # 아파트 관련 정보
    APT_HSMP_CO = Column(Integer, nullable=False, comment="아파트_단지_수")
    AVRG_AE = Column(Integer, nullable=False, comment="아파트_평균_면적")
    AVRG_MKTC = Column(BigInteger, nullable=False, comment="아파트_평균_시가")

    # 아파트 가격대별 세대 수
    PC_1_HDLMIL_BELO_HSHLD_CO = Column(Integer, nullable=False, comment="아파트_가격_1_억_미만_세대_수")
    PC_1_HDLMIL_HSHLD_CO = Column(Integer, nullable=False, comment="아파트_가격_1_억_세대_수")
    PC_2_HDLMIL_HSHLD_CO = Column(Integer, nullable=False, comment="아파트_가격_2_억_세대_수")
    PC_3_HDLMIL_HSHLD_CO = Column(Integer, nullable=False, comment="아파트_가격_3_억_세대_수")
    PC_4_HDLMIL_HSHLD_CO = Column(Integer, nullable=False, comment="아파트_가격_4_억_세대_수")
    PC_5_HDLMIL_HSHLD_CO = Column(Integer, nullable=False, comment="아파트_가격_5_억_세대_수")
    PC_6_HDLMIL_ABOVE_HSHLD_CO = Column(Integer, nullable=False, comment="아파트_가격_6_억_이상_세대_수")

    # 아파트 면적별 세대 수
    AE_66_SQMT_BELO_HSHLD_CO = Column(Integer, nullable=False, comment="아파트_면적_66_제곱미터_미만_세대_수")
    AE_66_SQMT_HSHLD_CO = Column(Integer, nullable=False, comment="아파트_면적_66_제곱미터_세대_수")
    AE_99_SQMT_HSHLD_CO = Column(Integer, nullable=False, comment="아파트_면적_99_제곱미터_세대_수")
    AE_132_SQMT_HSHLD_CO = Column(Integer, nullable=False, comment="아파트_면적_132_제곱미터_세대_수")
    AE_165_SQMT_HSHLD_CO = Column(Integer, nullable=False, comment="아파트_면적_165_제곱미터_세대_수")



# 상권 영역
class LocAdministrativeDistrict(Base):
    __tablename__ = 'loc_administrative_district'

    ID = Column(Integer, primary_key=True, autoincrement=True, comment="료이키_ID")

    # 상권 관련 정보
    TRDAR_CD = Column(Integer, nullable=False, comment="상권_코드")
    TRDAR_CD_NM = Column(String, nullable=False, comment="상권_코드_명")
    TRDAR_SE_CD = Column(String, nullable=False, comment="상권_구분_코드")
    TRDAR_SE_CD_NM = Column(String, nullable=False, comment="상권_구분_코드_명")

    # 행정동 관련 정보
    ADSTRD_CD = Column(String, nullable=False, comment="행정동_코드")
    ADSTRD_CD_NM = Column(String, nullable=False, comment="행정동_코드_명")

    # 자치구 관련 정보
    SIGNGU_CD = Column(String, nullable=False, comment="자치구_코드")
    SIGNGU_CD_NM = Column(String, nullable=False, comment="자치구_코드_명")

    # 좌표 값
    XCNTS_VALUE = Column(Integer, nullable=False, comment="엑스좌표_값")
    YDNTS_VALUE = Column(Integer, nullable=False, comment="와이좌표_값")

    RELM_AR = Column(Integer, nullable=False, comment="영역_면적")