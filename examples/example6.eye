import io.lye;
import controles.lye;
 
class miclase begin
    def A,B,C as integer;
    A = 1;
    B = 1;
    C = 1;

    while (C < 100)
        write(C);
        C = A + B;
        A = B;
        B = C;
    endwhile;
end
