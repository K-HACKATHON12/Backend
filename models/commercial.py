from sqlalchemy import *
from db_config import Base

# 상권 변화 지표 데이터 모델
class CommercialChangeIndicator(Base):
    __tablename__ = 'commercial_change_indicator'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="상권변화지표_ID")

    trdar_cd = Column(Integer, nullable=False, comment="상권_코드")
    trdar_cd_nm = Column(String, nullable=False, comment="상권_코드_명")

    stdr_yyqu_cd = Column(Integer, nullable=False, comment="기준_년분기_코드")

    trdar_se_cd = Column(String, nullable=False, comment="상권_구분_코드")
    trdar_se_cd_nm = Column(String, nullable=False, comment="상권_구분_코드_명")

    # 운영 영업 개월 평균
    su_opr_sale_mt_avrg = Column(Integer, nullable=False, comment="서울_운영_영업_개월_평균")
    opr_sale_mt_avrg = Column(Integer, nullable=False, comment="운영_영업_개월_평균")

    # 상권 변화 지표
    trdar_chnge_ix = Column(String, nullable=False, comment="상권_변화_지표")
    trdar_chnge_ix_nm = Column(String, nullable=False, comment="상권_변화_지표_명")

    # 서울 폐업 영업 개월 평균
    su_cls_sale_mt_avrg = Column(Integer, nullable=False, comment="서울_폐업_영업_개월_평균")

    # 폐업 영업 개월 평균
    cls_sale_mt_avrg = Column(Integer, nullable=False, comment="폐업_영업_개월_평균")



# 상권 소득 소비 데이터 모델
class CommercialExpenditure(Base):
    __tablename__ = 'commercial_expenditure'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="소득소비_ID")

    # 상권 관련 정보
    trdar_cd = Column(Integer, nullable=False, comment="상권_코드")
    trdar_cd_nm = Column(String, nullable=False, comment="상권_코드_명")
    trdar_se_cd = Column(String, nullable=False, comment="상권_구분_코드")
    trdar_se_cd_nm = Column(String, nullable=False, comment="상권_구분_코드_명")
    stdr_yyqu_cd = Column(Integer, nullable=False, comment="기준_년분기_코드")

    # 지출 항목별 총 금액
    lsr_expndtr_totamt = Column(BigInteger, nullable=False, comment="여가_지출_총금액")
    mcp_expndtr_totamt = Column(BigInteger, nullable=False, comment="의료비_지출_총금액")
    plesr_expndtr_totamt = Column(BigInteger, nullable=False, comment="유흥_지출_총금액")
    edc_expndtr_totamt = Column(BigInteger, nullable=False, comment="교육_지출_총금액")
    cltur_expndtr_totamt = Column(BigInteger, nullable=False, comment="문화_지출_총금액")
    expndtr_totamt = Column(BigInteger, nullable=False, comment="지출_총금액")
    fdstffs_expndtr_totamt = Column(BigInteger, nullable=False, comment="식료품_지출_총금액")
    clths_ftwr_expndtr_totamt = Column(BigInteger, nullable=False, comment="의류_신발_지출_총금액")
    lvspl_expndtr_totamt = Column(BigInteger, nullable=False, comment="생활용품_지출_총금액")
    trnsport_expndtr_totamt = Column(BigInteger, nullable=False, comment="교통_지출_총금액")

    # 소득 관련 정보
    income_sctn_cd = Column(Integer, nullable=False, comment="소득_구간_코드")
    mt_avrg_income_amt = Column(BigInteger, nullable=False, comment="월_평균_소득_금액")

