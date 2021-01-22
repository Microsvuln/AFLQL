import cpp 

/// function :  strncasecmp

from FunctionCall fucall, Expr size
where
    fucall.getTarget().hasName("strncasecmp")
select fucall.getArgument(_).getValueText()
