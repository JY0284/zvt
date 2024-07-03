# -*- coding: utf-8 -*-
# this file is generated by gen_kdata_schema function, dont't change it
from sqlalchemy.orm import declarative_base

from zvt.contract.register import register_schema
from zvt.domain.quotes import StockKdataCommon

KdataBase = declarative_base()


class Stock1hHfqKdata(KdataBase, StockKdataCommon):
    __tablename__ = "stock_1h_hfq_kdata"


register_schema(
    providers=["em", "qmt", "joinquant"], db_name="stock_1h_hfq_kdata", schema_base=KdataBase, entity_type="stock"
)


# the __all__ is generated
__all__ = ["Stock1hHfqKdata"]