# 상권 추정 매출 데이터 모델
class CommercialSalesInfo(Base):
    __tablename__ = 'commercial_sales_info'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, comment="추정매출_ID")
    trdar_cd = Column(Integer, nullable=False, comment="상권_코드")
    trdar_cd_nm = Column(String, nullable=False, comment="상권_코드_명")
    trdar_se_cd = Column(String, nullable=False, comment="상권_구분_코드")
    trdar_se_cd_nm = Column(String, nullable=False, comment="상권_구분_코드_명")
    stdr_yyqu_cd = Column(Integer, nullable=False, comment="기준_년분기_코드")

    # 연령대별 매출 금액 및 건수
    agrde_10_selng_amt = Column(BigInteger, nullable=False, default=0, comment="연령대_10_매출_금액")
    agrde_10_selng_co = Column(Integer, nullable=False, default=0, comment="연령대_10_매출_건수")
    agrde_20_selng_amt = Column(BigInteger, nullable=False, default=0, comment="연령대_20_매출_금액")
    agrde_20_selng_co = Column(Integer, nullable=False, default=0, comment="연령대_20_매출_건수")
    agrde_30_selng_amt = Column(BigInteger, nullable=False, default=0, comment="연령대_30_매출_금액")
    agrde_30_selng_co = Column(Integer, nullable=False, default=0, comment="연령대_30_매출_건수")
    agrde_40_selng_amt = Column(BigInteger, nullable=False, default=0, comment="연령대_40_매출_금액")
    agrde_40_selng_co = Column(Integer, nullable=False, default=0, comment="연령대_40_매출_건수")
    agrde_50_selng_amt = Column(BigInteger, nullable=False, default=0, comment="연령대_50_매출_금액")
    agrde_50_selng_co = Column(Integer, nullable=False, default=0, comment="연령대_50_매출_건수")
    agrde_60_above_selng_amt = Column(BigInteger, nullable=False, default=0, comment="연령대_60_이상_매출_금액")
    agrde_60_above_selng_co = Column(Integer, nullable=False, default=0, comment="연령대_60_이상_매출_건수")

    # 시간대별 매출 금액 및 건수
    tmzon_00_06_selng_amt = Column(BigInteger, nullable=False, default=0, comment="시간대_00~06_매출_금액")
    tmzon_00_06_selng_co = Column(Integer, nullable=False, default=0, comment="시간대_00~06_매출_건수")
    tmzon_06_11_selng_amt = Column(BigInteger, nullable=False, default=0, comment="시간대_06~11_매출_금액")
    tmzon_06_11_selng_co = Column(Integer, nullable=False, default=0, comment="시간대_06~11_매출_건수")
    tmzon_11_14_selng_amt = Column(BigInteger, nullable=False, default=0, comment="시간대_11~14_매출_금액")
    tmzon_11_14_selng_co = Column(Integer, nullable=False, default=0, comment="시간대_11~14_매출_건수")
    tmzon_14_17_selng_amt = Column(BigInteger, nullable=False, default=0, comment="시간대_14~17_매출_금액")
    tmzon_14_17_selng_co = Column(Integer, nullable=False, default=0, comment="시간대_14~17_매출_건수")
    tmzon_17_21_selng_amt = Column(BigInteger, nullable=False, default=0, comment="시간대_17~21_매출_금액")
    tmzon_17_21_selng_co = Column(Integer, nullable=False, default=0, comment="시간대_17~21_매출_건수")
    tmzon_21_24_selng_amt = Column(BigInteger, nullable=False, default=0, comment="시간대_21~24_매출_금액")
    tmzon_21_24_selng_co = Column(Integer, nullable=False, default=0, comment="시간대_21~24_매출_건수")

    # 요일별 매출 금액 및 건수
    mon_selng_amt = Column(BigInteger, nullable=False, default=0, comment="월요일_매출_금액")
    mon_selng_co = Column(Integer, nullable=False, default=0, comment="월요일_매출_건수")
    tues_selng_amt = Column(BigInteger, nullable=False, default=0, comment="화요일_매출_금액")
    tues_selng_co = Column(Integer, nullable=False, default=0, comment="화요일_매출_건수")
    wed_selng_amt = Column(BigInteger, nullable=False, default=0, comment="수요일_매출_금액")
    wed_selng_co = Column(Integer, nullable=False, default=0, comment="수요일_매출_건수")
    thur_selng_amt = Column(BigInteger, nullable=False, default=0, comment="목요일_매출_금액")
    thur_selng_co = Column(Integer, nullable=False, default=0, comment="목요일_매출_건수")
    fri_selng_amt = Column(BigInteger, nullable=False, default=0, comment="금요일_매출_금액")
    fri_selng_co = Column(Integer, nullable=False, default=0, comment="금요일_매출_건수")
    sat_selng_amt = Column(BigInteger, nullable=False, default=0, comment="토요일_매출_금액")
    sat_selng_co = Column(Integer, nullable=False, default=0, comment="토요일_매출_건수")
    sun_selng_amt = Column(BigInteger, nullable=False, default=0, comment="일요일_매출_금액")
    sun_selng_co = Column(Integer, nullable=False, default=0, comment="일요일_매출_건수")

    # 성별 매출 금액 및 건수
    ml_selng_amt = Column(BigInteger, nullable=False, default=0, comment="남성_매출_금액")
    ml_selng_co = Column(Integer, nullable=False, default=0, comment="남성_매출_건수")
    fml_selng_amt = Column(BigInteger, nullable=False, default=0, comment="여성_매출_금액")
    fml_selng_co = Column(Integer, nullable=False, default=0, comment="여성_매출_건수")

    # 주중 및 주말 매출 금액 및 건수
    mdwk_selng_amt = Column(BigInteger, nullable=False, default=0, comment="주중_매출_금액")
    mdwk_selng_co = Column(Integer, nullable=False, default=0, comment="주중_매출_건수")
    wkend_selng_amt = Column(BigInteger, nullable=False, default=0, comment="주말_매출_금액")
    wkend_selng_co = Column(Integer, nullable=False, default=0, comment="주말_매출_건수")

    # 당월 매출 금액 및 건수
    thsmon_selng_amt = Column(BigInteger, nullable=False, default=0, comment="당월_매출_금액")
    thsmon_selng_co = Column(Integer, nullable=False, default=0, comment="당월_매출_건수")

    # 서비스 업종 관련 정보
    svc_induty_cd = Column(String, nullable=False, comment="서비스_업종_코드")
    svc_induty_cd_nm = Column(String, nullable=False, comment="서비스_업종_코드_명")

