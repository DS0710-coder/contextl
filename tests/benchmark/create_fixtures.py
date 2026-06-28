import os
from pathlib import Path

def write(path_str, content):
    p = Path(path_str)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content.strip() + "\n")

# --- TypeScript ---
b = "tests/benchmark/fixtures/typescript"
write(f"{b}/index.ts", "import { A } from './pkg/a';\nimport { x } from './pkg/sub/x';")
write(f"{b}/dead.ts", "export const dead = true;")
write(f"{b}/contest.ts", "export const isTest = false;")
write(f"{b}/util.spec.ts", "import { A } from './pkg/a';")
write(f"{b}/pkg/index.ts", "export * from './a';\nexport * from './b';")
write(f"{b}/pkg/a.ts", "import { B } from './b';\nexport class A {}")
write(f"{b}/pkg/b.ts", "import { A } from './a';\nexport class B {}")
write(f"{b}/pkg/sub/index.ts", "export * from './x';")
write(f"{b}/pkg/sub/x.ts", "import { Y } from './y';\nimport { A } from '../a';\nexport const x = 1;")
write(f"{b}/pkg/sub/y.ts", "import { Z, W } from './z';\nexport class Y {}")
write(f"{b}/pkg/sub/z.ts", "export class Z {}\nexport class W {}")
write(f"{b}/test_🚀.ts", "export const rocket = 1;")
write(f"{b}/my file.ts", "export const space = 1;")
monster_ts = """
/**
 * Global doc
 */
export function myDec(target: any) {}

@myDec
export class Monster<T> {
  /** Size doc */
  get size(): number { return 100; }
  
  public nested = class {
    inner() {}
  }
"""
for i in range(250):
    monster_ts += f"  public method_{i}() {{}}\n"
monster_ts += "}\n"
write(f"{b}/monster.ts", monster_ts)

# --- JavaScript ---
b = "tests/benchmark/fixtures/javascript"
write(f"{b}/index.js", "const { A } = require('./pkg/a');")
write(f"{b}/dead.js", "module.exports = { dead: true };")
write(f"{b}/fastest.js", "module.exports = { speed: 10 };")
write(f"{b}/test_real.test.js", "require('./index');")
write(f"{b}/pkg/index.js", "module.exports = { ...require('./a') };")
write(f"{b}/pkg/a.js", "const b = require('./b'); module.exports = { A: 1 };")
write(f"{b}/pkg/b.js", "const a = require('./a'); module.exports = { B: 1 };")
write(f"{b}/test_🚀.js", "")
write(f"{b}/my file.js", "")
monster_js = "class Monster {\n"
for i in range(250):
    monster_js += f"  method_{i}() {{}}\n"
monster_js += "}\nmodule.exports = Monster;"
write(f"{b}/monster.js", monster_js)

# --- Java ---
b = "tests/benchmark/fixtures/java"
write(f"{b}/Main.java", "package com.example;\nimport com.example.pkg.A;\npublic class Main {}")
write(f"{b}/Dead.java", "package com.example;\npublic class Dead {}")
write(f"{b}/Contest.java", "package com.example;\npublic class Contest {}")
write(f"{b}/MainTest.java", "package com.example;\nimport org.junit.Test;\npublic class MainTest {}")
write(f"{b}/pkg/A.java", "package com.example.pkg;\nimport com.example.pkg.sub.X;\npublic class A {}")
write(f"{b}/pkg/B.java", "package com.example.pkg;\nimport com.example.pkg.A;\npublic class B {}")
write(f"{b}/pkg/sub/X.java", "package com.example.pkg.sub;\nimport com.example.pkg.B;\nimport java.util.List;\nimport java.util.Set;\npublic class X {}")
write(f"{b}/Test🚀.java", "package com.example;\npublic class Test🚀 {}")
write(f"{b}/My File.java", "package com.example;\npublic class MyFile {}")
monster_java = """package com.example;
import java.util.List;
/** Doc */
public class Monster<T> {
    @Override
    public String toString() { return ""; }
    public static class Nested {
        public void inner() {}
    }
"""
for i in range(250):
    monster_java += f"    public void method_{i}() {{}}\n"
monster_java += "}\n"
write(f"{b}/Monster.java", monster_java)

