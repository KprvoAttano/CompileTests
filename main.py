import program


def main() -> None:
    prog1 = '''
        int input_int(string name) {
            if (name != "") {
                print("Введите " + name + ": ");
            }
            return to_int(read());
        }
        float input_float(string name) {
            if (name != "") {
                print("Введите " + name + ": ");
            }
            return to_float(read());
        }

        int g, g2 = g, g4 = 90;

        int a = input_int("a");
        float b = input_float("b"), c = input_float("c");  /* comment 1
        int d = input_int("d");
        */
        for (int i = 0, j = 8; ((i <= 5)) && g; i = i + 1, print(5))
            for(; a < b;)
                if (a > 7 + b) {
                    c = a + b * (2 - 1) + 0;  // comment 2
                    string bb = "98\tура";
                }
                else if (a)
                    print((c + 1) + " " + 89.89);
        for(bool i = true;;);

        int z;
        z=0;
    '''
    prog2 = 'int f1(int p1, float p2) { string a = p1 + p2; int x; }'''
    prog3 = 'for (;;);'
    prog4 = '''
    
            int[] a = new int[4];
            
            class A
            {
            
            }
            
            int f()
            {
                int a = 4;
                return a;
            }
            
            for(int b = 0; b < 3; b = b + 1){
            b  = b - 1;
            }
            
            int c = 0;
            while (c < 5){
            c = c + 1;
            }
            '''
    prog5 = '''
        int input_int(string name) {
            if (name != "") {
                print("Введите " + name + ": ");
            }
            return to_int(read());

            // bool a() { }
        }
        int input_int2(string name, int a, int name2) {
            if (name != "") {
                print("Введите " + name + ": ");
            }
            return "";
        }
    '''

    program.execute(prog4)


if __name__ == "__main__":
    main()
