import cpp

from FunctionCall call, Function fcn
where
  call.getTarget() = fcn and  
  fcn.getDeclaringType().getSimpleName() = "basic_string" 
select call.getArgument(_).getValueText()