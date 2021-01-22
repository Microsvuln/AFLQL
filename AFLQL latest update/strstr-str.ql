import cpp 

/// function :  strstr

from FunctionCall fucall, Expr size
where
    fucall.getTarget().hasName("strstr")
select fucall.getArgument(_).getValueText()