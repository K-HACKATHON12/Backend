from pydantic import BaseModel

class CommercialChangeIndicatorPydantic(BaseModel):
    id: int
    trdar_cd: int
    trdar_cd_nm: str
    stdr_yyqu_cd: int
    trdar_se_cd: str
    trdar_se_cd_nm: str
    su_opr_sale_mt_avrg: int
    opr_sale_mt_avrg: int
    trdar_chnge_ix: str
    trdar_chnge_ix_nm: str
    su_cls_sale_mt_avrg: int
    cls_sale_mt_avrg: int

    class Config:
        orm_mode = True

class CommercialExpenditurePydantic(BaseModel):
    ID: int
    TRDAR_CD: int
    TRDAR_CD_NM: str
    TRDAR_SE_CD: str
    TRDAR_SE_CD_NM: str
    STDR_YYQU_CD: int
    LSR_EXPNDTR_TOTAMT: int
    MCP_EXPNDTR_TOTAMT: int
    PLESR_EXPNDTR_TOTAMT: int
    EDC_EXPNDTR_TOTAMT: int
    CLTUR_EXPNDTR_TOTAMT: int
    EXPNDTR_TOTAMT: int
    FDSTFFS_EXPNDTR_TOTAMT: int
    CLTHS_FTWR_EXPNDTR_TOTAMT: int
    LVSPL_EXPNDTR_TOTAMT: int
    TRNSPORT_EXPNDTR_TOTAMT: int
    INCOME_SCTN_CD: int
    MT_AVRG_INCOME_AMT: int

    class Config:
        orm_mode = True

class CommercialSalesInfoPydantic(BaseModel):
    id: int
    trdar_cd: int
    trdar_cd_nm: str
    trdar_se_cd: str
    trdar_se_cd_nm: str
    stdr_yyqu_cd: int

    # 연령대별 매출 금액 및 건수
    agrde_10_selng_amt: int
    agrde_10_selng_co: int
    agrde_20_selng_amt: int
    agrde_20_selng_co: int
    agrde_30_selng_amt: int
    agrde_30_selng_co: int
    agrde_40_selng_amt: int
    agrde_40_selng_co: int
    agrde_50_selng_amt: int
    agrde_50_selng_co: int
    agrde_60_above_selng_amt: int
    agrde_60_above_selng_co: int

    # 시간대별 매출 금액 및 건수
    tmzon_00_06_selng_amt: int
    tmzon_00_06_selng_co: int
    tmzon_06_11_selng_amt: int
    tmzon_06_11_selng_co: int
    tmzon_11_14_selng_amt: int
    tmzon_11_14_selng_co: int
    tmzon_14_17_selng_amt: int
    tmzon_14_17_selng_co: int
    tmzon_17_21_selng_amt: int
    tmzon_17_21_selng_co: int
    tmzon_21_24_selng_amt: int
    tmzon_21_24_selng_co: int

    # 요일별 매출 금액 및 건수
    mon_selng_amt: int
    mon_selng_co: int
    tues_selng_amt: int
    tues_selng_co: int
    wed_selng_amt: int
    wed_selng_co: int
    thur_selng_amt: int
    thur_selng_co: int
    fri_selng_amt: int
    fri_selng_co: int
    sat_selng_amt: int
    sat_selng_co: int
    sun_selng_amt: int
    sun_selng_co: int

    # 성별 매출 금액 및 건수
    ml_selng_amt: int
    ml_selng_co: int
    fml_selng_amt: int
    fml_selng_co: int

    # 주중 및 주말 매출 금액 및 건수
    mdwk_selng_amt: int
    mdwk_selng_co: int
    wkend_selng_amt: int
    wkend_selng_co: int

    # 당월 매출 금액 및 건수
    thsmon_selng_amt: int
    thsmon_selng_co: int

    # 서비스 업종 관련 정보
    svc_induty_cd: str
    svc_induty_cd_nm: str

    class Config:
        orm_mode = True

class CommercialBusinessInfoPydantic(BaseModel):
    id: int
    trdar_cd: int
    trdar_cd_nm: str
    trdar_se_cd: str
    trdar_se_cd_nm: str
    stdr_yyqu_cd: int

    # 점포 관련 정보
    stor_co: int
    opbiz_stor_co: int
    clsbiz_stor_co: int
    frc_stor_co: int
    similr_induty_stor_co: int

    # 서비스 업종 관련 정보
    svc_induty_cd: str
    svc_induty_cd_nm: str

    # 비율 관련 정보
    opbiz_rt: float
    clsbiz_rt: float

    class Config:
        orm_mode = True

class CommercialFacilityInfoPydantic(BaseModel):
    id: int
    trdar_cd: int
    trdar_cd_nm: str
    trdar_se_cd: str
    trdar_se_cd_nm: str
    stdr_yyqu_cd: int

    # 시설 관련 정보
    kndrgr_co: int
    bus_sttn_co: int
    rlroad_statn_co: int
    drts_co: int
    supmk_co: int
    hgschl_co: int
    univ_co: int
    gehspot_co: int
    elesch_co: int
    pblofc_co: int
    bank_co: int
    theat_co: int
    arprt_co: int
    bus_trminl_co: int
    viatr_fclty_co: int
    stayng_fclty_co: int
    mskul_co: int
    parmac_co: int
    gnrl_hsptl_co: int
    subway_statn_co: int

    class Config:
        orm_mode = True