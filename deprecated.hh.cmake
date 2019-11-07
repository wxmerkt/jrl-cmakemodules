#ifndef @PACKAGE_CPPNAME@_DEPRECATED_HH
# define @PACKAGE_CPPNAME@_DEPRECATED_HH

// Define a suffix which can be used to tag a type, a function or a a
// variable as deprecated (i.e. it will emit a warning when using it).
//
// Tagging a function as deprecated:
//  void foo () @PACKAGE_CPPNAME@_DEPRECATED;
//
// Tagging a type as deprecated:
//  class Foo {};
//  typedef Foo Bar @PACKAGE_CPPNAME@_DEPRECATED;
//
// Tagging a variable as deprecated:
//  int a @PACKAGE_CPPNAME@_DEPRECATED = 0;
//
// The use of a macro is required as this is /not/ a standardized
// feature of C++ language or preprocessor, even if most of the
// compilers support it.
# if defined(__GNUC__) || defined(__clang__)
#  define @PACKAGE_CPPNAME@_DEPRECATED __attribute__ ((deprecated))
# else
#  if defined(_MSC_VER) && !defined(__INTEL_COMPILER)
#   define @PACKAGE_CPPNAME@_DEPRECATED __declspec (deprecated)
#  else
// If the compiler is not recognized, drop the feature.
#   define @PACKAGE_CPPNAME@_DEPRECATED /* nothing */
#  endif // __MSVC__
# endif // __GNUC__

#endif //! @PACKAGE_CPPNAME@_DEPRECATED_HH
