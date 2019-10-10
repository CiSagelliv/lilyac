import io.lye;
import controles.lye;
 
class miclase
begin
def A,B, ready, res as integer;
 
write("Hola Mundo!!");
    enter;
    read (A,B);
    if (A > B)
        res = A + B;
    else
        res = A - B;
    endif;
    write("Resultado = "); 
end