# 점포
class CommercialBusinessInfo(Base):
    __tablename__ = 'commercial_business_info'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="점포_ID")

    # 상권 관련 정보
    trdar_cd = Column(Integer, nullable=False, comment="상권_코드")
    trdar_cd_nm = Column(String, nullable=False, comment="상권_코드_명")
    trdar_se_cd = Column(String, nullable=False, comment="상권_구분_코드")
    trdar_se_cd_nm = Column(String, nullable=False, comment="상권_구분_코드_명")
    stdr_yyqu_cd = Column(Integer, nullable=False, comment="기준_년분기_코드")

    # 점포 관련 정보
    stor_co = Column(Integer, nullable=False, comment="점포_수")
    opbiz_stor_co = Column(Integer, nullable=False, comment="개업_점포_수")
    clsbiz_stor_co = Column(Integer, nullable=False, comment="폐업_점포_수")
    frc_stor_co = Column(Integer, nullable=False, comment="프랜차이즈_점포_수")
    similr_induty_stor_co = Column(Integer, nullable=False, comment="유사_업종_점포_수")

    # 서비스 업종 관련 정보
    svc_induty_cd = Column(String, nullable=False, comment="서비스_업종_코드")
    svc_induty_cd_nm = Column(String, nullable=False, comment="서비스_업종_코드_명")

    # 비율 관련 정보
    opbiz_rt = Column(Float, nullable=False, comment="개업_율")
    clsbiz_rt = Column(Float, nullable=False, comment="폐업_률")


# 집객시설
class CommercialFacilityInfo(Base):
    __tablename__ = 'commercial_facility_info'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="집객시설_ID")

    # 상권 관련 정보
    trdar_cd = Column(Integer, nullable=False, comment="상권_코드")
    trdar_cd_nm = Column(String, nullable=False, comment="상권_코드_명")
    trdar_se_cd = Column(String, nullable=False, comment="상권_구분_코드")
    trdar_se_cd_nm = Column(String, nullable=False, comment="상권_구분_코드_명")
    stdr_yyqu_cd = Column(Integer, nullable=False, comment="기준_년분기_코드")

    # 시설 관련 정보
    kndrgr_co = Column(Integer, nullable=False, default=0, comment="유치원_수")
    bus_sttn_co = Column(Integer, nullable=False, default=0, comment="버스_정거장_수")
    rlroad_statn_co = Column(Integer, nullable=False, default=0, comment="철도_역_수")
    drts_co = Column(Integer, nullable=False, default=0, comment="백화점_수")
    supmk_co = Column(Integer, nullable=False, default=0, comment="슈퍼마켓_수")
    hgschl_co = Column(Integer, nullable=False, default=0, comment="고등학교_수")
    univ_co = Column(Integer, nullable=False, default=0, comment="대학교_수")
    gehspot_co = Column(Integer, nullable=False, default=0, comment="종합병원_수")
    elesch_co = Column(Integer, nullable=False, default=0, comment="초등학교_수")
    pblofc_co = Column(Integer, nullable=False, default=0, comment="관공서_수")
    bank_co = Column(Integer, nullable=False, default=0, comment="은행_수")
    theat_co = Column(Integer, nullable=False, default=0, comment="극장_수")
    arprt_co = Column(Integer, nullable=False, default=0, comment="공항_수")
    bus_trminl_co = Column(Integer, nullable=False, default=0, comment="버스_터미널_수")
    viatr_fclty_co = Column(Integer, nullable=False, default=0, comment="집객시설_수")
    stayng_fclty_co = Column(Integer, nullable=False, default=0, comment="숙박_시설_수")
    mskul_co = Column(Integer, nullable=False, default=0, comment="중학교_수")
    parmac_co = Column(Integer, nullable=False, default=0, comment="약국_수")
    gnrl_hsptl_co = Column(Integer, nullable=False, default=0, comment="일반_병원_수")
    subway_statn_co = Column(Integer, nullable=False, default=0, comment="지하철_역_수")