import io.lye;
import controles.lye;

class miclase
begin
def A,B, ready, res as integer;

write("Hola Mundo!!");
    enter;
    read (A,B);
    if (A > B)
      if (A < 25)
        res = A + B;
      endif;
    else
        res = A * B;
    endif;
    write("Resultado = ");
end
