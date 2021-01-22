import cpp 

/// function :  strcasecmp 

from FunctionCall fucall, Expr size
where
    fucall.getTarget().hasName("strcasecmp")
select fucall.getArgument(_).getValueText()