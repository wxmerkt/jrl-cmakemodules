#ifndef @PACKAGE_CPPNAME@_WARNING_HH
# define @PACKAGE_CPPNAME@_WARNING_HH

// Emits a warning in a portable way.
//
// To emit a warning, one can insert:
//
// #pragma message @PACKAGE_CPPNAME@_WARN("your warning message here")
//
// The use of this syntax is required as this is /not/ a standardized
// feature of C++ language or preprocessor, even if most of the
// compilers support it.

# define @PACKAGE_CPPNAME@_WARN_STRINGISE_IMPL(x) #x
# define @PACKAGE_CPPNAME@_WARN_STRINGISE(x) \
         @PACKAGE_CPPNAME@_WARN_STRINGISE_IMPL(x)
# ifdef __GNUC__
#   define @PACKAGE_CPPNAME@_WARN(exp) ("WARNING: " exp)
# else
#  ifdef _MSC_VER
#   define FILE_LINE_LINK __FILE__ "(" \
           @PACKAGE_CPPNAME@_WARN_STRINGISE(__LINE__) ") : "
#   define @PACKAGE_CPPNAME@_WARN(exp) (FILE_LINE_LINK "WARNING: " exp)
#  else
// If the compiler is not recognized, drop the feature.
#   define @PACKAGE_CPPNAME@_WARN(MSG) /* nothing */
#  endif // __MSVC__
# endif // __GNUC__

#endif //! @PACKAGE_CPPNAME@_WARNING_HH