# --- Rust ---
b = "tests/benchmark/fixtures/rust"
write(f"{b}/main.rs", "mod pkg;\nuse pkg::a::A;\nfn main() {}")
write(f"{b}/dead.rs", "pub fn dead() {}")
write(f"{b}/fastest.rs", "pub fn fast() {}")
write(f"{b}/real_test.rs", "use crate::pkg::a;\n#[test]\nfn test_a() {}")
write(f"{b}/pkg/mod.rs", "pub mod a;\npub mod b;\npub mod sub;")
write(f"{b}/pkg/a.rs", "use crate::pkg::b::B;\nuse super::sub::x::X;\npub struct A;")
write(f"{b}/pkg/b.rs", "use crate::pkg::a::A;\npub struct B;")
write(f"{b}/pkg/sub/mod.rs", "pub mod x;")
write(f"{b}/pkg/sub/x.rs", "use std::{collections::HashMap, vec::Vec};\npub struct X;")
write(f"{b}/test_🚀.rs", "")
write(f"{b}/my file.rs", "")
monster_rs = """
/// Doc
pub struct Monster<T> {
    val: T,
}
impl<T> Monster<T> {
"""
for i in range(250):
    monster_rs += f"    pub fn method_{i}() {{}}\n"
monster_rs += "}\n"
write(f"{b}/monster.rs", monster_rs)

# --- Go ---
b = "tests/benchmark/fixtures/go"
write(f"{b}/cmd/main.go", "package main\nimport \"benchmark/pkg/a\"\nfunc main() {}")
write(f"{b}/dead.go", "package dead")
write(f"{b}/contest.go", "package contest")
write(f"{b}/cmd/main_test.go", "package main\nimport \"testing\"")
write(f"{b}/pkg/a/a.go", "package a\nimport \"benchmark/pkg/b\"\nfunc A() {}")
write(f"{b}/pkg/b/b.go", "package b\nimport \"benchmark/pkg/a\"\nfunc B() {}")
write(f"{b}/pkg/sub/x/x.go", "package x\nimport (\n\t\"benchmark/pkg/a\"\n\t\"benchmark/pkg/b\"\n)")
write(f"{b}/test_🚀.go", "package rocket")
write(f"{b}/my file.go", "package space")
monster_go = "package monster\n\n// Doc\ntype Monster struct {}\n\n"
for i in range(250):
    monster_go += f"func (m *Monster) Method_{i}() {{}}\n"
write(f"{b}/monster.go", monster_go)

# --- C++ ---
b = "tests/benchmark/fixtures/cpp"
write(f"{b}/main.cpp", "#include \"pkg/a.hpp\"\nint main() { return 0; }")
write(f"{b}/dead.cpp", "void dead() {}")
write(f"{b}/fastest.cpp", "void fast() {}")
write(f"{b}/test_main.cpp", "#include \"main.cpp\"\nvoid test() {}")
write(f"{b}/pkg/a.hpp", "#ifndef A_H\n#define A_H\n#include \"b.hpp\"\nclass A {};\n#endif")
write(f"{b}/pkg/b.hpp", "#ifndef B_H\n#define B_H\n#include \"a.hpp\"\nclass B {};\n#endif")
write(f"{b}/pkg/sub/x.hpp", "#include \"../a.hpp\"\n#include <vector>")
write(f"{b}/test_🚀.cpp", "")
write(f"{b}/my file.cpp", "")
monster_cpp = "template <typename T>\nclass Monster {\npublic:\n"
for i in range(250):
    monster_cpp += f"    void method_{i}() {{}}\n"
monster_cpp += "};\n"
write(f"{b}/monster.hpp", monster_cpp)


# --- C ---
b = "tests/benchmark/fixtures/c"
write(f"{b}/main.c", "#include \"pkg/a.h\"\nint main() { return 0; }")
write(f"{b}/dead.c", "void dead() {}")
write(f"{b}/fastest.c", "void fast() {}")
write(f"{b}/test_main.c", "#include \"main.c\"\nvoid test() {}")
write(f"{b}/pkg/a.h", "#ifndef A_H\n#define A_H\n#include \"b.h\"\nvoid a();\n#endif")
write(f"{b}/pkg/b.h", "#ifndef B_H\n#define B_H\n#include \"a.h\"\nvoid b();\n#endif")
write(f"{b}/pkg/sub/x.h", "#include \"../a.h\"\n#include <stdio.h>")
write(f"{b}/test_🚀.c", "")
write(f"{b}/my file.c", "")
monster_c = "void monster() {\n"
for i in range(250):
    monster_c += f"    int a{i} = 0;\n"
monster_c += "}\n"
write(f"{b}/monster.h", monster_c)
