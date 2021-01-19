import cpp

from GlobalVariable  a
where a.isStatic() and a.isConst()
select a.getAnAssignedValue().getValueText()