CSS = """

/*
! tailwindcss v3.3.5 | MIT License | https://tailwindcss.com
*/

/*
1. Prevent padding and border from affecting element width. (https://github.com/mozdevs/cssremedy/issues/4)
2. Allow adding a border to an element by just adding a border-width. (https://github.com/tailwindcss/tailwindcss/pull/116)
*/

*,
::before,
::after {
  box-sizing: border-box;
  /* 1 */
  border-width: 0;
  /* 2 */
  border-style: solid;
  /* 2 */
  border-color: #e5e7eb;
  /* 2 */
}

::before,
::after {
  --tw-content: '';
}

/*
1. Use a consistent sensible line-height in all browsers.
2. Prevent adjustments of font size after orientation changes in iOS.
3. Use a more readable tab size.
4. Use the user's configured `sans` font-family by default.
5. Use the user's configured `sans` font-feature-settings by default.
6. Use the user's configured `sans` font-variation-settings by default.
*/

html {
  line-height: 1.5;
  /* 1 */
  -webkit-text-size-adjust: 100%;
  /* 2 */
  -moz-tab-size: 4;
  /* 3 */
  -o-tab-size: 4;
     tab-size: 4;
  /* 3 */
  font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  /* 4 */
  font-feature-settings: normal;
  /* 5 */
  font-variation-settings: normal;
  /* 6 */
}

/*
1. Remove the margin in all browsers.
2. Inherit line-height from `html` so users can set them as a class directly on the `html` element.
*/

body {
  margin: 0;
  /* 1 */
  line-height: inherit;
  /* 2 */
}

/*
1. Add the correct height in Firefox.
2. Correct the inheritance of border color in Firefox. (https://bugzilla.mozilla.org/show_bug.cgi?id=190655)
3. Ensure horizontal rules are visible by default.
*/

hr {
  height: 0;
  /* 1 */
  color: inherit;
  /* 2 */
  border-top-width: 1px;
  /* 3 */
}

/*
Add the correct text decoration in Chrome, Edge, and Safari.
*/

abbr:where([title]) {
  -webkit-text-decoration: underline dotted;
          text-decoration: underline dotted;
}

/*
Remove the default font size and weight for headings.
*/

h1,
h2,
h3,
h4,
h5,
h6 {
  font-size: inherit;
  font-weight: inherit;
}

/*
Reset links to optimize for opt-in styling instead of opt-out.
*/

a {
  color: inherit;
  text-decoration: inherit;
}

/*
Add the correct font weight in Edge and Safari.
*/

b,
strong {
  font-weight: bolder;
}

/*
1. Use the user's configured `mono` font family by default.
2. Correct the odd `em` font sizing in all browsers.
*/

code,
kbd,
samp,
pre {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  /* 1 */
  font-size: 1em;
  /* 2 */
}

/*
Add the correct font size in all browsers.
*/

small {
  font-size: 80%;
}

/*
Prevent `sub` and `sup` elements from affecting the line height in all browsers.
*/

sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}

sub {
  bottom: -0.25em;
}

sup {
  top: -0.5em;
}

/*
1. Remove text indentation from table contents in Chrome and Safari. (https://bugs.chromium.org/p/chromium/issues/detail?id=999088, https://bugs.webkit.org/show_bug.cgi?id=201297)
2. Correct table border color inheritance in all Chrome and Safari. (https://bugs.chromium.org/p/chromium/issues/detail?id=935729, https://bugs.webkit.org/show_bug.cgi?id=195016)
3. Remove gaps between table borders by default.
*/

table {
  text-indent: 0;
  /* 1 */
  border-color: inherit;
  /* 2 */
  border-collapse: collapse;
  /* 3 */
}

/*
1. Change the font styles in all browsers.
2. Remove the margin in Firefox and Safari.
3. Remove default padding in all browsers.
*/

button,
input,
optgroup,
select,
textarea {
  font-family: inherit;
  /* 1 */
  font-feature-settings: inherit;
  /* 1 */
  font-variation-settings: inherit;
  /* 1 */
  font-size: 100%;
  /* 1 */
  font-weight: inherit;
  /* 1 */
  line-height: inherit;
  /* 1 */
  color: inherit;
  /* 1 */
  margin: 0;
  /* 2 */
  padding: 0;
  /* 3 */
}

/*
Remove the inheritance of text transform in Edge and Firefox.
*/

button,
select {
  text-transform: none;
}

/*
1. Correct the inability to style clickable types in iOS and Safari.
2. Remove default button styles.
*/

button,
[type='button'],
[type='reset'],
[type='submit'] {
  -webkit-appearance: button;
  /* 1 */
  background-color: transparent;
  /* 2 */
  background-image: none;
  /* 2 */
}

/*
Use the modern Firefox focus style for all focusable elements.
*/

:-moz-focusring {
  outline: auto;
}

/*
Remove the additional `:invalid` styles in Firefox. (https://github.com/mozilla/gecko-dev/blob/2f9eacd9d3d995c937b4251a5557d95d494c9be1/layout/style/res/forms.css#L728-L737)
*/

:-moz-ui-invalid {
  box-shadow: none;
}

/*
Add the correct vertical alignment in Chrome and Firefox.
*/

progress {
  vertical-align: baseline;
}

/*
Correct the cursor style of increment and decrement buttons in Safari.
*/

::-webkit-inner-spin-button,
::-webkit-outer-spin-button {
  height: auto;
}

/*
1. Correct the odd appearance in Chrome and Safari.
2. Correct the outline style in Safari.
*/

[type='search'] {
  -webkit-appearance: textfield;
  /* 1 */
  outline-offset: -2px;
  /* 2 */
}

/*
Remove the inner padding in Chrome and Safari on macOS.
*/

::-webkit-search-decoration {
  -webkit-appearance: none;
}

/*
1. Correct the inability to style clickable types in iOS and Safari.
2. Change font properties to `inherit` in Safari.
*/

::-webkit-file-upload-button {
  -webkit-appearance: button;
  /* 1 */
  font: inherit;
  /* 2 */
}

/*
Add the correct display in Chrome and Safari.
*/

summary {
  display: list-item;
}

/*
Removes the default spacing and border for appropriate elements.
*/

blockquote,
dl,
dd,
h1,
h2,
h3,
h4,
h5,
h6,
hr,
figure,
p,
pre {
  margin: 0;
}

fieldset {
  margin: 0;
  padding: 0;
}

legend {
  padding: 0;
}

ol,
ul,
menu {
  list-style: none;
  margin: 0;
  padding: 0;
}

/*
Reset default styling for dialogs.
*/

dialog {
  padding: 0;
}

/*
Prevent resizing textareas horizontally by default.
*/

textarea {
  resize: vertical;
}

/*
1. Reset the default placeholder opacity in Firefox. (https://github.com/tailwindlabs/tailwindcss/issues/3300)
2. Set the default placeholder color to the user's configured gray 400 color.
*/

input::-moz-placeholder, textarea::-moz-placeholder {
  opacity: 1;
  /* 1 */
  color: #9ca3af;
  /* 2 */
}

input::placeholder,
textarea::placeholder {
  opacity: 1;
  /* 1 */
  color: #9ca3af;
  /* 2 */
}

/*
Set the default cursor for buttons.
*/

button,
[role="button"] {
  cursor: pointer;
}

/*
Make sure disabled buttons don't get the pointer cursor.
*/

:disabled {
  cursor: default;
}

/*
1. Make replaced elements `display: block` by default. (https://github.com/mozdevs/cssremedy/issues/14)
2. Add `vertical-align: middle` to align replaced elements more sensibly by default. (https://github.com/jensimmons/cssremedy/issues/14#issuecomment-634934210)
   This can trigger a poorly considered lint error in some tools but is included by design.
*/

img,
svg,
video,
canvas,
audio,
iframe,
embed,
object {
  display: block;
  /* 1 */
  vertical-align: middle;
  /* 2 */
}

/*
Constrain images and videos to the parent width and preserve their intrinsic aspect ratio. (https://github.com/mozdevs/cssremedy/issues/14)
*/

img,
video {
  max-width: 100%;
  height: auto;
}

/* Make elements with the HTML hidden attribute stay hidden by default */

[hidden] {
  display: none;
}

*, ::before, ::after {
  --tw-border-spacing-x: 0;
  --tw-border-spacing-y: 0;
  --tw-translate-x: 0;
  --tw-translate-y: 0;
  --tw-rotate: 0;
  --tw-skew-x: 0;
  --tw-skew-y: 0;
  --tw-scale-x: 1;
  --tw-scale-y: 1;
  --tw-pan-x:  ;
  --tw-pan-y:  ;
  --tw-pinch-zoom:  ;
  --tw-scroll-snap-strictness: proximity;
  --tw-gradient-from-position:  ;
  --tw-gradient-via-position:  ;
  --tw-gradient-to-position:  ;
  --tw-ordinal:  ;
  --tw-slashed-zero:  ;
  --tw-numeric-figure:  ;
  --tw-numeric-spacing:  ;
  --tw-numeric-fraction:  ;
  --tw-ring-inset:  ;
  --tw-ring-offset-width: 0px;
  --tw-ring-offset-color: #fff;
  --tw-ring-color: rgb(59 130 246 / 0.5);
  --tw-ring-offset-shadow: 0 0 #0000;
  --tw-ring-shadow: 0 0 #0000;
  --tw-shadow: 0 0 #0000;
  --tw-shadow-colored: 0 0 #0000;
  --tw-blur:  ;
  --tw-brightness:  ;
  --tw-contrast:  ;
  --tw-grayscale:  ;
  --tw-hue-rotate:  ;
  --tw-invert:  ;
  --tw-saturate:  ;
  --tw-sepia:  ;
  --tw-drop-shadow:  ;
  --tw-backdrop-blur:  ;
  --tw-backdrop-brightness:  ;
  --tw-backdrop-contrast:  ;
  --tw-backdrop-grayscale:  ;
  --tw-backdrop-hue-rotate:  ;
  --tw-backdrop-invert:  ;
  --tw-backdrop-opacity:  ;
  --tw-backdrop-saturate:  ;
  --tw-backdrop-sepia:  ;
}

::backdrop {
  --tw-border-spacing-x: 0;
  --tw-border-spacing-y: 0;
  --tw-translate-x: 0;
  --tw-translate-y: 0;
  --tw-rotate: 0;
  --tw-skew-x: 0;
  --tw-skew-y: 0;
  --tw-scale-x: 1;
  --tw-scale-y: 1;
  --tw-pan-x:  ;
  --tw-pan-y:  ;
  --tw-pinch-zoom:  ;
  --tw-scroll-snap-strictness: proximity;
  --tw-gradient-from-position:  ;
  --tw-gradient-via-position:  ;
  --tw-gradient-to-position:  ;
  --tw-ordinal:  ;
  --tw-slashed-zero:  ;
  --tw-numeric-figure:  ;
  --tw-numeric-spacing:  ;
  --tw-numeric-fraction:  ;
  --tw-ring-inset:  ;
  --tw-ring-offset-width: 0px;
  --tw-ring-offset-color: #fff;
  --tw-ring-color: rgb(59 130 246 / 0.5);
  --tw-ring-offset-shadow: 0 0 #0000;
  --tw-ring-shadow: 0 0 #0000;
  --tw-shadow: 0 0 #0000;
  --tw-shadow-colored: 0 0 #0000;
  --tw-blur:  ;
  --tw-brightness:  ;
  --tw-contrast:  ;
  --tw-grayscale:  ;
  --tw-hue-rotate:  ;
  --tw-invert:  ;
  --tw-saturate:  ;
  --tw-sepia:  ;
  --tw-drop-shadow:  ;
  --tw-backdrop-blur:  ;
  --tw-backdrop-brightness:  ;
  --tw-backdrop-contrast:  ;
  --tw-backdrop-grayscale:  ;
  --tw-backdrop-hue-rotate:  ;
  --tw-backdrop-invert:  ;
  --tw-backdrop-opacity:  ;
  --tw-backdrop-saturate:  ;
  --tw-backdrop-sepia:  ;
}

.container {
  width: 100%;
}

@media (min-width: 640px) {
  .container {
    max-width: 640px;
  }
}

@media (min-width: 768px) {
  .container {
    max-width: 768px;
  }
}

@media (min-width: 1024px) {
  .container {
    max-width: 1024px;
  }
}

@media (min-width: 1280px) {
  .container {
    max-width: 1280px;
  }
}

@media (min-width: 1536px) {
  .container {
    max-width: 1536px;
  }
}

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}

.not-sr-only {
  position: static;
  width: auto;
  height: auto;
  padding: 0;
  margin: 0;
  overflow: visible;
  clip: auto;
  white-space: normal;
}

.pointer-events-none {
  pointer-events: none;
}

.pointer-events-auto {
  pointer-events: auto;
}

.visible {
  visibility: visible;
}

.invisible {
  visibility: hidden;
}

.collapse {
  visibility: collapse;
}

.static {
  position: static;
}

.fixed {
  position: fixed;
}

.absolute {
  position: absolute;
}

.relative {
  position: relative;
}

.sticky {
  position: sticky;
}

.-inset-0 {
  inset: -0px;
}

.-inset-0.5 {
  inset: -0.125rem;
}

.-inset-1 {
  inset: -0.25rem;
}

.-inset-1.5 {
  inset: -0.375rem;
}

.-inset-1/2 {
  inset: -50%;
}

.-inset-1/3 {
  inset: -33.333333%;
}

.-inset-1/4 {
  inset: -25%;
}

.-inset-10 {
  inset: -2.5rem;
}

.-inset-11 {
  inset: -2.75rem;
}

.-inset-12 {
  inset: -3rem;
}

.-inset-14 {
  inset: -3.5rem;
}

.-inset-16 {
  inset: -4rem;
}

.-inset-2 {
  inset: -0.5rem;
}

.-inset-2.5 {
  inset: -0.625rem;
}

.-inset-2/3 {
  inset: -66.666667%;
}

.-inset-2/4 {
  inset: -50%;
}

.-inset-20 {
  inset: -5rem;
}

.-inset-24 {
  inset: -6rem;
}

.-inset-28 {
  inset: -7rem;
}

.-inset-3 {
  inset: -0.75rem;
}

.-inset-3.5 {
  inset: -0.875rem;
}

.-inset-3/4 {
  inset: -75%;
}

.-inset-32 {
  inset: -8rem;
}

.-inset-36 {
  inset: -9rem;
}

.-inset-4 {
  inset: -1rem;
}

.-inset-44 {
  inset: -11rem;
}

.-inset-48 {
  inset: -12rem;
}

.-inset-5 {
  inset: -1.25rem;
}

.-inset-52 {
  inset: -13rem;
}

.-inset-56 {
  inset: -14rem;
}

.-inset-6 {
  inset: -1.5rem;
}

.-inset-60 {
  inset: -15rem;
}

.-inset-64 {
  inset: -16rem;
}

.-inset-7 {
  inset: -1.75rem;
}

.-inset-72 {
  inset: -18rem;
}

.-inset-8 {
  inset: -2rem;
}

.-inset-80 {
  inset: -20rem;
}

.-inset-9 {
  inset: -2.25rem;
}

.-inset-96 {
  inset: -24rem;
}

.-inset-full {
  inset: -100%;
}

.-inset-px {
  inset: -1px;
}

.inset-0 {
  inset: 0px;
}

.inset-0.5 {
  inset: 0.125rem;
}

.inset-1 {
  inset: 0.25rem;
}

.inset-1.5 {
  inset: 0.375rem;
}

.inset-1/2 {
  inset: 50%;
}

.inset-1/3 {
  inset: 33.333333%;
}

.inset-1/4 {
  inset: 25%;
}

.inset-10 {
  inset: 2.5rem;
}

.inset-11 {
  inset: 2.75rem;
}

.inset-12 {
  inset: 3rem;
}

.inset-14 {
  inset: 3.5rem;
}

.inset-16 {
  inset: 4rem;
}

.inset-2 {
  inset: 0.5rem;
}

.inset-2.5 {
  inset: 0.625rem;
}

.inset-2/3 {
  inset: 66.666667%;
}

.inset-2/4 {
  inset: 50%;
}

.inset-20 {
  inset: 5rem;
}

.inset-24 {
  inset: 6rem;
}

.inset-28 {
  inset: 7rem;
}

.inset-3 {
  inset: 0.75rem;
}

.inset-3.5 {
  inset: 0.875rem;
}

.inset-3/4 {
  inset: 75%;
}

.inset-32 {
  inset: 8rem;
}

.inset-36 {
  inset: 9rem;
}

.inset-4 {
  inset: 1rem;
}

.inset-44 {
  inset: 11rem;
}

.inset-48 {
  inset: 12rem;
}

.inset-5 {
  inset: 1.25rem;
}

.inset-52 {
  inset: 13rem;
}

.inset-56 {
  inset: 14rem;
}

.inset-6 {
  inset: 1.5rem;
}

.inset-60 {
  inset: 15rem;
}

.inset-64 {
  inset: 16rem;
}

.inset-7 {
  inset: 1.75rem;
}

.inset-72 {
  inset: 18rem;
}

.inset-8 {
  inset: 2rem;
}

.inset-80 {
  inset: 20rem;
}

.inset-9 {
  inset: 2.25rem;
}

.inset-96 {
  inset: 24rem;
}

.inset-auto {
  inset: auto;
}

.inset-full {
  inset: 100%;
}

.inset-px {
  inset: 1px;
}

.-inset-x-0 {
  left: -0px;
  right: -0px;
}

.-inset-x-0.5 {
  left: -0.125rem;
  right: -0.125rem;
}

.-inset-x-1 {
  left: -0.25rem;
  right: -0.25rem;
}

.-inset-x-1.5 {
  left: -0.375rem;
  right: -0.375rem;
}

.-inset-x-1/2 {
  left: -50%;
  right: -50%;
}

.-inset-x-1/3 {
  left: -33.333333%;
  right: -33.333333%;
}

.-inset-x-1/4 {
  left: -25%;
  right: -25%;
}

.-inset-x-10 {
  left: -2.5rem;
  right: -2.5rem;
}

.-inset-x-11 {
  left: -2.75rem;
  right: -2.75rem;
}

.-inset-x-12 {
  left: -3rem;
  right: -3rem;
}

.-inset-x-14 {
  left: -3.5rem;
  right: -3.5rem;
}

.-inset-x-16 {
  left: -4rem;
  right: -4rem;
}

.-inset-x-2 {
  left: -0.5rem;
  right: -0.5rem;
}

.-inset-x-2.5 {
  left: -0.625rem;
  right: -0.625rem;
}

.-inset-x-2/3 {
  left: -66.666667%;
  right: -66.666667%;
}

.-inset-x-2/4 {
  left: -50%;
  right: -50%;
}

.-inset-x-20 {
  left: -5rem;
  right: -5rem;
}

.-inset-x-24 {
  left: -6rem;
  right: -6rem;
}

.-inset-x-28 {
  left: -7rem;
  right: -7rem;
}

.-inset-x-3 {
  left: -0.75rem;
  right: -0.75rem;
}

.-inset-x-3.5 {
  left: -0.875rem;
  right: -0.875rem;
}

.-inset-x-3/4 {
  left: -75%;
  right: -75%;
}

.-inset-x-32 {
  left: -8rem;
  right: -8rem;
}

.-inset-x-36 {
  left: -9rem;
  right: -9rem;
}

.-inset-x-4 {
  left: -1rem;
  right: -1rem;
}

.-inset-x-44 {
  left: -11rem;
  right: -11rem;
}

.-inset-x-48 {
  left: -12rem;
  right: -12rem;
}

.-inset-x-5 {
  left: -1.25rem;
  right: -1.25rem;
}

.-inset-x-52 {
  left: -13rem;
  right: -13rem;
}

.-inset-x-56 {
  left: -14rem;
  right: -14rem;
}

.-inset-x-6 {
  left: -1.5rem;
  right: -1.5rem;
}

.-inset-x-60 {
  left: -15rem;
  right: -15rem;
}

.-inset-x-64 {
  left: -16rem;
  right: -16rem;
}

.-inset-x-7 {
  left: -1.75rem;
  right: -1.75rem;
}

.-inset-x-72 {
  left: -18rem;
  right: -18rem;
}

.-inset-x-8 {
  left: -2rem;
  right: -2rem;
}

.-inset-x-80 {
  left: -20rem;
  right: -20rem;
}

.-inset-x-9 {
  left: -2.25rem;
  right: -2.25rem;
}

.-inset-x-96 {
  left: -24rem;
  right: -24rem;
}

.-inset-x-full {
  left: -100%;
  right: -100%;
}

.-inset-x-px {
  left: -1px;
  right: -1px;
}

.-inset-y-0 {
  top: -0px;
  bottom: -0px;
}

.-inset-y-0.5 {
  top: -0.125rem;
  bottom: -0.125rem;
}

.-inset-y-1 {
  top: -0.25rem;
  bottom: -0.25rem;
}

.-inset-y-1.5 {
  top: -0.375rem;
  bottom: -0.375rem;
}

.-inset-y-1/2 {
  top: -50%;
  bottom: -50%;
}

.-inset-y-1/3 {
  top: -33.333333%;
  bottom: -33.333333%;
}

.-inset-y-1/4 {
  top: -25%;
  bottom: -25%;
}

.-inset-y-10 {
  top: -2.5rem;
  bottom: -2.5rem;
}

.-inset-y-11 {
  top: -2.75rem;
  bottom: -2.75rem;
}

.-inset-y-12 {
  top: -3rem;
  bottom: -3rem;
}

.-inset-y-14 {
  top: -3.5rem;
  bottom: -3.5rem;
}

.-inset-y-16 {
  top: -4rem;
  bottom: -4rem;
}

.-inset-y-2 {
  top: -0.5rem;
  bottom: -0.5rem;
}

.-inset-y-2.5 {
  top: -0.625rem;
  bottom: -0.625rem;
}

.-inset-y-2/3 {
  top: -66.666667%;
  bottom: -66.666667%;
}

.-inset-y-2/4 {
  top: -50%;
  bottom: -50%;
}

.-inset-y-20 {
  top: -5rem;
  bottom: -5rem;
}

.-inset-y-24 {
  top: -6rem;
  bottom: -6rem;
}

.-inset-y-28 {
  top: -7rem;
  bottom: -7rem;
}

.-inset-y-3 {
  top: -0.75rem;
  bottom: -0.75rem;
}

.-inset-y-3.5 {
  top: -0.875rem;
  bottom: -0.875rem;
}

.-inset-y-3/4 {
  top: -75%;
  bottom: -75%;
}

.-inset-y-32 {
  top: -8rem;
  bottom: -8rem;
}

.-inset-y-36 {
  top: -9rem;
  bottom: -9rem;
}

.-inset-y-4 {
  top: -1rem;
  bottom: -1rem;
}

.-inset-y-44 {
  top: -11rem;
  bottom: -11rem;
}

.-inset-y-48 {
  top: -12rem;
  bottom: -12rem;
}

.-inset-y-5 {
  top: -1.25rem;
  bottom: -1.25rem;
}

.-inset-y-52 {
  top: -13rem;
  bottom: -13rem;
}

.-inset-y-56 {
  top: -14rem;
  bottom: -14rem;
}

.-inset-y-6 {
  top: -1.5rem;
  bottom: -1.5rem;
}

.-inset-y-60 {
  top: -15rem;
  bottom: -15rem;
}

.-inset-y-64 {
  top: -16rem;
  bottom: -16rem;
}

.-inset-y-7 {
  top: -1.75rem;
  bottom: -1.75rem;
}

.-inset-y-72 {
  top: -18rem;
  bottom: -18rem;
}

.-inset-y-8 {
  top: -2rem;
  bottom: -2rem;
}

.-inset-y-80 {
  top: -20rem;
  bottom: -20rem;
}

.-inset-y-9 {
  top: -2.25rem;
  bottom: -2.25rem;
}

.-inset-y-96 {
  top: -24rem;
  bottom: -24rem;
}

.-inset-y-full {
  top: -100%;
  bottom: -100%;
}

.-inset-y-px {
  top: -1px;
  bottom: -1px;
}

.inset-x-0 {
  left: 0px;
  right: 0px;
}

.inset-x-0.5 {
  left: 0.125rem;
  right: 0.125rem;
}

.inset-x-1 {
  left: 0.25rem;
  right: 0.25rem;
}

.inset-x-1.5 {
  left: 0.375rem;
  right: 0.375rem;
}

.inset-x-1/2 {
  left: 50%;
  right: 50%;
}

.inset-x-1/3 {
  left: 33.333333%;
  right: 33.333333%;
}

.inset-x-1/4 {
  left: 25%;
  right: 25%;
}

.inset-x-10 {
  left: 2.5rem;
  right: 2.5rem;
}

.inset-x-11 {
  left: 2.75rem;
  right: 2.75rem;
}

.inset-x-12 {
  left: 3rem;
  right: 3rem;
}

.inset-x-14 {
  left: 3.5rem;
  right: 3.5rem;
}

.inset-x-16 {
  left: 4rem;
  right: 4rem;
}

.inset-x-2 {
  left: 0.5rem;
  right: 0.5rem;
}

.inset-x-2.5 {
  left: 0.625rem;
  right: 0.625rem;
}

.inset-x-2/3 {
  left: 66.666667%;
  right: 66.666667%;
}

.inset-x-2/4 {
  left: 50%;
  right: 50%;
}

.inset-x-20 {
  left: 5rem;
  right: 5rem;
}

.inset-x-24 {
  left: 6rem;
  right: 6rem;
}

.inset-x-28 {
  left: 7rem;
  right: 7rem;
}

.inset-x-3 {
  left: 0.75rem;
  right: 0.75rem;
}

.inset-x-3.5 {
  left: 0.875rem;
  right: 0.875rem;
}

.inset-x-3/4 {
  left: 75%;
  right: 75%;
}

.inset-x-32 {
  left: 8rem;
  right: 8rem;
}

.inset-x-36 {
  left: 9rem;
  right: 9rem;
}

.inset-x-4 {
  left: 1rem;
  right: 1rem;
}

.inset-x-44 {
  left: 11rem;
  right: 11rem;
}

.inset-x-48 {
  left: 12rem;
  right: 12rem;
}

.inset-x-5 {
  left: 1.25rem;
  right: 1.25rem;
}

.inset-x-52 {
  left: 13rem;
  right: 13rem;
}

.inset-x-56 {
  left: 14rem;
  right: 14rem;
}

.inset-x-6 {
  left: 1.5rem;
  right: 1.5rem;
}

.inset-x-60 {
  left: 15rem;
  right: 15rem;
}

.inset-x-64 {
  left: 16rem;
  right: 16rem;
}

.inset-x-7 {
  left: 1.75rem;
  right: 1.75rem;
}

.inset-x-72 {
  left: 18rem;
  right: 18rem;
}

.inset-x-8 {
  left: 2rem;
  right: 2rem;
}

.inset-x-80 {
  left: 20rem;
  right: 20rem;
}

.inset-x-9 {
  left: 2.25rem;
  right: 2.25rem;
}

.inset-x-96 {
  left: 24rem;
  right: 24rem;
}

.inset-x-auto {
  left: auto;
  right: auto;
}

.inset-x-full {
  left: 100%;
  right: 100%;
}

.inset-x-px {
  left: 1px;
  right: 1px;
}

.inset-y-0 {
  top: 0px;
  bottom: 0px;
}

.inset-y-0.5 {
  top: 0.125rem;
  bottom: 0.125rem;
}

.inset-y-1 {
  top: 0.25rem;
  bottom: 0.25rem;
}

.inset-y-1.5 {
  top: 0.375rem;
  bottom: 0.375rem;
}

.inset-y-1/2 {
  top: 50%;
  bottom: 50%;
}

.inset-y-1/3 {
  top: 33.333333%;
  bottom: 33.333333%;
}

.inset-y-1/4 {
  top: 25%;
  bottom: 25%;
}

.inset-y-10 {
  top: 2.5rem;
  bottom: 2.5rem;
}

.inset-y-11 {
  top: 2.75rem;
  bottom: 2.75rem;
}

.inset-y-12 {
  top: 3rem;
  bottom: 3rem;
}

.inset-y-14 {
  top: 3.5rem;
  bottom: 3.5rem;
}

.inset-y-16 {
  top: 4rem;
  bottom: 4rem;
}

.inset-y-2 {
  top: 0.5rem;
  bottom: 0.5rem;
}

.inset-y-2.5 {
  top: 0.625rem;
  bottom: 0.625rem;
}

.inset-y-2/3 {
  top: 66.666667%;
  bottom: 66.666667%;
}

.inset-y-2/4 {
  top: 50%;
  bottom: 50%;
}

.inset-y-20 {
  top: 5rem;
  bottom: 5rem;
}

.inset-y-24 {
  top: 6rem;
  bottom: 6rem;
}

.inset-y-28 {
  top: 7rem;
  bottom: 7rem;
}

.inset-y-3 {
  top: 0.75rem;
  bottom: 0.75rem;
}

.inset-y-3.5 {
  top: 0.875rem;
  bottom: 0.875rem;
}

.inset-y-3/4 {
  top: 75%;
  bottom: 75%;
}

.inset-y-32 {
  top: 8rem;
  bottom: 8rem;
}

.inset-y-36 {
  top: 9rem;
  bottom: 9rem;
}

.inset-y-4 {
  top: 1rem;
  bottom: 1rem;
}

.inset-y-44 {
  top: 11rem;
  bottom: 11rem;
}

.inset-y-48 {
  top: 12rem;
  bottom: 12rem;
}

.inset-y-5 {
  top: 1.25rem;
  bottom: 1.25rem;
}

.inset-y-52 {
  top: 13rem;
  bottom: 13rem;
}

.inset-y-56 {
  top: 14rem;
  bottom: 14rem;
}

.inset-y-6 {
  top: 1.5rem;
  bottom: 1.5rem;
}

.inset-y-60 {
  top: 15rem;
  bottom: 15rem;
}

.inset-y-64 {
  top: 16rem;
  bottom: 16rem;
}

.inset-y-7 {
  top: 1.75rem;
  bottom: 1.75rem;
}

.inset-y-72 {
  top: 18rem;
  bottom: 18rem;
}

.inset-y-8 {
  top: 2rem;
  bottom: 2rem;
}

.inset-y-80 {
  top: 20rem;
  bottom: 20rem;
}

.inset-y-9 {
  top: 2.25rem;
  bottom: 2.25rem;
}

.inset-y-96 {
  top: 24rem;
  bottom: 24rem;
}

.inset-y-auto {
  top: auto;
  bottom: auto;
}

.inset-y-full {
  top: 100%;
  bottom: 100%;
}

.inset-y-px {
  top: 1px;
  bottom: 1px;
}

.-bottom-0 {
  bottom: -0px;
}

.-bottom-0.5 {
  bottom: -0.125rem;
}

.-bottom-1 {
  bottom: -0.25rem;
}

.-bottom-1.5 {
  bottom: -0.375rem;
}

.-bottom-1/2 {
  bottom: -50%;
}

.-bottom-1/3 {
  bottom: -33.333333%;
}

.-bottom-1/4 {
  bottom: -25%;
}

.-bottom-10 {
  bottom: -2.5rem;
}

.-bottom-11 {
  bottom: -2.75rem;
}

.-bottom-12 {
  bottom: -3rem;
}

.-bottom-14 {
  bottom: -3.5rem;
}

.-bottom-16 {
  bottom: -4rem;
}

.-bottom-2 {
  bottom: -0.5rem;
}

.-bottom-2.5 {
  bottom: -0.625rem;
}

.-bottom-2/3 {
  bottom: -66.666667%;
}

.-bottom-2/4 {
  bottom: -50%;
}

.-bottom-20 {
  bottom: -5rem;
}

.-bottom-24 {
  bottom: -6rem;
}

.-bottom-28 {
  bottom: -7rem;
}

.-bottom-3 {
  bottom: -0.75rem;
}

.-bottom-3.5 {
  bottom: -0.875rem;
}

.-bottom-3/4 {
  bottom: -75%;
}

.-bottom-32 {
  bottom: -8rem;
}

.-bottom-36 {
  bottom: -9rem;
}

.-bottom-4 {
  bottom: -1rem;
}

.-bottom-44 {
  bottom: -11rem;
}

.-bottom-48 {
  bottom: -12rem;
}

.-bottom-5 {
  bottom: -1.25rem;
}

.-bottom-52 {
  bottom: -13rem;
}

.-bottom-56 {
  bottom: -14rem;
}

.-bottom-6 {
  bottom: -1.5rem;
}

.-bottom-60 {
  bottom: -15rem;
}

.-bottom-64 {
  bottom: -16rem;
}

.-bottom-7 {
  bottom: -1.75rem;
}

.-bottom-72 {
  bottom: -18rem;
}

.-bottom-8 {
  bottom: -2rem;
}

.-bottom-80 {
  bottom: -20rem;
}

.-bottom-9 {
  bottom: -2.25rem;
}

.-bottom-96 {
  bottom: -24rem;
}

.-bottom-full {
  bottom: -100%;
}

.-bottom-px {
  bottom: -1px;
}

.-end-0 {
  inset-inline-end: -0px;
}

.-end-0.5 {
  inset-inline-end: -0.125rem;
}

.-end-1 {
  inset-inline-end: -0.25rem;
}

.-end-1.5 {
  inset-inline-end: -0.375rem;
}

.-end-1/2 {
  inset-inline-end: -50%;
}

.-end-1/3 {
  inset-inline-end: -33.333333%;
}

.-end-1/4 {
  inset-inline-end: -25%;
}

.-end-10 {
  inset-inline-end: -2.5rem;
}

.-end-11 {
  inset-inline-end: -2.75rem;
}

.-end-12 {
  inset-inline-end: -3rem;
}

.-end-14 {
  inset-inline-end: -3.5rem;
}

.-end-16 {
  inset-inline-end: -4rem;
}

.-end-2 {
  inset-inline-end: -0.5rem;
}

.-end-2.5 {
  inset-inline-end: -0.625rem;
}

.-end-2/3 {
  inset-inline-end: -66.666667%;
}

.-end-2/4 {
  inset-inline-end: -50%;
}

.-end-20 {
  inset-inline-end: -5rem;
}

.-end-24 {
  inset-inline-end: -6rem;
}

.-end-28 {
  inset-inline-end: -7rem;
}

.-end-3 {
  inset-inline-end: -0.75rem;
}

.-end-3.5 {
  inset-inline-end: -0.875rem;
}

.-end-3/4 {
  inset-inline-end: -75%;
}

.-end-32 {
  inset-inline-end: -8rem;
}

.-end-36 {
  inset-inline-end: -9rem;
}

.-end-4 {
  inset-inline-end: -1rem;
}

.-end-44 {
  inset-inline-end: -11rem;
}

.-end-48 {
  inset-inline-end: -12rem;
}

.-end-5 {
  inset-inline-end: -1.25rem;
}

.-end-52 {
  inset-inline-end: -13rem;
}

.-end-56 {
  inset-inline-end: -14rem;
}

.-end-6 {
  inset-inline-end: -1.5rem;
}

.-end-60 {
  inset-inline-end: -15rem;
}

.-end-64 {
  inset-inline-end: -16rem;
}

.-end-7 {
  inset-inline-end: -1.75rem;
}

.-end-72 {
  inset-inline-end: -18rem;
}

.-end-8 {
  inset-inline-end: -2rem;
}

.-end-80 {
  inset-inline-end: -20rem;
}

.-end-9 {
  inset-inline-end: -2.25rem;
}

.-end-96 {
  inset-inline-end: -24rem;
}

.-end-full {
  inset-inline-end: -100%;
}

.-end-px {
  inset-inline-end: -1px;
}

.-left-0 {
  left: -0px;
}

.-left-0.5 {
  left: -0.125rem;
}

.-left-1 {
  left: -0.25rem;
}

.-left-1.5 {
  left: -0.375rem;
}

.-left-1/2 {
  left: -50%;
}

.-left-1/3 {
  left: -33.333333%;
}

.-left-1/4 {
  left: -25%;
}

.-left-10 {
  left: -2.5rem;
}

.-left-11 {
  left: -2.75rem;
}

.-left-12 {
  left: -3rem;
}

.-left-14 {
  left: -3.5rem;
}

.-left-16 {
  left: -4rem;
}

.-left-2 {
  left: -0.5rem;
}

.-left-2.5 {
  left: -0.625rem;
}

.-left-2/3 {
  left: -66.666667%;
}

.-left-2/4 {
  left: -50%;
}

.-left-20 {
  left: -5rem;
}

.-left-24 {
  left: -6rem;
}

.-left-28 {
  left: -7rem;
}

.-left-3 {
  left: -0.75rem;
}

.-left-3.5 {
  left: -0.875rem;
}

.-left-3/4 {
  left: -75%;
}

.-left-32 {
  left: -8rem;
}

.-left-36 {
  left: -9rem;
}

.-left-4 {
  left: -1rem;
}

.-left-44 {
  left: -11rem;
}

.-left-48 {
  left: -12rem;
}

.-left-5 {
  left: -1.25rem;
}

.-left-52 {
  left: -13rem;
}

.-left-56 {
  left: -14rem;
}

.-left-6 {
  left: -1.5rem;
}

.-left-60 {
  left: -15rem;
}

.-left-64 {
  left: -16rem;
}

.-left-7 {
  left: -1.75rem;
}

.-left-72 {
  left: -18rem;
}

.-left-8 {
  left: -2rem;
}

.-left-80 {
  left: -20rem;
}

.-left-9 {
  left: -2.25rem;
}

.-left-96 {
  left: -24rem;
}

.-left-full {
  left: -100%;
}

.-left-px {
  left: -1px;
}

.-right-0 {
  right: -0px;
}

.-right-0.5 {
  right: -0.125rem;
}

.-right-1 {
  right: -0.25rem;
}

.-right-1.5 {
  right: -0.375rem;
}

.-right-1/2 {
  right: -50%;
}

.-right-1/3 {
  right: -33.333333%;
}

.-right-1/4 {
  right: -25%;
}

.-right-10 {
  right: -2.5rem;
}

.-right-11 {
  right: -2.75rem;
}

.-right-12 {
  right: -3rem;
}

.-right-14 {
  right: -3.5rem;
}

.-right-16 {
  right: -4rem;
}

.-right-2 {
  right: -0.5rem;
}

.-right-2.5 {
  right: -0.625rem;
}

.-right-2/3 {
  right: -66.666667%;
}

.-right-2/4 {
  right: -50%;
}

.-right-20 {
  right: -5rem;
}

.-right-24 {
  right: -6rem;
}

.-right-28 {
  right: -7rem;
}

.-right-3 {
  right: -0.75rem;
}

.-right-3.5 {
  right: -0.875rem;
}

.-right-3/4 {
  right: -75%;
}

.-right-32 {
  right: -8rem;
}

.-right-36 {
  right: -9rem;
}

.-right-4 {
  right: -1rem;
}

.-right-44 {
  right: -11rem;
}

.-right-48 {
  right: -12rem;
}

.-right-5 {
  right: -1.25rem;
}

.-right-52 {
  right: -13rem;
}

.-right-56 {
  right: -14rem;
}

.-right-6 {
  right: -1.5rem;
}

.-right-60 {
  right: -15rem;
}

.-right-64 {
  right: -16rem;
}

.-right-7 {
  right: -1.75rem;
}

.-right-72 {
  right: -18rem;
}

.-right-8 {
  right: -2rem;
}

.-right-80 {
  right: -20rem;
}

.-right-9 {
  right: -2.25rem;
}

.-right-96 {
  right: -24rem;
}

.-right-full {
  right: -100%;
}

.-right-px {
  right: -1px;
}

.-start-0 {
  inset-inline-start: -0px;
}

.-start-0.5 {
  inset-inline-start: -0.125rem;
}

.-start-1 {
  inset-inline-start: -0.25rem;
}

.-start-1.5 {
  inset-inline-start: -0.375rem;
}

.-start-1/2 {
  inset-inline-start: -50%;
}

.-start-1/3 {
  inset-inline-start: -33.333333%;
}

.-start-1/4 {
  inset-inline-start: -25%;
}

.-start-10 {
  inset-inline-start: -2.5rem;
}

.-start-11 {
  inset-inline-start: -2.75rem;
}

.-start-12 {
  inset-inline-start: -3rem;
}

.-start-14 {
  inset-inline-start: -3.5rem;
}

.-start-16 {
  inset-inline-start: -4rem;
}

.-start-2 {
  inset-inline-start: -0.5rem;
}

.-start-2.5 {
  inset-inline-start: -0.625rem;
}

.-start-2/3 {
  inset-inline-start: -66.666667%;
}

.-start-2/4 {
  inset-inline-start: -50%;
}

.-start-20 {
  inset-inline-start: -5rem;
}

.-start-24 {
  inset-inline-start: -6rem;
}

.-start-28 {
  inset-inline-start: -7rem;
}

.-start-3 {
  inset-inline-start: -0.75rem;
}

.-start-3.5 {
  inset-inline-start: -0.875rem;
}

.-start-3/4 {
  inset-inline-start: -75%;
}

.-start-32 {
  inset-inline-start: -8rem;
}

.-start-36 {
  inset-inline-start: -9rem;
}

.-start-4 {
  inset-inline-start: -1rem;
}

.-start-44 {
  inset-inline-start: -11rem;
}

.-start-48 {
  inset-inline-start: -12rem;
}

.-start-5 {
  inset-inline-start: -1.25rem;
}

.-start-52 {
  inset-inline-start: -13rem;
}

.-start-56 {
  inset-inline-start: -14rem;
}

.-start-6 {
  inset-inline-start: -1.5rem;
}

.-start-60 {
  inset-inline-start: -15rem;
}

.-start-64 {
  inset-inline-start: -16rem;
}

.-start-7 {
  inset-inline-start: -1.75rem;
}

.-start-72 {
  inset-inline-start: -18rem;
}

.-start-8 {
  inset-inline-start: -2rem;
}

.-start-80 {
  inset-inline-start: -20rem;
}

.-start-9 {
  inset-inline-start: -2.25rem;
}

.-start-96 {
  inset-inline-start: -24rem;
}

.-start-full {
  inset-inline-start: -100%;
}

.-start-px {
  inset-inline-start: -1px;
}

.-top-0 {
  top: -0px;
}

.-top-0.5 {
  top: -0.125rem;
}

.-top-1 {
  top: -0.25rem;
}

.-top-1.5 {
  top: -0.375rem;
}

.-top-1/2 {
  top: -50%;
}

.-top-1/3 {
  top: -33.333333%;
}

.-top-1/4 {
  top: -25%;
}

.-top-10 {
  top: -2.5rem;
}

.-top-11 {
  top: -2.75rem;
}

.-top-12 {
  top: -3rem;
}

.-top-14 {
  top: -3.5rem;
}

.-top-16 {
  top: -4rem;
}

.-top-2 {
  top: -0.5rem;
}

.-top-2.5 {
  top: -0.625rem;
}

.-top-2/3 {
  top: -66.666667%;
}

.-top-2/4 {
  top: -50%;
}

.-top-20 {
  top: -5rem;
}

.-top-24 {
  top: -6rem;
}

.-top-28 {
  top: -7rem;
}

.-top-3 {
  top: -0.75rem;
}

.-top-3.5 {
  top: -0.875rem;
}

.-top-3/4 {
  top: -75%;
}

.-top-32 {
  top: -8rem;
}

.-top-36 {
  top: -9rem;
}

.-top-4 {
  top: -1rem;
}

.-top-44 {
  top: -11rem;
}

.-top-48 {
  top: -12rem;
}

.-top-5 {
  top: -1.25rem;
}

.-top-52 {
  top: -13rem;
}

.-top-56 {
  top: -14rem;
}

.-top-6 {
  top: -1.5rem;
}

.-top-60 {
  top: -15rem;
}

.-top-64 {
  top: -16rem;
}

.-top-7 {
  top: -1.75rem;
}

.-top-72 {
  top: -18rem;
}

.-top-8 {
  top: -2rem;
}

.-top-80 {
  top: -20rem;
}

.-top-9 {
  top: -2.25rem;
}

.-top-96 {
  top: -24rem;
}

.-top-full {
  top: -100%;
}

.-top-px {
  top: -1px;
}

.bottom-0 {
  bottom: 0px;
}

.bottom-0.5 {
  bottom: 0.125rem;
}

.bottom-1 {
  bottom: 0.25rem;
}

.bottom-1.5 {
  bottom: 0.375rem;
}

.bottom-1/2 {
  bottom: 50%;
}

.bottom-1/3 {
  bottom: 33.333333%;
}

.bottom-1/4 {
  bottom: 25%;
}

.bottom-10 {
  bottom: 2.5rem;
}

.bottom-11 {
  bottom: 2.75rem;
}

.bottom-12 {
  bottom: 3rem;
}

.bottom-14 {
  bottom: 3.5rem;
}

.bottom-16 {
  bottom: 4rem;
}

.bottom-2 {
  bottom: 0.5rem;
}

.bottom-2.5 {
  bottom: 0.625rem;
}

.bottom-2/3 {
  bottom: 66.666667%;
}

.bottom-2/4 {
  bottom: 50%;
}

.bottom-20 {
  bottom: 5rem;
}

.bottom-24 {
  bottom: 6rem;
}

.bottom-28 {
  bottom: 7rem;
}

.bottom-3 {
  bottom: 0.75rem;
}

.bottom-3.5 {
  bottom: 0.875rem;
}

.bottom-3/4 {
  bottom: 75%;
}

.bottom-32 {
  bottom: 8rem;
}

.bottom-36 {
  bottom: 9rem;
}

.bottom-4 {
  bottom: 1rem;
}

.bottom-44 {
  bottom: 11rem;
}

.bottom-48 {
  bottom: 12rem;
}

.bottom-5 {
  bottom: 1.25rem;
}

.bottom-52 {
  bottom: 13rem;
}

.bottom-56 {
  bottom: 14rem;
}

.bottom-6 {
  bottom: 1.5rem;
}

.bottom-60 {
  bottom: 15rem;
}

.bottom-64 {
  bottom: 16rem;
}

.bottom-7 {
  bottom: 1.75rem;
}

.bottom-72 {
  bottom: 18rem;
}

.bottom-8 {
  bottom: 2rem;
}

.bottom-80 {
  bottom: 20rem;
}

.bottom-9 {
  bottom: 2.25rem;
}

.bottom-96 {
  bottom: 24rem;
}

.bottom-auto {
  bottom: auto;
}

.bottom-full {
  bottom: 100%;
}

.bottom-px {
  bottom: 1px;
}

.end-0 {
  inset-inline-end: 0px;
}

.end-0.5 {
  inset-inline-end: 0.125rem;
}

.end-1 {
  inset-inline-end: 0.25rem;
}

.end-1.5 {
  inset-inline-end: 0.375rem;
}

.end-1/2 {
  inset-inline-end: 50%;
}

.end-1/3 {
  inset-inline-end: 33.333333%;
}

.end-1/4 {
  inset-inline-end: 25%;
}

.end-10 {
  inset-inline-end: 2.5rem;
}

.end-11 {
  inset-inline-end: 2.75rem;
}

.end-12 {
  inset-inline-end: 3rem;
}

.end-14 {
  inset-inline-end: 3.5rem;
}

.end-16 {
  inset-inline-end: 4rem;
}

.end-2 {
  inset-inline-end: 0.5rem;
}

.end-2.5 {
  inset-inline-end: 0.625rem;
}

.end-2/3 {
  inset-inline-end: 66.666667%;
}

.end-2/4 {
  inset-inline-end: 50%;
}

.end-20 {
  inset-inline-end: 5rem;
}

.end-24 {
  inset-inline-end: 6rem;
}

.end-28 {
  inset-inline-end: 7rem;
}

.end-3 {
  inset-inline-end: 0.75rem;
}

.end-3.5 {
  inset-inline-end: 0.875rem;
}

.end-3/4 {
  inset-inline-end: 75%;
}

.end-32 {
  inset-inline-end: 8rem;
}

.end-36 {
  inset-inline-end: 9rem;
}

.end-4 {
  inset-inline-end: 1rem;
}

.end-44 {
  inset-inline-end: 11rem;
}

.end-48 {
  inset-inline-end: 12rem;
}

.end-5 {
  inset-inline-end: 1.25rem;
}

.end-52 {
  inset-inline-end: 13rem;
}

.end-56 {
  inset-inline-end: 14rem;
}

.end-6 {
  inset-inline-end: 1.5rem;
}

.end-60 {
  inset-inline-end: 15rem;
}

.end-64 {
  inset-inline-end: 16rem;
}

.end-7 {
  inset-inline-end: 1.75rem;
}

.end-72 {
  inset-inline-end: 18rem;
}

.end-8 {
  inset-inline-end: 2rem;
}

.end-80 {
  inset-inline-end: 20rem;
}

.end-9 {
  inset-inline-end: 2.25rem;
}

.end-96 {
  inset-inline-end: 24rem;
}

.end-auto {
  inset-inline-end: auto;
}

.end-full {
  inset-inline-end: 100%;
}

.end-px {
  inset-inline-end: 1px;
}

.left-0 {
  left: 0px;
}

.left-0.5 {
  left: 0.125rem;
}

.left-1 {
  left: 0.25rem;
}

.left-1.5 {
  left: 0.375rem;
}

.left-1/2 {
  left: 50%;
}

.left-1/3 {
  left: 33.333333%;
}

.left-1/4 {
  left: 25%;
}

.left-10 {
  left: 2.5rem;
}

.left-11 {
  left: 2.75rem;
}

.left-12 {
  left: 3rem;
}

.left-14 {
  left: 3.5rem;
}

.left-16 {
  left: 4rem;
}

.left-2 {
  left: 0.5rem;
}

.left-2.5 {
  left: 0.625rem;
}

.left-2/3 {
  left: 66.666667%;
}

.left-2/4 {
  left: 50%;
}

.left-20 {
  left: 5rem;
}

.left-24 {
  left: 6rem;
}

.left-28 {
  left: 7rem;
}

.left-3 {
  left: 0.75rem;
}

.left-3.5 {
  left: 0.875rem;
}

.left-3/4 {
  left: 75%;
}

.left-32 {
  left: 8rem;
}

.left-36 {
  left: 9rem;
}

.left-4 {
  left: 1rem;
}

.left-44 {
  left: 11rem;
}

.left-48 {
  left: 12rem;
}

.left-5 {
  left: 1.25rem;
}

.left-52 {
  left: 13rem;
}

.left-56 {
  left: 14rem;
}

.left-6 {
  left: 1.5rem;
}

.left-60 {
  left: 15rem;
}

.left-64 {
  left: 16rem;
}

.left-7 {
  left: 1.75rem;
}

.left-72 {
  left: 18rem;
}

.left-8 {
  left: 2rem;
}

.left-80 {
  left: 20rem;
}

.left-9 {
  left: 2.25rem;
}

.left-96 {
  left: 24rem;
}

.left-auto {
  left: auto;
}

.left-full {
  left: 100%;
}

.left-px {
  left: 1px;
}

.right-0 {
  right: 0px;
}

.right-0.5 {
  right: 0.125rem;
}

.right-1 {
  right: 0.25rem;
}

.right-1.5 {
  right: 0.375rem;
}

.right-1/2 {
  right: 50%;
}

.right-1/3 {
  right: 33.333333%;
}

.right-1/4 {
  right: 25%;
}

.right-10 {
  right: 2.5rem;
}

.right-11 {
  right: 2.75rem;
}

.right-12 {
  right: 3rem;
}

.right-14 {
  right: 3.5rem;
}

.right-16 {
  right: 4rem;
}

.right-2 {
  right: 0.5rem;
}

.right-2.5 {
  right: 0.625rem;
}

.right-2/3 {
  right: 66.666667%;
}

.right-2/4 {
  right: 50%;
}

.right-20 {
  right: 5rem;
}

.right-24 {
  right: 6rem;
}

.right-28 {
  right: 7rem;
}

.right-3 {
  right: 0.75rem;
}

.right-3.5 {
  right: 0.875rem;
}

.right-3/4 {
  right: 75%;
}

.right-32 {
  right: 8rem;
}

.right-36 {
  right: 9rem;
}

.right-4 {
  right: 1rem;
}

.right-44 {
  right: 11rem;
}

.right-48 {
  right: 12rem;
}

.right-5 {
  right: 1.25rem;
}

.right-52 {
  right: 13rem;
}

.right-56 {
  right: 14rem;
}

.right-6 {
  right: 1.5rem;
}

.right-60 {
  right: 15rem;
}

.right-64 {
  right: 16rem;
}

.right-7 {
  right: 1.75rem;
}

.right-72 {
  right: 18rem;
}

.right-8 {
  right: 2rem;
}

.right-80 {
  right: 20rem;
}

.right-9 {
  right: 2.25rem;
}

.right-96 {
  right: 24rem;
}

.right-auto {
  right: auto;
}

.right-full {
  right: 100%;
}

.right-px {
  right: 1px;
}

.start-0 {
  inset-inline-start: 0px;
}

.start-0.5 {
  inset-inline-start: 0.125rem;
}

.start-1 {
  inset-inline-start: 0.25rem;
}

.start-1.5 {
  inset-inline-start: 0.375rem;
}

.start-1/2 {
  inset-inline-start: 50%;
}

.start-1/3 {
  inset-inline-start: 33.333333%;
}

.start-1/4 {
  inset-inline-start: 25%;
}

.start-10 {
  inset-inline-start: 2.5rem;
}

.start-11 {
  inset-inline-start: 2.75rem;
}

.start-12 {
  inset-inline-start: 3rem;
}

.start-14 {
  inset-inline-start: 3.5rem;
}

.start-16 {
  inset-inline-start: 4rem;
}

.start-2 {
  inset-inline-start: 0.5rem;
}

.start-2.5 {
  inset-inline-start: 0.625rem;
}

.start-2/3 {
  inset-inline-start: 66.666667%;
}

.start-2/4 {
  inset-inline-start: 50%;
}

.start-20 {
  inset-inline-start: 5rem;
}

.start-24 {
  inset-inline-start: 6rem;
}

.start-28 {
  inset-inline-start: 7rem;
}

.start-3 {
  inset-inline-start: 0.75rem;
}

.start-3.5 {
  inset-inline-start: 0.875rem;
}

.start-3/4 {
  inset-inline-start: 75%;
}

.start-32 {
  inset-inline-start: 8rem;
}

.start-36 {
  inset-inline-start: 9rem;
}

.start-4 {
  inset-inline-start: 1rem;
}

.start-44 {
  inset-inline-start: 11rem;
}

.start-48 {
  inset-inline-start: 12rem;
}

.start-5 {
  inset-inline-start: 1.25rem;
}

.start-52 {
  inset-inline-start: 13rem;
}

.start-56 {
  inset-inline-start: 14rem;
}

.start-6 {
  inset-inline-start: 1.5rem;
}

.start-60 {
  inset-inline-start: 15rem;
}

.start-64 {
  inset-inline-start: 16rem;
}

.start-7 {
  inset-inline-start: 1.75rem;
}

.start-72 {
  inset-inline-start: 18rem;
}

.start-8 {
  inset-inline-start: 2rem;
}

.start-80 {
  inset-inline-start: 20rem;
}

.start-9 {
  inset-inline-start: 2.25rem;
}

.start-96 {
  inset-inline-start: 24rem;
}

.start-auto {
  inset-inline-start: auto;
}

.start-full {
  inset-inline-start: 100%;
}

.start-px {
  inset-inline-start: 1px;
}

.top-0 {
  top: 0px;
}

.top-0.5 {
  top: 0.125rem;
}

.top-1 {
  top: 0.25rem;
}

.top-1.5 {
  top: 0.375rem;
}

.top-1/2 {
  top: 50%;
}

.top-1/3 {
  top: 33.333333%;
}

.top-1/4 {
  top: 25%;
}

.top-10 {
  top: 2.5rem;
}

.top-11 {
  top: 2.75rem;
}

.top-12 {
  top: 3rem;
}

.top-14 {
  top: 3.5rem;
}

.top-16 {
  top: 4rem;
}

.top-2 {
  top: 0.5rem;
}

.top-2.5 {
  top: 0.625rem;
}

.top-2/3 {
  top: 66.666667%;
}

.top-2/4 {
  top: 50%;
}

.top-20 {
  top: 5rem;
}

.top-24 {
  top: 6rem;
}

.top-28 {
  top: 7rem;
}

.top-3 {
  top: 0.75rem;
}

.top-3.5 {
  top: 0.875rem;
}

.top-3/4 {
  top: 75%;
}

.top-32 {
  top: 8rem;
}

.top-36 {
  top: 9rem;
}

.top-4 {
  top: 1rem;
}

.top-44 {
  top: 11rem;
}

.top-48 {
  top: 12rem;
}

.top-5 {
  top: 1.25rem;
}

.top-52 {
  top: 13rem;
}

.top-56 {
  top: 14rem;
}

.top-6 {
  top: 1.5rem;
}

.top-60 {
  top: 15rem;
}

.top-64 {
  top: 16rem;
}

.top-7 {
  top: 1.75rem;
}

.top-72 {
  top: 18rem;
}

.top-8 {
  top: 2rem;
}

.top-80 {
  top: 20rem;
}

.top-9 {
  top: 2.25rem;
}

.top-96 {
  top: 24rem;
}

.top-auto {
  top: auto;
}

.top-full {
  top: 100%;
}

.top-px {
  top: 1px;
}

.isolate {
  isolation: isolate;
}

.isolation-auto {
  isolation: auto;
}

.-z-0 {
  z-index: 0;
}

.-z-10 {
  z-index: -10;
}

.-z-20 {
  z-index: -20;
}

.-z-30 {
  z-index: -30;
}

.-z-40 {
  z-index: -40;
}

.-z-50 {
  z-index: -50;
}

.z-0 {
  z-index: 0;
}

.z-10 {
  z-index: 10;
}

.z-20 {
  z-index: 20;
}

.z-30 {
  z-index: 30;
}

.z-40 {
  z-index: 40;
}

.z-50 {
  z-index: 50;
}

.z-auto {
  z-index: auto;
}

.-order-1 {
  order: -1;
}

.-order-10 {
  order: -10;
}

.-order-11 {
  order: -11;
}

.-order-12 {
  order: -12;
}

.-order-2 {
  order: -2;
}

.-order-3 {
  order: -3;
}

.-order-4 {
  order: -4;
}

.-order-5 {
  order: -5;
}

.-order-6 {
  order: -6;
}

.-order-7 {
  order: -7;
}

.-order-8 {
  order: -8;
}

.-order-9 {
  order: -9;
}

.-order-first {
  order: 9999;
}

.-order-last {
  order: -9999;
}

.-order-none {
  order: 0;
}

.order-1 {
  order: 1;
}

.order-10 {
  order: 10;
}

.order-11 {
  order: 11;
}

.order-12 {
  order: 12;
}

.order-2 {
  order: 2;
}

.order-3 {
  order: 3;
}

.order-4 {
  order: 4;
}

.order-5 {
  order: 5;
}

.order-6 {
  order: 6;
}

.order-7 {
  order: 7;
}

.order-8 {
  order: 8;
}

.order-9 {
  order: 9;
}

.order-first {
  order: -9999;
}

.order-last {
  order: 9999;
}

.order-none {
  order: 0;
}

.col-auto {
  grid-column: auto;
}

.col-span-1 {
  grid-column: span 1 / span 1;
}

.col-span-10 {
  grid-column: span 10 / span 10;
}

.col-span-11 {
  grid-column: span 11 / span 11;
}

.col-span-12 {
  grid-column: span 12 / span 12;
}

.col-span-2 {
  grid-column: span 2 / span 2;
}

.col-span-3 {
  grid-column: span 3 / span 3;
}

.col-span-4 {
  grid-column: span 4 / span 4;
}

.col-span-5 {
  grid-column: span 5 / span 5;
}

.col-span-6 {
  grid-column: span 6 / span 6;
}

.col-span-7 {
  grid-column: span 7 / span 7;
}

.col-span-8 {
  grid-column: span 8 / span 8;
}

.col-span-9 {
  grid-column: span 9 / span 9;
}

.col-span-full {
  grid-column: 1 / -1;
}

.col-start-1 {
  grid-column-start: 1;
}

.col-start-10 {
  grid-column-start: 10;
}

.col-start-11 {
  grid-column-start: 11;
}

.col-start-12 {
  grid-column-start: 12;
}

.col-start-13 {
  grid-column-start: 13;
}

.col-start-2 {
  grid-column-start: 2;
}

.col-start-3 {
  grid-column-start: 3;
}

.col-start-4 {
  grid-column-start: 4;
}

.col-start-5 {
  grid-column-start: 5;
}

.col-start-6 {
  grid-column-start: 6;
}

.col-start-7 {
  grid-column-start: 7;
}

.col-start-8 {
  grid-column-start: 8;
}

.col-start-9 {
  grid-column-start: 9;
}

.col-start-auto {
  grid-column-start: auto;
}

.col-end-1 {
  grid-column-end: 1;
}

.col-end-10 {
  grid-column-end: 10;
}

.col-end-11 {
  grid-column-end: 11;
}

.col-end-12 {
  grid-column-end: 12;
}

.col-end-13 {
  grid-column-end: 13;
}

.col-end-2 {
  grid-column-end: 2;
}

.col-end-3 {
  grid-column-end: 3;
}

.col-end-4 {
  grid-column-end: 4;
}

.col-end-5 {
  grid-column-end: 5;
}

.col-end-6 {
  grid-column-end: 6;
}

.col-end-7 {
  grid-column-end: 7;
}

.col-end-8 {
  grid-column-end: 8;
}

.col-end-9 {
  grid-column-end: 9;
}

.col-end-auto {
  grid-column-end: auto;
}

.row-auto {
  grid-row: auto;
}

.row-span-1 {
  grid-row: span 1 / span 1;
}

.row-span-2 {
  grid-row: span 2 / span 2;
}

.row-span-3 {
  grid-row: span 3 / span 3;
}

.row-span-4 {
  grid-row: span 4 / span 4;
}

.row-span-5 {
  grid-row: span 5 / span 5;
}

.row-span-6 {
  grid-row: span 6 / span 6;
}

.row-span-full {
  grid-row: 1 / -1;
}

.row-start-1 {
  grid-row-start: 1;
}

.row-start-2 {
  grid-row-start: 2;
}

.row-start-3 {
  grid-row-start: 3;
}

.row-start-4 {
  grid-row-start: 4;
}

.row-start-5 {
  grid-row-start: 5;
}

.row-start-6 {
  grid-row-start: 6;
}

.row-start-7 {
  grid-row-start: 7;
}

.row-start-auto {
  grid-row-start: auto;
}

.row-end-1 {
  grid-row-end: 1;
}

.row-end-2 {
  grid-row-end: 2;
}

.row-end-3 {
  grid-row-end: 3;
}

.row-end-4 {
  grid-row-end: 4;
}

.row-end-5 {
  grid-row-end: 5;
}

.row-end-6 {
  grid-row-end: 6;
}

.row-end-7 {
  grid-row-end: 7;
}

.row-end-auto {
  grid-row-end: auto;
}

.float-right {
  float: right;
}

.float-left {
  float: left;
}

.float-none {
  float: none;
}

.clear-left {
  clear: left;
}

.clear-right {
  clear: right;
}

.clear-both {
  clear: both;
}

.clear-none {
  clear: none;
}

.-m-0 {
  margin: -0px;
}

.-m-0.5 {
  margin: -0.125rem;
}

.-m-1 {
  margin: -0.25rem;
}

.-m-1.5 {
  margin: -0.375rem;
}

.-m-10 {
  margin: -2.5rem;
}

.-m-11 {
  margin: -2.75rem;
}

.-m-12 {
  margin: -3rem;
}

.-m-14 {
  margin: -3.5rem;
}

.-m-16 {
  margin: -4rem;
}

.-m-2 {
  margin: -0.5rem;
}

.-m-2.5 {
  margin: -0.625rem;
}

.-m-20 {
  margin: -5rem;
}

.-m-24 {
  margin: -6rem;
}

.-m-28 {
  margin: -7rem;
}

.-m-3 {
  margin: -0.75rem;
}

.-m-3.5 {
  margin: -0.875rem;
}

.-m-32 {
  margin: -8rem;
}

.-m-36 {
  margin: -9rem;
}

.-m-4 {
  margin: -1rem;
}

.-m-40 {
  margin: -10rem;
}

.-m-44 {
  margin: -11rem;
}

.-m-48 {
  margin: -12rem;
}

.-m-5 {
  margin: -1.25rem;
}

.-m-52 {
  margin: -13rem;
}

.-m-56 {
  margin: -14rem;
}

.-m-6 {
  margin: -1.5rem;
}

.-m-60 {
  margin: -15rem;
}

.-m-64 {
  margin: -16rem;
}

.-m-7 {
  margin: -1.75rem;
}

.-m-72 {
  margin: -18rem;
}

.-m-8 {
  margin: -2rem;
}

.-m-80 {
  margin: -20rem;
}

.-m-9 {
  margin: -2.25rem;
}

.-m-96 {
  margin: -24rem;
}

.-m-px {
  margin: -1px;
}

.m-0 {
  margin: 0px;
}

.m-0.5 {
  margin: 0.125rem;
}

.m-1 {
  margin: 0.25rem;
}

.m-1.5 {
  margin: 0.375rem;
}

.m-10 {
  margin: 2.5rem;
}

.m-11 {
  margin: 2.75rem;
}

.m-12 {
  margin: 3rem;
}

.m-14 {
  margin: 3.5rem;
}

.m-16 {
  margin: 4rem;
}

.m-2 {
  margin: 0.5rem;
}

.m-2.5 {
  margin: 0.625rem;
}

.m-20 {
  margin: 5rem;
}

.m-24 {
  margin: 6rem;
}

.m-28 {
  margin: 7rem;
}

.m-3 {
  margin: 0.75rem;
}

.m-3.5 {
  margin: 0.875rem;
}

.m-32 {
  margin: 8rem;
}

.m-36 {
  margin: 9rem;
}

.m-4 {
  margin: 1rem;
}

.m-40 {
  margin: 10rem;
}

.m-44 {
  margin: 11rem;
}

.m-48 {
  margin: 12rem;
}

.m-5 {
  margin: 1.25rem;
}

.m-52 {
  margin: 13rem;
}

.m-56 {
  margin: 14rem;
}

.m-6 {
  margin: 1.5rem;
}

.m-60 {
  margin: 15rem;
}

.m-64 {
  margin: 16rem;
}

.m-7 {
  margin: 1.75rem;
}

.m-72 {
  margin: 18rem;
}

.m-8 {
  margin: 2rem;
}

.m-80 {
  margin: 20rem;
}

.m-9 {
  margin: 2.25rem;
}

.m-96 {
  margin: 24rem;
}

.m-px {
  margin: 1px;
}

.-mx-0 {
  margin-left: -0px;
  margin-right: -0px;
}

.-mx-0.5 {
  margin-left: -0.125rem;
  margin-right: -0.125rem;
}

.-mx-1 {
  margin-left: -0.25rem;
  margin-right: -0.25rem;
}

.-mx-1.5 {
  margin-left: -0.375rem;
  margin-right: -0.375rem;
}

.-mx-10 {
  margin-left: -2.5rem;
  margin-right: -2.5rem;
}

.-mx-11 {
  margin-left: -2.75rem;
  margin-right: -2.75rem;
}

.-mx-12 {
  margin-left: -3rem;
  margin-right: -3rem;
}

.-mx-14 {
  margin-left: -3.5rem;
  margin-right: -3.5rem;
}

.-mx-16 {
  margin-left: -4rem;
  margin-right: -4rem;
}

.-mx-2 {
  margin-left: -0.5rem;
  margin-right: -0.5rem;
}

.-mx-2.5 {
  margin-left: -0.625rem;
  margin-right: -0.625rem;
}

.-mx-20 {
  margin-left: -5rem;
  margin-right: -5rem;
}

.-mx-24 {
  margin-left: -6rem;
  margin-right: -6rem;
}

.-mx-28 {
  margin-left: -7rem;
  margin-right: -7rem;
}

.-mx-3 {
  margin-left: -0.75rem;
  margin-right: -0.75rem;
}

.-mx-3.5 {
  margin-left: -0.875rem;
  margin-right: -0.875rem;
}

.-mx-32 {
  margin-left: -8rem;
  margin-right: -8rem;
}

.-mx-36 {
  margin-left: -9rem;
  margin-right: -9rem;
}

.-mx-4 {
  margin-left: -1rem;
  margin-right: -1rem;
}

.-mx-40 {
  margin-left: -10rem;
  margin-right: -10rem;
}

.-mx-44 {
  margin-left: -11rem;
  margin-right: -11rem;
}

.-mx-48 {
  margin-left: -12rem;
  margin-right: -12rem;
}

.-mx-5 {
  margin-left: -1.25rem;
  margin-right: -1.25rem;
}

.-mx-52 {
  margin-left: -13rem;
  margin-right: -13rem;
}

.-mx-56 {
  margin-left: -14rem;
  margin-right: -14rem;
}

.-mx-6 {
  margin-left: -1.5rem;
  margin-right: -1.5rem;
}

.-mx-60 {
  margin-left: -15rem;
  margin-right: -15rem;
}

.-mx-64 {
  margin-left: -16rem;
  margin-right: -16rem;
}

.-mx-7 {
  margin-left: -1.75rem;
  margin-right: -1.75rem;
}

.-mx-72 {
  margin-left: -18rem;
  margin-right: -18rem;
}

.-mx-8 {
  margin-left: -2rem;
  margin-right: -2rem;
}

.-mx-80 {
  margin-left: -20rem;
  margin-right: -20rem;
}

.-mx-9 {
  margin-left: -2.25rem;
  margin-right: -2.25rem;
}

.-mx-96 {
  margin-left: -24rem;
  margin-right: -24rem;
}

.-mx-px {
  margin-left: -1px;
  margin-right: -1px;
}

.-my-0 {
  margin-top: -0px;
  margin-bottom: -0px;
}

.-my-0.5 {
  margin-top: -0.125rem;
  margin-bottom: -0.125rem;
}

.-my-1 {
  margin-top: -0.25rem;
  margin-bottom: -0.25rem;
}

.-my-1.5 {
  margin-top: -0.375rem;
  margin-bottom: -0.375rem;
}

.-my-10 {
  margin-top: -2.5rem;
  margin-bottom: -2.5rem;
}

.-my-11 {
  margin-top: -2.75rem;
  margin-bottom: -2.75rem;
}

.-my-12 {
  margin-top: -3rem;
  margin-bottom: -3rem;
}

.-my-14 {
  margin-top: -3.5rem;
  margin-bottom: -3.5rem;
}

.-my-16 {
  margin-top: -4rem;
  margin-bottom: -4rem;
}

.-my-2 {
  margin-top: -0.5rem;
  margin-bottom: -0.5rem;
}

.-my-2.5 {
  margin-top: -0.625rem;
  margin-bottom: -0.625rem;
}

.-my-20 {
  margin-top: -5rem;
  margin-bottom: -5rem;
}

.-my-24 {
  margin-top: -6rem;
  margin-bottom: -6rem;
}

.-my-28 {
  margin-top: -7rem;
  margin-bottom: -7rem;
}

.-my-3 {
  margin-top: -0.75rem;
  margin-bottom: -0.75rem;
}

.-my-3.5 {
  margin-top: -0.875rem;
  margin-bottom: -0.875rem;
}

.-my-32 {
  margin-top: -8rem;
  margin-bottom: -8rem;
}

.-my-36 {
  margin-top: -9rem;
  margin-bottom: -9rem;
}

.-my-4 {
  margin-top: -1rem;
  margin-bottom: -1rem;
}

.-my-40 {
  margin-top: -10rem;
  margin-bottom: -10rem;
}

.-my-44 {
  margin-top: -11rem;
  margin-bottom: -11rem;
}

.-my-48 {
  margin-top: -12rem;
  margin-bottom: -12rem;
}

.-my-5 {
  margin-top: -1.25rem;
  margin-bottom: -1.25rem;
}

.-my-52 {
  margin-top: -13rem;
  margin-bottom: -13rem;
}

.-my-56 {
  margin-top: -14rem;
  margin-bottom: -14rem;
}

.-my-6 {
  margin-top: -1.5rem;
  margin-bottom: -1.5rem;
}

.-my-60 {
  margin-top: -15rem;
  margin-bottom: -15rem;
}

.-my-64 {
  margin-top: -16rem;
  margin-bottom: -16rem;
}

.-my-7 {
  margin-top: -1.75rem;
  margin-bottom: -1.75rem;
}

.-my-72 {
  margin-top: -18rem;
  margin-bottom: -18rem;
}

.-my-8 {
  margin-top: -2rem;
  margin-bottom: -2rem;
}

.-my-80 {
  margin-top: -20rem;
  margin-bottom: -20rem;
}

.-my-9 {
  margin-top: -2.25rem;
  margin-bottom: -2.25rem;
}

.-my-96 {
  margin-top: -24rem;
  margin-bottom: -24rem;
}

.-my-px {
  margin-top: -1px;
  margin-bottom: -1px;
}

.mx-0 {
  margin-left: 0px;
  margin-right: 0px;
}

.mx-0.5 {
  margin-left: 0.125rem;
  margin-right: 0.125rem;
}

.mx-1 {
  margin-left: 0.25rem;
  margin-right: 0.25rem;
}

.mx-1.5 {
  margin-left: 0.375rem;
  margin-right: 0.375rem;
}

.mx-10 {
  margin-left: 2.5rem;
  margin-right: 2.5rem;
}

.mx-11 {
  margin-left: 2.75rem;
  margin-right: 2.75rem;
}

.mx-12 {
  margin-left: 3rem;
  margin-right: 3rem;
}

.mx-14 {
  margin-left: 3.5rem;
  margin-right: 3.5rem;
}

.mx-16 {
  margin-left: 4rem;
  margin-right: 4rem;
}

.mx-2 {
  margin-left: 0.5rem;
  margin-right: 0.5rem;
}

.mx-2.5 {
  margin-left: 0.625rem;
  margin-right: 0.625rem;
}

.mx-20 {
  margin-left: 5rem;
  margin-right: 5rem;
}

.mx-24 {
  margin-left: 6rem;
  margin-right: 6rem;
}

.mx-28 {
  margin-left: 7rem;
  margin-right: 7rem;
}

.mx-3 {
  margin-left: 0.75rem;
  margin-right: 0.75rem;
}

.mx-3.5 {
  margin-left: 0.875rem;
  margin-right: 0.875rem;
}

.mx-32 {
  margin-left: 8rem;
  margin-right: 8rem;
}

.mx-36 {
  margin-left: 9rem;
  margin-right: 9rem;
}

.mx-4 {
  margin-left: 1rem;
  margin-right: 1rem;
}

.mx-40 {
  margin-left: 10rem;
  margin-right: 10rem;
}

.mx-44 {
  margin-left: 11rem;
  margin-right: 11rem;
}

.mx-48 {
  margin-left: 12rem;
  margin-right: 12rem;
}

.mx-5 {
  margin-left: 1.25rem;
  margin-right: 1.25rem;
}

.mx-52 {
  margin-left: 13rem;
  margin-right: 13rem;
}

.mx-56 {
  margin-left: 14rem;
  margin-right: 14rem;
}

.mx-6 {
  margin-left: 1.5rem;
  margin-right: 1.5rem;
}

.mx-60 {
  margin-left: 15rem;
  margin-right: 15rem;
}

.mx-64 {
  margin-left: 16rem;
  margin-right: 16rem;
}

.mx-7 {
  margin-left: 1.75rem;
  margin-right: 1.75rem;
}

.mx-72 {
  margin-left: 18rem;
  margin-right: 18rem;
}

.mx-8 {
  margin-left: 2rem;
  margin-right: 2rem;
}

.mx-80 {
  margin-left: 20rem;
  margin-right: 20rem;
}

.mx-9 {
  margin-left: 2.25rem;
  margin-right: 2.25rem;
}

.mx-96 {
  margin-left: 24rem;
  margin-right: 24rem;
}

.mx-auto {
  margin-left: auto;
  margin-right: auto;
}

.mx-px {
  margin-left: 1px;
  margin-right: 1px;
}

.my-0 {
  margin-top: 0px;
  margin-bottom: 0px;
}

.my-0.5 {
  margin-top: 0.125rem;
  margin-bottom: 0.125rem;
}

.my-1 {
  margin-top: 0.25rem;
  margin-bottom: 0.25rem;
}

.my-1.5 {
  margin-top: 0.375rem;
  margin-bottom: 0.375rem;
}

.my-10 {
  margin-top: 2.5rem;
  margin-bottom: 2.5rem;
}

.my-11 {
  margin-top: 2.75rem;
  margin-bottom: 2.75rem;
}

.my-12 {
  margin-top: 3rem;
  margin-bottom: 3rem;
}

.my-14 {
  margin-top: 3.5rem;
  margin-bottom: 3.5rem;
}

.my-16 {
  margin-top: 4rem;
  margin-bottom: 4rem;
}

.my-2 {
  margin-top: 0.5rem;
  margin-bottom: 0.5rem;
}

.my-2.5 {
  margin-top: 0.625rem;
  margin-bottom: 0.625rem;
}

.my-20 {
  margin-top: 5rem;
  margin-bottom: 5rem;
}

.my-24 {
  margin-top: 6rem;
  margin-bottom: 6rem;
}

.my-28 {
  margin-top: 7rem;
  margin-bottom: 7rem;
}

.my-3 {
  margin-top: 0.75rem;
  margin-bottom: 0.75rem;
}

.my-3.5 {
  margin-top: 0.875rem;
  margin-bottom: 0.875rem;
}

.my-32 {
  margin-top: 8rem;
  margin-bottom: 8rem;
}

.my-36 {
  margin-top: 9rem;
  margin-bottom: 9rem;
}

.my-4 {
  margin-top: 1rem;
  margin-bottom: 1rem;
}

.my-40 {
  margin-top: 10rem;
  margin-bottom: 10rem;
}

.my-44 {
  margin-top: 11rem;
  margin-bottom: 11rem;
}

.my-48 {
  margin-top: 12rem;
  margin-bottom: 12rem;
}

.my-5 {
  margin-top: 1.25rem;
  margin-bottom: 1.25rem;
}

.my-52 {
  margin-top: 13rem;
  margin-bottom: 13rem;
}

.my-56 {
  margin-top: 14rem;
  margin-bottom: 14rem;
}

.my-6 {
  margin-top: 1.5rem;
  margin-bottom: 1.5rem;
}

.my-60 {
  margin-top: 15rem;
  margin-bottom: 15rem;
}

.my-64 {
  margin-top: 16rem;
  margin-bottom: 16rem;
}

.my-7 {
  margin-top: 1.75rem;
  margin-bottom: 1.75rem;
}

.my-72 {
  margin-top: 18rem;
  margin-bottom: 18rem;
}

.my-8 {
  margin-top: 2rem;
  margin-bottom: 2rem;
}

.my-80 {
  margin-top: 20rem;
  margin-bottom: 20rem;
}

.my-9 {
  margin-top: 2.25rem;
  margin-bottom: 2.25rem;
}

.my-96 {
  margin-top: 24rem;
  margin-bottom: 24rem;
}

.my-px {
  margin-top: 1px;
  margin-bottom: 1px;
}

.-mb-0 {
  margin-bottom: -0px;
}

.-mb-0.5 {
  margin-bottom: -0.125rem;
}

.-mb-1 {
  margin-bottom: -0.25rem;
}

.-mb-1.5 {
  margin-bottom: -0.375rem;
}

.-mb-10 {
  margin-bottom: -2.5rem;
}

.-mb-11 {
  margin-bottom: -2.75rem;
}

.-mb-12 {
  margin-bottom: -3rem;
}

.-mb-14 {
  margin-bottom: -3.5rem;
}

.-mb-16 {
  margin-bottom: -4rem;
}

.-mb-2 {
  margin-bottom: -0.5rem;
}

.-mb-2.5 {
  margin-bottom: -0.625rem;
}

.-mb-20 {
  margin-bottom: -5rem;
}

.-mb-24 {
  margin-bottom: -6rem;
}

.-mb-28 {
  margin-bottom: -7rem;
}

.-mb-3 {
  margin-bottom: -0.75rem;
}

.-mb-3.5 {
  margin-bottom: -0.875rem;
}

.-mb-32 {
  margin-bottom: -8rem;
}

.-mb-36 {
  margin-bottom: -9rem;
}

.-mb-4 {
  margin-bottom: -1rem;
}

.-mb-40 {
  margin-bottom: -10rem;
}

.-mb-44 {
  margin-bottom: -11rem;
}

.-mb-48 {
  margin-bottom: -12rem;
}

.-mb-5 {
  margin-bottom: -1.25rem;
}

.-mb-52 {
  margin-bottom: -13rem;
}

.-mb-56 {
  margin-bottom: -14rem;
}

.-mb-6 {
  margin-bottom: -1.5rem;
}

.-mb-60 {
  margin-bottom: -15rem;
}

.-mb-64 {
  margin-bottom: -16rem;
}

.-mb-7 {
  margin-bottom: -1.75rem;
}

.-mb-72 {
  margin-bottom: -18rem;
}

.-mb-8 {
  margin-bottom: -2rem;
}

.-mb-80 {
  margin-bottom: -20rem;
}

.-mb-9 {
  margin-bottom: -2.25rem;
}

.-mb-96 {
  margin-bottom: -24rem;
}

.-mb-px {
  margin-bottom: -1px;
}

.-me-0 {
  margin-inline-end: -0px;
}

.-me-0.5 {
  margin-inline-end: -0.125rem;
}

.-me-1 {
  margin-inline-end: -0.25rem;
}

.-me-1.5 {
  margin-inline-end: -0.375rem;
}

.-me-10 {
  margin-inline-end: -2.5rem;
}

.-me-11 {
  margin-inline-end: -2.75rem;
}

.-me-12 {
  margin-inline-end: -3rem;
}

.-me-14 {
  margin-inline-end: -3.5rem;
}

.-me-16 {
  margin-inline-end: -4rem;
}

.-me-2 {
  margin-inline-end: -0.5rem;
}

.-me-2.5 {
  margin-inline-end: -0.625rem;
}

.-me-20 {
  margin-inline-end: -5rem;
}

.-me-24 {
  margin-inline-end: -6rem;
}

.-me-28 {
  margin-inline-end: -7rem;
}

.-me-3 {
  margin-inline-end: -0.75rem;
}

.-me-3.5 {
  margin-inline-end: -0.875rem;
}

.-me-32 {
  margin-inline-end: -8rem;
}

.-me-36 {
  margin-inline-end: -9rem;
}

.-me-4 {
  margin-inline-end: -1rem;
}

.-me-40 {
  margin-inline-end: -10rem;
}

.-me-44 {
  margin-inline-end: -11rem;
}

.-me-48 {
  margin-inline-end: -12rem;
}

.-me-5 {
  margin-inline-end: -1.25rem;
}

.-me-52 {
  margin-inline-end: -13rem;
}

.-me-56 {
  margin-inline-end: -14rem;
}

.-me-6 {
  margin-inline-end: -1.5rem;
}

.-me-60 {
  margin-inline-end: -15rem;
}

.-me-64 {
  margin-inline-end: -16rem;
}

.-me-7 {
  margin-inline-end: -1.75rem;
}

.-me-72 {
  margin-inline-end: -18rem;
}

.-me-8 {
  margin-inline-end: -2rem;
}

.-me-80 {
  margin-inline-end: -20rem;
}

.-me-9 {
  margin-inline-end: -2.25rem;
}

.-me-96 {
  margin-inline-end: -24rem;
}

.-me-px {
  margin-inline-end: -1px;
}

.-ml-0 {
  margin-left: -0px;
}

.-ml-0.5 {
  margin-left: -0.125rem;
}

.-ml-1 {
  margin-left: -0.25rem;
}

.-ml-1.5 {
  margin-left: -0.375rem;
}

.-ml-10 {
  margin-left: -2.5rem;
}

.-ml-11 {
  margin-left: -2.75rem;
}

.-ml-12 {
  margin-left: -3rem;
}

.-ml-14 {
  margin-left: -3.5rem;
}

.-ml-16 {
  margin-left: -4rem;
}

.-ml-2 {
  margin-left: -0.5rem;
}

.-ml-2.5 {
  margin-left: -0.625rem;
}

.-ml-20 {
  margin-left: -5rem;
}

.-ml-24 {
  margin-left: -6rem;
}

.-ml-28 {
  margin-left: -7rem;
}

.-ml-3 {
  margin-left: -0.75rem;
}

.-ml-3.5 {
  margin-left: -0.875rem;
}

.-ml-32 {
  margin-left: -8rem;
}

.-ml-36 {
  margin-left: -9rem;
}

.-ml-4 {
  margin-left: -1rem;
}

.-ml-40 {
  margin-left: -10rem;
}

.-ml-44 {
  margin-left: -11rem;
}

.-ml-48 {
  margin-left: -12rem;
}

.-ml-5 {
  margin-left: -1.25rem;
}

.-ml-52 {
  margin-left: -13rem;
}

.-ml-56 {
  margin-left: -14rem;
}

.-ml-6 {
  margin-left: -1.5rem;
}

.-ml-60 {
  margin-left: -15rem;
}

.-ml-64 {
  margin-left: -16rem;
}

.-ml-7 {
  margin-left: -1.75rem;
}

.-ml-72 {
  margin-left: -18rem;
}

.-ml-8 {
  margin-left: -2rem;
}

.-ml-80 {
  margin-left: -20rem;
}

.-ml-9 {
  margin-left: -2.25rem;
}

.-ml-96 {
  margin-left: -24rem;
}

.-ml-px {
  margin-left: -1px;
}

.-mr-0 {
  margin-right: -0px;
}

.-mr-0.5 {
  margin-right: -0.125rem;
}

.-mr-1 {
  margin-right: -0.25rem;
}

.-mr-1.5 {
  margin-right: -0.375rem;
}

.-mr-10 {
  margin-right: -2.5rem;
}

.-mr-11 {
  margin-right: -2.75rem;
}

.-mr-12 {
  margin-right: -3rem;
}

.-mr-14 {
  margin-right: -3.5rem;
}

.-mr-16 {
  margin-right: -4rem;
}

.-mr-2 {
  margin-right: -0.5rem;
}

.-mr-2.5 {
  margin-right: -0.625rem;
}

.-mr-20 {
  margin-right: -5rem;
}

.-mr-24 {
  margin-right: -6rem;
}

.-mr-28 {
  margin-right: -7rem;
}

.-mr-3 {
  margin-right: -0.75rem;
}

.-mr-3.5 {
  margin-right: -0.875rem;
}

.-mr-32 {
  margin-right: -8rem;
}

.-mr-36 {
  margin-right: -9rem;
}

.-mr-4 {
  margin-right: -1rem;
}

.-mr-40 {
  margin-right: -10rem;
}

.-mr-44 {
  margin-right: -11rem;
}

.-mr-48 {
  margin-right: -12rem;
}

.-mr-5 {
  margin-right: -1.25rem;
}

.-mr-52 {
  margin-right: -13rem;
}

.-mr-56 {
  margin-right: -14rem;
}

.-mr-6 {
  margin-right: -1.5rem;
}

.-mr-60 {
  margin-right: -15rem;
}

.-mr-64 {
  margin-right: -16rem;
}

.-mr-7 {
  margin-right: -1.75rem;
}

.-mr-72 {
  margin-right: -18rem;
}

.-mr-8 {
  margin-right: -2rem;
}

.-mr-80 {
  margin-right: -20rem;
}

.-mr-9 {
  margin-right: -2.25rem;
}

.-mr-96 {
  margin-right: -24rem;
}

.-mr-px {
  margin-right: -1px;
}

.-ms-0 {
  margin-inline-start: -0px;
}

.-ms-0.5 {
  margin-inline-start: -0.125rem;
}

.-ms-1 {
  margin-inline-start: -0.25rem;
}

.-ms-1.5 {
  margin-inline-start: -0.375rem;
}

.-ms-10 {
  margin-inline-start: -2.5rem;
}

.-ms-11 {
  margin-inline-start: -2.75rem;
}

.-ms-12 {
  margin-inline-start: -3rem;
}

.-ms-14 {
  margin-inline-start: -3.5rem;
}

.-ms-16 {
  margin-inline-start: -4rem;
}

.-ms-2 {
  margin-inline-start: -0.5rem;
}

.-ms-2.5 {
  margin-inline-start: -0.625rem;
}

.-ms-20 {
  margin-inline-start: -5rem;
}

.-ms-24 {
  margin-inline-start: -6rem;
}

.-ms-28 {
  margin-inline-start: -7rem;
}

.-ms-3 {
  margin-inline-start: -0.75rem;
}

.-ms-3.5 {
  margin-inline-start: -0.875rem;
}

.-ms-32 {
  margin-inline-start: -8rem;
}

.-ms-36 {
  margin-inline-start: -9rem;
}

.-ms-4 {
  margin-inline-start: -1rem;
}

.-ms-40 {
  margin-inline-start: -10rem;
}

.-ms-44 {
  margin-inline-start: -11rem;
}

.-ms-48 {
  margin-inline-start: -12rem;
}

.-ms-5 {
  margin-inline-start: -1.25rem;
}

.-ms-52 {
  margin-inline-start: -13rem;
}

.-ms-56 {
  margin-inline-start: -14rem;
}

.-ms-6 {
  margin-inline-start: -1.5rem;
}

.-ms-60 {
  margin-inline-start: -15rem;
}

.-ms-64 {
  margin-inline-start: -16rem;
}

.-ms-7 {
  margin-inline-start: -1.75rem;
}

.-ms-72 {
  margin-inline-start: -18rem;
}

.-ms-8 {
  margin-inline-start: -2rem;
}

.-ms-80 {
  margin-inline-start: -20rem;
}

.-ms-9 {
  margin-inline-start: -2.25rem;
}

.-ms-96 {
  margin-inline-start: -24rem;
}

.-ms-px {
  margin-inline-start: -1px;
}

.-mt-0 {
  margin-top: -0px;
}

.-mt-0.5 {
  margin-top: -0.125rem;
}

.-mt-1 {
  margin-top: -0.25rem;
}

.-mt-1.5 {
  margin-top: -0.375rem;
}

.-mt-10 {
  margin-top: -2.5rem;
}

.-mt-11 {
  margin-top: -2.75rem;
}

.-mt-12 {
  margin-top: -3rem;
}

.-mt-14 {
  margin-top: -3.5rem;
}

.-mt-16 {
  margin-top: -4rem;
}

.-mt-2 {
  margin-top: -0.5rem;
}

.-mt-2.5 {
  margin-top: -0.625rem;
}

.-mt-20 {
  margin-top: -5rem;
}

.-mt-24 {
  margin-top: -6rem;
}

.-mt-28 {
  margin-top: -7rem;
}

.-mt-3 {
  margin-top: -0.75rem;
}

.-mt-3.5 {
  margin-top: -0.875rem;
}

.-mt-32 {
  margin-top: -8rem;
}

.-mt-36 {
  margin-top: -9rem;
}

.-mt-4 {
  margin-top: -1rem;
}

.-mt-40 {
  margin-top: -10rem;
}

.-mt-44 {
  margin-top: -11rem;
}

.-mt-48 {
  margin-top: -12rem;
}

.-mt-5 {
  margin-top: -1.25rem;
}

.-mt-52 {
  margin-top: -13rem;
}

.-mt-56 {
  margin-top: -14rem;
}

.-mt-6 {
  margin-top: -1.5rem;
}

.-mt-60 {
  margin-top: -15rem;
}

.-mt-64 {
  margin-top: -16rem;
}

.-mt-7 {
  margin-top: -1.75rem;
}

.-mt-72 {
  margin-top: -18rem;
}

.-mt-8 {
  margin-top: -2rem;
}

.-mt-80 {
  margin-top: -20rem;
}

.-mt-9 {
  margin-top: -2.25rem;
}

.-mt-96 {
  margin-top: -24rem;
}

.-mt-px {
  margin-top: -1px;
}

.mb-0 {
  margin-bottom: 0px;
}

.mb-0.5 {
  margin-bottom: 0.125rem;
}

.mb-1 {
  margin-bottom: 0.25rem;
}

.mb-1.5 {
  margin-bottom: 0.375rem;
}

.mb-10 {
  margin-bottom: 2.5rem;
}

.mb-11 {
  margin-bottom: 2.75rem;
}

.mb-12 {
  margin-bottom: 3rem;
}

.mb-14 {
  margin-bottom: 3.5rem;
}

.mb-16 {
  margin-bottom: 4rem;
}

.mb-2 {
  margin-bottom: 0.5rem;
}

.mb-2.5 {
  margin-bottom: 0.625rem;
}

.mb-20 {
  margin-bottom: 5rem;
}

.mb-24 {
  margin-bottom: 6rem;
}

.mb-28 {
  margin-bottom: 7rem;
}

.mb-3 {
  margin-bottom: 0.75rem;
}

.mb-3.5 {
  margin-bottom: 0.875rem;
}

.mb-32 {
  margin-bottom: 8rem;
}

.mb-36 {
  margin-bottom: 9rem;
}

.mb-4 {
  margin-bottom: 1rem;
}

.mb-40 {
  margin-bottom: 10rem;
}

.mb-44 {
  margin-bottom: 11rem;
}

.mb-48 {
  margin-bottom: 12rem;
}

.mb-5 {
  margin-bottom: 1.25rem;
}

.mb-52 {
  margin-bottom: 13rem;
}

.mb-56 {
  margin-bottom: 14rem;
}

.mb-6 {
  margin-bottom: 1.5rem;
}

.mb-60 {
  margin-bottom: 15rem;
}

.mb-64 {
  margin-bottom: 16rem;
}

.mb-7 {
  margin-bottom: 1.75rem;
}

.mb-72 {
  margin-bottom: 18rem;
}

.mb-8 {
  margin-bottom: 2rem;
}

.mb-80 {
  margin-bottom: 20rem;
}

.mb-9 {
  margin-bottom: 2.25rem;
}

.mb-96 {
  margin-bottom: 24rem;
}

.mb-px {
  margin-bottom: 1px;
}

.me-0 {
  margin-inline-end: 0px;
}

.me-0.5 {
  margin-inline-end: 0.125rem;
}

.me-1 {
  margin-inline-end: 0.25rem;
}

.me-1.5 {
  margin-inline-end: 0.375rem;
}

.me-10 {
  margin-inline-end: 2.5rem;
}

.me-11 {
  margin-inline-end: 2.75rem;
}

.me-12 {
  margin-inline-end: 3rem;
}

.me-14 {
  margin-inline-end: 3.5rem;
}

.me-16 {
  margin-inline-end: 4rem;
}

.me-2 {
  margin-inline-end: 0.5rem;
}

.me-2.5 {
  margin-inline-end: 0.625rem;
}

.me-20 {
  margin-inline-end: 5rem;
}

.me-24 {
  margin-inline-end: 6rem;
}

.me-28 {
  margin-inline-end: 7rem;
}

.me-3 {
  margin-inline-end: 0.75rem;
}

.me-3.5 {
  margin-inline-end: 0.875rem;
}

.me-32 {
  margin-inline-end: 8rem;
}

.me-36 {
  margin-inline-end: 9rem;
}

.me-4 {
  margin-inline-end: 1rem;
}

.me-40 {
  margin-inline-end: 10rem;
}

.me-44 {
  margin-inline-end: 11rem;
}

.me-48 {
  margin-inline-end: 12rem;
}

.me-5 {
  margin-inline-end: 1.25rem;
}

.me-52 {
  margin-inline-end: 13rem;
}

.me-56 {
  margin-inline-end: 14rem;
}

.me-6 {
  margin-inline-end: 1.5rem;
}

.me-60 {
  margin-inline-end: 15rem;
}

.me-64 {
  margin-inline-end: 16rem;
}

.me-7 {
  margin-inline-end: 1.75rem;
}

.me-72 {
  margin-inline-end: 18rem;
}

.me-8 {
  margin-inline-end: 2rem;
}

.me-80 {
  margin-inline-end: 20rem;
}

.me-9 {
  margin-inline-end: 2.25rem;
}

.me-96 {
  margin-inline-end: 24rem;
}

.me-px {
  margin-inline-end: 1px;
}

.ml-0 {
  margin-left: 0px;
}

.ml-0.5 {
  margin-left: 0.125rem;
}

.ml-1 {
  margin-left: 0.25rem;
}

.ml-1.5 {
  margin-left: 0.375rem;
}

.ml-10 {
  margin-left: 2.5rem;
}

.ml-11 {
  margin-left: 2.75rem;
}

.ml-12 {
  margin-left: 3rem;
}

.ml-14 {
  margin-left: 3.5rem;
}

.ml-16 {
  margin-left: 4rem;
}

.ml-2 {
  margin-left: 0.5rem;
}

.ml-2.5 {
  margin-left: 0.625rem;
}

.ml-20 {
  margin-left: 5rem;
}

.ml-24 {
  margin-left: 6rem;
}

.ml-28 {
  margin-left: 7rem;
}

.ml-3 {
  margin-left: 0.75rem;
}

.ml-3.5 {
  margin-left: 0.875rem;
}

.ml-32 {
  margin-left: 8rem;
}

.ml-36 {
  margin-left: 9rem;
}

.ml-4 {
  margin-left: 1rem;
}

.ml-40 {
  margin-left: 10rem;
}

.ml-44 {
  margin-left: 11rem;
}

.ml-48 {
  margin-left: 12rem;
}

.ml-5 {
  margin-left: 1.25rem;
}

.ml-52 {
  margin-left: 13rem;
}

.ml-56 {
  margin-left: 14rem;
}

.ml-6 {
  margin-left: 1.5rem;
}

.ml-60 {
  margin-left: 15rem;
}

.ml-64 {
  margin-left: 16rem;
}

.ml-7 {
  margin-left: 1.75rem;
}

.ml-72 {
  margin-left: 18rem;
}

.ml-8 {
  margin-left: 2rem;
}

.ml-80 {
  margin-left: 20rem;
}

.ml-9 {
  margin-left: 2.25rem;
}

.ml-96 {
  margin-left: 24rem;
}

.ml-px {
  margin-left: 1px;
}

.mr-0 {
  margin-right: 0px;
}

.mr-0.5 {
  margin-right: 0.125rem;
}

.mr-1 {
  margin-right: 0.25rem;
}

.mr-1.5 {
  margin-right: 0.375rem;
}

.mr-10 {
  margin-right: 2.5rem;
}

.mr-11 {
  margin-right: 2.75rem;
}

.mr-12 {
  margin-right: 3rem;
}

.mr-14 {
  margin-right: 3.5rem;
}

.mr-16 {
  margin-right: 4rem;
}

.mr-2 {
  margin-right: 0.5rem;
}

.mr-2.5 {
  margin-right: 0.625rem;
}

.mr-20 {
  margin-right: 5rem;
}

.mr-24 {
  margin-right: 6rem;
}

.mr-28 {
  margin-right: 7rem;
}

.mr-3 {
  margin-right: 0.75rem;
}

.mr-3.5 {
  margin-right: 0.875rem;
}

.mr-32 {
  margin-right: 8rem;
}

.mr-36 {
  margin-right: 9rem;
}

.mr-4 {
  margin-right: 1rem;
}

.mr-40 {
  margin-right: 10rem;
}

.mr-44 {
  margin-right: 11rem;
}

.mr-48 {
  margin-right: 12rem;
}

.mr-5 {
  margin-right: 1.25rem;
}

.mr-52 {
  margin-right: 13rem;
}

.mr-56 {
  margin-right: 14rem;
}

.mr-6 {
  margin-right: 1.5rem;
}

.mr-60 {
  margin-right: 15rem;
}

.mr-64 {
  margin-right: 16rem;
}

.mr-7 {
  margin-right: 1.75rem;
}

.mr-72 {
  margin-right: 18rem;
}

.mr-8 {
  margin-right: 2rem;
}

.mr-80 {
  margin-right: 20rem;
}

.mr-9 {
  margin-right: 2.25rem;
}

.mr-96 {
  margin-right: 24rem;
}

.mr-px {
  margin-right: 1px;
}

.ms-0 {
  margin-inline-start: 0px;
}

.ms-0.5 {
  margin-inline-start: 0.125rem;
}

.ms-1 {
  margin-inline-start: 0.25rem;
}

.ms-1.5 {
  margin-inline-start: 0.375rem;
}

.ms-10 {
  margin-inline-start: 2.5rem;
}

.ms-11 {
  margin-inline-start: 2.75rem;
}

.ms-12 {
  margin-inline-start: 3rem;
}

.ms-14 {
  margin-inline-start: 3.5rem;
}

.ms-16 {
  margin-inline-start: 4rem;
}

.ms-2 {
  margin-inline-start: 0.5rem;
}

.ms-2.5 {
  margin-inline-start: 0.625rem;
}

.ms-20 {
  margin-inline-start: 5rem;
}

.ms-24 {
  margin-inline-start: 6rem;
}

.ms-28 {
  margin-inline-start: 7rem;
}

.ms-3 {
  margin-inline-start: 0.75rem;
}

.ms-3.5 {
  margin-inline-start: 0.875rem;
}

.ms-32 {
  margin-inline-start: 8rem;
}

.ms-36 {
  margin-inline-start: 9rem;
}

.ms-4 {
  margin-inline-start: 1rem;
}

.ms-40 {
  margin-inline-start: 10rem;
}

.ms-44 {
  margin-inline-start: 11rem;
}

.ms-48 {
  margin-inline-start: 12rem;
}

.ms-5 {
  margin-inline-start: 1.25rem;
}

.ms-52 {
  margin-inline-start: 13rem;
}

.ms-56 {
  margin-inline-start: 14rem;
}

.ms-6 {
  margin-inline-start: 1.5rem;
}

.ms-60 {
  margin-inline-start: 15rem;
}

.ms-64 {
  margin-inline-start: 16rem;
}

.ms-7 {
  margin-inline-start: 1.75rem;
}

.ms-72 {
  margin-inline-start: 18rem;
}

.ms-8 {
  margin-inline-start: 2rem;
}

.ms-80 {
  margin-inline-start: 20rem;
}

.ms-9 {
  margin-inline-start: 2.25rem;
}

.ms-96 {
  margin-inline-start: 24rem;
}

.ms-px {
  margin-inline-start: 1px;
}

.mt-0 {
  margin-top: 0px;
}

.mt-0.5 {
  margin-top: 0.125rem;
}

.mt-1 {
  margin-top: 0.25rem;
}

.mt-1.5 {
  margin-top: 0.375rem;
}

.mt-10 {
  margin-top: 2.5rem;
}

.mt-11 {
  margin-top: 2.75rem;
}

.mt-12 {
  margin-top: 3rem;
}

.mt-14 {
  margin-top: 3.5rem;
}

.mt-16 {
  margin-top: 4rem;
}

.mt-2 {
  margin-top: 0.5rem;
}

.mt-2.5 {
  margin-top: 0.625rem;
}

.mt-20 {
  margin-top: 5rem;
}

.mt-24 {
  margin-top: 6rem;
}

.mt-28 {
  margin-top: 7rem;
}

.mt-3 {
  margin-top: 0.75rem;
}

.mt-3.5 {
  margin-top: 0.875rem;
}

.mt-32 {
  margin-top: 8rem;
}

.mt-36 {
  margin-top: 9rem;
}

.mt-4 {
  margin-top: 1rem;
}

.mt-40 {
  margin-top: 10rem;
}

.mt-44 {
  margin-top: 11rem;
}

.mt-48 {
  margin-top: 12rem;
}

.mt-5 {
  margin-top: 1.25rem;
}

.mt-52 {
  margin-top: 13rem;
}

.mt-56 {
  margin-top: 14rem;
}

.mt-6 {
  margin-top: 1.5rem;
}

.mt-60 {
  margin-top: 15rem;
}

.mt-64 {
  margin-top: 16rem;
}

.mt-7 {
  margin-top: 1.75rem;
}

.mt-72 {
  margin-top: 18rem;
}

.mt-8 {
  margin-top: 2rem;
}

.mt-80 {
  margin-top: 20rem;
}

.mt-9 {
  margin-top: 2.25rem;
}

.mt-96 {
  margin-top: 24rem;
}

.mt-px {
  margin-top: 1px;
}

.box-border {
  box-sizing: border-box;
}

.box-content {
  box-sizing: content-box;
}

.line-clamp-1 {
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 1;
}

.line-clamp-2 {
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
}

.line-clamp-3 {
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 3;
}

.line-clamp-4 {
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 4;
}

.line-clamp-5 {
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 5;
}

.line-clamp-6 {
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 6;
}

.line-clamp-none {
  overflow: visible;
  display: block;
  -webkit-box-orient: horizontal;
  -webkit-line-clamp: none;
}

.block {
  display: block;
}

.inline-block {
  display: inline-block;
}

.inline {
  display: inline;
}

.flex {
  display: flex;
}

.inline-flex {
  display: inline-flex;
}

.table {
  display: table;
}

.inline-table {
  display: inline-table;
}

.table-caption {
  display: table-caption;
}

.table-cell {
  display: table-cell;
}

.table-column {
  display: table-column;
}

.table-column-group {
  display: table-column-group;
}

.table-footer-group {
  display: table-footer-group;
}

.table-header-group {
  display: table-header-group;
}

.table-row-group {
  display: table-row-group;
}

.table-row {
  display: table-row;
}

.flow-root {
  display: flow-root;
}

.grid {
  display: grid;
}

.inline-grid {
  display: inline-grid;
}

.contents {
  display: contents;
}

.list-item {
  display: list-item;
}

.hidden {
  display: none;
}

.aspect-auto {
  aspect-ratio: auto;
}

.aspect-square {
  aspect-ratio: 1 / 1;
}

.aspect-video {
  aspect-ratio: 16 / 9;
}

.h-0 {
  height: 0px;
}

.h-0.5 {
  height: 0.125rem;
}

.h-1 {
  height: 0.25rem;
}

.h-1.5 {
  height: 0.375rem;
}

.h-1/2 {
  height: 50%;
}

.h-1/3 {
  height: 33.333333%;
}

.h-1/4 {
  height: 25%;
}

.h-1/5 {
  height: 20%;
}

.h-1/6 {
  height: 16.666667%;
}

.h-10 {
  height: 2.5rem;
}

.h-11 {
  height: 2.75rem;
}

.h-12 {
  height: 3rem;
}

.h-14 {
  height: 3.5rem;
}

.h-16 {
  height: 4rem;
}

.h-2 {
  height: 0.5rem;
}

.h-2.5 {
  height: 0.625rem;
}

.h-2/3 {
  height: 66.666667%;
}

.h-2/4 {
  height: 50%;
}

.h-2/5 {
  height: 40%;
}

.h-2/6 {
  height: 33.333333%;
}

.h-20 {
  height: 5rem;
}

.h-24 {
  height: 6rem;
}

.h-28 {
  height: 7rem;
}

.h-3 {
  height: 0.75rem;
}

.h-3.5 {
  height: 0.875rem;
}

.h-3/4 {
  height: 75%;
}

.h-3/5 {
  height: 60%;
}

.h-3/6 {
  height: 50%;
}

.h-32 {
  height: 8rem;
}

.h-36 {
  height: 9rem;
}

.h-4 {
  height: 1rem;
}

.h-4/5 {
  height: 80%;
}

.h-4/6 {
  height: 66.666667%;
}

.h-40 {
  height: 10rem;
}

.h-44 {
  height: 11rem;
}

.h-48 {
  height: 12rem;
}

.h-5 {
  height: 1.25rem;
}

.h-5/6 {
  height: 83.333333%;
}

.h-52 {
  height: 13rem;
}

.h-56 {
  height: 14rem;
}

.h-6 {
  height: 1.5rem;
}

.h-60 {
  height: 15rem;
}

.h-64 {
  height: 16rem;
}

.h-7 {
  height: 1.75rem;
}

.h-72 {
  height: 18rem;
}

.h-8 {
  height: 2rem;
}

.h-80 {
  height: 20rem;
}

.h-9 {
  height: 2.25rem;
}

.h-96 {
  height: 24rem;
}

.h-auto {
  height: auto;
}

.h-fit {
  height: -moz-fit-content;
  height: fit-content;
}

.h-full {
  height: 100%;
}

.h-max {
  height: -moz-max-content;
  height: max-content;
}

.h-min {
  height: -moz-min-content;
  height: min-content;
}

.h-px {
  height: 1px;
}

.h-screen {
  height: 100vh;
}

.max-h-0 {
  max-height: 0px;
}

.max-h-0.5 {
  max-height: 0.125rem;
}

.max-h-1 {
  max-height: 0.25rem;
}

.max-h-1.5 {
  max-height: 0.375rem;
}

.max-h-10 {
  max-height: 2.5rem;
}

.max-h-11 {
  max-height: 2.75rem;
}

.max-h-12 {
  max-height: 3rem;
}

.max-h-14 {
  max-height: 3.5rem;
}

.max-h-16 {
  max-height: 4rem;
}

.max-h-2 {
  max-height: 0.5rem;
}

.max-h-2.5 {
  max-height: 0.625rem;
}

.max-h-20 {
  max-height: 5rem;
}

.max-h-24 {
  max-height: 6rem;
}

.max-h-28 {
  max-height: 7rem;
}

.max-h-3 {
  max-height: 0.75rem;
}

.max-h-3.5 {
  max-height: 0.875rem;
}

.max-h-32 {
  max-height: 8rem;
}

.max-h-36 {
  max-height: 9rem;
}

.max-h-4 {
  max-height: 1rem;
}

.max-h-40 {
  max-height: 10rem;
}

.max-h-44 {
  max-height: 11rem;
}

.max-h-48 {
  max-height: 12rem;
}

.max-h-5 {
  max-height: 1.25rem;
}

.max-h-52 {
  max-height: 13rem;
}

.max-h-56 {
  max-height: 14rem;
}

.max-h-6 {
  max-height: 1.5rem;
}

.max-h-60 {
  max-height: 15rem;
}

.max-h-64 {
  max-height: 16rem;
}

.max-h-7 {
  max-height: 1.75rem;
}

.max-h-72 {
  max-height: 18rem;
}

.max-h-8 {
  max-height: 2rem;
}

.max-h-80 {
  max-height: 20rem;
}

.max-h-9 {
  max-height: 2.25rem;
}

.max-h-96 {
  max-height: 24rem;
}

.max-h-fit {
  max-height: -moz-fit-content;
  max-height: fit-content;
}

.max-h-full {
  max-height: 100%;
}

.max-h-max {
  max-height: -moz-max-content;
  max-height: max-content;
}

.max-h-min {
  max-height: -moz-min-content;
  max-height: min-content;
}

.max-h-none {
  max-height: none;
}

.max-h-px {
  max-height: 1px;
}

.max-h-screen {
  max-height: 100vh;
}

.min-h-0 {
  min-height: 0px;
}

.min-h-fit {
  min-height: -moz-fit-content;
  min-height: fit-content;
}

.min-h-full {
  min-height: 100%;
}

.min-h-max {
  min-height: -moz-max-content;
  min-height: max-content;
}

.min-h-min {
  min-height: -moz-min-content;
  min-height: min-content;
}

.min-h-screen {
  min-height: 100vh;
}

.w-0 {
  width: 0px;
}

.w-0.5 {
  width: 0.125rem;
}

.w-1 {
  width: 0.25rem;
}

.w-1.5 {
  width: 0.375rem;
}

.w-1/12 {
  width: 8.333333%;
}

.w-1/2 {
  width: 50%;
}

.w-1/3 {
  width: 33.333333%;
}

.w-1/4 {
  width: 25%;
}

.w-1/5 {
  width: 20%;
}

.w-1/6 {
  width: 16.666667%;
}

.w-10 {
  width: 2.5rem;
}

.w-10/12 {
  width: 83.333333%;
}

.w-11 {
  width: 2.75rem;
}

.w-11/12 {
  width: 91.666667%;
}

.w-12 {
  width: 3rem;
}

.w-14 {
  width: 3.5rem;
}

.w-16 {
  width: 4rem;
}

.w-2 {
  width: 0.5rem;
}

.w-2.5 {
  width: 0.625rem;
}

.w-2/12 {
  width: 16.666667%;
}

.w-2/3 {
  width: 66.666667%;
}

.w-2/4 {
  width: 50%;
}

.w-2/5 {
  width: 40%;
}

.w-2/6 {
  width: 33.333333%;
}

.w-20 {
  width: 5rem;
}

.w-24 {
  width: 6rem;
}

.w-28 {
  width: 7rem;
}

.w-3 {
  width: 0.75rem;
}

.w-3.5 {
  width: 0.875rem;
}

.w-3/12 {
  width: 25%;
}

.w-3/4 {
  width: 75%;
}

.w-3/5 {
  width: 60%;
}

.w-3/6 {
  width: 50%;
}

.w-32 {
  width: 8rem;
}

.w-36 {
  width: 9rem;
}

.w-4 {
  width: 1rem;
}

.w-4/12 {
  width: 33.333333%;
}

.w-4/5 {
  width: 80%;
}

.w-4/6 {
  width: 66.666667%;
}

.w-40 {
  width: 10rem;
}

.w-44 {
  width: 11rem;
}

.w-48 {
  width: 12rem;
}

.w-5 {
  width: 1.25rem;
}

.w-5/12 {
  width: 41.666667%;
}

.w-5/6 {
  width: 83.333333%;
}

.w-52 {
  width: 13rem;
}

.w-56 {
  width: 14rem;
}

.w-6 {
  width: 1.5rem;
}

.w-6/12 {
  width: 50%;
}

.w-60 {
  width: 15rem;
}

.w-64 {
  width: 16rem;
}

.w-7 {
  width: 1.75rem;
}

.w-7/12 {
  width: 58.333333%;
}

.w-72 {
  width: 18rem;
}

.w-8 {
  width: 2rem;
}

.w-8/12 {
  width: 66.666667%;
}

.w-80 {
  width: 20rem;
}

.w-9 {
  width: 2.25rem;
}

.w-9/12 {
  width: 75%;
}

.w-96 {
  width: 24rem;
}

.w-auto {
  width: auto;
}

.w-fit {
  width: -moz-fit-content;
  width: fit-content;
}

.w-full {
  width: 100%;
}

.w-max {
  width: -moz-max-content;
  width: max-content;
}

.w-min {
  width: -moz-min-content;
  width: min-content;
}

.w-px {
  width: 1px;
}

.w-screen {
  width: 100vw;
}

.min-w-0 {
  min-width: 0px;
}

.min-w-fit {
  min-width: -moz-fit-content;
  min-width: fit-content;
}

.min-w-full {
  min-width: 100%;
}

.min-w-max {
  min-width: -moz-max-content;
  min-width: max-content;
}

.min-w-min {
  min-width: -moz-min-content;
  min-width: min-content;
}

.max-w-0 {
  max-width: 0rem;
}

.max-w-2xl {
  max-width: 42rem;
}

.max-w-3xl {
  max-width: 48rem;
}

.max-w-4xl {
  max-width: 56rem;
}

.max-w-5xl {
  max-width: 64rem;
}

.max-w-6xl {
  max-width: 72rem;
}

.max-w-7xl {
  max-width: 80rem;
}

.max-w-fit {
  max-width: -moz-fit-content;
  max-width: fit-content;
}

.max-w-full {
  max-width: 100%;
}

.max-w-lg {
  max-width: 32rem;
}

.max-w-max {
  max-width: -moz-max-content;
  max-width: max-content;
}

.max-w-md {
  max-width: 28rem;
}

.max-w-min {
  max-width: -moz-min-content;
  max-width: min-content;
}

.max-w-none {
  max-width: none;
}

.max-w-prose {
  max-width: 65ch;
}

.max-w-screen-2xl {
  max-width: 1536px;
}

.max-w-screen-lg {
  max-width: 1024px;
}

.max-w-screen-md {
  max-width: 768px;
}

.max-w-screen-sm {
  max-width: 640px;
}

.max-w-screen-xl {
  max-width: 1280px;
}

.max-w-sm {
  max-width: 24rem;
}

.max-w-xl {
  max-width: 36rem;
}

.max-w-xs {
  max-width: 20rem;
}

.flex-1 {
  flex: 1 1 0%;
}

.flex-auto {
  flex: 1 1 auto;
}

.flex-initial {
  flex: 0 1 auto;
}

.flex-none {
  flex: none;
}

.shrink {
  flex-shrink: 1;
}

.shrink-0 {
  flex-shrink: 0;
}

.grow {
  flex-grow: 1;
}

.grow-0 {
  flex-grow: 0;
}

.basis-0 {
  flex-basis: 0px;
}

.basis-0.5 {
  flex-basis: 0.125rem;
}

.basis-1 {
  flex-basis: 0.25rem;
}

.basis-1.5 {
  flex-basis: 0.375rem;
}

.basis-1/12 {
  flex-basis: 8.333333%;
}

.basis-1/2 {
  flex-basis: 50%;
}

.basis-1/3 {
  flex-basis: 33.333333%;
}

.basis-1/4 {
  flex-basis: 25%;
}

.basis-1/5 {
  flex-basis: 20%;
}

.basis-1/6 {
  flex-basis: 16.666667%;
}

.basis-10 {
  flex-basis: 2.5rem;
}

.basis-10/12 {
  flex-basis: 83.333333%;
}

.basis-11 {
  flex-basis: 2.75rem;
}

.basis-11/12 {
  flex-basis: 91.666667%;
}

.basis-12 {
  flex-basis: 3rem;
}

.basis-14 {
  flex-basis: 3.5rem;
}

.basis-16 {
  flex-basis: 4rem;
}

.basis-2 {
  flex-basis: 0.5rem;
}

.basis-2.5 {
  flex-basis: 0.625rem;
}

.basis-2/12 {
  flex-basis: 16.666667%;
}

.basis-2/3 {
  flex-basis: 66.666667%;
}

.basis-2/4 {
  flex-basis: 50%;
}

.basis-2/5 {
  flex-basis: 40%;
}

.basis-2/6 {
  flex-basis: 33.333333%;
}

.basis-20 {
  flex-basis: 5rem;
}

.basis-24 {
  flex-basis: 6rem;
}

.basis-28 {
  flex-basis: 7rem;
}

.basis-3 {
  flex-basis: 0.75rem;
}

.basis-3.5 {
  flex-basis: 0.875rem;
}

.basis-3/12 {
  flex-basis: 25%;
}

.basis-3/4 {
  flex-basis: 75%;
}

.basis-3/5 {
  flex-basis: 60%;
}

.basis-3/6 {
  flex-basis: 50%;
}

.basis-32 {
  flex-basis: 8rem;
}

.basis-36 {
  flex-basis: 9rem;
}

.basis-4 {
  flex-basis: 1rem;
}

.basis-4/12 {
  flex-basis: 33.333333%;
}

.basis-4/5 {
  flex-basis: 80%;
}

.basis-4/6 {
  flex-basis: 66.666667%;
}

.basis-40 {
  flex-basis: 10rem;
}

.basis-44 {
  flex-basis: 11rem;
}

.basis-48 {
  flex-basis: 12rem;
}

.basis-5 {
  flex-basis: 1.25rem;
}

.basis-5/12 {
  flex-basis: 41.666667%;
}

.basis-5/6 {
  flex-basis: 83.333333%;
}

.basis-52 {
  flex-basis: 13rem;
}

.basis-56 {
  flex-basis: 14rem;
}

.basis-6 {
  flex-basis: 1.5rem;
}

.basis-6/12 {
  flex-basis: 50%;
}

.basis-60 {
  flex-basis: 15rem;
}

.basis-64 {
  flex-basis: 16rem;
}

.basis-7 {
  flex-basis: 1.75rem;
}

.basis-7/12 {
  flex-basis: 58.333333%;
}

.basis-72 {
  flex-basis: 18rem;
}

.basis-8 {
  flex-basis: 2rem;
}

.basis-8/12 {
  flex-basis: 66.666667%;
}

.basis-80 {
  flex-basis: 20rem;
}

.basis-9 {
  flex-basis: 2.25rem;
}

.basis-9/12 {
  flex-basis: 75%;
}

.basis-96 {
  flex-basis: 24rem;
}

.basis-auto {
  flex-basis: auto;
}

.basis-full {
  flex-basis: 100%;
}

.basis-px {
  flex-basis: 1px;
}

.table-auto {
  table-layout: auto;
}

.table-fixed {
  table-layout: fixed;
}

.caption-top {
  caption-side: top;
}

.caption-bottom {
  caption-side: bottom;
}

.border-collapse {
  border-collapse: collapse;
}

.border-separate {
  border-collapse: separate;
}

.border-spacing-0 {
  --tw-border-spacing-x: 0px;
  --tw-border-spacing-y: 0px;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-0.5 {
  --tw-border-spacing-x: 0.125rem;
  --tw-border-spacing-y: 0.125rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-1 {
  --tw-border-spacing-x: 0.25rem;
  --tw-border-spacing-y: 0.25rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-1.5 {
  --tw-border-spacing-x: 0.375rem;
  --tw-border-spacing-y: 0.375rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-10 {
  --tw-border-spacing-x: 2.5rem;
  --tw-border-spacing-y: 2.5rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-11 {
  --tw-border-spacing-x: 2.75rem;
  --tw-border-spacing-y: 2.75rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-12 {
  --tw-border-spacing-x: 3rem;
  --tw-border-spacing-y: 3rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-14 {
  --tw-border-spacing-x: 3.5rem;
  --tw-border-spacing-y: 3.5rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-16 {
  --tw-border-spacing-x: 4rem;
  --tw-border-spacing-y: 4rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-2 {
  --tw-border-spacing-x: 0.5rem;
  --tw-border-spacing-y: 0.5rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-2.5 {
  --tw-border-spacing-x: 0.625rem;
  --tw-border-spacing-y: 0.625rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-20 {
  --tw-border-spacing-x: 5rem;
  --tw-border-spacing-y: 5rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-24 {
  --tw-border-spacing-x: 6rem;
  --tw-border-spacing-y: 6rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-28 {
  --tw-border-spacing-x: 7rem;
  --tw-border-spacing-y: 7rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-3 {
  --tw-border-spacing-x: 0.75rem;
  --tw-border-spacing-y: 0.75rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-3.5 {
  --tw-border-spacing-x: 0.875rem;
  --tw-border-spacing-y: 0.875rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-32 {
  --tw-border-spacing-x: 8rem;
  --tw-border-spacing-y: 8rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-36 {
  --tw-border-spacing-x: 9rem;
  --tw-border-spacing-y: 9rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-4 {
  --tw-border-spacing-x: 1rem;
  --tw-border-spacing-y: 1rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-40 {
  --tw-border-spacing-x: 10rem;
  --tw-border-spacing-y: 10rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-44 {
  --tw-border-spacing-x: 11rem;
  --tw-border-spacing-y: 11rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-48 {
  --tw-border-spacing-x: 12rem;
  --tw-border-spacing-y: 12rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-5 {
  --tw-border-spacing-x: 1.25rem;
  --tw-border-spacing-y: 1.25rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-52 {
  --tw-border-spacing-x: 13rem;
  --tw-border-spacing-y: 13rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-56 {
  --tw-border-spacing-x: 14rem;
  --tw-border-spacing-y: 14rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-6 {
  --tw-border-spacing-x: 1.5rem;
  --tw-border-spacing-y: 1.5rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-60 {
  --tw-border-spacing-x: 15rem;
  --tw-border-spacing-y: 15rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-64 {
  --tw-border-spacing-x: 16rem;
  --tw-border-spacing-y: 16rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-7 {
  --tw-border-spacing-x: 1.75rem;
  --tw-border-spacing-y: 1.75rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-72 {
  --tw-border-spacing-x: 18rem;
  --tw-border-spacing-y: 18rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-8 {
  --tw-border-spacing-x: 2rem;
  --tw-border-spacing-y: 2rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-80 {
  --tw-border-spacing-x: 20rem;
  --tw-border-spacing-y: 20rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-9 {
  --tw-border-spacing-x: 2.25rem;
  --tw-border-spacing-y: 2.25rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-96 {
  --tw-border-spacing-x: 24rem;
  --tw-border-spacing-y: 24rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-px {
  --tw-border-spacing-x: 1px;
  --tw-border-spacing-y: 1px;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-0 {
  --tw-border-spacing-x: 0px;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-0.5 {
  --tw-border-spacing-x: 0.125rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-1 {
  --tw-border-spacing-x: 0.25rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-1.5 {
  --tw-border-spacing-x: 0.375rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-10 {
  --tw-border-spacing-x: 2.5rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-11 {
  --tw-border-spacing-x: 2.75rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-12 {
  --tw-border-spacing-x: 3rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-14 {
  --tw-border-spacing-x: 3.5rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-16 {
  --tw-border-spacing-x: 4rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-2 {
  --tw-border-spacing-x: 0.5rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-2.5 {
  --tw-border-spacing-x: 0.625rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-20 {
  --tw-border-spacing-x: 5rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-24 {
  --tw-border-spacing-x: 6rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-28 {
  --tw-border-spacing-x: 7rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-3 {
  --tw-border-spacing-x: 0.75rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-3.5 {
  --tw-border-spacing-x: 0.875rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-32 {
  --tw-border-spacing-x: 8rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-36 {
  --tw-border-spacing-x: 9rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-4 {
  --tw-border-spacing-x: 1rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-40 {
  --tw-border-spacing-x: 10rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-44 {
  --tw-border-spacing-x: 11rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-48 {
  --tw-border-spacing-x: 12rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-5 {
  --tw-border-spacing-x: 1.25rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-52 {
  --tw-border-spacing-x: 13rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-56 {
  --tw-border-spacing-x: 14rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-6 {
  --tw-border-spacing-x: 1.5rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-60 {
  --tw-border-spacing-x: 15rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-64 {
  --tw-border-spacing-x: 16rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-7 {
  --tw-border-spacing-x: 1.75rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-72 {
  --tw-border-spacing-x: 18rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-8 {
  --tw-border-spacing-x: 2rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-80 {
  --tw-border-spacing-x: 20rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-9 {
  --tw-border-spacing-x: 2.25rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-96 {
  --tw-border-spacing-x: 24rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-x-px {
  --tw-border-spacing-x: 1px;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-0 {
  --tw-border-spacing-y: 0px;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-0.5 {
  --tw-border-spacing-y: 0.125rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-1 {
  --tw-border-spacing-y: 0.25rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-1.5 {
  --tw-border-spacing-y: 0.375rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-10 {
  --tw-border-spacing-y: 2.5rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-11 {
  --tw-border-spacing-y: 2.75rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-12 {
  --tw-border-spacing-y: 3rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-14 {
  --tw-border-spacing-y: 3.5rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-16 {
  --tw-border-spacing-y: 4rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-2 {
  --tw-border-spacing-y: 0.5rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-2.5 {
  --tw-border-spacing-y: 0.625rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-20 {
  --tw-border-spacing-y: 5rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-24 {
  --tw-border-spacing-y: 6rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-28 {
  --tw-border-spacing-y: 7rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-3 {
  --tw-border-spacing-y: 0.75rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-3.5 {
  --tw-border-spacing-y: 0.875rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-32 {
  --tw-border-spacing-y: 8rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-36 {
  --tw-border-spacing-y: 9rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-4 {
  --tw-border-spacing-y: 1rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-40 {
  --tw-border-spacing-y: 10rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-44 {
  --tw-border-spacing-y: 11rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-48 {
  --tw-border-spacing-y: 12rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-5 {
  --tw-border-spacing-y: 1.25rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-52 {
  --tw-border-spacing-y: 13rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-56 {
  --tw-border-spacing-y: 14rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-6 {
  --tw-border-spacing-y: 1.5rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-60 {
  --tw-border-spacing-y: 15rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-64 {
  --tw-border-spacing-y: 16rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-7 {
  --tw-border-spacing-y: 1.75rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-72 {
  --tw-border-spacing-y: 18rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-8 {
  --tw-border-spacing-y: 2rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-80 {
  --tw-border-spacing-y: 20rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-9 {
  --tw-border-spacing-y: 2.25rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-96 {
  --tw-border-spacing-y: 24rem;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.border-spacing-y-px {
  --tw-border-spacing-y: 1px;
  border-spacing: var(--tw-border-spacing-x) var(--tw-border-spacing-y);
}

.origin-bottom {
  transform-origin: bottom;
}

.origin-bottom-left {
  transform-origin: bottom left;
}

.origin-bottom-right {
  transform-origin: bottom right;
}

.origin-center {
  transform-origin: center;
}

.origin-left {
  transform-origin: left;
}

.origin-right {
  transform-origin: right;
}

.origin-top {
  transform-origin: top;
}

.origin-top-left {
  transform-origin: top left;
}

.origin-top-right {
  transform-origin: top right;
}

.-translate-x-0 {
  --tw-translate-x: -0px;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-0.5 {
  --tw-translate-x: -0.125rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-1 {
  --tw-translate-x: -0.25rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-1.5 {
  --tw-translate-x: -0.375rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-1/2 {
  --tw-translate-x: -50%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-1/3 {
  --tw-translate-x: -33.333333%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-1/4 {
  --tw-translate-x: -25%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-10 {
  --tw-translate-x: -2.5rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-11 {
  --tw-translate-x: -2.75rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-12 {
  --tw-translate-x: -3rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-14 {
  --tw-translate-x: -3.5rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-16 {
  --tw-translate-x: -4rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-2 {
  --tw-translate-x: -0.5rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-2.5 {
  --tw-translate-x: -0.625rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-2/3 {
  --tw-translate-x: -66.666667%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-2/4 {
  --tw-translate-x: -50%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-20 {
  --tw-translate-x: -5rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-24 {
  --tw-translate-x: -6rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-28 {
  --tw-translate-x: -7rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-3 {
  --tw-translate-x: -0.75rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-3.5 {
  --tw-translate-x: -0.875rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-3/4 {
  --tw-translate-x: -75%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-32 {
  --tw-translate-x: -8rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-36 {
  --tw-translate-x: -9rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-4 {
  --tw-translate-x: -1rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-40 {
  --tw-translate-x: -10rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-44 {
  --tw-translate-x: -11rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-48 {
  --tw-translate-x: -12rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-5 {
  --tw-translate-x: -1.25rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-52 {
  --tw-translate-x: -13rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-56 {
  --tw-translate-x: -14rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-6 {
  --tw-translate-x: -1.5rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-60 {
  --tw-translate-x: -15rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-64 {
  --tw-translate-x: -16rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-7 {
  --tw-translate-x: -1.75rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-72 {
  --tw-translate-x: -18rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-8 {
  --tw-translate-x: -2rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-80 {
  --tw-translate-x: -20rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-9 {
  --tw-translate-x: -2.25rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-96 {
  --tw-translate-x: -24rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-full {
  --tw-translate-x: -100%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-x-px {
  --tw-translate-x: -1px;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-0 {
  --tw-translate-y: -0px;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-0.5 {
  --tw-translate-y: -0.125rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-1 {
  --tw-translate-y: -0.25rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-1.5 {
  --tw-translate-y: -0.375rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-1/2 {
  --tw-translate-y: -50%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-1/3 {
  --tw-translate-y: -33.333333%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-1/4 {
  --tw-translate-y: -25%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-10 {
  --tw-translate-y: -2.5rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-11 {
  --tw-translate-y: -2.75rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-12 {
  --tw-translate-y: -3rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-14 {
  --tw-translate-y: -3.5rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-16 {
  --tw-translate-y: -4rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-2 {
  --tw-translate-y: -0.5rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-2.5 {
  --tw-translate-y: -0.625rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-2/3 {
  --tw-translate-y: -66.666667%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-2/4 {
  --tw-translate-y: -50%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-20 {
  --tw-translate-y: -5rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-24 {
  --tw-translate-y: -6rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-28 {
  --tw-translate-y: -7rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-3 {
  --tw-translate-y: -0.75rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-3.5 {
  --tw-translate-y: -0.875rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-3/4 {
  --tw-translate-y: -75%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-32 {
  --tw-translate-y: -8rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-36 {
  --tw-translate-y: -9rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-4 {
  --tw-translate-y: -1rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-40 {
  --tw-translate-y: -10rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-44 {
  --tw-translate-y: -11rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-48 {
  --tw-translate-y: -12rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-5 {
  --tw-translate-y: -1.25rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-52 {
  --tw-translate-y: -13rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-56 {
  --tw-translate-y: -14rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-6 {
  --tw-translate-y: -1.5rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-60 {
  --tw-translate-y: -15rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-64 {
  --tw-translate-y: -16rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-7 {
  --tw-translate-y: -1.75rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-72 {
  --tw-translate-y: -18rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-8 {
  --tw-translate-y: -2rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-80 {
  --tw-translate-y: -20rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-9 {
  --tw-translate-y: -2.25rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-96 {
  --tw-translate-y: -24rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-full {
  --tw-translate-y: -100%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-translate-y-px {
  --tw-translate-y: -1px;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-0 {
  --tw-translate-x: 0px;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-0.5 {
  --tw-translate-x: 0.125rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-1 {
  --tw-translate-x: 0.25rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-1.5 {
  --tw-translate-x: 0.375rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-1/2 {
  --tw-translate-x: 50%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-1/3 {
  --tw-translate-x: 33.333333%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-1/4 {
  --tw-translate-x: 25%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-10 {
  --tw-translate-x: 2.5rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-11 {
  --tw-translate-x: 2.75rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-12 {
  --tw-translate-x: 3rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-14 {
  --tw-translate-x: 3.5rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-16 {
  --tw-translate-x: 4rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-2 {
  --tw-translate-x: 0.5rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-2.5 {
  --tw-translate-x: 0.625rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-2/3 {
  --tw-translate-x: 66.666667%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-2/4 {
  --tw-translate-x: 50%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-20 {
  --tw-translate-x: 5rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-24 {
  --tw-translate-x: 6rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-28 {
  --tw-translate-x: 7rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-3 {
  --tw-translate-x: 0.75rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-3.5 {
  --tw-translate-x: 0.875rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-3/4 {
  --tw-translate-x: 75%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-32 {
  --tw-translate-x: 8rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-36 {
  --tw-translate-x: 9rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-4 {
  --tw-translate-x: 1rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-40 {
  --tw-translate-x: 10rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-44 {
  --tw-translate-x: 11rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-48 {
  --tw-translate-x: 12rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-5 {
  --tw-translate-x: 1.25rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-52 {
  --tw-translate-x: 13rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-56 {
  --tw-translate-x: 14rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-6 {
  --tw-translate-x: 1.5rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-60 {
  --tw-translate-x: 15rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-64 {
  --tw-translate-x: 16rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-7 {
  --tw-translate-x: 1.75rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-72 {
  --tw-translate-x: 18rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-8 {
  --tw-translate-x: 2rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-80 {
  --tw-translate-x: 20rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-9 {
  --tw-translate-x: 2.25rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-96 {
  --tw-translate-x: 24rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-full {
  --tw-translate-x: 100%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-x-px {
  --tw-translate-x: 1px;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-0 {
  --tw-translate-y: 0px;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-0.5 {
  --tw-translate-y: 0.125rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-1 {
  --tw-translate-y: 0.25rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-1.5 {
  --tw-translate-y: 0.375rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-1/2 {
  --tw-translate-y: 50%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-1/3 {
  --tw-translate-y: 33.333333%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-1/4 {
  --tw-translate-y: 25%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-10 {
  --tw-translate-y: 2.5rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-11 {
  --tw-translate-y: 2.75rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-12 {
  --tw-translate-y: 3rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-14 {
  --tw-translate-y: 3.5rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-16 {
  --tw-translate-y: 4rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-2 {
  --tw-translate-y: 0.5rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-2.5 {
  --tw-translate-y: 0.625rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-2/3 {
  --tw-translate-y: 66.666667%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-2/4 {
  --tw-translate-y: 50%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-20 {
  --tw-translate-y: 5rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-24 {
  --tw-translate-y: 6rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-28 {
  --tw-translate-y: 7rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-3 {
  --tw-translate-y: 0.75rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-3.5 {
  --tw-translate-y: 0.875rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-3/4 {
  --tw-translate-y: 75%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-32 {
  --tw-translate-y: 8rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-36 {
  --tw-translate-y: 9rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-4 {
  --tw-translate-y: 1rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-40 {
  --tw-translate-y: 10rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-44 {
  --tw-translate-y: 11rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-48 {
  --tw-translate-y: 12rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-5 {
  --tw-translate-y: 1.25rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-52 {
  --tw-translate-y: 13rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-56 {
  --tw-translate-y: 14rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-6 {
  --tw-translate-y: 1.5rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-60 {
  --tw-translate-y: 15rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-64 {
  --tw-translate-y: 16rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-7 {
  --tw-translate-y: 1.75rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-72 {
  --tw-translate-y: 18rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-8 {
  --tw-translate-y: 2rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-80 {
  --tw-translate-y: 20rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-9 {
  --tw-translate-y: 2.25rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-96 {
  --tw-translate-y: 24rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-full {
  --tw-translate-y: 100%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.translate-y-px {
  --tw-translate-y: 1px;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-rotate-0 {
  --tw-rotate: -0deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-rotate-1 {
  --tw-rotate: -1deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-rotate-12 {
  --tw-rotate: -12deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-rotate-180 {
  --tw-rotate: -180deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-rotate-2 {
  --tw-rotate: -2deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-rotate-3 {
  --tw-rotate: -3deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-rotate-45 {
  --tw-rotate: -45deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-rotate-6 {
  --tw-rotate: -6deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-rotate-90 {
  --tw-rotate: -90deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.rotate-0 {
  --tw-rotate: 0deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.rotate-1 {
  --tw-rotate: 1deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.rotate-12 {
  --tw-rotate: 12deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.rotate-180 {
  --tw-rotate: 180deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.rotate-2 {
  --tw-rotate: 2deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.rotate-3 {
  --tw-rotate: 3deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.rotate-45 {
  --tw-rotate: 45deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.rotate-6 {
  --tw-rotate: 6deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.rotate-90 {
  --tw-rotate: 90deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-skew-x-0 {
  --tw-skew-x: -0deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-skew-x-1 {
  --tw-skew-x: -1deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-skew-x-12 {
  --tw-skew-x: -12deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-skew-x-2 {
  --tw-skew-x: -2deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-skew-x-3 {
  --tw-skew-x: -3deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-skew-x-6 {
  --tw-skew-x: -6deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-skew-y-0 {
  --tw-skew-y: -0deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-skew-y-1 {
  --tw-skew-y: -1deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-skew-y-12 {
  --tw-skew-y: -12deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-skew-y-2 {
  --tw-skew-y: -2deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-skew-y-3 {
  --tw-skew-y: -3deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-skew-y-6 {
  --tw-skew-y: -6deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.skew-x-0 {
  --tw-skew-x: 0deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.skew-x-1 {
  --tw-skew-x: 1deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.skew-x-12 {
  --tw-skew-x: 12deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.skew-x-2 {
  --tw-skew-x: 2deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.skew-x-3 {
  --tw-skew-x: 3deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.skew-x-6 {
  --tw-skew-x: 6deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.skew-y-0 {
  --tw-skew-y: 0deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.skew-y-1 {
  --tw-skew-y: 1deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.skew-y-12 {
  --tw-skew-y: 12deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.skew-y-2 {
  --tw-skew-y: 2deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.skew-y-3 {
  --tw-skew-y: 3deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.skew-y-6 {
  --tw-skew-y: 6deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-0 {
  --tw-scale-x: 0;
  --tw-scale-y: 0;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-100 {
  --tw-scale-x: -1;
  --tw-scale-y: -1;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-105 {
  --tw-scale-x: -1.05;
  --tw-scale-y: -1.05;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-110 {
  --tw-scale-x: -1.1;
  --tw-scale-y: -1.1;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-125 {
  --tw-scale-x: -1.25;
  --tw-scale-y: -1.25;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-150 {
  --tw-scale-x: -1.5;
  --tw-scale-y: -1.5;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-50 {
  --tw-scale-x: -.5;
  --tw-scale-y: -.5;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-75 {
  --tw-scale-x: -.75;
  --tw-scale-y: -.75;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-90 {
  --tw-scale-x: -.9;
  --tw-scale-y: -.9;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-95 {
  --tw-scale-x: -.95;
  --tw-scale-y: -.95;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-0 {
  --tw-scale-x: 0;
  --tw-scale-y: 0;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-100 {
  --tw-scale-x: 1;
  --tw-scale-y: 1;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-105 {
  --tw-scale-x: 1.05;
  --tw-scale-y: 1.05;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-110 {
  --tw-scale-x: 1.1;
  --tw-scale-y: 1.1;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-125 {
  --tw-scale-x: 1.25;
  --tw-scale-y: 1.25;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-150 {
  --tw-scale-x: 1.5;
  --tw-scale-y: 1.5;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-50 {
  --tw-scale-x: .5;
  --tw-scale-y: .5;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-75 {
  --tw-scale-x: .75;
  --tw-scale-y: .75;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-90 {
  --tw-scale-x: .9;
  --tw-scale-y: .9;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-95 {
  --tw-scale-x: .95;
  --tw-scale-y: .95;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-x-0 {
  --tw-scale-x: 0;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-x-100 {
  --tw-scale-x: -1;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-x-105 {
  --tw-scale-x: -1.05;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-x-110 {
  --tw-scale-x: -1.1;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-x-125 {
  --tw-scale-x: -1.25;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-x-150 {
  --tw-scale-x: -1.5;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-x-50 {
  --tw-scale-x: -.5;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-x-75 {
  --tw-scale-x: -.75;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-x-90 {
  --tw-scale-x: -.9;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-x-95 {
  --tw-scale-x: -.95;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-y-0 {
  --tw-scale-y: 0;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-y-100 {
  --tw-scale-y: -1;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-y-105 {
  --tw-scale-y: -1.05;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-y-110 {
  --tw-scale-y: -1.1;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-y-125 {
  --tw-scale-y: -1.25;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-y-150 {
  --tw-scale-y: -1.5;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-y-50 {
  --tw-scale-y: -.5;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-y-75 {
  --tw-scale-y: -.75;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-y-90 {
  --tw-scale-y: -.9;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-scale-y-95 {
  --tw-scale-y: -.95;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-x-0 {
  --tw-scale-x: 0;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-x-100 {
  --tw-scale-x: 1;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-x-105 {
  --tw-scale-x: 1.05;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-x-110 {
  --tw-scale-x: 1.1;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-x-125 {
  --tw-scale-x: 1.25;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-x-150 {
  --tw-scale-x: 1.5;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-x-50 {
  --tw-scale-x: .5;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-x-75 {
  --tw-scale-x: .75;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-x-90 {
  --tw-scale-x: .9;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-x-95 {
  --tw-scale-x: .95;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-y-0 {
  --tw-scale-y: 0;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-y-100 {
  --tw-scale-y: 1;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-y-105 {
  --tw-scale-y: 1.05;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-y-110 {
  --tw-scale-y: 1.1;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-y-125 {
  --tw-scale-y: 1.25;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-y-150 {
  --tw-scale-y: 1.5;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-y-50 {
  --tw-scale-y: .5;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-y-75 {
  --tw-scale-y: .75;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-y-90 {
  --tw-scale-y: .9;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.scale-y-95 {
  --tw-scale-y: .95;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

@keyframes bounce {
  0%, 100% {
    transform: translateY(-25%);
    animation-timing-function: cubic-bezier(0.8,0,1,1);
  }

  50% {
    transform: none;
    animation-timing-function: cubic-bezier(0,0,0.2,1);
  }
}

.animate-bounce {
  animation: bounce 1s infinite;
}

.animate-none {
  animation: none;
}

@keyframes ping {
  75%, 100% {
    transform: scale(2);
    opacity: 0;
  }
}

.animate-ping {
  animation: ping 1s cubic-bezier(0, 0, 0.2, 1) infinite;
}

@keyframes pulse {
  50% {
    opacity: .5;
  }
}

.animate-pulse {
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.animate-spin {
  animation: spin 1s linear infinite;
}

.cursor-alias {
  cursor: alias;
}

.cursor-all-scroll {
  cursor: all-scroll;
}

.cursor-auto {
  cursor: auto;
}

.cursor-cell {
  cursor: cell;
}

.cursor-col-resize {
  cursor: col-resize;
}

.cursor-context-menu {
  cursor: context-menu;
}

.cursor-copy {
  cursor: copy;
}

.cursor-crosshair {
  cursor: crosshair;
}

.cursor-default {
  cursor: default;
}

.cursor-e-resize {
  cursor: e-resize;
}

.cursor-ew-resize {
  cursor: ew-resize;
}

.cursor-grab {
  cursor: grab;
}

.cursor-grabbing {
  cursor: grabbing;
}

.cursor-help {
  cursor: help;
}

.cursor-move {
  cursor: move;
}

.cursor-n-resize {
  cursor: n-resize;
}

.cursor-ne-resize {
  cursor: ne-resize;
}

.cursor-nesw-resize {
  cursor: nesw-resize;
}

.cursor-no-drop {
  cursor: no-drop;
}

.cursor-none {
  cursor: none;
}

.cursor-not-allowed {
  cursor: not-allowed;
}

.cursor-ns-resize {
  cursor: ns-resize;
}

.cursor-nw-resize {
  cursor: nw-resize;
}

.cursor-nwse-resize {
  cursor: nwse-resize;
}

.cursor-pointer {
  cursor: pointer;
}

.cursor-progress {
  cursor: progress;
}

.cursor-row-resize {
  cursor: row-resize;
}

.cursor-s-resize {
  cursor: s-resize;
}

.cursor-se-resize {
  cursor: se-resize;
}

.cursor-sw-resize {
  cursor: sw-resize;
}

.cursor-text {
  cursor: text;
}

.cursor-vertical-text {
  cursor: vertical-text;
}

.cursor-w-resize {
  cursor: w-resize;
}

.cursor-wait {
  cursor: wait;
}

.cursor-zoom-in {
  cursor: zoom-in;
}

.cursor-zoom-out {
  cursor: zoom-out;
}

.touch-auto {
  touch-action: auto;
}

.touch-none {
  touch-action: none;
}

.touch-pan-x {
  --tw-pan-x: pan-x;
  touch-action: var(--tw-pan-x) var(--tw-pan-y) var(--tw-pinch-zoom);
}

.touch-pan-left {
  --tw-pan-x: pan-left;
  touch-action: var(--tw-pan-x) var(--tw-pan-y) var(--tw-pinch-zoom);
}

.touch-pan-right {
  --tw-pan-x: pan-right;
  touch-action: var(--tw-pan-x) var(--tw-pan-y) var(--tw-pinch-zoom);
}

.touch-pan-y {
  --tw-pan-y: pan-y;
  touch-action: var(--tw-pan-x) var(--tw-pan-y) var(--tw-pinch-zoom);
}

.touch-pan-up {
  --tw-pan-y: pan-up;
  touch-action: var(--tw-pan-x) var(--tw-pan-y) var(--tw-pinch-zoom);
}

.touch-pan-down {
  --tw-pan-y: pan-down;
  touch-action: var(--tw-pan-x) var(--tw-pan-y) var(--tw-pinch-zoom);
}

.touch-pinch-zoom {
  --tw-pinch-zoom: pinch-zoom;
  touch-action: var(--tw-pan-x) var(--tw-pan-y) var(--tw-pinch-zoom);
}

.touch-manipulation {
  touch-action: manipulation;
}

.select-none {
  -webkit-user-select: none;
     -moz-user-select: none;
          user-select: none;
}

.select-text {
  -webkit-user-select: text;
     -moz-user-select: text;
          user-select: text;
}

.select-all {
  -webkit-user-select: all;
     -moz-user-select: all;
          user-select: all;
}

.select-auto {
  -webkit-user-select: auto;
     -moz-user-select: auto;
          user-select: auto;
}

.resize-none {
  resize: none;
}

.resize-y {
  resize: vertical;
}

.resize-x {
  resize: horizontal;
}

.resize {
  resize: both;
}

.snap-none {
  scroll-snap-type: none;
}

.snap-x {
  scroll-snap-type: x var(--tw-scroll-snap-strictness);
}

.snap-y {
  scroll-snap-type: y var(--tw-scroll-snap-strictness);
}

.snap-both {
  scroll-snap-type: both var(--tw-scroll-snap-strictness);
}

.snap-mandatory {
  --tw-scroll-snap-strictness: mandatory;
}

.snap-proximity {
  --tw-scroll-snap-strictness: proximity;
}

.snap-start {
  scroll-snap-align: start;
}

.snap-end {
  scroll-snap-align: end;
}

.snap-center {
  scroll-snap-align: center;
}

.snap-align-none {
  scroll-snap-align: none;
}

.snap-normal {
  scroll-snap-stop: normal;
}

.snap-always {
  scroll-snap-stop: always;
}

.-scroll-m-0 {
  scroll-margin: -0px;
}

.-scroll-m-0.5 {
  scroll-margin: -0.125rem;
}

.-scroll-m-1 {
  scroll-margin: -0.25rem;
}

.-scroll-m-1.5 {
  scroll-margin: -0.375rem;
}

.-scroll-m-10 {
  scroll-margin: -2.5rem;
}

.-scroll-m-11 {
  scroll-margin: -2.75rem;
}

.-scroll-m-12 {
  scroll-margin: -3rem;
}

.-scroll-m-14 {
  scroll-margin: -3.5rem;
}

.-scroll-m-16 {
  scroll-margin: -4rem;
}

.-scroll-m-2 {
  scroll-margin: -0.5rem;
}

.-scroll-m-2.5 {
  scroll-margin: -0.625rem;
}

.-scroll-m-20 {
  scroll-margin: -5rem;
}

.-scroll-m-24 {
  scroll-margin: -6rem;
}

.-scroll-m-28 {
  scroll-margin: -7rem;
}

.-scroll-m-3 {
  scroll-margin: -0.75rem;
}

.-scroll-m-3.5 {
  scroll-margin: -0.875rem;
}

.-scroll-m-32 {
  scroll-margin: -8rem;
}

.-scroll-m-36 {
  scroll-margin: -9rem;
}

.-scroll-m-4 {
  scroll-margin: -1rem;
}

.-scroll-m-40 {
  scroll-margin: -10rem;
}

.-scroll-m-44 {
  scroll-margin: -11rem;
}

.-scroll-m-48 {
  scroll-margin: -12rem;
}

.-scroll-m-5 {
  scroll-margin: -1.25rem;
}

.-scroll-m-52 {
  scroll-margin: -13rem;
}

.-scroll-m-56 {
  scroll-margin: -14rem;
}

.-scroll-m-6 {
  scroll-margin: -1.5rem;
}

.-scroll-m-60 {
  scroll-margin: -15rem;
}

.-scroll-m-64 {
  scroll-margin: -16rem;
}

.-scroll-m-7 {
  scroll-margin: -1.75rem;
}

.-scroll-m-72 {
  scroll-margin: -18rem;
}

.-scroll-m-8 {
  scroll-margin: -2rem;
}

.-scroll-m-80 {
  scroll-margin: -20rem;
}

.-scroll-m-9 {
  scroll-margin: -2.25rem;
}

.-scroll-m-96 {
  scroll-margin: -24rem;
}

.-scroll-m-px {
  scroll-margin: -1px;
}

.scroll-m-0 {
  scroll-margin: 0px;
}

.scroll-m-0.5 {
  scroll-margin: 0.125rem;
}

.scroll-m-1 {
  scroll-margin: 0.25rem;
}

.scroll-m-1.5 {
  scroll-margin: 0.375rem;
}

.scroll-m-10 {
  scroll-margin: 2.5rem;
}

.scroll-m-11 {
  scroll-margin: 2.75rem;
}

.scroll-m-12 {
  scroll-margin: 3rem;
}

.scroll-m-14 {
  scroll-margin: 3.5rem;
}

.scroll-m-16 {
  scroll-margin: 4rem;
}

.scroll-m-2 {
  scroll-margin: 0.5rem;
}

.scroll-m-2.5 {
  scroll-margin: 0.625rem;
}

.scroll-m-20 {
  scroll-margin: 5rem;
}

.scroll-m-24 {
  scroll-margin: 6rem;
}

.scroll-m-28 {
  scroll-margin: 7rem;
}

.scroll-m-3 {
  scroll-margin: 0.75rem;
}

.scroll-m-3.5 {
  scroll-margin: 0.875rem;
}

.scroll-m-32 {
  scroll-margin: 8rem;
}

.scroll-m-36 {
  scroll-margin: 9rem;
}

.scroll-m-4 {
  scroll-margin: 1rem;
}

.scroll-m-40 {
  scroll-margin: 10rem;
}

.scroll-m-44 {
  scroll-margin: 11rem;
}

.scroll-m-48 {
  scroll-margin: 12rem;
}

.scroll-m-5 {
  scroll-margin: 1.25rem;
}

.scroll-m-52 {
  scroll-margin: 13rem;
}

.scroll-m-56 {
  scroll-margin: 14rem;
}

.scroll-m-6 {
  scroll-margin: 1.5rem;
}

.scroll-m-60 {
  scroll-margin: 15rem;
}

.scroll-m-64 {
  scroll-margin: 16rem;
}

.scroll-m-7 {
  scroll-margin: 1.75rem;
}

.scroll-m-72 {
  scroll-margin: 18rem;
}

.scroll-m-8 {
  scroll-margin: 2rem;
}

.scroll-m-80 {
  scroll-margin: 20rem;
}

.scroll-m-9 {
  scroll-margin: 2.25rem;
}

.scroll-m-96 {
  scroll-margin: 24rem;
}

.scroll-m-px {
  scroll-margin: 1px;
}

.-scroll-mx-0 {
  scroll-margin-left: -0px;
  scroll-margin-right: -0px;
}

.-scroll-mx-0.5 {
  scroll-margin-left: -0.125rem;
  scroll-margin-right: -0.125rem;
}

.-scroll-mx-1 {
  scroll-margin-left: -0.25rem;
  scroll-margin-right: -0.25rem;
}

.-scroll-mx-1.5 {
  scroll-margin-left: -0.375rem;
  scroll-margin-right: -0.375rem;
}

.-scroll-mx-10 {
  scroll-margin-left: -2.5rem;
  scroll-margin-right: -2.5rem;
}

.-scroll-mx-11 {
  scroll-margin-left: -2.75rem;
  scroll-margin-right: -2.75rem;
}

.-scroll-mx-12 {
  scroll-margin-left: -3rem;
  scroll-margin-right: -3rem;
}

.-scroll-mx-14 {
  scroll-margin-left: -3.5rem;
  scroll-margin-right: -3.5rem;
}

.-scroll-mx-16 {
  scroll-margin-left: -4rem;
  scroll-margin-right: -4rem;
}

.-scroll-mx-2 {
  scroll-margin-left: -0.5rem;
  scroll-margin-right: -0.5rem;
}

.-scroll-mx-2.5 {
  scroll-margin-left: -0.625rem;
  scroll-margin-right: -0.625rem;
}

.-scroll-mx-20 {
  scroll-margin-left: -5rem;
  scroll-margin-right: -5rem;
}

.-scroll-mx-24 {
  scroll-margin-left: -6rem;
  scroll-margin-right: -6rem;
}

.-scroll-mx-28 {
  scroll-margin-left: -7rem;
  scroll-margin-right: -7rem;
}

.-scroll-mx-3 {
  scroll-margin-left: -0.75rem;
  scroll-margin-right: -0.75rem;
}

.-scroll-mx-3.5 {
  scroll-margin-left: -0.875rem;
  scroll-margin-right: -0.875rem;
}

.-scroll-mx-32 {
  scroll-margin-left: -8rem;
  scroll-margin-right: -8rem;
}

.-scroll-mx-36 {
  scroll-margin-left: -9rem;
  scroll-margin-right: -9rem;
}

.-scroll-mx-4 {
  scroll-margin-left: -1rem;
  scroll-margin-right: -1rem;
}

.-scroll-mx-40 {
  scroll-margin-left: -10rem;
  scroll-margin-right: -10rem;
}

.-scroll-mx-44 {
  scroll-margin-left: -11rem;
  scroll-margin-right: -11rem;
}

.-scroll-mx-48 {
  scroll-margin-left: -12rem;
  scroll-margin-right: -12rem;
}

.-scroll-mx-5 {
  scroll-margin-left: -1.25rem;
  scroll-margin-right: -1.25rem;
}

.-scroll-mx-52 {
  scroll-margin-left: -13rem;
  scroll-margin-right: -13rem;
}

.-scroll-mx-56 {
  scroll-margin-left: -14rem;
  scroll-margin-right: -14rem;
}

.-scroll-mx-6 {
  scroll-margin-left: -1.5rem;
  scroll-margin-right: -1.5rem;
}

.-scroll-mx-60 {
  scroll-margin-left: -15rem;
  scroll-margin-right: -15rem;
}

.-scroll-mx-64 {
  scroll-margin-left: -16rem;
  scroll-margin-right: -16rem;
}

.-scroll-mx-7 {
  scroll-margin-left: -1.75rem;
  scroll-margin-right: -1.75rem;
}

.-scroll-mx-72 {
  scroll-margin-left: -18rem;
  scroll-margin-right: -18rem;
}

.-scroll-mx-8 {
  scroll-margin-left: -2rem;
  scroll-margin-right: -2rem;
}

.-scroll-mx-80 {
  scroll-margin-left: -20rem;
  scroll-margin-right: -20rem;
}

.-scroll-mx-9 {
  scroll-margin-left: -2.25rem;
  scroll-margin-right: -2.25rem;
}

.-scroll-mx-96 {
  scroll-margin-left: -24rem;
  scroll-margin-right: -24rem;
}

.-scroll-mx-px {
  scroll-margin-left: -1px;
  scroll-margin-right: -1px;
}

.-scroll-my-0 {
  scroll-margin-top: -0px;
  scroll-margin-bottom: -0px;
}

.-scroll-my-0.5 {
  scroll-margin-top: -0.125rem;
  scroll-margin-bottom: -0.125rem;
}

.-scroll-my-1 {
  scroll-margin-top: -0.25rem;
  scroll-margin-bottom: -0.25rem;
}

.-scroll-my-1.5 {
  scroll-margin-top: -0.375rem;
  scroll-margin-bottom: -0.375rem;
}

.-scroll-my-10 {
  scroll-margin-top: -2.5rem;
  scroll-margin-bottom: -2.5rem;
}

.-scroll-my-11 {
  scroll-margin-top: -2.75rem;
  scroll-margin-bottom: -2.75rem;
}

.-scroll-my-12 {
  scroll-margin-top: -3rem;
  scroll-margin-bottom: -3rem;
}

.-scroll-my-14 {
  scroll-margin-top: -3.5rem;
  scroll-margin-bottom: -3.5rem;
}

.-scroll-my-16 {
  scroll-margin-top: -4rem;
  scroll-margin-bottom: -4rem;
}

.-scroll-my-2 {
  scroll-margin-top: -0.5rem;
  scroll-margin-bottom: -0.5rem;
}

.-scroll-my-2.5 {
  scroll-margin-top: -0.625rem;
  scroll-margin-bottom: -0.625rem;
}

.-scroll-my-20 {
  scroll-margin-top: -5rem;
  scroll-margin-bottom: -5rem;
}

.-scroll-my-24 {
  scroll-margin-top: -6rem;
  scroll-margin-bottom: -6rem;
}

.-scroll-my-28 {
  scroll-margin-top: -7rem;
  scroll-margin-bottom: -7rem;
}

.-scroll-my-3 {
  scroll-margin-top: -0.75rem;
  scroll-margin-bottom: -0.75rem;
}

.-scroll-my-3.5 {
  scroll-margin-top: -0.875rem;
  scroll-margin-bottom: -0.875rem;
}

.-scroll-my-32 {
  scroll-margin-top: -8rem;
  scroll-margin-bottom: -8rem;
}

.-scroll-my-36 {
  scroll-margin-top: -9rem;
  scroll-margin-bottom: -9rem;
}

.-scroll-my-4 {
  scroll-margin-top: -1rem;
  scroll-margin-bottom: -1rem;
}

.-scroll-my-40 {
  scroll-margin-top: -10rem;
  scroll-margin-bottom: -10rem;
}

.-scroll-my-44 {
  scroll-margin-top: -11rem;
  scroll-margin-bottom: -11rem;
}

.-scroll-my-48 {
  scroll-margin-top: -12rem;
  scroll-margin-bottom: -12rem;
}

.-scroll-my-5 {
  scroll-margin-top: -1.25rem;
  scroll-margin-bottom: -1.25rem;
}

.-scroll-my-52 {
  scroll-margin-top: -13rem;
  scroll-margin-bottom: -13rem;
}

.-scroll-my-56 {
  scroll-margin-top: -14rem;
  scroll-margin-bottom: -14rem;
}

.-scroll-my-6 {
  scroll-margin-top: -1.5rem;
  scroll-margin-bottom: -1.5rem;
}

.-scroll-my-60 {
  scroll-margin-top: -15rem;
  scroll-margin-bottom: -15rem;
}

.-scroll-my-64 {
  scroll-margin-top: -16rem;
  scroll-margin-bottom: -16rem;
}

.-scroll-my-7 {
  scroll-margin-top: -1.75rem;
  scroll-margin-bottom: -1.75rem;
}

.-scroll-my-72 {
  scroll-margin-top: -18rem;
  scroll-margin-bottom: -18rem;
}

.-scroll-my-8 {
  scroll-margin-top: -2rem;
  scroll-margin-bottom: -2rem;
}

.-scroll-my-80 {
  scroll-margin-top: -20rem;
  scroll-margin-bottom: -20rem;
}

.-scroll-my-9 {
  scroll-margin-top: -2.25rem;
  scroll-margin-bottom: -2.25rem;
}

.-scroll-my-96 {
  scroll-margin-top: -24rem;
  scroll-margin-bottom: -24rem;
}

.-scroll-my-px {
  scroll-margin-top: -1px;
  scroll-margin-bottom: -1px;
}

.scroll-mx-0 {
  scroll-margin-left: 0px;
  scroll-margin-right: 0px;
}

.scroll-mx-0.5 {
  scroll-margin-left: 0.125rem;
  scroll-margin-right: 0.125rem;
}

.scroll-mx-1 {
  scroll-margin-left: 0.25rem;
  scroll-margin-right: 0.25rem;
}

.scroll-mx-1.5 {
  scroll-margin-left: 0.375rem;
  scroll-margin-right: 0.375rem;
}

.scroll-mx-10 {
  scroll-margin-left: 2.5rem;
  scroll-margin-right: 2.5rem;
}

.scroll-mx-11 {
  scroll-margin-left: 2.75rem;
  scroll-margin-right: 2.75rem;
}

.scroll-mx-12 {
  scroll-margin-left: 3rem;
  scroll-margin-right: 3rem;
}

.scroll-mx-14 {
  scroll-margin-left: 3.5rem;
  scroll-margin-right: 3.5rem;
}

.scroll-mx-16 {
  scroll-margin-left: 4rem;
  scroll-margin-right: 4rem;
}

.scroll-mx-2 {
  scroll-margin-left: 0.5rem;
  scroll-margin-right: 0.5rem;
}

.scroll-mx-2.5 {
  scroll-margin-left: 0.625rem;
  scroll-margin-right: 0.625rem;
}

.scroll-mx-20 {
  scroll-margin-left: 5rem;
  scroll-margin-right: 5rem;
}

.scroll-mx-24 {
  scroll-margin-left: 6rem;
  scroll-margin-right: 6rem;
}

.scroll-mx-28 {
  scroll-margin-left: 7rem;
  scroll-margin-right: 7rem;
}

.scroll-mx-3 {
  scroll-margin-left: 0.75rem;
  scroll-margin-right: 0.75rem;
}

.scroll-mx-3.5 {
  scroll-margin-left: 0.875rem;
  scroll-margin-right: 0.875rem;
}

.scroll-mx-32 {
  scroll-margin-left: 8rem;
  scroll-margin-right: 8rem;
}

.scroll-mx-36 {
  scroll-margin-left: 9rem;
  scroll-margin-right: 9rem;
}

.scroll-mx-4 {
  scroll-margin-left: 1rem;
  scroll-margin-right: 1rem;
}

.scroll-mx-40 {
  scroll-margin-left: 10rem;
  scroll-margin-right: 10rem;
}

.scroll-mx-44 {
  scroll-margin-left: 11rem;
  scroll-margin-right: 11rem;
}

.scroll-mx-48 {
  scroll-margin-left: 12rem;
  scroll-margin-right: 12rem;
}

.scroll-mx-5 {
  scroll-margin-left: 1.25rem;
  scroll-margin-right: 1.25rem;
}

.scroll-mx-52 {
  scroll-margin-left: 13rem;
  scroll-margin-right: 13rem;
}

.scroll-mx-56 {
  scroll-margin-left: 14rem;
  scroll-margin-right: 14rem;
}

.scroll-mx-6 {
  scroll-margin-left: 1.5rem;
  scroll-margin-right: 1.5rem;
}

.scroll-mx-60 {
  scroll-margin-left: 15rem;
  scroll-margin-right: 15rem;
}

.scroll-mx-64 {
  scroll-margin-left: 16rem;
  scroll-margin-right: 16rem;
}

.scroll-mx-7 {
  scroll-margin-left: 1.75rem;
  scroll-margin-right: 1.75rem;
}

.scroll-mx-72 {
  scroll-margin-left: 18rem;
  scroll-margin-right: 18rem;
}

.scroll-mx-8 {
  scroll-margin-left: 2rem;
  scroll-margin-right: 2rem;
}

.scroll-mx-80 {
  scroll-margin-left: 20rem;
  scroll-margin-right: 20rem;
}

.scroll-mx-9 {
  scroll-margin-left: 2.25rem;
  scroll-margin-right: 2.25rem;
}

.scroll-mx-96 {
  scroll-margin-left: 24rem;
  scroll-margin-right: 24rem;
}

.scroll-mx-px {
  scroll-margin-left: 1px;
  scroll-margin-right: 1px;
}

.scroll-my-0 {
  scroll-margin-top: 0px;
  scroll-margin-bottom: 0px;
}

.scroll-my-0.5 {
  scroll-margin-top: 0.125rem;
  scroll-margin-bottom: 0.125rem;
}

.scroll-my-1 {
  scroll-margin-top: 0.25rem;
  scroll-margin-bottom: 0.25rem;
}

.scroll-my-1.5 {
  scroll-margin-top: 0.375rem;
  scroll-margin-bottom: 0.375rem;
}

.scroll-my-10 {
  scroll-margin-top: 2.5rem;
  scroll-margin-bottom: 2.5rem;
}

.scroll-my-11 {
  scroll-margin-top: 2.75rem;
  scroll-margin-bottom: 2.75rem;
}

.scroll-my-12 {
  scroll-margin-top: 3rem;
  scroll-margin-bottom: 3rem;
}

.scroll-my-14 {
  scroll-margin-top: 3.5rem;
  scroll-margin-bottom: 3.5rem;
}

.scroll-my-16 {
  scroll-margin-top: 4rem;
  scroll-margin-bottom: 4rem;
}

.scroll-my-2 {
  scroll-margin-top: 0.5rem;
  scroll-margin-bottom: 0.5rem;
}

.scroll-my-2.5 {
  scroll-margin-top: 0.625rem;
  scroll-margin-bottom: 0.625rem;
}

.scroll-my-20 {
  scroll-margin-top: 5rem;
  scroll-margin-bottom: 5rem;
}

.scroll-my-24 {
  scroll-margin-top: 6rem;
  scroll-margin-bottom: 6rem;
}

.scroll-my-28 {
  scroll-margin-top: 7rem;
  scroll-margin-bottom: 7rem;
}

.scroll-my-3 {
  scroll-margin-top: 0.75rem;
  scroll-margin-bottom: 0.75rem;
}

.scroll-my-3.5 {
  scroll-margin-top: 0.875rem;
  scroll-margin-bottom: 0.875rem;
}

.scroll-my-32 {
  scroll-margin-top: 8rem;
  scroll-margin-bottom: 8rem;
}

.scroll-my-36 {
  scroll-margin-top: 9rem;
  scroll-margin-bottom: 9rem;
}

.scroll-my-4 {
  scroll-margin-top: 1rem;
  scroll-margin-bottom: 1rem;
}

.scroll-my-40 {
  scroll-margin-top: 10rem;
  scroll-margin-bottom: 10rem;
}

.scroll-my-44 {
  scroll-margin-top: 11rem;
  scroll-margin-bottom: 11rem;
}

.scroll-my-48 {
  scroll-margin-top: 12rem;
  scroll-margin-bottom: 12rem;
}

.scroll-my-5 {
  scroll-margin-top: 1.25rem;
  scroll-margin-bottom: 1.25rem;
}

.scroll-my-52 {
  scroll-margin-top: 13rem;
  scroll-margin-bottom: 13rem;
}

.scroll-my-56 {
  scroll-margin-top: 14rem;
  scroll-margin-bottom: 14rem;
}

.scroll-my-6 {
  scroll-margin-top: 1.5rem;
  scroll-margin-bottom: 1.5rem;
}

.scroll-my-60 {
  scroll-margin-top: 15rem;
  scroll-margin-bottom: 15rem;
}

.scroll-my-64 {
  scroll-margin-top: 16rem;
  scroll-margin-bottom: 16rem;
}

.scroll-my-7 {
  scroll-margin-top: 1.75rem;
  scroll-margin-bottom: 1.75rem;
}

.scroll-my-72 {
  scroll-margin-top: 18rem;
  scroll-margin-bottom: 18rem;
}

.scroll-my-8 {
  scroll-margin-top: 2rem;
  scroll-margin-bottom: 2rem;
}

.scroll-my-80 {
  scroll-margin-top: 20rem;
  scroll-margin-bottom: 20rem;
}

.scroll-my-9 {
  scroll-margin-top: 2.25rem;
  scroll-margin-bottom: 2.25rem;
}

.scroll-my-96 {
  scroll-margin-top: 24rem;
  scroll-margin-bottom: 24rem;
}

.scroll-my-px {
  scroll-margin-top: 1px;
  scroll-margin-bottom: 1px;
}

.-scroll-mb-0 {
  scroll-margin-bottom: -0px;
}

.-scroll-mb-0.5 {
  scroll-margin-bottom: -0.125rem;
}

.-scroll-mb-1 {
  scroll-margin-bottom: -0.25rem;
}

.-scroll-mb-1.5 {
  scroll-margin-bottom: -0.375rem;
}

.-scroll-mb-10 {
  scroll-margin-bottom: -2.5rem;
}

.-scroll-mb-11 {
  scroll-margin-bottom: -2.75rem;
}

.-scroll-mb-12 {
  scroll-margin-bottom: -3rem;
}

.-scroll-mb-14 {
  scroll-margin-bottom: -3.5rem;
}

.-scroll-mb-16 {
  scroll-margin-bottom: -4rem;
}

.-scroll-mb-2 {
  scroll-margin-bottom: -0.5rem;
}

.-scroll-mb-2.5 {
  scroll-margin-bottom: -0.625rem;
}

.-scroll-mb-20 {
  scroll-margin-bottom: -5rem;
}

.-scroll-mb-24 {
  scroll-margin-bottom: -6rem;
}

.-scroll-mb-28 {
  scroll-margin-bottom: -7rem;
}

.-scroll-mb-3 {
  scroll-margin-bottom: -0.75rem;
}

.-scroll-mb-3.5 {
  scroll-margin-bottom: -0.875rem;
}

.-scroll-mb-32 {
  scroll-margin-bottom: -8rem;
}

.-scroll-mb-36 {
  scroll-margin-bottom: -9rem;
}

.-scroll-mb-4 {
  scroll-margin-bottom: -1rem;
}

.-scroll-mb-40 {
  scroll-margin-bottom: -10rem;
}

.-scroll-mb-44 {
  scroll-margin-bottom: -11rem;
}

.-scroll-mb-48 {
  scroll-margin-bottom: -12rem;
}

.-scroll-mb-5 {
  scroll-margin-bottom: -1.25rem;
}

.-scroll-mb-52 {
  scroll-margin-bottom: -13rem;
}

.-scroll-mb-56 {
  scroll-margin-bottom: -14rem;
}

.-scroll-mb-6 {
  scroll-margin-bottom: -1.5rem;
}

.-scroll-mb-60 {
  scroll-margin-bottom: -15rem;
}

.-scroll-mb-64 {
  scroll-margin-bottom: -16rem;
}

.-scroll-mb-7 {
  scroll-margin-bottom: -1.75rem;
}

.-scroll-mb-72 {
  scroll-margin-bottom: -18rem;
}

.-scroll-mb-8 {
  scroll-margin-bottom: -2rem;
}

.-scroll-mb-80 {
  scroll-margin-bottom: -20rem;
}

.-scroll-mb-9 {
  scroll-margin-bottom: -2.25rem;
}

.-scroll-mb-96 {
  scroll-margin-bottom: -24rem;
}

.-scroll-mb-px {
  scroll-margin-bottom: -1px;
}

.-scroll-me-0 {
  scroll-margin-inline-end: -0px;
}

.-scroll-me-0.5 {
  scroll-margin-inline-end: -0.125rem;
}

.-scroll-me-1 {
  scroll-margin-inline-end: -0.25rem;
}

.-scroll-me-1.5 {
  scroll-margin-inline-end: -0.375rem;
}

.-scroll-me-10 {
  scroll-margin-inline-end: -2.5rem;
}

.-scroll-me-11 {
  scroll-margin-inline-end: -2.75rem;
}

.-scroll-me-12 {
  scroll-margin-inline-end: -3rem;
}

.-scroll-me-14 {
  scroll-margin-inline-end: -3.5rem;
}

.-scroll-me-16 {
  scroll-margin-inline-end: -4rem;
}

.-scroll-me-2 {
  scroll-margin-inline-end: -0.5rem;
}

.-scroll-me-2.5 {
  scroll-margin-inline-end: -0.625rem;
}

.-scroll-me-20 {
  scroll-margin-inline-end: -5rem;
}

.-scroll-me-24 {
  scroll-margin-inline-end: -6rem;
}

.-scroll-me-28 {
  scroll-margin-inline-end: -7rem;
}

.-scroll-me-3 {
  scroll-margin-inline-end: -0.75rem;
}

.-scroll-me-3.5 {
  scroll-margin-inline-end: -0.875rem;
}

.-scroll-me-32 {
  scroll-margin-inline-end: -8rem;
}

.-scroll-me-36 {
  scroll-margin-inline-end: -9rem;
}

.-scroll-me-4 {
  scroll-margin-inline-end: -1rem;
}

.-scroll-me-40 {
  scroll-margin-inline-end: -10rem;
}

.-scroll-me-44 {
  scroll-margin-inline-end: -11rem;
}

.-scroll-me-48 {
  scroll-margin-inline-end: -12rem;
}

.-scroll-me-5 {
  scroll-margin-inline-end: -1.25rem;
}

.-scroll-me-52 {
  scroll-margin-inline-end: -13rem;
}

.-scroll-me-56 {
  scroll-margin-inline-end: -14rem;
}

.-scroll-me-6 {
  scroll-margin-inline-end: -1.5rem;
}

.-scroll-me-60 {
  scroll-margin-inline-end: -15rem;
}

.-scroll-me-64 {
  scroll-margin-inline-end: -16rem;
}

.-scroll-me-7 {
  scroll-margin-inline-end: -1.75rem;
}

.-scroll-me-72 {
  scroll-margin-inline-end: -18rem;
}

.-scroll-me-8 {
  scroll-margin-inline-end: -2rem;
}

.-scroll-me-80 {
  scroll-margin-inline-end: -20rem;
}

.-scroll-me-9 {
  scroll-margin-inline-end: -2.25rem;
}

.-scroll-me-96 {
  scroll-margin-inline-end: -24rem;
}

.-scroll-me-px {
  scroll-margin-inline-end: -1px;
}

.-scroll-ml-0 {
  scroll-margin-left: -0px;
}

.-scroll-ml-0.5 {
  scroll-margin-left: -0.125rem;
}

.-scroll-ml-1 {
  scroll-margin-left: -0.25rem;
}

.-scroll-ml-1.5 {
  scroll-margin-left: -0.375rem;
}

.-scroll-ml-10 {
  scroll-margin-left: -2.5rem;
}

.-scroll-ml-11 {
  scroll-margin-left: -2.75rem;
}

.-scroll-ml-12 {
  scroll-margin-left: -3rem;
}

.-scroll-ml-14 {
  scroll-margin-left: -3.5rem;
}

.-scroll-ml-16 {
  scroll-margin-left: -4rem;
}

.-scroll-ml-2 {
  scroll-margin-left: -0.5rem;
}

.-scroll-ml-2.5 {
  scroll-margin-left: -0.625rem;
}

.-scroll-ml-20 {
  scroll-margin-left: -5rem;
}

.-scroll-ml-24 {
  scroll-margin-left: -6rem;
}

.-scroll-ml-28 {
  scroll-margin-left: -7rem;
}

.-scroll-ml-3 {
  scroll-margin-left: -0.75rem;
}

.-scroll-ml-3.5 {
  scroll-margin-left: -0.875rem;
}

.-scroll-ml-32 {
  scroll-margin-left: -8rem;
}

.-scroll-ml-36 {
  scroll-margin-left: -9rem;
}

.-scroll-ml-4 {
  scroll-margin-left: -1rem;
}

.-scroll-ml-40 {
  scroll-margin-left: -10rem;
}

.-scroll-ml-44 {
  scroll-margin-left: -11rem;
}

.-scroll-ml-48 {
  scroll-margin-left: -12rem;
}

.-scroll-ml-5 {
  scroll-margin-left: -1.25rem;
}

.-scroll-ml-52 {
  scroll-margin-left: -13rem;
}

.-scroll-ml-56 {
  scroll-margin-left: -14rem;
}

.-scroll-ml-6 {
  scroll-margin-left: -1.5rem;
}

.-scroll-ml-60 {
  scroll-margin-left: -15rem;
}

.-scroll-ml-64 {
  scroll-margin-left: -16rem;
}

.-scroll-ml-7 {
  scroll-margin-left: -1.75rem;
}

.-scroll-ml-72 {
  scroll-margin-left: -18rem;
}

.-scroll-ml-8 {
  scroll-margin-left: -2rem;
}

.-scroll-ml-80 {
  scroll-margin-left: -20rem;
}

.-scroll-ml-9 {
  scroll-margin-left: -2.25rem;
}

.-scroll-ml-96 {
  scroll-margin-left: -24rem;
}

.-scroll-ml-px {
  scroll-margin-left: -1px;
}

.-scroll-mr-0 {
  scroll-margin-right: -0px;
}

.-scroll-mr-0.5 {
  scroll-margin-right: -0.125rem;
}

.-scroll-mr-1 {
  scroll-margin-right: -0.25rem;
}

.-scroll-mr-1.5 {
  scroll-margin-right: -0.375rem;
}

.-scroll-mr-10 {
  scroll-margin-right: -2.5rem;
}

.-scroll-mr-11 {
  scroll-margin-right: -2.75rem;
}

.-scroll-mr-12 {
  scroll-margin-right: -3rem;
}

.-scroll-mr-14 {
  scroll-margin-right: -3.5rem;
}

.-scroll-mr-16 {
  scroll-margin-right: -4rem;
}

.-scroll-mr-2 {
  scroll-margin-right: -0.5rem;
}

.-scroll-mr-2.5 {
  scroll-margin-right: -0.625rem;
}

.-scroll-mr-20 {
  scroll-margin-right: -5rem;
}

.-scroll-mr-24 {
  scroll-margin-right: -6rem;
}

.-scroll-mr-28 {
  scroll-margin-right: -7rem;
}

.-scroll-mr-3 {
  scroll-margin-right: -0.75rem;
}

.-scroll-mr-3.5 {
  scroll-margin-right: -0.875rem;
}

.-scroll-mr-32 {
  scroll-margin-right: -8rem;
}

.-scroll-mr-36 {
  scroll-margin-right: -9rem;
}

.-scroll-mr-4 {
  scroll-margin-right: -1rem;
}

.-scroll-mr-40 {
  scroll-margin-right: -10rem;
}

.-scroll-mr-44 {
  scroll-margin-right: -11rem;
}

.-scroll-mr-48 {
  scroll-margin-right: -12rem;
}

.-scroll-mr-5 {
  scroll-margin-right: -1.25rem;
}

.-scroll-mr-52 {
  scroll-margin-right: -13rem;
}

.-scroll-mr-56 {
  scroll-margin-right: -14rem;
}

.-scroll-mr-6 {
  scroll-margin-right: -1.5rem;
}

.-scroll-mr-60 {
  scroll-margin-right: -15rem;
}

.-scroll-mr-64 {
  scroll-margin-right: -16rem;
}

.-scroll-mr-7 {
  scroll-margin-right: -1.75rem;
}

.-scroll-mr-72 {
  scroll-margin-right: -18rem;
}

.-scroll-mr-8 {
  scroll-margin-right: -2rem;
}

.-scroll-mr-80 {
  scroll-margin-right: -20rem;
}

.-scroll-mr-9 {
  scroll-margin-right: -2.25rem;
}

.-scroll-mr-96 {
  scroll-margin-right: -24rem;
}

.-scroll-mr-px {
  scroll-margin-right: -1px;
}

.-scroll-ms-0 {
  scroll-margin-inline-start: -0px;
}

.-scroll-ms-0.5 {
  scroll-margin-inline-start: -0.125rem;
}

.-scroll-ms-1 {
  scroll-margin-inline-start: -0.25rem;
}

.-scroll-ms-1.5 {
  scroll-margin-inline-start: -0.375rem;
}

.-scroll-ms-10 {
  scroll-margin-inline-start: -2.5rem;
}

.-scroll-ms-11 {
  scroll-margin-inline-start: -2.75rem;
}

.-scroll-ms-12 {
  scroll-margin-inline-start: -3rem;
}

.-scroll-ms-14 {
  scroll-margin-inline-start: -3.5rem;
}

.-scroll-ms-16 {
  scroll-margin-inline-start: -4rem;
}

.-scroll-ms-2 {
  scroll-margin-inline-start: -0.5rem;
}

.-scroll-ms-2.5 {
  scroll-margin-inline-start: -0.625rem;
}

.-scroll-ms-20 {
  scroll-margin-inline-start: -5rem;
}

.-scroll-ms-24 {
  scroll-margin-inline-start: -6rem;
}

.-scroll-ms-28 {
  scroll-margin-inline-start: -7rem;
}

.-scroll-ms-3 {
  scroll-margin-inline-start: -0.75rem;
}

.-scroll-ms-3.5 {
  scroll-margin-inline-start: -0.875rem;
}

.-scroll-ms-32 {
  scroll-margin-inline-start: -8rem;
}

.-scroll-ms-36 {
  scroll-margin-inline-start: -9rem;
}

.-scroll-ms-4 {
  scroll-margin-inline-start: -1rem;
}

.-scroll-ms-40 {
  scroll-margin-inline-start: -10rem;
}

.-scroll-ms-44 {
  scroll-margin-inline-start: -11rem;
}

.-scroll-ms-48 {
  scroll-margin-inline-start: -12rem;
}

.-scroll-ms-5 {
  scroll-margin-inline-start: -1.25rem;
}

.-scroll-ms-52 {
  scroll-margin-inline-start: -13rem;
}

.-scroll-ms-56 {
  scroll-margin-inline-start: -14rem;
}

.-scroll-ms-6 {
  scroll-margin-inline-start: -1.5rem;
}

.-scroll-ms-60 {
  scroll-margin-inline-start: -15rem;
}

.-scroll-ms-64 {
  scroll-margin-inline-start: -16rem;
}

.-scroll-ms-7 {
  scroll-margin-inline-start: -1.75rem;
}

.-scroll-ms-72 {
  scroll-margin-inline-start: -18rem;
}

.-scroll-ms-8 {
  scroll-margin-inline-start: -2rem;
}

.-scroll-ms-80 {
  scroll-margin-inline-start: -20rem;
}

.-scroll-ms-9 {
  scroll-margin-inline-start: -2.25rem;
}

.-scroll-ms-96 {
  scroll-margin-inline-start: -24rem;
}

.-scroll-ms-px {
  scroll-margin-inline-start: -1px;
}

.-scroll-mt-0 {
  scroll-margin-top: -0px;
}

.-scroll-mt-0.5 {
  scroll-margin-top: -0.125rem;
}

.-scroll-mt-1 {
  scroll-margin-top: -0.25rem;
}

.-scroll-mt-1.5 {
  scroll-margin-top: -0.375rem;
}

.-scroll-mt-10 {
  scroll-margin-top: -2.5rem;
}

.-scroll-mt-11 {
  scroll-margin-top: -2.75rem;
}

.-scroll-mt-12 {
  scroll-margin-top: -3rem;
}

.-scroll-mt-14 {
  scroll-margin-top: -3.5rem;
}

.-scroll-mt-16 {
  scroll-margin-top: -4rem;
}

.-scroll-mt-2 {
  scroll-margin-top: -0.5rem;
}

.-scroll-mt-2.5 {
  scroll-margin-top: -0.625rem;
}

.-scroll-mt-20 {
  scroll-margin-top: -5rem;
}

.-scroll-mt-24 {
  scroll-margin-top: -6rem;
}

.-scroll-mt-28 {
  scroll-margin-top: -7rem;
}

.-scroll-mt-3 {
  scroll-margin-top: -0.75rem;
}

.-scroll-mt-3.5 {
  scroll-margin-top: -0.875rem;
}

.-scroll-mt-32 {
  scroll-margin-top: -8rem;
}

.-scroll-mt-36 {
  scroll-margin-top: -9rem;
}

.-scroll-mt-4 {
  scroll-margin-top: -1rem;
}

.-scroll-mt-40 {
  scroll-margin-top: -10rem;
}

.-scroll-mt-44 {
  scroll-margin-top: -11rem;
}

.-scroll-mt-48 {
  scroll-margin-top: -12rem;
}

.-scroll-mt-5 {
  scroll-margin-top: -1.25rem;
}

.-scroll-mt-52 {
  scroll-margin-top: -13rem;
}

.-scroll-mt-56 {
  scroll-margin-top: -14rem;
}

.-scroll-mt-6 {
  scroll-margin-top: -1.5rem;
}

.-scroll-mt-60 {
  scroll-margin-top: -15rem;
}

.-scroll-mt-64 {
  scroll-margin-top: -16rem;
}

.-scroll-mt-7 {
  scroll-margin-top: -1.75rem;
}

.-scroll-mt-72 {
  scroll-margin-top: -18rem;
}

.-scroll-mt-8 {
  scroll-margin-top: -2rem;
}

.-scroll-mt-80 {
  scroll-margin-top: -20rem;
}

.-scroll-mt-9 {
  scroll-margin-top: -2.25rem;
}

.-scroll-mt-96 {
  scroll-margin-top: -24rem;
}

.-scroll-mt-px {
  scroll-margin-top: -1px;
}

.scroll-mb-0 {
  scroll-margin-bottom: 0px;
}

.scroll-mb-0.5 {
  scroll-margin-bottom: 0.125rem;
}

.scroll-mb-1 {
  scroll-margin-bottom: 0.25rem;
}

.scroll-mb-1.5 {
  scroll-margin-bottom: 0.375rem;
}

.scroll-mb-10 {
  scroll-margin-bottom: 2.5rem;
}

.scroll-mb-11 {
  scroll-margin-bottom: 2.75rem;
}

.scroll-mb-12 {
  scroll-margin-bottom: 3rem;
}

.scroll-mb-14 {
  scroll-margin-bottom: 3.5rem;
}

.scroll-mb-16 {
  scroll-margin-bottom: 4rem;
}

.scroll-mb-2 {
  scroll-margin-bottom: 0.5rem;
}

.scroll-mb-2.5 {
  scroll-margin-bottom: 0.625rem;
}

.scroll-mb-20 {
  scroll-margin-bottom: 5rem;
}

.scroll-mb-24 {
  scroll-margin-bottom: 6rem;
}

.scroll-mb-28 {
  scroll-margin-bottom: 7rem;
}

.scroll-mb-3 {
  scroll-margin-bottom: 0.75rem;
}

.scroll-mb-3.5 {
  scroll-margin-bottom: 0.875rem;
}

.scroll-mb-32 {
  scroll-margin-bottom: 8rem;
}

.scroll-mb-36 {
  scroll-margin-bottom: 9rem;
}

.scroll-mb-4 {
  scroll-margin-bottom: 1rem;
}

.scroll-mb-40 {
  scroll-margin-bottom: 10rem;
}

.scroll-mb-44 {
  scroll-margin-bottom: 11rem;
}

.scroll-mb-48 {
  scroll-margin-bottom: 12rem;
}

.scroll-mb-5 {
  scroll-margin-bottom: 1.25rem;
}

.scroll-mb-52 {
  scroll-margin-bottom: 13rem;
}

.scroll-mb-56 {
  scroll-margin-bottom: 14rem;
}

.scroll-mb-6 {
  scroll-margin-bottom: 1.5rem;
}

.scroll-mb-60 {
  scroll-margin-bottom: 15rem;
}

.scroll-mb-64 {
  scroll-margin-bottom: 16rem;
}

.scroll-mb-7 {
  scroll-margin-bottom: 1.75rem;
}

.scroll-mb-72 {
  scroll-margin-bottom: 18rem;
}

.scroll-mb-8 {
  scroll-margin-bottom: 2rem;
}

.scroll-mb-80 {
  scroll-margin-bottom: 20rem;
}

.scroll-mb-9 {
  scroll-margin-bottom: 2.25rem;
}

.scroll-mb-96 {
  scroll-margin-bottom: 24rem;
}

.scroll-mb-px {
  scroll-margin-bottom: 1px;
}

.scroll-me-0 {
  scroll-margin-inline-end: 0px;
}

.scroll-me-0.5 {
  scroll-margin-inline-end: 0.125rem;
}

.scroll-me-1 {
  scroll-margin-inline-end: 0.25rem;
}

.scroll-me-1.5 {
  scroll-margin-inline-end: 0.375rem;
}

.scroll-me-10 {
  scroll-margin-inline-end: 2.5rem;
}

.scroll-me-11 {
  scroll-margin-inline-end: 2.75rem;
}

.scroll-me-12 {
  scroll-margin-inline-end: 3rem;
}

.scroll-me-14 {
  scroll-margin-inline-end: 3.5rem;
}

.scroll-me-16 {
  scroll-margin-inline-end: 4rem;
}

.scroll-me-2 {
  scroll-margin-inline-end: 0.5rem;
}

.scroll-me-2.5 {
  scroll-margin-inline-end: 0.625rem;
}

.scroll-me-20 {
  scroll-margin-inline-end: 5rem;
}

.scroll-me-24 {
  scroll-margin-inline-end: 6rem;
}

.scroll-me-28 {
  scroll-margin-inline-end: 7rem;
}

.scroll-me-3 {
  scroll-margin-inline-end: 0.75rem;
}

.scroll-me-3.5 {
  scroll-margin-inline-end: 0.875rem;
}

.scroll-me-32 {
  scroll-margin-inline-end: 8rem;
}

.scroll-me-36 {
  scroll-margin-inline-end: 9rem;
}

.scroll-me-4 {
  scroll-margin-inline-end: 1rem;
}

.scroll-me-40 {
  scroll-margin-inline-end: 10rem;
}

.scroll-me-44 {
  scroll-margin-inline-end: 11rem;
}

.scroll-me-48 {
  scroll-margin-inline-end: 12rem;
}

.scroll-me-5 {
  scroll-margin-inline-end: 1.25rem;
}

.scroll-me-52 {
  scroll-margin-inline-end: 13rem;
}

.scroll-me-56 {
  scroll-margin-inline-end: 14rem;
}

.scroll-me-6 {
  scroll-margin-inline-end: 1.5rem;
}

.scroll-me-60 {
  scroll-margin-inline-end: 15rem;
}

.scroll-me-64 {
  scroll-margin-inline-end: 16rem;
}

.scroll-me-7 {
  scroll-margin-inline-end: 1.75rem;
}

.scroll-me-72 {
  scroll-margin-inline-end: 18rem;
}

.scroll-me-8 {
  scroll-margin-inline-end: 2rem;
}

.scroll-me-80 {
  scroll-margin-inline-end: 20rem;
}

.scroll-me-9 {
  scroll-margin-inline-end: 2.25rem;
}

.scroll-me-96 {
  scroll-margin-inline-end: 24rem;
}

.scroll-me-px {
  scroll-margin-inline-end: 1px;
}

.scroll-ml-0 {
  scroll-margin-left: 0px;
}

.scroll-ml-0.5 {
  scroll-margin-left: 0.125rem;
}

.scroll-ml-1 {
  scroll-margin-left: 0.25rem;
}

.scroll-ml-1.5 {
  scroll-margin-left: 0.375rem;
}

.scroll-ml-10 {
  scroll-margin-left: 2.5rem;
}

.scroll-ml-11 {
  scroll-margin-left: 2.75rem;
}

.scroll-ml-12 {
  scroll-margin-left: 3rem;
}

.scroll-ml-14 {
  scroll-margin-left: 3.5rem;
}

.scroll-ml-16 {
  scroll-margin-left: 4rem;
}

.scroll-ml-2 {
  scroll-margin-left: 0.5rem;
}

.scroll-ml-2.5 {
  scroll-margin-left: 0.625rem;
}

.scroll-ml-20 {
  scroll-margin-left: 5rem;
}

.scroll-ml-24 {
  scroll-margin-left: 6rem;
}

.scroll-ml-28 {
  scroll-margin-left: 7rem;
}

.scroll-ml-3 {
  scroll-margin-left: 0.75rem;
}

.scroll-ml-3.5 {
  scroll-margin-left: 0.875rem;
}

.scroll-ml-32 {
  scroll-margin-left: 8rem;
}

.scroll-ml-36 {
  scroll-margin-left: 9rem;
}

.scroll-ml-4 {
  scroll-margin-left: 1rem;
}

.scroll-ml-40 {
  scroll-margin-left: 10rem;
}

.scroll-ml-44 {
  scroll-margin-left: 11rem;
}

.scroll-ml-48 {
  scroll-margin-left: 12rem;
}

.scroll-ml-5 {
  scroll-margin-left: 1.25rem;
}

.scroll-ml-52 {
  scroll-margin-left: 13rem;
}

.scroll-ml-56 {
  scroll-margin-left: 14rem;
}

.scroll-ml-6 {
  scroll-margin-left: 1.5rem;
}

.scroll-ml-60 {
  scroll-margin-left: 15rem;
}

.scroll-ml-64 {
  scroll-margin-left: 16rem;
}

.scroll-ml-7 {
  scroll-margin-left: 1.75rem;
}

.scroll-ml-72 {
  scroll-margin-left: 18rem;
}

.scroll-ml-8 {
  scroll-margin-left: 2rem;
}

.scroll-ml-80 {
  scroll-margin-left: 20rem;
}

.scroll-ml-9 {
  scroll-margin-left: 2.25rem;
}

.scroll-ml-96 {
  scroll-margin-left: 24rem;
}

.scroll-ml-px {
  scroll-margin-left: 1px;
}

.scroll-mr-0 {
  scroll-margin-right: 0px;
}

.scroll-mr-0.5 {
  scroll-margin-right: 0.125rem;
}

.scroll-mr-1 {
  scroll-margin-right: 0.25rem;
}

.scroll-mr-1.5 {
  scroll-margin-right: 0.375rem;
}

.scroll-mr-10 {
  scroll-margin-right: 2.5rem;
}

.scroll-mr-11 {
  scroll-margin-right: 2.75rem;
}

.scroll-mr-12 {
  scroll-margin-right: 3rem;
}

.scroll-mr-14 {
  scroll-margin-right: 3.5rem;
}

.scroll-mr-16 {
  scroll-margin-right: 4rem;
}

.scroll-mr-2 {
  scroll-margin-right: 0.5rem;
}

.scroll-mr-2.5 {
  scroll-margin-right: 0.625rem;
}

.scroll-mr-20 {
  scroll-margin-right: 5rem;
}

.scroll-mr-24 {
  scroll-margin-right: 6rem;
}

.scroll-mr-28 {
  scroll-margin-right: 7rem;
}

.scroll-mr-3 {
  scroll-margin-right: 0.75rem;
}

.scroll-mr-3.5 {
  scroll-margin-right: 0.875rem;
}

.scroll-mr-32 {
  scroll-margin-right: 8rem;
}

.scroll-mr-36 {
  scroll-margin-right: 9rem;
}

.scroll-mr-4 {
  scroll-margin-right: 1rem;
}

.scroll-mr-40 {
  scroll-margin-right: 10rem;
}

.scroll-mr-44 {
  scroll-margin-right: 11rem;
}

.scroll-mr-48 {
  scroll-margin-right: 12rem;
}

.scroll-mr-5 {
  scroll-margin-right: 1.25rem;
}

.scroll-mr-52 {
  scroll-margin-right: 13rem;
}

.scroll-mr-56 {
  scroll-margin-right: 14rem;
}

.scroll-mr-6 {
  scroll-margin-right: 1.5rem;
}

.scroll-mr-60 {
  scroll-margin-right: 15rem;
}

.scroll-mr-64 {
  scroll-margin-right: 16rem;
}

.scroll-mr-7 {
  scroll-margin-right: 1.75rem;
}

.scroll-mr-72 {
  scroll-margin-right: 18rem;
}

.scroll-mr-8 {
  scroll-margin-right: 2rem;
}

.scroll-mr-80 {
  scroll-margin-right: 20rem;
}

.scroll-mr-9 {
  scroll-margin-right: 2.25rem;
}

.scroll-mr-96 {
  scroll-margin-right: 24rem;
}

.scroll-mr-px {
  scroll-margin-right: 1px;
}

.scroll-ms-0 {
  scroll-margin-inline-start: 0px;
}

.scroll-ms-0.5 {
  scroll-margin-inline-start: 0.125rem;
}

.scroll-ms-1 {
  scroll-margin-inline-start: 0.25rem;
}

.scroll-ms-1.5 {
  scroll-margin-inline-start: 0.375rem;
}

.scroll-ms-10 {
  scroll-margin-inline-start: 2.5rem;
}

.scroll-ms-11 {
  scroll-margin-inline-start: 2.75rem;
}

.scroll-ms-12 {
  scroll-margin-inline-start: 3rem;
}

.scroll-ms-14 {
  scroll-margin-inline-start: 3.5rem;
}

.scroll-ms-16 {
  scroll-margin-inline-start: 4rem;
}

.scroll-ms-2 {
  scroll-margin-inline-start: 0.5rem;
}

.scroll-ms-2.5 {
  scroll-margin-inline-start: 0.625rem;
}

.scroll-ms-20 {
  scroll-margin-inline-start: 5rem;
}

.scroll-ms-24 {
  scroll-margin-inline-start: 6rem;
}

.scroll-ms-28 {
  scroll-margin-inline-start: 7rem;
}

.scroll-ms-3 {
  scroll-margin-inline-start: 0.75rem;
}

.scroll-ms-3.5 {
  scroll-margin-inline-start: 0.875rem;
}

.scroll-ms-32 {
  scroll-margin-inline-start: 8rem;
}

.scroll-ms-36 {
  scroll-margin-inline-start: 9rem;
}

.scroll-ms-4 {
  scroll-margin-inline-start: 1rem;
}

.scroll-ms-40 {
  scroll-margin-inline-start: 10rem;
}

.scroll-ms-44 {
  scroll-margin-inline-start: 11rem;
}

.scroll-ms-48 {
  scroll-margin-inline-start: 12rem;
}

.scroll-ms-5 {
  scroll-margin-inline-start: 1.25rem;
}

.scroll-ms-52 {
  scroll-margin-inline-start: 13rem;
}

.scroll-ms-56 {
  scroll-margin-inline-start: 14rem;
}

.scroll-ms-6 {
  scroll-margin-inline-start: 1.5rem;
}

.scroll-ms-60 {
  scroll-margin-inline-start: 15rem;
}

.scroll-ms-64 {
  scroll-margin-inline-start: 16rem;
}

.scroll-ms-7 {
  scroll-margin-inline-start: 1.75rem;
}

.scroll-ms-72 {
  scroll-margin-inline-start: 18rem;
}

.scroll-ms-8 {
  scroll-margin-inline-start: 2rem;
}

.scroll-ms-80 {
  scroll-margin-inline-start: 20rem;
}

.scroll-ms-9 {
  scroll-margin-inline-start: 2.25rem;
}

.scroll-ms-96 {
  scroll-margin-inline-start: 24rem;
}

.scroll-ms-px {
  scroll-margin-inline-start: 1px;
}

.scroll-mt-0 {
  scroll-margin-top: 0px;
}

.scroll-mt-0.5 {
  scroll-margin-top: 0.125rem;
}

.scroll-mt-1 {
  scroll-margin-top: 0.25rem;
}

.scroll-mt-1.5 {
  scroll-margin-top: 0.375rem;
}

.scroll-mt-10 {
  scroll-margin-top: 2.5rem;
}

.scroll-mt-11 {
  scroll-margin-top: 2.75rem;
}

.scroll-mt-12 {
  scroll-margin-top: 3rem;
}

.scroll-mt-14 {
  scroll-margin-top: 3.5rem;
}

.scroll-mt-16 {
  scroll-margin-top: 4rem;
}

.scroll-mt-2 {
  scroll-margin-top: 0.5rem;
}

.scroll-mt-2.5 {
  scroll-margin-top: 0.625rem;
}

.scroll-mt-20 {
  scroll-margin-top: 5rem;
}

.scroll-mt-24 {
  scroll-margin-top: 6rem;
}

.scroll-mt-28 {
  scroll-margin-top: 7rem;
}

.scroll-mt-3 {
  scroll-margin-top: 0.75rem;
}

.scroll-mt-3.5 {
  scroll-margin-top: 0.875rem;
}

.scroll-mt-32 {
  scroll-margin-top: 8rem;
}

.scroll-mt-36 {
  scroll-margin-top: 9rem;
}

.scroll-mt-4 {
  scroll-margin-top: 1rem;
}

.scroll-mt-40 {
  scroll-margin-top: 10rem;
}

.scroll-mt-44 {
  scroll-margin-top: 11rem;
}

.scroll-mt-48 {
  scroll-margin-top: 12rem;
}

.scroll-mt-5 {
  scroll-margin-top: 1.25rem;
}

.scroll-mt-52 {
  scroll-margin-top: 13rem;
}

.scroll-mt-56 {
  scroll-margin-top: 14rem;
}

.scroll-mt-6 {
  scroll-margin-top: 1.5rem;
}

.scroll-mt-60 {
  scroll-margin-top: 15rem;
}

.scroll-mt-64 {
  scroll-margin-top: 16rem;
}

.scroll-mt-7 {
  scroll-margin-top: 1.75rem;
}

.scroll-mt-72 {
  scroll-margin-top: 18rem;
}

.scroll-mt-8 {
  scroll-margin-top: 2rem;
}

.scroll-mt-80 {
  scroll-margin-top: 20rem;
}

.scroll-mt-9 {
  scroll-margin-top: 2.25rem;
}

.scroll-mt-96 {
  scroll-margin-top: 24rem;
}

.scroll-mt-px {
  scroll-margin-top: 1px;
}

.scroll-p-0 {
  scroll-padding: 0px;
}

.scroll-p-0.5 {
  scroll-padding: 0.125rem;
}

.scroll-p-1 {
  scroll-padding: 0.25rem;
}

.scroll-p-1.5 {
  scroll-padding: 0.375rem;
}

.scroll-p-10 {
  scroll-padding: 2.5rem;
}

.scroll-p-11 {
  scroll-padding: 2.75rem;
}

.scroll-p-12 {
  scroll-padding: 3rem;
}

.scroll-p-14 {
  scroll-padding: 3.5rem;
}

.scroll-p-16 {
  scroll-padding: 4rem;
}

.scroll-p-2 {
  scroll-padding: 0.5rem;
}

.scroll-p-2.5 {
  scroll-padding: 0.625rem;
}

.scroll-p-20 {
  scroll-padding: 5rem;
}

.scroll-p-24 {
  scroll-padding: 6rem;
}

.scroll-p-28 {
  scroll-padding: 7rem;
}

.scroll-p-3 {
  scroll-padding: 0.75rem;
}

.scroll-p-3.5 {
  scroll-padding: 0.875rem;
}

.scroll-p-32 {
  scroll-padding: 8rem;
}

.scroll-p-36 {
  scroll-padding: 9rem;
}

.scroll-p-4 {
  scroll-padding: 1rem;
}

.scroll-p-40 {
  scroll-padding: 10rem;
}

.scroll-p-44 {
  scroll-padding: 11rem;
}

.scroll-p-48 {
  scroll-padding: 12rem;
}

.scroll-p-5 {
  scroll-padding: 1.25rem;
}

.scroll-p-52 {
  scroll-padding: 13rem;
}

.scroll-p-56 {
  scroll-padding: 14rem;
}

.scroll-p-6 {
  scroll-padding: 1.5rem;
}

.scroll-p-60 {
  scroll-padding: 15rem;
}

.scroll-p-64 {
  scroll-padding: 16rem;
}

.scroll-p-7 {
  scroll-padding: 1.75rem;
}

.scroll-p-72 {
  scroll-padding: 18rem;
}

.scroll-p-8 {
  scroll-padding: 2rem;
}

.scroll-p-80 {
  scroll-padding: 20rem;
}

.scroll-p-9 {
  scroll-padding: 2.25rem;
}

.scroll-p-96 {
  scroll-padding: 24rem;
}

.scroll-p-px {
  scroll-padding: 1px;
}

.scroll-px-0 {
  scroll-padding-left: 0px;
  scroll-padding-right: 0px;
}

.scroll-px-0.5 {
  scroll-padding-left: 0.125rem;
  scroll-padding-right: 0.125rem;
}

.scroll-px-1 {
  scroll-padding-left: 0.25rem;
  scroll-padding-right: 0.25rem;
}

.scroll-px-1.5 {
  scroll-padding-left: 0.375rem;
  scroll-padding-right: 0.375rem;
}

.scroll-px-10 {
  scroll-padding-left: 2.5rem;
  scroll-padding-right: 2.5rem;
}

.scroll-px-11 {
  scroll-padding-left: 2.75rem;
  scroll-padding-right: 2.75rem;
}

.scroll-px-12 {
  scroll-padding-left: 3rem;
  scroll-padding-right: 3rem;
}

.scroll-px-14 {
  scroll-padding-left: 3.5rem;
  scroll-padding-right: 3.5rem;
}

.scroll-px-16 {
  scroll-padding-left: 4rem;
  scroll-padding-right: 4rem;
}

.scroll-px-2 {
  scroll-padding-left: 0.5rem;
  scroll-padding-right: 0.5rem;
}

.scroll-px-2.5 {
  scroll-padding-left: 0.625rem;
  scroll-padding-right: 0.625rem;
}

.scroll-px-20 {
  scroll-padding-left: 5rem;
  scroll-padding-right: 5rem;
}

.scroll-px-24 {
  scroll-padding-left: 6rem;
  scroll-padding-right: 6rem;
}

.scroll-px-28 {
  scroll-padding-left: 7rem;
  scroll-padding-right: 7rem;
}

.scroll-px-3 {
  scroll-padding-left: 0.75rem;
  scroll-padding-right: 0.75rem;
}

.scroll-px-3.5 {
  scroll-padding-left: 0.875rem;
  scroll-padding-right: 0.875rem;
}

.scroll-px-32 {
  scroll-padding-left: 8rem;
  scroll-padding-right: 8rem;
}

.scroll-px-36 {
  scroll-padding-left: 9rem;
  scroll-padding-right: 9rem;
}

.scroll-px-4 {
  scroll-padding-left: 1rem;
  scroll-padding-right: 1rem;
}

.scroll-px-40 {
  scroll-padding-left: 10rem;
  scroll-padding-right: 10rem;
}

.scroll-px-44 {
  scroll-padding-left: 11rem;
  scroll-padding-right: 11rem;
}

.scroll-px-48 {
  scroll-padding-left: 12rem;
  scroll-padding-right: 12rem;
}

.scroll-px-5 {
  scroll-padding-left: 1.25rem;
  scroll-padding-right: 1.25rem;
}

.scroll-px-52 {
  scroll-padding-left: 13rem;
  scroll-padding-right: 13rem;
}

.scroll-px-56 {
  scroll-padding-left: 14rem;
  scroll-padding-right: 14rem;
}

.scroll-px-6 {
  scroll-padding-left: 1.5rem;
  scroll-padding-right: 1.5rem;
}

.scroll-px-60 {
  scroll-padding-left: 15rem;
  scroll-padding-right: 15rem;
}

.scroll-px-64 {
  scroll-padding-left: 16rem;
  scroll-padding-right: 16rem;
}

.scroll-px-7 {
  scroll-padding-left: 1.75rem;
  scroll-padding-right: 1.75rem;
}

.scroll-px-72 {
  scroll-padding-left: 18rem;
  scroll-padding-right: 18rem;
}

.scroll-px-8 {
  scroll-padding-left: 2rem;
  scroll-padding-right: 2rem;
}

.scroll-px-80 {
  scroll-padding-left: 20rem;
  scroll-padding-right: 20rem;
}

.scroll-px-9 {
  scroll-padding-left: 2.25rem;
  scroll-padding-right: 2.25rem;
}

.scroll-px-96 {
  scroll-padding-left: 24rem;
  scroll-padding-right: 24rem;
}

.scroll-px-px {
  scroll-padding-left: 1px;
  scroll-padding-right: 1px;
}

.scroll-py-0 {
  scroll-padding-top: 0px;
  scroll-padding-bottom: 0px;
}

.scroll-py-0.5 {
  scroll-padding-top: 0.125rem;
  scroll-padding-bottom: 0.125rem;
}

.scroll-py-1 {
  scroll-padding-top: 0.25rem;
  scroll-padding-bottom: 0.25rem;
}

.scroll-py-1.5 {
  scroll-padding-top: 0.375rem;
  scroll-padding-bottom: 0.375rem;
}

.scroll-py-10 {
  scroll-padding-top: 2.5rem;
  scroll-padding-bottom: 2.5rem;
}

.scroll-py-11 {
  scroll-padding-top: 2.75rem;
  scroll-padding-bottom: 2.75rem;
}

.scroll-py-12 {
  scroll-padding-top: 3rem;
  scroll-padding-bottom: 3rem;
}

.scroll-py-14 {
  scroll-padding-top: 3.5rem;
  scroll-padding-bottom: 3.5rem;
}

.scroll-py-16 {
  scroll-padding-top: 4rem;
  scroll-padding-bottom: 4rem;
}

.scroll-py-2 {
  scroll-padding-top: 0.5rem;
  scroll-padding-bottom: 0.5rem;
}

.scroll-py-2.5 {
  scroll-padding-top: 0.625rem;
  scroll-padding-bottom: 0.625rem;
}

.scroll-py-20 {
  scroll-padding-top: 5rem;
  scroll-padding-bottom: 5rem;
}

.scroll-py-24 {
  scroll-padding-top: 6rem;
  scroll-padding-bottom: 6rem;
}

.scroll-py-28 {
  scroll-padding-top: 7rem;
  scroll-padding-bottom: 7rem;
}

.scroll-py-3 {
  scroll-padding-top: 0.75rem;
  scroll-padding-bottom: 0.75rem;
}

.scroll-py-3.5 {
  scroll-padding-top: 0.875rem;
  scroll-padding-bottom: 0.875rem;
}

.scroll-py-32 {
  scroll-padding-top: 8rem;
  scroll-padding-bottom: 8rem;
}

.scroll-py-36 {
  scroll-padding-top: 9rem;
  scroll-padding-bottom: 9rem;
}

.scroll-py-4 {
  scroll-padding-top: 1rem;
  scroll-padding-bottom: 1rem;
}

.scroll-py-40 {
  scroll-padding-top: 10rem;
  scroll-padding-bottom: 10rem;
}

.scroll-py-44 {
  scroll-padding-top: 11rem;
  scroll-padding-bottom: 11rem;
}

.scroll-py-48 {
  scroll-padding-top: 12rem;
  scroll-padding-bottom: 12rem;
}

.scroll-py-5 {
  scroll-padding-top: 1.25rem;
  scroll-padding-bottom: 1.25rem;
}

.scroll-py-52 {
  scroll-padding-top: 13rem;
  scroll-padding-bottom: 13rem;
}

.scroll-py-56 {
  scroll-padding-top: 14rem;
  scroll-padding-bottom: 14rem;
}

.scroll-py-6 {
  scroll-padding-top: 1.5rem;
  scroll-padding-bottom: 1.5rem;
}

.scroll-py-60 {
  scroll-padding-top: 15rem;
  scroll-padding-bottom: 15rem;
}

.scroll-py-64 {
  scroll-padding-top: 16rem;
  scroll-padding-bottom: 16rem;
}

.scroll-py-7 {
  scroll-padding-top: 1.75rem;
  scroll-padding-bottom: 1.75rem;
}

.scroll-py-72 {
  scroll-padding-top: 18rem;
  scroll-padding-bottom: 18rem;
}

.scroll-py-8 {
  scroll-padding-top: 2rem;
  scroll-padding-bottom: 2rem;
}

.scroll-py-80 {
  scroll-padding-top: 20rem;
  scroll-padding-bottom: 20rem;
}

.scroll-py-9 {
  scroll-padding-top: 2.25rem;
  scroll-padding-bottom: 2.25rem;
}

.scroll-py-96 {
  scroll-padding-top: 24rem;
  scroll-padding-bottom: 24rem;
}

.scroll-py-px {
  scroll-padding-top: 1px;
  scroll-padding-bottom: 1px;
}

.scroll-pb-0 {
  scroll-padding-bottom: 0px;
}

.scroll-pb-0.5 {
  scroll-padding-bottom: 0.125rem;
}

.scroll-pb-1 {
  scroll-padding-bottom: 0.25rem;
}

.scroll-pb-1.5 {
  scroll-padding-bottom: 0.375rem;
}

.scroll-pb-10 {
  scroll-padding-bottom: 2.5rem;
}

.scroll-pb-11 {
  scroll-padding-bottom: 2.75rem;
}

.scroll-pb-12 {
  scroll-padding-bottom: 3rem;
}

.scroll-pb-14 {
  scroll-padding-bottom: 3.5rem;
}

.scroll-pb-16 {
  scroll-padding-bottom: 4rem;
}

.scroll-pb-2 {
  scroll-padding-bottom: 0.5rem;
}

.scroll-pb-2.5 {
  scroll-padding-bottom: 0.625rem;
}

.scroll-pb-20 {
  scroll-padding-bottom: 5rem;
}

.scroll-pb-24 {
  scroll-padding-bottom: 6rem;
}

.scroll-pb-28 {
  scroll-padding-bottom: 7rem;
}

.scroll-pb-3 {
  scroll-padding-bottom: 0.75rem;
}

.scroll-pb-3.5 {
  scroll-padding-bottom: 0.875rem;
}

.scroll-pb-32 {
  scroll-padding-bottom: 8rem;
}

.scroll-pb-36 {
  scroll-padding-bottom: 9rem;
}

.scroll-pb-4 {
  scroll-padding-bottom: 1rem;
}

.scroll-pb-40 {
  scroll-padding-bottom: 10rem;
}

.scroll-pb-44 {
  scroll-padding-bottom: 11rem;
}

.scroll-pb-48 {
  scroll-padding-bottom: 12rem;
}

.scroll-pb-5 {
  scroll-padding-bottom: 1.25rem;
}

.scroll-pb-52 {
  scroll-padding-bottom: 13rem;
}

.scroll-pb-56 {
  scroll-padding-bottom: 14rem;
}

.scroll-pb-6 {
  scroll-padding-bottom: 1.5rem;
}

.scroll-pb-60 {
  scroll-padding-bottom: 15rem;
}

.scroll-pb-64 {
  scroll-padding-bottom: 16rem;
}

.scroll-pb-7 {
  scroll-padding-bottom: 1.75rem;
}

.scroll-pb-72 {
  scroll-padding-bottom: 18rem;
}

.scroll-pb-8 {
  scroll-padding-bottom: 2rem;
}

.scroll-pb-80 {
  scroll-padding-bottom: 20rem;
}

.scroll-pb-9 {
  scroll-padding-bottom: 2.25rem;
}

.scroll-pb-96 {
  scroll-padding-bottom: 24rem;
}

.scroll-pb-px {
  scroll-padding-bottom: 1px;
}

.scroll-pe-0 {
  scroll-padding-inline-end: 0px;
}

.scroll-pe-0.5 {
  scroll-padding-inline-end: 0.125rem;
}

.scroll-pe-1 {
  scroll-padding-inline-end: 0.25rem;
}

.scroll-pe-1.5 {
  scroll-padding-inline-end: 0.375rem;
}

.scroll-pe-10 {
  scroll-padding-inline-end: 2.5rem;
}

.scroll-pe-11 {
  scroll-padding-inline-end: 2.75rem;
}

.scroll-pe-12 {
  scroll-padding-inline-end: 3rem;
}

.scroll-pe-14 {
  scroll-padding-inline-end: 3.5rem;
}

.scroll-pe-16 {
  scroll-padding-inline-end: 4rem;
}

.scroll-pe-2 {
  scroll-padding-inline-end: 0.5rem;
}

.scroll-pe-2.5 {
  scroll-padding-inline-end: 0.625rem;
}

.scroll-pe-20 {
  scroll-padding-inline-end: 5rem;
}

.scroll-pe-24 {
  scroll-padding-inline-end: 6rem;
}

.scroll-pe-28 {
  scroll-padding-inline-end: 7rem;
}

.scroll-pe-3 {
  scroll-padding-inline-end: 0.75rem;
}

.scroll-pe-3.5 {
  scroll-padding-inline-end: 0.875rem;
}

.scroll-pe-32 {
  scroll-padding-inline-end: 8rem;
}

.scroll-pe-36 {
  scroll-padding-inline-end: 9rem;
}

.scroll-pe-4 {
  scroll-padding-inline-end: 1rem;
}

.scroll-pe-40 {
  scroll-padding-inline-end: 10rem;
}

.scroll-pe-44 {
  scroll-padding-inline-end: 11rem;
}

.scroll-pe-48 {
  scroll-padding-inline-end: 12rem;
}

.scroll-pe-5 {
  scroll-padding-inline-end: 1.25rem;
}

.scroll-pe-52 {
  scroll-padding-inline-end: 13rem;
}

.scroll-pe-56 {
  scroll-padding-inline-end: 14rem;
}

.scroll-pe-6 {
  scroll-padding-inline-end: 1.5rem;
}

.scroll-pe-60 {
  scroll-padding-inline-end: 15rem;
}

.scroll-pe-64 {
  scroll-padding-inline-end: 16rem;
}

.scroll-pe-7 {
  scroll-padding-inline-end: 1.75rem;
}

.scroll-pe-72 {
  scroll-padding-inline-end: 18rem;
}

.scroll-pe-8 {
  scroll-padding-inline-end: 2rem;
}

.scroll-pe-80 {
  scroll-padding-inline-end: 20rem;
}

.scroll-pe-9 {
  scroll-padding-inline-end: 2.25rem;
}

.scroll-pe-96 {
  scroll-padding-inline-end: 24rem;
}

.scroll-pe-px {
  scroll-padding-inline-end: 1px;
}

.scroll-pl-0 {
  scroll-padding-left: 0px;
}

.scroll-pl-0.5 {
  scroll-padding-left: 0.125rem;
}

.scroll-pl-1 {
  scroll-padding-left: 0.25rem;
}

.scroll-pl-1.5 {
  scroll-padding-left: 0.375rem;
}

.scroll-pl-10 {
  scroll-padding-left: 2.5rem;
}

.scroll-pl-11 {
  scroll-padding-left: 2.75rem;
}

.scroll-pl-12 {
  scroll-padding-left: 3rem;
}

.scroll-pl-14 {
  scroll-padding-left: 3.5rem;
}

.scroll-pl-16 {
  scroll-padding-left: 4rem;
}

.scroll-pl-2 {
  scroll-padding-left: 0.5rem;
}

.scroll-pl-2.5 {
  scroll-padding-left: 0.625rem;
}

.scroll-pl-20 {
  scroll-padding-left: 5rem;
}

.scroll-pl-24 {
  scroll-padding-left: 6rem;
}

.scroll-pl-28 {
  scroll-padding-left: 7rem;
}

.scroll-pl-3 {
  scroll-padding-left: 0.75rem;
}

.scroll-pl-3.5 {
  scroll-padding-left: 0.875rem;
}

.scroll-pl-32 {
  scroll-padding-left: 8rem;
}

.scroll-pl-36 {
  scroll-padding-left: 9rem;
}

.scroll-pl-4 {
  scroll-padding-left: 1rem;
}

.scroll-pl-40 {
  scroll-padding-left: 10rem;
}

.scroll-pl-44 {
  scroll-padding-left: 11rem;
}

.scroll-pl-48 {
  scroll-padding-left: 12rem;
}

.scroll-pl-5 {
  scroll-padding-left: 1.25rem;
}

.scroll-pl-52 {
  scroll-padding-left: 13rem;
}

.scroll-pl-56 {
  scroll-padding-left: 14rem;
}

.scroll-pl-6 {
  scroll-padding-left: 1.5rem;
}

.scroll-pl-60 {
  scroll-padding-left: 15rem;
}

.scroll-pl-64 {
  scroll-padding-left: 16rem;
}

.scroll-pl-7 {
  scroll-padding-left: 1.75rem;
}

.scroll-pl-72 {
  scroll-padding-left: 18rem;
}

.scroll-pl-8 {
  scroll-padding-left: 2rem;
}

.scroll-pl-80 {
  scroll-padding-left: 20rem;
}

.scroll-pl-9 {
  scroll-padding-left: 2.25rem;
}

.scroll-pl-96 {
  scroll-padding-left: 24rem;
}

.scroll-pl-px {
  scroll-padding-left: 1px;
}

.scroll-pr-0 {
  scroll-padding-right: 0px;
}

.scroll-pr-0.5 {
  scroll-padding-right: 0.125rem;
}

.scroll-pr-1 {
  scroll-padding-right: 0.25rem;
}

.scroll-pr-1.5 {
  scroll-padding-right: 0.375rem;
}

.scroll-pr-10 {
  scroll-padding-right: 2.5rem;
}

.scroll-pr-11 {
  scroll-padding-right: 2.75rem;
}

.scroll-pr-12 {
  scroll-padding-right: 3rem;
}

.scroll-pr-14 {
  scroll-padding-right: 3.5rem;
}

.scroll-pr-16 {
  scroll-padding-right: 4rem;
}

.scroll-pr-2 {
  scroll-padding-right: 0.5rem;
}

.scroll-pr-2.5 {
  scroll-padding-right: 0.625rem;
}

.scroll-pr-20 {
  scroll-padding-right: 5rem;
}

.scroll-pr-24 {
  scroll-padding-right: 6rem;
}

.scroll-pr-28 {
  scroll-padding-right: 7rem;
}

.scroll-pr-3 {
  scroll-padding-right: 0.75rem;
}

.scroll-pr-3.5 {
  scroll-padding-right: 0.875rem;
}

.scroll-pr-32 {
  scroll-padding-right: 8rem;
}

.scroll-pr-36 {
  scroll-padding-right: 9rem;
}

.scroll-pr-4 {
  scroll-padding-right: 1rem;
}

.scroll-pr-40 {
  scroll-padding-right: 10rem;
}

.scroll-pr-44 {
  scroll-padding-right: 11rem;
}

.scroll-pr-48 {
  scroll-padding-right: 12rem;
}

.scroll-pr-5 {
  scroll-padding-right: 1.25rem;
}

.scroll-pr-52 {
  scroll-padding-right: 13rem;
}

.scroll-pr-56 {
  scroll-padding-right: 14rem;
}

.scroll-pr-6 {
  scroll-padding-right: 1.5rem;
}

.scroll-pr-60 {
  scroll-padding-right: 15rem;
}

.scroll-pr-64 {
  scroll-padding-right: 16rem;
}

.scroll-pr-7 {
  scroll-padding-right: 1.75rem;
}

.scroll-pr-72 {
  scroll-padding-right: 18rem;
}

.scroll-pr-8 {
  scroll-padding-right: 2rem;
}

.scroll-pr-80 {
  scroll-padding-right: 20rem;
}

.scroll-pr-9 {
  scroll-padding-right: 2.25rem;
}

.scroll-pr-96 {
  scroll-padding-right: 24rem;
}

.scroll-pr-px {
  scroll-padding-right: 1px;
}

.scroll-ps-0 {
  scroll-padding-inline-start: 0px;
}

.scroll-ps-0.5 {
  scroll-padding-inline-start: 0.125rem;
}

.scroll-ps-1 {
  scroll-padding-inline-start: 0.25rem;
}

.scroll-ps-1.5 {
  scroll-padding-inline-start: 0.375rem;
}

.scroll-ps-10 {
  scroll-padding-inline-start: 2.5rem;
}

.scroll-ps-11 {
  scroll-padding-inline-start: 2.75rem;
}

.scroll-ps-12 {
  scroll-padding-inline-start: 3rem;
}

.scroll-ps-14 {
  scroll-padding-inline-start: 3.5rem;
}

.scroll-ps-16 {
  scroll-padding-inline-start: 4rem;
}

.scroll-ps-2 {
  scroll-padding-inline-start: 0.5rem;
}

.scroll-ps-2.5 {
  scroll-padding-inline-start: 0.625rem;
}

.scroll-ps-20 {
  scroll-padding-inline-start: 5rem;
}

.scroll-ps-24 {
  scroll-padding-inline-start: 6rem;
}

.scroll-ps-28 {
  scroll-padding-inline-start: 7rem;
}

.scroll-ps-3 {
  scroll-padding-inline-start: 0.75rem;
}

.scroll-ps-3.5 {
  scroll-padding-inline-start: 0.875rem;
}

.scroll-ps-32 {
  scroll-padding-inline-start: 8rem;
}

.scroll-ps-36 {
  scroll-padding-inline-start: 9rem;
}

.scroll-ps-4 {
  scroll-padding-inline-start: 1rem;
}

.scroll-ps-40 {
  scroll-padding-inline-start: 10rem;
}

.scroll-ps-44 {
  scroll-padding-inline-start: 11rem;
}

.scroll-ps-48 {
  scroll-padding-inline-start: 12rem;
}

.scroll-ps-5 {
  scroll-padding-inline-start: 1.25rem;
}

.scroll-ps-52 {
  scroll-padding-inline-start: 13rem;
}

.scroll-ps-56 {
  scroll-padding-inline-start: 14rem;
}

.scroll-ps-6 {
  scroll-padding-inline-start: 1.5rem;
}

.scroll-ps-60 {
  scroll-padding-inline-start: 15rem;
}

.scroll-ps-64 {
  scroll-padding-inline-start: 16rem;
}

.scroll-ps-7 {
  scroll-padding-inline-start: 1.75rem;
}

.scroll-ps-72 {
  scroll-padding-inline-start: 18rem;
}

.scroll-ps-8 {
  scroll-padding-inline-start: 2rem;
}

.scroll-ps-80 {
  scroll-padding-inline-start: 20rem;
}

.scroll-ps-9 {
  scroll-padding-inline-start: 2.25rem;
}

.scroll-ps-96 {
  scroll-padding-inline-start: 24rem;
}

.scroll-ps-px {
  scroll-padding-inline-start: 1px;
}

.scroll-pt-0 {
  scroll-padding-top: 0px;
}

.scroll-pt-0.5 {
  scroll-padding-top: 0.125rem;
}

.scroll-pt-1 {
  scroll-padding-top: 0.25rem;
}

.scroll-pt-1.5 {
  scroll-padding-top: 0.375rem;
}

.scroll-pt-10 {
  scroll-padding-top: 2.5rem;
}

.scroll-pt-11 {
  scroll-padding-top: 2.75rem;
}

.scroll-pt-12 {
  scroll-padding-top: 3rem;
}

.scroll-pt-14 {
  scroll-padding-top: 3.5rem;
}

.scroll-pt-16 {
  scroll-padding-top: 4rem;
}

.scroll-pt-2 {
  scroll-padding-top: 0.5rem;
}

.scroll-pt-2.5 {
  scroll-padding-top: 0.625rem;
}

.scroll-pt-20 {
  scroll-padding-top: 5rem;
}

.scroll-pt-24 {
  scroll-padding-top: 6rem;
}

.scroll-pt-28 {
  scroll-padding-top: 7rem;
}

.scroll-pt-3 {
  scroll-padding-top: 0.75rem;
}

.scroll-pt-3.5 {
  scroll-padding-top: 0.875rem;
}

.scroll-pt-32 {
  scroll-padding-top: 8rem;
}

.scroll-pt-36 {
  scroll-padding-top: 9rem;
}

.scroll-pt-4 {
  scroll-padding-top: 1rem;
}

.scroll-pt-40 {
  scroll-padding-top: 10rem;
}

.scroll-pt-44 {
  scroll-padding-top: 11rem;
}

.scroll-pt-48 {
  scroll-padding-top: 12rem;
}

.scroll-pt-5 {
  scroll-padding-top: 1.25rem;
}

.scroll-pt-52 {
  scroll-padding-top: 13rem;
}

.scroll-pt-56 {
  scroll-padding-top: 14rem;
}

.scroll-pt-6 {
  scroll-padding-top: 1.5rem;
}

.scroll-pt-60 {
  scroll-padding-top: 15rem;
}

.scroll-pt-64 {
  scroll-padding-top: 16rem;
}

.scroll-pt-7 {
  scroll-padding-top: 1.75rem;
}

.scroll-pt-72 {
  scroll-padding-top: 18rem;
}

.scroll-pt-8 {
  scroll-padding-top: 2rem;
}

.scroll-pt-80 {
  scroll-padding-top: 20rem;
}

.scroll-pt-9 {
  scroll-padding-top: 2.25rem;
}

.scroll-pt-96 {
  scroll-padding-top: 24rem;
}

.scroll-pt-px {
  scroll-padding-top: 1px;
}

.list-inside {
  list-style-position: inside;
}

.list-outside {
  list-style-position: outside;
}

.list-decimal {
  list-style-type: decimal;
}

.list-disc {
  list-style-type: disc;
}

.list-none {
  list-style-type: none;
}

.list-image-none {
  list-style-image: none;
}

.appearance-none {
  -webkit-appearance: none;
     -moz-appearance: none;
          appearance: none;
}

.columns-1 {
  -moz-columns: 1;
       columns: 1;
}

.columns-10 {
  -moz-columns: 10;
       columns: 10;
}

.columns-11 {
  -moz-columns: 11;
       columns: 11;
}

.columns-12 {
  -moz-columns: 12;
       columns: 12;
}

.columns-2 {
  -moz-columns: 2;
       columns: 2;
}

.columns-2xl {
  -moz-columns: 42rem;
       columns: 42rem;
}

.columns-2xs {
  -moz-columns: 18rem;
       columns: 18rem;
}

.columns-3 {
  -moz-columns: 3;
       columns: 3;
}

.columns-3xl {
  -moz-columns: 48rem;
       columns: 48rem;
}

.columns-3xs {
  -moz-columns: 16rem;
       columns: 16rem;
}

.columns-4 {
  -moz-columns: 4;
       columns: 4;
}

.columns-4xl {
  -moz-columns: 56rem;
       columns: 56rem;
}

.columns-5 {
  -moz-columns: 5;
       columns: 5;
}

.columns-5xl {
  -moz-columns: 64rem;
       columns: 64rem;
}

.columns-6 {
  -moz-columns: 6;
       columns: 6;
}

.columns-6xl {
  -moz-columns: 72rem;
       columns: 72rem;
}

.columns-7 {
  -moz-columns: 7;
       columns: 7;
}

.columns-7xl {
  -moz-columns: 80rem;
       columns: 80rem;
}

.columns-8 {
  -moz-columns: 8;
       columns: 8;
}

.columns-9 {
  -moz-columns: 9;
       columns: 9;
}

.columns-auto {
  -moz-columns: auto;
       columns: auto;
}

.columns-lg {
  -moz-columns: 32rem;
       columns: 32rem;
}

.columns-md {
  -moz-columns: 28rem;
       columns: 28rem;
}

.columns-sm {
  -moz-columns: 24rem;
       columns: 24rem;
}

.columns-xl {
  -moz-columns: 36rem;
       columns: 36rem;
}

.columns-xs {
  -moz-columns: 20rem;
       columns: 20rem;
}

.break-before-auto {
  -moz-column-break-before: auto;
       break-before: auto;
}

.break-before-avoid {
  -moz-column-break-before: avoid;
       break-before: avoid;
}

.break-before-all {
  -moz-column-break-before: all;
       break-before: all;
}

.break-before-avoid-page {
  -moz-column-break-before: avoid;
       break-before: avoid-page;
}

.break-before-page {
  -moz-column-break-before: page;
       break-before: page;
}

.break-before-left {
  -moz-column-break-before: left;
       break-before: left;
}

.break-before-right {
  -moz-column-break-before: right;
       break-before: right;
}

.break-before-column {
  -moz-column-break-before: column;
       break-before: column;
}

.break-inside-auto {
  -moz-column-break-inside: auto;
       break-inside: auto;
}

.break-inside-avoid {
  -moz-column-break-inside: avoid;
       break-inside: avoid;
}

.break-inside-avoid-page {
  break-inside: avoid-page;
}

.break-inside-avoid-column {
  -moz-column-break-inside: avoid;
       break-inside: avoid-column;
}

.break-after-auto {
  -moz-column-break-after: auto;
       break-after: auto;
}

.break-after-avoid {
  -moz-column-break-after: avoid;
       break-after: avoid;
}

.break-after-all {
  -moz-column-break-after: all;
       break-after: all;
}

.break-after-avoid-page {
  -moz-column-break-after: avoid;
       break-after: avoid-page;
}

.break-after-page {
  -moz-column-break-after: page;
       break-after: page;
}

.break-after-left {
  -moz-column-break-after: left;
       break-after: left;
}

.break-after-right {
  -moz-column-break-after: right;
       break-after: right;
}

.break-after-column {
  -moz-column-break-after: column;
       break-after: column;
}

.auto-cols-auto {
  grid-auto-columns: auto;
}

.auto-cols-fr {
  grid-auto-columns: minmax(0, 1fr);
}

.auto-cols-max {
  grid-auto-columns: max-content;
}

.auto-cols-min {
  grid-auto-columns: min-content;
}

.grid-flow-row {
  grid-auto-flow: row;
}

.grid-flow-col {
  grid-auto-flow: column;
}

.grid-flow-dense {
  grid-auto-flow: dense;
}

.grid-flow-row-dense {
  grid-auto-flow: row dense;
}

.grid-flow-col-dense {
  grid-auto-flow: column dense;
}

.auto-rows-auto {
  grid-auto-rows: auto;
}

.auto-rows-fr {
  grid-auto-rows: minmax(0, 1fr);
}

.auto-rows-max {
  grid-auto-rows: max-content;
}

.auto-rows-min {
  grid-auto-rows: min-content;
}

.grid-cols-1 {
  grid-template-columns: repeat(1, minmax(0, 1fr));
}

.grid-cols-10 {
  grid-template-columns: repeat(10, minmax(0, 1fr));
}

.grid-cols-11 {
  grid-template-columns: repeat(11, minmax(0, 1fr));
}

.grid-cols-12 {
  grid-template-columns: repeat(12, minmax(0, 1fr));
}

.grid-cols-2 {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

.grid-cols-3 {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}

.grid-cols-4 {
  grid-template-columns: repeat(4, minmax(0, 1fr));
}

.grid-cols-5 {
  grid-template-columns: repeat(5, minmax(0, 1fr));
}

.grid-cols-6 {
  grid-template-columns: repeat(6, minmax(0, 1fr));
}

.grid-cols-7 {
  grid-template-columns: repeat(7, minmax(0, 1fr));
}

.grid-cols-8 {
  grid-template-columns: repeat(8, minmax(0, 1fr));
}

.grid-cols-9 {
  grid-template-columns: repeat(9, minmax(0, 1fr));
}

.grid-cols-none {
  grid-template-columns: none;
}

.grid-rows-1 {
  grid-template-rows: repeat(1, minmax(0, 1fr));
}

.grid-rows-2 {
  grid-template-rows: repeat(2, minmax(0, 1fr));
}

.grid-rows-3 {
  grid-template-rows: repeat(3, minmax(0, 1fr));
}

.grid-rows-4 {
  grid-template-rows: repeat(4, minmax(0, 1fr));
}

.grid-rows-5 {
  grid-template-rows: repeat(5, minmax(0, 1fr));
}

.grid-rows-6 {
  grid-template-rows: repeat(6, minmax(0, 1fr));
}

.grid-rows-none {
  grid-template-rows: none;
}

.flex-row {
  flex-direction: row;
}

.flex-row-reverse {
  flex-direction: row-reverse;
}

.flex-col {
  flex-direction: column;
}

.flex-col-reverse {
  flex-direction: column-reverse;
}

.flex-wrap {
  flex-wrap: wrap;
}

.flex-wrap-reverse {
  flex-wrap: wrap-reverse;
}

.flex-nowrap {
  flex-wrap: nowrap;
}

.place-content-center {
  place-content: center;
}

.place-content-start {
  place-content: start;
}

.place-content-end {
  place-content: end;
}

.place-content-between {
  place-content: space-between;
}

.place-content-around {
  place-content: space-around;
}

.place-content-evenly {
  place-content: space-evenly;
}

.place-content-baseline {
  place-content: baseline;
}

.place-content-stretch {
  place-content: stretch;
}

.place-items-start {
  place-items: start;
}

.place-items-end {
  place-items: end;
}

.place-items-center {
  place-items: center;
}

.place-items-baseline {
  place-items: baseline;
}

.place-items-stretch {
  place-items: stretch;
}

.content-normal {
  align-content: normal;
}

.content-center {
  align-content: center;
}

.content-start {
  align-content: flex-start;
}

.content-end {
  align-content: flex-end;
}

.content-between {
  align-content: space-between;
}

.content-around {
  align-content: space-around;
}

.content-evenly {
  align-content: space-evenly;
}

.content-baseline {
  align-content: baseline;
}

.content-stretch {
  align-content: stretch;
}

.items-start {
  align-items: flex-start;
}

.items-end {
  align-items: flex-end;
}

.items-center {
  align-items: center;
}

.items-baseline {
  align-items: baseline;
}

.items-stretch {
  align-items: stretch;
}

.justify-normal {
  justify-content: normal;
}

.justify-start {
  justify-content: flex-start;
}

.justify-end {
  justify-content: flex-end;
}

.justify-center {
  justify-content: center;
}

.justify-between {
  justify-content: space-between;
}

.justify-around {
  justify-content: space-around;
}

.justify-evenly {
  justify-content: space-evenly;
}

.justify-stretch {
  justify-content: stretch;
}

.justify-items-start {
  justify-items: start;
}

.justify-items-end {
  justify-items: end;
}

.justify-items-center {
  justify-items: center;
}

.justify-items-stretch {
  justify-items: stretch;
}

.gap-0 {
  gap: 0px;
}

.gap-0.5 {
  gap: 0.125rem;
}

.gap-1 {
  gap: 0.25rem;
}

.gap-1.5 {
  gap: 0.375rem;
}

.gap-10 {
  gap: 2.5rem;
}

.gap-11 {
  gap: 2.75rem;
}

.gap-12 {
  gap: 3rem;
}

.gap-14 {
  gap: 3.5rem;
}

.gap-16 {
  gap: 4rem;
}

.gap-2 {
  gap: 0.5rem;
}

.gap-2.5 {
  gap: 0.625rem;
}

.gap-20 {
  gap: 5rem;
}

.gap-24 {
  gap: 6rem;
}

.gap-28 {
  gap: 7rem;
}

.gap-3 {
  gap: 0.75rem;
}

.gap-3.5 {
  gap: 0.875rem;
}

.gap-32 {
  gap: 8rem;
}

.gap-36 {
  gap: 9rem;
}

.gap-4 {
  gap: 1rem;
}

.gap-40 {
  gap: 10rem;
}

.gap-44 {
  gap: 11rem;
}

.gap-48 {
  gap: 12rem;
}

.gap-5 {
  gap: 1.25rem;
}

.gap-52 {
  gap: 13rem;
}

.gap-56 {
  gap: 14rem;
}

.gap-6 {
  gap: 1.5rem;
}

.gap-60 {
  gap: 15rem;
}

.gap-64 {
  gap: 16rem;
}

.gap-7 {
  gap: 1.75rem;
}

.gap-72 {
  gap: 18rem;
}

.gap-8 {
  gap: 2rem;
}

.gap-80 {
  gap: 20rem;
}

.gap-9 {
  gap: 2.25rem;
}

.gap-96 {
  gap: 24rem;
}

.gap-px {
  gap: 1px;
}

.gap-x-0 {
  -moz-column-gap: 0px;
       column-gap: 0px;
}

.gap-x-0.5 {
  -moz-column-gap: 0.125rem;
       column-gap: 0.125rem;
}

.gap-x-1 {
  -moz-column-gap: 0.25rem;
       column-gap: 0.25rem;
}

.gap-x-1.5 {
  -moz-column-gap: 0.375rem;
       column-gap: 0.375rem;
}

.gap-x-10 {
  -moz-column-gap: 2.5rem;
       column-gap: 2.5rem;
}

.gap-x-11 {
  -moz-column-gap: 2.75rem;
       column-gap: 2.75rem;
}

.gap-x-12 {
  -moz-column-gap: 3rem;
       column-gap: 3rem;
}

.gap-x-14 {
  -moz-column-gap: 3.5rem;
       column-gap: 3.5rem;
}

.gap-x-16 {
  -moz-column-gap: 4rem;
       column-gap: 4rem;
}

.gap-x-2 {
  -moz-column-gap: 0.5rem;
       column-gap: 0.5rem;
}

.gap-x-2.5 {
  -moz-column-gap: 0.625rem;
       column-gap: 0.625rem;
}

.gap-x-20 {
  -moz-column-gap: 5rem;
       column-gap: 5rem;
}

.gap-x-24 {
  -moz-column-gap: 6rem;
       column-gap: 6rem;
}

.gap-x-28 {
  -moz-column-gap: 7rem;
       column-gap: 7rem;
}

.gap-x-3 {
  -moz-column-gap: 0.75rem;
       column-gap: 0.75rem;
}

.gap-x-3.5 {
  -moz-column-gap: 0.875rem;
       column-gap: 0.875rem;
}

.gap-x-32 {
  -moz-column-gap: 8rem;
       column-gap: 8rem;
}

.gap-x-36 {
  -moz-column-gap: 9rem;
       column-gap: 9rem;
}

.gap-x-4 {
  -moz-column-gap: 1rem;
       column-gap: 1rem;
}

.gap-x-40 {
  -moz-column-gap: 10rem;
       column-gap: 10rem;
}

.gap-x-44 {
  -moz-column-gap: 11rem;
       column-gap: 11rem;
}

.gap-x-48 {
  -moz-column-gap: 12rem;
       column-gap: 12rem;
}

.gap-x-5 {
  -moz-column-gap: 1.25rem;
       column-gap: 1.25rem;
}

.gap-x-52 {
  -moz-column-gap: 13rem;
       column-gap: 13rem;
}

.gap-x-56 {
  -moz-column-gap: 14rem;
       column-gap: 14rem;
}

.gap-x-6 {
  -moz-column-gap: 1.5rem;
       column-gap: 1.5rem;
}

.gap-x-60 {
  -moz-column-gap: 15rem;
       column-gap: 15rem;
}

.gap-x-64 {
  -moz-column-gap: 16rem;
       column-gap: 16rem;
}

.gap-x-7 {
  -moz-column-gap: 1.75rem;
       column-gap: 1.75rem;
}

.gap-x-72 {
  -moz-column-gap: 18rem;
       column-gap: 18rem;
}

.gap-x-8 {
  -moz-column-gap: 2rem;
       column-gap: 2rem;
}

.gap-x-80 {
  -moz-column-gap: 20rem;
       column-gap: 20rem;
}

.gap-x-9 {
  -moz-column-gap: 2.25rem;
       column-gap: 2.25rem;
}

.gap-x-96 {
  -moz-column-gap: 24rem;
       column-gap: 24rem;
}

.gap-x-px {
  -moz-column-gap: 1px;
       column-gap: 1px;
}

.gap-y-0 {
  row-gap: 0px;
}

.gap-y-0.5 {
  row-gap: 0.125rem;
}

.gap-y-1 {
  row-gap: 0.25rem;
}

.gap-y-1.5 {
  row-gap: 0.375rem;
}

.gap-y-10 {
  row-gap: 2.5rem;
}

.gap-y-11 {
  row-gap: 2.75rem;
}

.gap-y-12 {
  row-gap: 3rem;
}

.gap-y-14 {
  row-gap: 3.5rem;
}

.gap-y-16 {
  row-gap: 4rem;
}

.gap-y-2 {
  row-gap: 0.5rem;
}

.gap-y-2.5 {
  row-gap: 0.625rem;
}

.gap-y-20 {
  row-gap: 5rem;
}

.gap-y-24 {
  row-gap: 6rem;
}

.gap-y-28 {
  row-gap: 7rem;
}

.gap-y-3 {
  row-gap: 0.75rem;
}

.gap-y-3.5 {
  row-gap: 0.875rem;
}

.gap-y-32 {
  row-gap: 8rem;
}

.gap-y-36 {
  row-gap: 9rem;
}

.gap-y-4 {
  row-gap: 1rem;
}

.gap-y-40 {
  row-gap: 10rem;
}

.gap-y-44 {
  row-gap: 11rem;
}

.gap-y-48 {
  row-gap: 12rem;
}

.gap-y-5 {
  row-gap: 1.25rem;
}

.gap-y-52 {
  row-gap: 13rem;
}

.gap-y-56 {
  row-gap: 14rem;
}

.gap-y-6 {
  row-gap: 1.5rem;
}

.gap-y-60 {
  row-gap: 15rem;
}

.gap-y-64 {
  row-gap: 16rem;
}

.gap-y-7 {
  row-gap: 1.75rem;
}

.gap-y-72 {
  row-gap: 18rem;
}

.gap-y-8 {
  row-gap: 2rem;
}

.gap-y-80 {
  row-gap: 20rem;
}

.gap-y-9 {
  row-gap: 2.25rem;
}

.gap-y-96 {
  row-gap: 24rem;
}

.gap-y-px {
  row-gap: 1px;
}

.-space-x-0 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-0px * var(--tw-space-x-reverse));
  margin-left: calc(-0px * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-0.5 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-0.125rem * var(--tw-space-x-reverse));
  margin-left: calc(-0.125rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-1 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-0.25rem * var(--tw-space-x-reverse));
  margin-left: calc(-0.25rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-1.5 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-0.375rem * var(--tw-space-x-reverse));
  margin-left: calc(-0.375rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-10 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-2.5rem * var(--tw-space-x-reverse));
  margin-left: calc(-2.5rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-11 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-2.75rem * var(--tw-space-x-reverse));
  margin-left: calc(-2.75rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-12 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-3rem * var(--tw-space-x-reverse));
  margin-left: calc(-3rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-14 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-3.5rem * var(--tw-space-x-reverse));
  margin-left: calc(-3.5rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-16 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-4rem * var(--tw-space-x-reverse));
  margin-left: calc(-4rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-2 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-0.5rem * var(--tw-space-x-reverse));
  margin-left: calc(-0.5rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-2.5 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-0.625rem * var(--tw-space-x-reverse));
  margin-left: calc(-0.625rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-20 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-5rem * var(--tw-space-x-reverse));
  margin-left: calc(-5rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-24 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-6rem * var(--tw-space-x-reverse));
  margin-left: calc(-6rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-28 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-7rem * var(--tw-space-x-reverse));
  margin-left: calc(-7rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-3 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-0.75rem * var(--tw-space-x-reverse));
  margin-left: calc(-0.75rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-3.5 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-0.875rem * var(--tw-space-x-reverse));
  margin-left: calc(-0.875rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-32 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-8rem * var(--tw-space-x-reverse));
  margin-left: calc(-8rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-36 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-9rem * var(--tw-space-x-reverse));
  margin-left: calc(-9rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-4 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-1rem * var(--tw-space-x-reverse));
  margin-left: calc(-1rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-40 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-10rem * var(--tw-space-x-reverse));
  margin-left: calc(-10rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-44 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-11rem * var(--tw-space-x-reverse));
  margin-left: calc(-11rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-48 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-12rem * var(--tw-space-x-reverse));
  margin-left: calc(-12rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-5 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-1.25rem * var(--tw-space-x-reverse));
  margin-left: calc(-1.25rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-52 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-13rem * var(--tw-space-x-reverse));
  margin-left: calc(-13rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-56 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-14rem * var(--tw-space-x-reverse));
  margin-left: calc(-14rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-6 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-1.5rem * var(--tw-space-x-reverse));
  margin-left: calc(-1.5rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-60 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-15rem * var(--tw-space-x-reverse));
  margin-left: calc(-15rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-64 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-16rem * var(--tw-space-x-reverse));
  margin-left: calc(-16rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-7 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-1.75rem * var(--tw-space-x-reverse));
  margin-left: calc(-1.75rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-72 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-18rem * var(--tw-space-x-reverse));
  margin-left: calc(-18rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-8 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-2rem * var(--tw-space-x-reverse));
  margin-left: calc(-2rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-80 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-20rem * var(--tw-space-x-reverse));
  margin-left: calc(-20rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-9 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-2.25rem * var(--tw-space-x-reverse));
  margin-left: calc(-2.25rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-96 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-24rem * var(--tw-space-x-reverse));
  margin-left: calc(-24rem * calc(1 - var(--tw-space-x-reverse)));
}

.-space-x-px > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(-1px * var(--tw-space-x-reverse));
  margin-left: calc(-1px * calc(1 - var(--tw-space-x-reverse)));
}

.-space-y-0 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-0px * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-0px * var(--tw-space-y-reverse));
}

.-space-y-0.5 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-0.125rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-0.125rem * var(--tw-space-y-reverse));
}

.-space-y-1 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-0.25rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-0.25rem * var(--tw-space-y-reverse));
}

.-space-y-1.5 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-0.375rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-0.375rem * var(--tw-space-y-reverse));
}

.-space-y-10 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-2.5rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-2.5rem * var(--tw-space-y-reverse));
}

.-space-y-11 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-2.75rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-2.75rem * var(--tw-space-y-reverse));
}

.-space-y-12 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-3rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-3rem * var(--tw-space-y-reverse));
}

.-space-y-14 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-3.5rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-3.5rem * var(--tw-space-y-reverse));
}

.-space-y-16 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-4rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-4rem * var(--tw-space-y-reverse));
}

.-space-y-2 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-0.5rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-0.5rem * var(--tw-space-y-reverse));
}

.-space-y-2.5 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-0.625rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-0.625rem * var(--tw-space-y-reverse));
}

.-space-y-20 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-5rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-5rem * var(--tw-space-y-reverse));
}

.-space-y-24 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-6rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-6rem * var(--tw-space-y-reverse));
}

.-space-y-28 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-7rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-7rem * var(--tw-space-y-reverse));
}

.-space-y-3 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-0.75rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-0.75rem * var(--tw-space-y-reverse));
}

.-space-y-3.5 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-0.875rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-0.875rem * var(--tw-space-y-reverse));
}

.-space-y-32 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-8rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-8rem * var(--tw-space-y-reverse));
}

.-space-y-36 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-9rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-9rem * var(--tw-space-y-reverse));
}

.-space-y-4 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-1rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-1rem * var(--tw-space-y-reverse));
}

.-space-y-40 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-10rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-10rem * var(--tw-space-y-reverse));
}

.-space-y-44 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-11rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-11rem * var(--tw-space-y-reverse));
}

.-space-y-48 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-12rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-12rem * var(--tw-space-y-reverse));
}

.-space-y-5 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-1.25rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-1.25rem * var(--tw-space-y-reverse));
}

.-space-y-52 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-13rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-13rem * var(--tw-space-y-reverse));
}

.-space-y-56 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-14rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-14rem * var(--tw-space-y-reverse));
}

.-space-y-6 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-1.5rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-1.5rem * var(--tw-space-y-reverse));
}

.-space-y-60 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-15rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-15rem * var(--tw-space-y-reverse));
}

.-space-y-64 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-16rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-16rem * var(--tw-space-y-reverse));
}

.-space-y-7 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-1.75rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-1.75rem * var(--tw-space-y-reverse));
}

.-space-y-72 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-18rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-18rem * var(--tw-space-y-reverse));
}

.-space-y-8 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-2rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-2rem * var(--tw-space-y-reverse));
}

.-space-y-80 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-20rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-20rem * var(--tw-space-y-reverse));
}

.-space-y-9 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-2.25rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-2.25rem * var(--tw-space-y-reverse));
}

.-space-y-96 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-24rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-24rem * var(--tw-space-y-reverse));
}

.-space-y-px > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(-1px * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(-1px * var(--tw-space-y-reverse));
}

.space-x-0 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(0px * var(--tw-space-x-reverse));
  margin-left: calc(0px * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-0.5 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(0.125rem * var(--tw-space-x-reverse));
  margin-left: calc(0.125rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-1 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(0.25rem * var(--tw-space-x-reverse));
  margin-left: calc(0.25rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-1.5 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(0.375rem * var(--tw-space-x-reverse));
  margin-left: calc(0.375rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-10 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(2.5rem * var(--tw-space-x-reverse));
  margin-left: calc(2.5rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-11 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(2.75rem * var(--tw-space-x-reverse));
  margin-left: calc(2.75rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-12 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(3rem * var(--tw-space-x-reverse));
  margin-left: calc(3rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-14 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(3.5rem * var(--tw-space-x-reverse));
  margin-left: calc(3.5rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-16 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(4rem * var(--tw-space-x-reverse));
  margin-left: calc(4rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-2 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(0.5rem * var(--tw-space-x-reverse));
  margin-left: calc(0.5rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-2.5 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(0.625rem * var(--tw-space-x-reverse));
  margin-left: calc(0.625rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-20 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(5rem * var(--tw-space-x-reverse));
  margin-left: calc(5rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-24 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(6rem * var(--tw-space-x-reverse));
  margin-left: calc(6rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-28 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(7rem * var(--tw-space-x-reverse));
  margin-left: calc(7rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-3 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(0.75rem * var(--tw-space-x-reverse));
  margin-left: calc(0.75rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-3.5 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(0.875rem * var(--tw-space-x-reverse));
  margin-left: calc(0.875rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-32 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(8rem * var(--tw-space-x-reverse));
  margin-left: calc(8rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-36 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(9rem * var(--tw-space-x-reverse));
  margin-left: calc(9rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-4 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(1rem * var(--tw-space-x-reverse));
  margin-left: calc(1rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-40 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(10rem * var(--tw-space-x-reverse));
  margin-left: calc(10rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-44 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(11rem * var(--tw-space-x-reverse));
  margin-left: calc(11rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-48 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(12rem * var(--tw-space-x-reverse));
  margin-left: calc(12rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-5 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(1.25rem * var(--tw-space-x-reverse));
  margin-left: calc(1.25rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-52 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(13rem * var(--tw-space-x-reverse));
  margin-left: calc(13rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-56 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(14rem * var(--tw-space-x-reverse));
  margin-left: calc(14rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-6 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(1.5rem * var(--tw-space-x-reverse));
  margin-left: calc(1.5rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-60 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(15rem * var(--tw-space-x-reverse));
  margin-left: calc(15rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-64 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(16rem * var(--tw-space-x-reverse));
  margin-left: calc(16rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-7 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(1.75rem * var(--tw-space-x-reverse));
  margin-left: calc(1.75rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-72 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(18rem * var(--tw-space-x-reverse));
  margin-left: calc(18rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-8 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(2rem * var(--tw-space-x-reverse));
  margin-left: calc(2rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-80 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(20rem * var(--tw-space-x-reverse));
  margin-left: calc(20rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-9 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(2.25rem * var(--tw-space-x-reverse));
  margin-left: calc(2.25rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-96 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(24rem * var(--tw-space-x-reverse));
  margin-left: calc(24rem * calc(1 - var(--tw-space-x-reverse)));
}

.space-x-px > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 0;
  margin-right: calc(1px * var(--tw-space-x-reverse));
  margin-left: calc(1px * calc(1 - var(--tw-space-x-reverse)));
}

.space-y-0 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(0px * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(0px * var(--tw-space-y-reverse));
}

.space-y-0.5 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(0.125rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(0.125rem * var(--tw-space-y-reverse));
}

.space-y-1 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(0.25rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(0.25rem * var(--tw-space-y-reverse));
}

.space-y-1.5 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(0.375rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(0.375rem * var(--tw-space-y-reverse));
}

.space-y-10 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(2.5rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(2.5rem * var(--tw-space-y-reverse));
}

.space-y-11 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(2.75rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(2.75rem * var(--tw-space-y-reverse));
}

.space-y-12 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(3rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(3rem * var(--tw-space-y-reverse));
}

.space-y-14 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(3.5rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(3.5rem * var(--tw-space-y-reverse));
}

.space-y-16 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(4rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(4rem * var(--tw-space-y-reverse));
}

.space-y-2 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(0.5rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(0.5rem * var(--tw-space-y-reverse));
}

.space-y-2.5 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(0.625rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(0.625rem * var(--tw-space-y-reverse));
}

.space-y-20 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(5rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(5rem * var(--tw-space-y-reverse));
}

.space-y-24 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(6rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(6rem * var(--tw-space-y-reverse));
}

.space-y-28 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(7rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(7rem * var(--tw-space-y-reverse));
}

.space-y-3 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(0.75rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(0.75rem * var(--tw-space-y-reverse));
}

.space-y-3.5 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(0.875rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(0.875rem * var(--tw-space-y-reverse));
}

.space-y-32 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(8rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(8rem * var(--tw-space-y-reverse));
}

.space-y-36 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(9rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(9rem * var(--tw-space-y-reverse));
}

.space-y-4 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(1rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(1rem * var(--tw-space-y-reverse));
}

.space-y-40 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(10rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(10rem * var(--tw-space-y-reverse));
}

.space-y-44 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(11rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(11rem * var(--tw-space-y-reverse));
}

.space-y-48 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(12rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(12rem * var(--tw-space-y-reverse));
}

.space-y-5 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(1.25rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(1.25rem * var(--tw-space-y-reverse));
}

.space-y-52 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(13rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(13rem * var(--tw-space-y-reverse));
}

.space-y-56 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(14rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(14rem * var(--tw-space-y-reverse));
}

.space-y-6 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(1.5rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(1.5rem * var(--tw-space-y-reverse));
}

.space-y-60 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(15rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(15rem * var(--tw-space-y-reverse));
}

.space-y-64 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(16rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(16rem * var(--tw-space-y-reverse));
}

.space-y-7 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(1.75rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(1.75rem * var(--tw-space-y-reverse));
}

.space-y-72 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(18rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(18rem * var(--tw-space-y-reverse));
}

.space-y-8 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(2rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(2rem * var(--tw-space-y-reverse));
}

.space-y-80 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(20rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(20rem * var(--tw-space-y-reverse));
}

.space-y-9 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(2.25rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(2.25rem * var(--tw-space-y-reverse));
}

.space-y-96 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(24rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(24rem * var(--tw-space-y-reverse));
}

.space-y-px > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(1px * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(1px * var(--tw-space-y-reverse));
}

.space-y-reverse > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 1;
}

.space-x-reverse > :not([hidden]) ~ :not([hidden]) {
  --tw-space-x-reverse: 1;
}

.divide-x > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-x-reverse: 0;
  border-right-width: calc(1px * var(--tw-divide-x-reverse));
  border-left-width: calc(1px * calc(1 - var(--tw-divide-x-reverse)));
}

.divide-x-0 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-x-reverse: 0;
  border-right-width: calc(0px * var(--tw-divide-x-reverse));
  border-left-width: calc(0px * calc(1 - var(--tw-divide-x-reverse)));
}

.divide-x-2 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-x-reverse: 0;
  border-right-width: calc(2px * var(--tw-divide-x-reverse));
  border-left-width: calc(2px * calc(1 - var(--tw-divide-x-reverse)));
}

.divide-x-4 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-x-reverse: 0;
  border-right-width: calc(4px * var(--tw-divide-x-reverse));
  border-left-width: calc(4px * calc(1 - var(--tw-divide-x-reverse)));
}

.divide-x-8 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-x-reverse: 0;
  border-right-width: calc(8px * var(--tw-divide-x-reverse));
  border-left-width: calc(8px * calc(1 - var(--tw-divide-x-reverse)));
}

.divide-y > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-y-reverse: 0;
  border-top-width: calc(1px * calc(1 - var(--tw-divide-y-reverse)));
  border-bottom-width: calc(1px * var(--tw-divide-y-reverse));
}

.divide-y-0 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-y-reverse: 0;
  border-top-width: calc(0px * calc(1 - var(--tw-divide-y-reverse)));
  border-bottom-width: calc(0px * var(--tw-divide-y-reverse));
}

.divide-y-2 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-y-reverse: 0;
  border-top-width: calc(2px * calc(1 - var(--tw-divide-y-reverse)));
  border-bottom-width: calc(2px * var(--tw-divide-y-reverse));
}

.divide-y-4 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-y-reverse: 0;
  border-top-width: calc(4px * calc(1 - var(--tw-divide-y-reverse)));
  border-bottom-width: calc(4px * var(--tw-divide-y-reverse));
}

.divide-y-8 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-y-reverse: 0;
  border-top-width: calc(8px * calc(1 - var(--tw-divide-y-reverse)));
  border-bottom-width: calc(8px * var(--tw-divide-y-reverse));
}

.divide-y-reverse > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-y-reverse: 1;
}

.divide-x-reverse > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-x-reverse: 1;
}

.divide-solid > :not([hidden]) ~ :not([hidden]) {
  border-style: solid;
}

.divide-dashed > :not([hidden]) ~ :not([hidden]) {
  border-style: dashed;
}

.divide-dotted > :not([hidden]) ~ :not([hidden]) {
  border-style: dotted;
}

.divide-double > :not([hidden]) ~ :not([hidden]) {
  border-style: double;
}

.divide-none > :not([hidden]) ~ :not([hidden]) {
  border-style: none;
}

.divide-amber-100 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(254 243 199 / var(--tw-divide-opacity));
}

.divide-amber-200 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(253 230 138 / var(--tw-divide-opacity));
}

.divide-amber-300 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(252 211 77 / var(--tw-divide-opacity));
}

.divide-amber-400 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(251 191 36 / var(--tw-divide-opacity));
}

.divide-amber-50 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(255 251 235 / var(--tw-divide-opacity));
}

.divide-amber-500 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(245 158 11 / var(--tw-divide-opacity));
}

.divide-amber-600 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(217 119 6 / var(--tw-divide-opacity));
}

.divide-amber-700 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(180 83 9 / var(--tw-divide-opacity));
}

.divide-amber-800 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(146 64 14 / var(--tw-divide-opacity));
}

.divide-amber-900 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(120 53 15 / var(--tw-divide-opacity));
}

.divide-amber-950 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(69 26 3 / var(--tw-divide-opacity));
}

.divide-black > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(0 0 0 / var(--tw-divide-opacity));
}

.divide-blue-100 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(219 234 254 / var(--tw-divide-opacity));
}

.divide-blue-200 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(191 219 254 / var(--tw-divide-opacity));
}

.divide-blue-300 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(147 197 253 / var(--tw-divide-opacity));
}

.divide-blue-400 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(96 165 250 / var(--tw-divide-opacity));
}

.divide-blue-50 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(239 246 255 / var(--tw-divide-opacity));
}

.divide-blue-500 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(59 130 246 / var(--tw-divide-opacity));
}

.divide-blue-600 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(37 99 235 / var(--tw-divide-opacity));
}

.divide-blue-700 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(29 78 216 / var(--tw-divide-opacity));
}

.divide-blue-800 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(30 64 175 / var(--tw-divide-opacity));
}

.divide-blue-900 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(30 58 138 / var(--tw-divide-opacity));
}

.divide-blue-950 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(23 37 84 / var(--tw-divide-opacity));
}

.divide-current > :not([hidden]) ~ :not([hidden]) {
  border-color: currentColor;
}

.divide-cyan-100 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(207 250 254 / var(--tw-divide-opacity));
}

.divide-cyan-200 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(165 243 252 / var(--tw-divide-opacity));
}

.divide-cyan-300 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(103 232 249 / var(--tw-divide-opacity));
}

.divide-cyan-400 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(34 211 238 / var(--tw-divide-opacity));
}

.divide-cyan-50 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(236 254 255 / var(--tw-divide-opacity));
}

.divide-cyan-500 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(6 182 212 / var(--tw-divide-opacity));
}

.divide-cyan-600 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(8 145 178 / var(--tw-divide-opacity));
}

.divide-cyan-700 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(14 116 144 / var(--tw-divide-opacity));
}

.divide-cyan-800 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(21 94 117 / var(--tw-divide-opacity));
}

.divide-cyan-900 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(22 78 99 / var(--tw-divide-opacity));
}

.divide-cyan-950 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(8 51 68 / var(--tw-divide-opacity));
}

.divide-emerald-100 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(209 250 229 / var(--tw-divide-opacity));
}

.divide-emerald-200 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(167 243 208 / var(--tw-divide-opacity));
}

.divide-emerald-300 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(110 231 183 / var(--tw-divide-opacity));
}

.divide-emerald-400 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(52 211 153 / var(--tw-divide-opacity));
}

.divide-emerald-50 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(236 253 245 / var(--tw-divide-opacity));
}

.divide-emerald-500 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(16 185 129 / var(--tw-divide-opacity));
}

.divide-emerald-600 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(5 150 105 / var(--tw-divide-opacity));
}

.divide-emerald-700 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(4 120 87 / var(--tw-divide-opacity));
}

.divide-emerald-800 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(6 95 70 / var(--tw-divide-opacity));
}

.divide-emerald-900 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(6 78 59 / var(--tw-divide-opacity));
}

.divide-emerald-950 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(2 44 34 / var(--tw-divide-opacity));
}

.divide-fuchsia-100 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(250 232 255 / var(--tw-divide-opacity));
}

.divide-fuchsia-200 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(245 208 254 / var(--tw-divide-opacity));
}

.divide-fuchsia-300 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(240 171 252 / var(--tw-divide-opacity));
}

.divide-fuchsia-400 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(232 121 249 / var(--tw-divide-opacity));
}

.divide-fuchsia-50 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(253 244 255 / var(--tw-divide-opacity));
}

.divide-fuchsia-500 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(217 70 239 / var(--tw-divide-opacity));
}

.divide-fuchsia-600 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(192 38 211 / var(--tw-divide-opacity));
}

.divide-fuchsia-700 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(162 28 175 / var(--tw-divide-opacity));
}

.divide-fuchsia-800 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(134 25 143 / var(--tw-divide-opacity));
}

.divide-fuchsia-900 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(112 26 117 / var(--tw-divide-opacity));
}

.divide-fuchsia-950 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(74 4 78 / var(--tw-divide-opacity));
}

.divide-gray-100 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(243 244 246 / var(--tw-divide-opacity));
}

.divide-gray-200 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(229 231 235 / var(--tw-divide-opacity));
}

.divide-gray-300 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(209 213 219 / var(--tw-divide-opacity));
}

.divide-gray-400 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(156 163 175 / var(--tw-divide-opacity));
}

.divide-gray-50 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(249 250 251 / var(--tw-divide-opacity));
}

.divide-gray-500 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(107 114 128 / var(--tw-divide-opacity));
}

.divide-gray-600 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(75 85 99 / var(--tw-divide-opacity));
}

.divide-gray-700 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(55 65 81 / var(--tw-divide-opacity));
}

.divide-gray-800 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(31 41 55 / var(--tw-divide-opacity));
}

.divide-gray-900 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(17 24 39 / var(--tw-divide-opacity));
}

.divide-gray-950 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(3 7 18 / var(--tw-divide-opacity));
}

.divide-green-100 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(220 252 231 / var(--tw-divide-opacity));
}

.divide-green-200 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(187 247 208 / var(--tw-divide-opacity));
}

.divide-green-300 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(134 239 172 / var(--tw-divide-opacity));
}

.divide-green-400 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(74 222 128 / var(--tw-divide-opacity));
}

.divide-green-50 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(240 253 244 / var(--tw-divide-opacity));
}

.divide-green-500 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(34 197 94 / var(--tw-divide-opacity));
}

.divide-green-600 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(22 163 74 / var(--tw-divide-opacity));
}

.divide-green-700 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(21 128 61 / var(--tw-divide-opacity));
}

.divide-green-800 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(22 101 52 / var(--tw-divide-opacity));
}

.divide-green-900 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(20 83 45 / var(--tw-divide-opacity));
}

.divide-green-950 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(5 46 22 / var(--tw-divide-opacity));
}

.divide-indigo-100 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(224 231 255 / var(--tw-divide-opacity));
}

.divide-indigo-200 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(199 210 254 / var(--tw-divide-opacity));
}

.divide-indigo-300 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(165 180 252 / var(--tw-divide-opacity));
}

.divide-indigo-400 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(129 140 248 / var(--tw-divide-opacity));
}

.divide-indigo-50 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(238 242 255 / var(--tw-divide-opacity));
}

.divide-indigo-500 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(99 102 241 / var(--tw-divide-opacity));
}

.divide-indigo-600 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(79 70 229 / var(--tw-divide-opacity));
}

.divide-indigo-700 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(67 56 202 / var(--tw-divide-opacity));
}

.divide-indigo-800 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(55 48 163 / var(--tw-divide-opacity));
}

.divide-indigo-900 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(49 46 129 / var(--tw-divide-opacity));
}

.divide-indigo-950 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(30 27 75 / var(--tw-divide-opacity));
}

.divide-inherit > :not([hidden]) ~ :not([hidden]) {
  border-color: inherit;
}

.divide-lime-100 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(236 252 203 / var(--tw-divide-opacity));
}

.divide-lime-200 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(217 249 157 / var(--tw-divide-opacity));
}

.divide-lime-300 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(190 242 100 / var(--tw-divide-opacity));
}

.divide-lime-400 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(163 230 53 / var(--tw-divide-opacity));
}

.divide-lime-50 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(247 254 231 / var(--tw-divide-opacity));
}

.divide-lime-500 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(132 204 22 / var(--tw-divide-opacity));
}

.divide-lime-600 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(101 163 13 / var(--tw-divide-opacity));
}

.divide-lime-700 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(77 124 15 / var(--tw-divide-opacity));
}

.divide-lime-800 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(63 98 18 / var(--tw-divide-opacity));
}

.divide-lime-900 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(54 83 20 / var(--tw-divide-opacity));
}

.divide-lime-950 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(26 46 5 / var(--tw-divide-opacity));
}

.divide-neutral-100 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(245 245 245 / var(--tw-divide-opacity));
}

.divide-neutral-200 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(229 229 229 / var(--tw-divide-opacity));
}

.divide-neutral-300 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(212 212 212 / var(--tw-divide-opacity));
}

.divide-neutral-400 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(163 163 163 / var(--tw-divide-opacity));
}

.divide-neutral-50 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(250 250 250 / var(--tw-divide-opacity));
}

.divide-neutral-500 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(115 115 115 / var(--tw-divide-opacity));
}

.divide-neutral-600 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(82 82 82 / var(--tw-divide-opacity));
}

.divide-neutral-700 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(64 64 64 / var(--tw-divide-opacity));
}

.divide-neutral-800 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(38 38 38 / var(--tw-divide-opacity));
}

.divide-neutral-900 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(23 23 23 / var(--tw-divide-opacity));
}

.divide-neutral-950 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(10 10 10 / var(--tw-divide-opacity));
}

.divide-orange-100 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(255 237 213 / var(--tw-divide-opacity));
}

.divide-orange-200 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(254 215 170 / var(--tw-divide-opacity));
}

.divide-orange-300 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(253 186 116 / var(--tw-divide-opacity));
}

.divide-orange-400 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(251 146 60 / var(--tw-divide-opacity));
}

.divide-orange-50 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(255 247 237 / var(--tw-divide-opacity));
}

.divide-orange-500 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(249 115 22 / var(--tw-divide-opacity));
}

.divide-orange-600 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(234 88 12 / var(--tw-divide-opacity));
}

.divide-orange-700 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(194 65 12 / var(--tw-divide-opacity));
}

.divide-orange-800 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(154 52 18 / var(--tw-divide-opacity));
}

.divide-orange-900 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(124 45 18 / var(--tw-divide-opacity));
}

.divide-orange-950 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(67 20 7 / var(--tw-divide-opacity));
}

.divide-pink-100 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(252 231 243 / var(--tw-divide-opacity));
}

.divide-pink-200 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(251 207 232 / var(--tw-divide-opacity));
}

.divide-pink-300 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(249 168 212 / var(--tw-divide-opacity));
}

.divide-pink-400 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(244 114 182 / var(--tw-divide-opacity));
}

.divide-pink-50 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(253 242 248 / var(--tw-divide-opacity));
}

.divide-pink-500 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(236 72 153 / var(--tw-divide-opacity));
}

.divide-pink-600 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(219 39 119 / var(--tw-divide-opacity));
}

.divide-pink-700 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(190 24 93 / var(--tw-divide-opacity));
}

.divide-pink-800 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(157 23 77 / var(--tw-divide-opacity));
}

.divide-pink-900 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(131 24 67 / var(--tw-divide-opacity));
}

.divide-pink-950 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(80 7 36 / var(--tw-divide-opacity));
}

.divide-purple-100 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(243 232 255 / var(--tw-divide-opacity));
}

.divide-purple-200 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(233 213 255 / var(--tw-divide-opacity));
}

.divide-purple-300 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(216 180 254 / var(--tw-divide-opacity));
}

.divide-purple-400 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(192 132 252 / var(--tw-divide-opacity));
}

.divide-purple-50 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(250 245 255 / var(--tw-divide-opacity));
}

.divide-purple-500 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(168 85 247 / var(--tw-divide-opacity));
}

.divide-purple-600 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(147 51 234 / var(--tw-divide-opacity));
}

.divide-purple-700 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(126 34 206 / var(--tw-divide-opacity));
}

.divide-purple-800 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(107 33 168 / var(--tw-divide-opacity));
}

.divide-purple-900 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(88 28 135 / var(--tw-divide-opacity));
}

.divide-purple-950 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(59 7 100 / var(--tw-divide-opacity));
}

.divide-red-100 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(254 226 226 / var(--tw-divide-opacity));
}

.divide-red-200 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(254 202 202 / var(--tw-divide-opacity));
}

.divide-red-300 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(252 165 165 / var(--tw-divide-opacity));
}

.divide-red-400 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(248 113 113 / var(--tw-divide-opacity));
}

.divide-red-50 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(254 242 242 / var(--tw-divide-opacity));
}

.divide-red-500 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(239 68 68 / var(--tw-divide-opacity));
}

.divide-red-600 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(220 38 38 / var(--tw-divide-opacity));
}

.divide-red-700 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(185 28 28 / var(--tw-divide-opacity));
}

.divide-red-800 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(153 27 27 / var(--tw-divide-opacity));
}

.divide-red-900 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(127 29 29 / var(--tw-divide-opacity));
}

.divide-red-950 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(69 10 10 / var(--tw-divide-opacity));
}

.divide-rose-100 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(255 228 230 / var(--tw-divide-opacity));
}

.divide-rose-200 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(254 205 211 / var(--tw-divide-opacity));
}

.divide-rose-300 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(253 164 175 / var(--tw-divide-opacity));
}

.divide-rose-400 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(251 113 133 / var(--tw-divide-opacity));
}

.divide-rose-50 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(255 241 242 / var(--tw-divide-opacity));
}

.divide-rose-500 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(244 63 94 / var(--tw-divide-opacity));
}

.divide-rose-600 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(225 29 72 / var(--tw-divide-opacity));
}

.divide-rose-700 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(190 18 60 / var(--tw-divide-opacity));
}

.divide-rose-800 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(159 18 57 / var(--tw-divide-opacity));
}

.divide-rose-900 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(136 19 55 / var(--tw-divide-opacity));
}

.divide-rose-950 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(76 5 25 / var(--tw-divide-opacity));
}

.divide-sky-100 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(224 242 254 / var(--tw-divide-opacity));
}

.divide-sky-200 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(186 230 253 / var(--tw-divide-opacity));
}

.divide-sky-300 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(125 211 252 / var(--tw-divide-opacity));
}

.divide-sky-400 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(56 189 248 / var(--tw-divide-opacity));
}

.divide-sky-50 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(240 249 255 / var(--tw-divide-opacity));
}

.divide-sky-500 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(14 165 233 / var(--tw-divide-opacity));
}

.divide-sky-600 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(2 132 199 / var(--tw-divide-opacity));
}

.divide-sky-700 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(3 105 161 / var(--tw-divide-opacity));
}

.divide-sky-800 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(7 89 133 / var(--tw-divide-opacity));
}

.divide-sky-900 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(12 74 110 / var(--tw-divide-opacity));
}

.divide-sky-950 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(8 47 73 / var(--tw-divide-opacity));
}

.divide-slate-100 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(241 245 249 / var(--tw-divide-opacity));
}

.divide-slate-200 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(226 232 240 / var(--tw-divide-opacity));
}

.divide-slate-300 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(203 213 225 / var(--tw-divide-opacity));
}

.divide-slate-400 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(148 163 184 / var(--tw-divide-opacity));
}

.divide-slate-50 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(248 250 252 / var(--tw-divide-opacity));
}

.divide-slate-500 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(100 116 139 / var(--tw-divide-opacity));
}

.divide-slate-600 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(71 85 105 / var(--tw-divide-opacity));
}

.divide-slate-700 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(51 65 85 / var(--tw-divide-opacity));
}

.divide-slate-800 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(30 41 59 / var(--tw-divide-opacity));
}

.divide-slate-900 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(15 23 42 / var(--tw-divide-opacity));
}

.divide-slate-950 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(2 6 23 / var(--tw-divide-opacity));
}

.divide-stone-100 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(245 245 244 / var(--tw-divide-opacity));
}

.divide-stone-200 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(231 229 228 / var(--tw-divide-opacity));
}

.divide-stone-300 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(214 211 209 / var(--tw-divide-opacity));
}

.divide-stone-400 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(168 162 158 / var(--tw-divide-opacity));
}

.divide-stone-50 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(250 250 249 / var(--tw-divide-opacity));
}

.divide-stone-500 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(120 113 108 / var(--tw-divide-opacity));
}

.divide-stone-600 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(87 83 78 / var(--tw-divide-opacity));
}

.divide-stone-700 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(68 64 60 / var(--tw-divide-opacity));
}

.divide-stone-800 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(41 37 36 / var(--tw-divide-opacity));
}

.divide-stone-900 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(28 25 23 / var(--tw-divide-opacity));
}

.divide-stone-950 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(12 10 9 / var(--tw-divide-opacity));
}

.divide-teal-100 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(204 251 241 / var(--tw-divide-opacity));
}

.divide-teal-200 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(153 246 228 / var(--tw-divide-opacity));
}

.divide-teal-300 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(94 234 212 / var(--tw-divide-opacity));
}

.divide-teal-400 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(45 212 191 / var(--tw-divide-opacity));
}

.divide-teal-50 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(240 253 250 / var(--tw-divide-opacity));
}

.divide-teal-500 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(20 184 166 / var(--tw-divide-opacity));
}

.divide-teal-600 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(13 148 136 / var(--tw-divide-opacity));
}

.divide-teal-700 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(15 118 110 / var(--tw-divide-opacity));
}

.divide-teal-800 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(17 94 89 / var(--tw-divide-opacity));
}

.divide-teal-900 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(19 78 74 / var(--tw-divide-opacity));
}

.divide-teal-950 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(4 47 46 / var(--tw-divide-opacity));
}

.divide-transparent > :not([hidden]) ~ :not([hidden]) {
  border-color: transparent;
}

.divide-violet-100 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(237 233 254 / var(--tw-divide-opacity));
}

.divide-violet-200 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(221 214 254 / var(--tw-divide-opacity));
}

.divide-violet-300 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(196 181 253 / var(--tw-divide-opacity));
}

.divide-violet-400 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(167 139 250 / var(--tw-divide-opacity));
}

.divide-violet-50 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(245 243 255 / var(--tw-divide-opacity));
}

.divide-violet-500 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(139 92 246 / var(--tw-divide-opacity));
}

.divide-violet-600 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(124 58 237 / var(--tw-divide-opacity));
}

.divide-violet-700 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(109 40 217 / var(--tw-divide-opacity));
}

.divide-violet-800 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(91 33 182 / var(--tw-divide-opacity));
}

.divide-violet-900 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(76 29 149 / var(--tw-divide-opacity));
}

.divide-violet-950 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(46 16 101 / var(--tw-divide-opacity));
}

.divide-white > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(255 255 255 / var(--tw-divide-opacity));
}

.divide-yellow-100 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(254 249 195 / var(--tw-divide-opacity));
}

.divide-yellow-200 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(254 240 138 / var(--tw-divide-opacity));
}

.divide-yellow-300 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(253 224 71 / var(--tw-divide-opacity));
}

.divide-yellow-400 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(250 204 21 / var(--tw-divide-opacity));
}

.divide-yellow-50 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(254 252 232 / var(--tw-divide-opacity));
}

.divide-yellow-500 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(234 179 8 / var(--tw-divide-opacity));
}

.divide-yellow-600 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(202 138 4 / var(--tw-divide-opacity));
}

.divide-yellow-700 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(161 98 7 / var(--tw-divide-opacity));
}

.divide-yellow-800 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(133 77 14 / var(--tw-divide-opacity));
}

.divide-yellow-900 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(113 63 18 / var(--tw-divide-opacity));
}

.divide-yellow-950 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(66 32 6 / var(--tw-divide-opacity));
}

.divide-zinc-100 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(244 244 245 / var(--tw-divide-opacity));
}

.divide-zinc-200 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(228 228 231 / var(--tw-divide-opacity));
}

.divide-zinc-300 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(212 212 216 / var(--tw-divide-opacity));
}

.divide-zinc-400 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(161 161 170 / var(--tw-divide-opacity));
}

.divide-zinc-50 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(250 250 250 / var(--tw-divide-opacity));
}

.divide-zinc-500 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(113 113 122 / var(--tw-divide-opacity));
}

.divide-zinc-600 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(82 82 91 / var(--tw-divide-opacity));
}

.divide-zinc-700 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(63 63 70 / var(--tw-divide-opacity));
}

.divide-zinc-800 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(39 39 42 / var(--tw-divide-opacity));
}

.divide-zinc-900 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(24 24 27 / var(--tw-divide-opacity));
}

.divide-zinc-950 > :not([hidden]) ~ :not([hidden]) {
  --tw-divide-opacity: 1;
  border-color: rgb(9 9 11 / var(--tw-divide-opacity));
}

.place-self-auto {
  place-self: auto;
}

.place-self-start {
  place-self: start;
}

.place-self-end {
  place-self: end;
}

.place-self-center {
  place-self: center;
}

.place-self-stretch {
  place-self: stretch;
}

.self-auto {
  align-self: auto;
}

.self-start {
  align-self: flex-start;
}

.self-end {
  align-self: flex-end;
}

.self-center {
  align-self: center;
}

.self-stretch {
  align-self: stretch;
}

.self-baseline {
  align-self: baseline;
}

.justify-self-auto {
  justify-self: auto;
}

.justify-self-start {
  justify-self: start;
}

.justify-self-end {
  justify-self: end;
}

.justify-self-center {
  justify-self: center;
}

.justify-self-stretch {
  justify-self: stretch;
}

.overflow-auto {
  overflow: auto;
}

.overflow-hidden {
  overflow: hidden;
}

.overflow-clip {
  overflow: clip;
}

.overflow-visible {
  overflow: visible;
}

.overflow-scroll {
  overflow: scroll;
}

.overflow-x-auto {
  overflow-x: auto;
}

.overflow-y-auto {
  overflow-y: auto;
}

.overflow-x-hidden {
  overflow-x: hidden;
}

.overflow-y-hidden {
  overflow-y: hidden;
}

.overflow-x-clip {
  overflow-x: clip;
}

.overflow-y-clip {
  overflow-y: clip;
}

.overflow-x-visible {
  overflow-x: visible;
}

.overflow-y-visible {
  overflow-y: visible;
}

.overflow-x-scroll {
  overflow-x: scroll;
}

.overflow-y-scroll {
  overflow-y: scroll;
}

.overscroll-auto {
  overscroll-behavior: auto;
}

.overscroll-contain {
  overscroll-behavior: contain;
}

.overscroll-none {
  overscroll-behavior: none;
}

.overscroll-y-auto {
  overscroll-behavior-y: auto;
}

.overscroll-y-contain {
  overscroll-behavior-y: contain;
}

.overscroll-y-none {
  overscroll-behavior-y: none;
}

.overscroll-x-auto {
  overscroll-behavior-x: auto;
}

.overscroll-x-contain {
  overscroll-behavior-x: contain;
}

.overscroll-x-none {
  overscroll-behavior-x: none;
}

.scroll-auto {
  scroll-behavior: auto;
}

.scroll-smooth {
  scroll-behavior: smooth;
}

.truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.text-ellipsis {
  text-overflow: ellipsis;
}

.text-clip {
  text-overflow: clip;
}

.hyphens-none {
  -webkit-hyphens: none;
          hyphens: none;
}

.hyphens-manual {
  -webkit-hyphens: manual;
          hyphens: manual;
}

.hyphens-auto {
  -webkit-hyphens: auto;
          hyphens: auto;
}

.whitespace-normal {
  white-space: normal;
}

.whitespace-nowrap {
  white-space: nowrap;
}

.whitespace-pre {
  white-space: pre;
}

.whitespace-pre-line {
  white-space: pre-line;
}

.whitespace-pre-wrap {
  white-space: pre-wrap;
}

.whitespace-break-spaces {
  white-space: break-spaces;
}

.break-normal {
  overflow-wrap: normal;
  word-break: normal;
}

.break-words {
  overflow-wrap: break-word;
}

.break-all {
  word-break: break-all;
}

.break-keep {
  word-break: keep-all;
}

.rounded {
  border-radius: 0.25rem;
}

.rounded-2xl {
  border-radius: 1rem;
}

.rounded-3xl {
  border-radius: 1.5rem;
}

.rounded-full {
  border-radius: 9999px;
}

.rounded-lg {
  border-radius: 0.5rem;
}

.rounded-md {
  border-radius: 0.375rem;
}

.rounded-none {
  border-radius: 0px;
}

.rounded-sm {
  border-radius: 0.125rem;
}

.rounded-xl {
  border-radius: 0.75rem;
}

.rounded-b {
  border-bottom-right-radius: 0.25rem;
  border-bottom-left-radius: 0.25rem;
}

.rounded-b-2xl {
  border-bottom-right-radius: 1rem;
  border-bottom-left-radius: 1rem;
}

.rounded-b-3xl {
  border-bottom-right-radius: 1.5rem;
  border-bottom-left-radius: 1.5rem;
}

.rounded-b-full {
  border-bottom-right-radius: 9999px;
  border-bottom-left-radius: 9999px;
}

.rounded-b-lg {
  border-bottom-right-radius: 0.5rem;
  border-bottom-left-radius: 0.5rem;
}

.rounded-b-md {
  border-bottom-right-radius: 0.375rem;
  border-bottom-left-radius: 0.375rem;
}

.rounded-b-none {
  border-bottom-right-radius: 0px;
  border-bottom-left-radius: 0px;
}

.rounded-b-sm {
  border-bottom-right-radius: 0.125rem;
  border-bottom-left-radius: 0.125rem;
}

.rounded-b-xl {
  border-bottom-right-radius: 0.75rem;
  border-bottom-left-radius: 0.75rem;
}

.rounded-e {
  border-start-end-radius: 0.25rem;
  border-end-end-radius: 0.25rem;
}

.rounded-e-2xl {
  border-start-end-radius: 1rem;
  border-end-end-radius: 1rem;
}

.rounded-e-3xl {
  border-start-end-radius: 1.5rem;
  border-end-end-radius: 1.5rem;
}

.rounded-e-full {
  border-start-end-radius: 9999px;
  border-end-end-radius: 9999px;
}

.rounded-e-lg {
  border-start-end-radius: 0.5rem;
  border-end-end-radius: 0.5rem;
}

.rounded-e-md {
  border-start-end-radius: 0.375rem;
  border-end-end-radius: 0.375rem;
}

.rounded-e-none {
  border-start-end-radius: 0px;
  border-end-end-radius: 0px;
}

.rounded-e-sm {
  border-start-end-radius: 0.125rem;
  border-end-end-radius: 0.125rem;
}

.rounded-e-xl {
  border-start-end-radius: 0.75rem;
  border-end-end-radius: 0.75rem;
}

.rounded-l {
  border-top-left-radius: 0.25rem;
  border-bottom-left-radius: 0.25rem;
}

.rounded-l-2xl {
  border-top-left-radius: 1rem;
  border-bottom-left-radius: 1rem;
}

.rounded-l-3xl {
  border-top-left-radius: 1.5rem;
  border-bottom-left-radius: 1.5rem;
}

.rounded-l-full {
  border-top-left-radius: 9999px;
  border-bottom-left-radius: 9999px;
}

.rounded-l-lg {
  border-top-left-radius: 0.5rem;
  border-bottom-left-radius: 0.5rem;
}

.rounded-l-md {
  border-top-left-radius: 0.375rem;
  border-bottom-left-radius: 0.375rem;
}

.rounded-l-none {
  border-top-left-radius: 0px;
  border-bottom-left-radius: 0px;
}

.rounded-l-sm {
  border-top-left-radius: 0.125rem;
  border-bottom-left-radius: 0.125rem;
}

.rounded-l-xl {
  border-top-left-radius: 0.75rem;
  border-bottom-left-radius: 0.75rem;
}

.rounded-r {
  border-top-right-radius: 0.25rem;
  border-bottom-right-radius: 0.25rem;
}

.rounded-r-2xl {
  border-top-right-radius: 1rem;
  border-bottom-right-radius: 1rem;
}

.rounded-r-3xl {
  border-top-right-radius: 1.5rem;
  border-bottom-right-radius: 1.5rem;
}

.rounded-r-full {
  border-top-right-radius: 9999px;
  border-bottom-right-radius: 9999px;
}

.rounded-r-lg {
  border-top-right-radius: 0.5rem;
  border-bottom-right-radius: 0.5rem;
}

.rounded-r-md {
  border-top-right-radius: 0.375rem;
  border-bottom-right-radius: 0.375rem;
}

.rounded-r-none {
  border-top-right-radius: 0px;
  border-bottom-right-radius: 0px;
}

.rounded-r-sm {
  border-top-right-radius: 0.125rem;
  border-bottom-right-radius: 0.125rem;
}

.rounded-r-xl {
  border-top-right-radius: 0.75rem;
  border-bottom-right-radius: 0.75rem;
}

.rounded-s {
  border-start-start-radius: 0.25rem;
  border-end-start-radius: 0.25rem;
}

.rounded-s-2xl {
  border-start-start-radius: 1rem;
  border-end-start-radius: 1rem;
}

.rounded-s-3xl {
  border-start-start-radius: 1.5rem;
  border-end-start-radius: 1.5rem;
}

.rounded-s-full {
  border-start-start-radius: 9999px;
  border-end-start-radius: 9999px;
}

.rounded-s-lg {
  border-start-start-radius: 0.5rem;
  border-end-start-radius: 0.5rem;
}

.rounded-s-md {
  border-start-start-radius: 0.375rem;
  border-end-start-radius: 0.375rem;
}

.rounded-s-none {
  border-start-start-radius: 0px;
  border-end-start-radius: 0px;
}

.rounded-s-sm {
  border-start-start-radius: 0.125rem;
  border-end-start-radius: 0.125rem;
}

.rounded-s-xl {
  border-start-start-radius: 0.75rem;
  border-end-start-radius: 0.75rem;
}

.rounded-t {
  border-top-left-radius: 0.25rem;
  border-top-right-radius: 0.25rem;
}

.rounded-t-2xl {
  border-top-left-radius: 1rem;
  border-top-right-radius: 1rem;
}

.rounded-t-3xl {
  border-top-left-radius: 1.5rem;
  border-top-right-radius: 1.5rem;
}

.rounded-t-full {
  border-top-left-radius: 9999px;
  border-top-right-radius: 9999px;
}

.rounded-t-lg {
  border-top-left-radius: 0.5rem;
  border-top-right-radius: 0.5rem;
}

.rounded-t-md {
  border-top-left-radius: 0.375rem;
  border-top-right-radius: 0.375rem;
}

.rounded-t-none {
  border-top-left-radius: 0px;
  border-top-right-radius: 0px;
}

.rounded-t-sm {
  border-top-left-radius: 0.125rem;
  border-top-right-radius: 0.125rem;
}

.rounded-t-xl {
  border-top-left-radius: 0.75rem;
  border-top-right-radius: 0.75rem;
}

.rounded-bl {
  border-bottom-left-radius: 0.25rem;
}

.rounded-bl-2xl {
  border-bottom-left-radius: 1rem;
}

.rounded-bl-3xl {
  border-bottom-left-radius: 1.5rem;
}

.rounded-bl-full {
  border-bottom-left-radius: 9999px;
}

.rounded-bl-lg {
  border-bottom-left-radius: 0.5rem;
}

.rounded-bl-md {
  border-bottom-left-radius: 0.375rem;
}

.rounded-bl-none {
  border-bottom-left-radius: 0px;
}

.rounded-bl-sm {
  border-bottom-left-radius: 0.125rem;
}

.rounded-bl-xl {
  border-bottom-left-radius: 0.75rem;
}

.rounded-br {
  border-bottom-right-radius: 0.25rem;
}

.rounded-br-2xl {
  border-bottom-right-radius: 1rem;
}

.rounded-br-3xl {
  border-bottom-right-radius: 1.5rem;
}

.rounded-br-full {
  border-bottom-right-radius: 9999px;
}

.rounded-br-lg {
  border-bottom-right-radius: 0.5rem;
}

.rounded-br-md {
  border-bottom-right-radius: 0.375rem;
}

.rounded-br-none {
  border-bottom-right-radius: 0px;
}

.rounded-br-sm {
  border-bottom-right-radius: 0.125rem;
}

.rounded-br-xl {
  border-bottom-right-radius: 0.75rem;
}

.rounded-ee {
  border-end-end-radius: 0.25rem;
}

.rounded-ee-2xl {
  border-end-end-radius: 1rem;
}

.rounded-ee-3xl {
  border-end-end-radius: 1.5rem;
}

.rounded-ee-full {
  border-end-end-radius: 9999px;
}

.rounded-ee-lg {
  border-end-end-radius: 0.5rem;
}

.rounded-ee-md {
  border-end-end-radius: 0.375rem;
}

.rounded-ee-none {
  border-end-end-radius: 0px;
}

.rounded-ee-sm {
  border-end-end-radius: 0.125rem;
}

.rounded-ee-xl {
  border-end-end-radius: 0.75rem;
}

.rounded-es {
  border-end-start-radius: 0.25rem;
}

.rounded-es-2xl {
  border-end-start-radius: 1rem;
}

.rounded-es-3xl {
  border-end-start-radius: 1.5rem;
}

.rounded-es-full {
  border-end-start-radius: 9999px;
}

.rounded-es-lg {
  border-end-start-radius: 0.5rem;
}

.rounded-es-md {
  border-end-start-radius: 0.375rem;
}

.rounded-es-none {
  border-end-start-radius: 0px;
}

.rounded-es-sm {
  border-end-start-radius: 0.125rem;
}

.rounded-es-xl {
  border-end-start-radius: 0.75rem;
}

.rounded-se {
  border-start-end-radius: 0.25rem;
}

.rounded-se-2xl {
  border-start-end-radius: 1rem;
}

.rounded-se-3xl {
  border-start-end-radius: 1.5rem;
}

.rounded-se-full {
  border-start-end-radius: 9999px;
}

.rounded-se-lg {
  border-start-end-radius: 0.5rem;
}

.rounded-se-md {
  border-start-end-radius: 0.375rem;
}

.rounded-se-none {
  border-start-end-radius: 0px;
}

.rounded-se-sm {
  border-start-end-radius: 0.125rem;
}

.rounded-se-xl {
  border-start-end-radius: 0.75rem;
}

.rounded-ss {
  border-start-start-radius: 0.25rem;
}

.rounded-ss-2xl {
  border-start-start-radius: 1rem;
}

.rounded-ss-3xl {
  border-start-start-radius: 1.5rem;
}

.rounded-ss-full {
  border-start-start-radius: 9999px;
}

.rounded-ss-lg {
  border-start-start-radius: 0.5rem;
}

.rounded-ss-md {
  border-start-start-radius: 0.375rem;
}

.rounded-ss-none {
  border-start-start-radius: 0px;
}

.rounded-ss-sm {
  border-start-start-radius: 0.125rem;
}

.rounded-ss-xl {
  border-start-start-radius: 0.75rem;
}

.rounded-tl {
  border-top-left-radius: 0.25rem;
}

.rounded-tl-2xl {
  border-top-left-radius: 1rem;
}

.rounded-tl-3xl {
  border-top-left-radius: 1.5rem;
}

.rounded-tl-full {
  border-top-left-radius: 9999px;
}

.rounded-tl-lg {
  border-top-left-radius: 0.5rem;
}

.rounded-tl-md {
  border-top-left-radius: 0.375rem;
}

.rounded-tl-none {
  border-top-left-radius: 0px;
}

.rounded-tl-sm {
  border-top-left-radius: 0.125rem;
}

.rounded-tl-xl {
  border-top-left-radius: 0.75rem;
}

.rounded-tr {
  border-top-right-radius: 0.25rem;
}

.rounded-tr-2xl {
  border-top-right-radius: 1rem;
}

.rounded-tr-3xl {
  border-top-right-radius: 1.5rem;
}

.rounded-tr-full {
  border-top-right-radius: 9999px;
}

.rounded-tr-lg {
  border-top-right-radius: 0.5rem;
}

.rounded-tr-md {
  border-top-right-radius: 0.375rem;
}

.rounded-tr-none {
  border-top-right-radius: 0px;
}

.rounded-tr-sm {
  border-top-right-radius: 0.125rem;
}

.rounded-tr-xl {
  border-top-right-radius: 0.75rem;
}

.border {
  border-width: 1px;
}

.border-0 {
  border-width: 0px;
}

.border-2 {
  border-width: 2px;
}

.border-4 {
  border-width: 4px;
}

.border-8 {
  border-width: 8px;
}

.border-x {
  border-left-width: 1px;
  border-right-width: 1px;
}

.border-x-0 {
  border-left-width: 0px;
  border-right-width: 0px;
}

.border-x-2 {
  border-left-width: 2px;
  border-right-width: 2px;
}

.border-x-4 {
  border-left-width: 4px;
  border-right-width: 4px;
}

.border-x-8 {
  border-left-width: 8px;
  border-right-width: 8px;
}

.border-y {
  border-top-width: 1px;
  border-bottom-width: 1px;
}

.border-y-0 {
  border-top-width: 0px;
  border-bottom-width: 0px;
}

.border-y-2 {
  border-top-width: 2px;
  border-bottom-width: 2px;
}

.border-y-4 {
  border-top-width: 4px;
  border-bottom-width: 4px;
}

.border-y-8 {
  border-top-width: 8px;
  border-bottom-width: 8px;
}

.border-b {
  border-bottom-width: 1px;
}

.border-b-0 {
  border-bottom-width: 0px;
}

.border-b-2 {
  border-bottom-width: 2px;
}

.border-b-4 {
  border-bottom-width: 4px;
}

.border-b-8 {
  border-bottom-width: 8px;
}

.border-e {
  border-inline-end-width: 1px;
}

.border-e-0 {
  border-inline-end-width: 0px;
}

.border-e-2 {
  border-inline-end-width: 2px;
}

.border-e-4 {
  border-inline-end-width: 4px;
}

.border-e-8 {
  border-inline-end-width: 8px;
}

.border-l {
  border-left-width: 1px;
}

.border-l-0 {
  border-left-width: 0px;
}

.border-l-2 {
  border-left-width: 2px;
}

.border-l-4 {
  border-left-width: 4px;
}

.border-l-8 {
  border-left-width: 8px;
}

.border-r {
  border-right-width: 1px;
}

.border-r-0 {
  border-right-width: 0px;
}

.border-r-2 {
  border-right-width: 2px;
}

.border-r-4 {
  border-right-width: 4px;
}

.border-r-8 {
  border-right-width: 8px;
}

.border-s {
  border-inline-start-width: 1px;
}

.border-s-0 {
  border-inline-start-width: 0px;
}

.border-s-2 {
  border-inline-start-width: 2px;
}

.border-s-4 {
  border-inline-start-width: 4px;
}

.border-s-8 {
  border-inline-start-width: 8px;
}

.border-t {
  border-top-width: 1px;
}

.border-t-0 {
  border-top-width: 0px;
}

.border-t-2 {
  border-top-width: 2px;
}

.border-t-4 {
  border-top-width: 4px;
}

.border-t-8 {
  border-top-width: 8px;
}

.border-solid {
  border-style: solid;
}

.border-dashed {
  border-style: dashed;
}

.border-dotted {
  border-style: dotted;
}

.border-double {
  border-style: double;
}

.border-hidden {
  border-style: hidden;
}

.border-none {
  border-style: none;
}

.border-amber-100 {
  --tw-border-opacity: 1;
  border-color: rgb(254 243 199 / var(--tw-border-opacity));
}

.border-amber-200 {
  --tw-border-opacity: 1;
  border-color: rgb(253 230 138 / var(--tw-border-opacity));
}

.border-amber-300 {
  --tw-border-opacity: 1;
  border-color: rgb(252 211 77 / var(--tw-border-opacity));
}

.border-amber-400 {
  --tw-border-opacity: 1;
  border-color: rgb(251 191 36 / var(--tw-border-opacity));
}

.border-amber-50 {
  --tw-border-opacity: 1;
  border-color: rgb(255 251 235 / var(--tw-border-opacity));
}

.border-amber-500 {
  --tw-border-opacity: 1;
  border-color: rgb(245 158 11 / var(--tw-border-opacity));
}

.border-amber-600 {
  --tw-border-opacity: 1;
  border-color: rgb(217 119 6 / var(--tw-border-opacity));
}

.border-amber-700 {
  --tw-border-opacity: 1;
  border-color: rgb(180 83 9 / var(--tw-border-opacity));
}

.border-amber-800 {
  --tw-border-opacity: 1;
  border-color: rgb(146 64 14 / var(--tw-border-opacity));
}

.border-amber-900 {
  --tw-border-opacity: 1;
  border-color: rgb(120 53 15 / var(--tw-border-opacity));
}

.border-amber-950 {
  --tw-border-opacity: 1;
  border-color: rgb(69 26 3 / var(--tw-border-opacity));
}

.border-black {
  --tw-border-opacity: 1;
  border-color: rgb(0 0 0 / var(--tw-border-opacity));
}

.border-blue-100 {
  --tw-border-opacity: 1;
  border-color: rgb(219 234 254 / var(--tw-border-opacity));
}

.border-blue-200 {
  --tw-border-opacity: 1;
  border-color: rgb(191 219 254 / var(--tw-border-opacity));
}

.border-blue-300 {
  --tw-border-opacity: 1;
  border-color: rgb(147 197 253 / var(--tw-border-opacity));
}

.border-blue-400 {
  --tw-border-opacity: 1;
  border-color: rgb(96 165 250 / var(--tw-border-opacity));
}

.border-blue-50 {
  --tw-border-opacity: 1;
  border-color: rgb(239 246 255 / var(--tw-border-opacity));
}

.border-blue-500 {
  --tw-border-opacity: 1;
  border-color: rgb(59 130 246 / var(--tw-border-opacity));
}

.border-blue-600 {
  --tw-border-opacity: 1;
  border-color: rgb(37 99 235 / var(--tw-border-opacity));
}

.border-blue-700 {
  --tw-border-opacity: 1;
  border-color: rgb(29 78 216 / var(--tw-border-opacity));
}

.border-blue-800 {
  --tw-border-opacity: 1;
  border-color: rgb(30 64 175 / var(--tw-border-opacity));
}

.border-blue-900 {
  --tw-border-opacity: 1;
  border-color: rgb(30 58 138 / var(--tw-border-opacity));
}

.border-blue-950 {
  --tw-border-opacity: 1;
  border-color: rgb(23 37 84 / var(--tw-border-opacity));
}

.border-current {
  border-color: currentColor;
}

.border-cyan-100 {
  --tw-border-opacity: 1;
  border-color: rgb(207 250 254 / var(--tw-border-opacity));
}

.border-cyan-200 {
  --tw-border-opacity: 1;
  border-color: rgb(165 243 252 / var(--tw-border-opacity));
}

.border-cyan-300 {
  --tw-border-opacity: 1;
  border-color: rgb(103 232 249 / var(--tw-border-opacity));
}

.border-cyan-400 {
  --tw-border-opacity: 1;
  border-color: rgb(34 211 238 / var(--tw-border-opacity));
}

.border-cyan-50 {
  --tw-border-opacity: 1;
  border-color: rgb(236 254 255 / var(--tw-border-opacity));
}

.border-cyan-500 {
  --tw-border-opacity: 1;
  border-color: rgb(6 182 212 / var(--tw-border-opacity));
}

.border-cyan-600 {
  --tw-border-opacity: 1;
  border-color: rgb(8 145 178 / var(--tw-border-opacity));
}

.border-cyan-700 {
  --tw-border-opacity: 1;
  border-color: rgb(14 116 144 / var(--tw-border-opacity));
}

.border-cyan-800 {
  --tw-border-opacity: 1;
  border-color: rgb(21 94 117 / var(--tw-border-opacity));
}

.border-cyan-900 {
  --tw-border-opacity: 1;
  border-color: rgb(22 78 99 / var(--tw-border-opacity));
}

.border-cyan-950 {
  --tw-border-opacity: 1;
  border-color: rgb(8 51 68 / var(--tw-border-opacity));
}

.border-emerald-100 {
  --tw-border-opacity: 1;
  border-color: rgb(209 250 229 / var(--tw-border-opacity));
}

.border-emerald-200 {
  --tw-border-opacity: 1;
  border-color: rgb(167 243 208 / var(--tw-border-opacity));
}

.border-emerald-300 {
  --tw-border-opacity: 1;
  border-color: rgb(110 231 183 / var(--tw-border-opacity));
}

.border-emerald-400 {
  --tw-border-opacity: 1;
  border-color: rgb(52 211 153 / var(--tw-border-opacity));
}

.border-emerald-50 {
  --tw-border-opacity: 1;
  border-color: rgb(236 253 245 / var(--tw-border-opacity));
}

.border-emerald-500 {
  --tw-border-opacity: 1;
  border-color: rgb(16 185 129 / var(--tw-border-opacity));
}

.border-emerald-600 {
  --tw-border-opacity: 1;
  border-color: rgb(5 150 105 / var(--tw-border-opacity));
}

.border-emerald-700 {
  --tw-border-opacity: 1;
  border-color: rgb(4 120 87 / var(--tw-border-opacity));
}

.border-emerald-800 {
  --tw-border-opacity: 1;
  border-color: rgb(6 95 70 / var(--tw-border-opacity));
}

.border-emerald-900 {
  --tw-border-opacity: 1;
  border-color: rgb(6 78 59 / var(--tw-border-opacity));
}

.border-emerald-950 {
  --tw-border-opacity: 1;
  border-color: rgb(2 44 34 / var(--tw-border-opacity));
}

.border-fuchsia-100 {
  --tw-border-opacity: 1;
  border-color: rgb(250 232 255 / var(--tw-border-opacity));
}

.border-fuchsia-200 {
  --tw-border-opacity: 1;
  border-color: rgb(245 208 254 / var(--tw-border-opacity));
}

.border-fuchsia-300 {
  --tw-border-opacity: 1;
  border-color: rgb(240 171 252 / var(--tw-border-opacity));
}

.border-fuchsia-400 {
  --tw-border-opacity: 1;
  border-color: rgb(232 121 249 / var(--tw-border-opacity));
}

.border-fuchsia-50 {
  --tw-border-opacity: 1;
  border-color: rgb(253 244 255 / var(--tw-border-opacity));
}

.border-fuchsia-500 {
  --tw-border-opacity: 1;
  border-color: rgb(217 70 239 / var(--tw-border-opacity));
}

.border-fuchsia-600 {
  --tw-border-opacity: 1;
  border-color: rgb(192 38 211 / var(--tw-border-opacity));
}

.border-fuchsia-700 {
  --tw-border-opacity: 1;
  border-color: rgb(162 28 175 / var(--tw-border-opacity));
}

.border-fuchsia-800 {
  --tw-border-opacity: 1;
  border-color: rgb(134 25 143 / var(--tw-border-opacity));
}

.border-fuchsia-900 {
  --tw-border-opacity: 1;
  border-color: rgb(112 26 117 / var(--tw-border-opacity));
}

.border-fuchsia-950 {
  --tw-border-opacity: 1;
  border-color: rgb(74 4 78 / var(--tw-border-opacity));
}

.border-gray-100 {
  --tw-border-opacity: 1;
  border-color: rgb(243 244 246 / var(--tw-border-opacity));
}

.border-gray-200 {
  --tw-border-opacity: 1;
  border-color: rgb(229 231 235 / var(--tw-border-opacity));
}

.border-gray-300 {
  --tw-border-opacity: 1;
  border-color: rgb(209 213 219 / var(--tw-border-opacity));
}

.border-gray-400 {
  --tw-border-opacity: 1;
  border-color: rgb(156 163 175 / var(--tw-border-opacity));
}

.border-gray-50 {
  --tw-border-opacity: 1;
  border-color: rgb(249 250 251 / var(--tw-border-opacity));
}

.border-gray-500 {
  --tw-border-opacity: 1;
  border-color: rgb(107 114 128 / var(--tw-border-opacity));
}

.border-gray-600 {
  --tw-border-opacity: 1;
  border-color: rgb(75 85 99 / var(--tw-border-opacity));
}

.border-gray-700 {
  --tw-border-opacity: 1;
  border-color: rgb(55 65 81 / var(--tw-border-opacity));
}

.border-gray-800 {
  --tw-border-opacity: 1;
  border-color: rgb(31 41 55 / var(--tw-border-opacity));
}

.border-gray-900 {
  --tw-border-opacity: 1;
  border-color: rgb(17 24 39 / var(--tw-border-opacity));
}

.border-gray-950 {
  --tw-border-opacity: 1;
  border-color: rgb(3 7 18 / var(--tw-border-opacity));
}

.border-green-100 {
  --tw-border-opacity: 1;
  border-color: rgb(220 252 231 / var(--tw-border-opacity));
}

.border-green-200 {
  --tw-border-opacity: 1;
  border-color: rgb(187 247 208 / var(--tw-border-opacity));
}

.border-green-300 {
  --tw-border-opacity: 1;
  border-color: rgb(134 239 172 / var(--tw-border-opacity));
}

.border-green-400 {
  --tw-border-opacity: 1;
  border-color: rgb(74 222 128 / var(--tw-border-opacity));
}

.border-green-50 {
  --tw-border-opacity: 1;
  border-color: rgb(240 253 244 / var(--tw-border-opacity));
}

.border-green-500 {
  --tw-border-opacity: 1;
  border-color: rgb(34 197 94 / var(--tw-border-opacity));
}

.border-green-600 {
  --tw-border-opacity: 1;
  border-color: rgb(22 163 74 / var(--tw-border-opacity));
}

.border-green-700 {
  --tw-border-opacity: 1;
  border-color: rgb(21 128 61 / var(--tw-border-opacity));
}

.border-green-800 {
  --tw-border-opacity: 1;
  border-color: rgb(22 101 52 / var(--tw-border-opacity));
}

.border-green-900 {
  --tw-border-opacity: 1;
  border-color: rgb(20 83 45 / var(--tw-border-opacity));
}

.border-green-950 {
  --tw-border-opacity: 1;
  border-color: rgb(5 46 22 / var(--tw-border-opacity));
}

.border-indigo-100 {
  --tw-border-opacity: 1;
  border-color: rgb(224 231 255 / var(--tw-border-opacity));
}

.border-indigo-200 {
  --tw-border-opacity: 1;
  border-color: rgb(199 210 254 / var(--tw-border-opacity));
}

.border-indigo-300 {
  --tw-border-opacity: 1;
  border-color: rgb(165 180 252 / var(--tw-border-opacity));
}

.border-indigo-400 {
  --tw-border-opacity: 1;
  border-color: rgb(129 140 248 / var(--tw-border-opacity));
}

.border-indigo-50 {
  --tw-border-opacity: 1;
  border-color: rgb(238 242 255 / var(--tw-border-opacity));
}

.border-indigo-500 {
  --tw-border-opacity: 1;
  border-color: rgb(99 102 241 / var(--tw-border-opacity));
}

.border-indigo-600 {
  --tw-border-opacity: 1;
  border-color: rgb(79 70 229 / var(--tw-border-opacity));
}

.border-indigo-700 {
  --tw-border-opacity: 1;
  border-color: rgb(67 56 202 / var(--tw-border-opacity));
}

.border-indigo-800 {
  --tw-border-opacity: 1;
  border-color: rgb(55 48 163 / var(--tw-border-opacity));
}

.border-indigo-900 {
  --tw-border-opacity: 1;
  border-color: rgb(49 46 129 / var(--tw-border-opacity));
}

.border-indigo-950 {
  --tw-border-opacity: 1;
  border-color: rgb(30 27 75 / var(--tw-border-opacity));
}

.border-inherit {
  border-color: inherit;
}

.border-lime-100 {
  --tw-border-opacity: 1;
  border-color: rgb(236 252 203 / var(--tw-border-opacity));
}

.border-lime-200 {
  --tw-border-opacity: 1;
  border-color: rgb(217 249 157 / var(--tw-border-opacity));
}

.border-lime-300 {
  --tw-border-opacity: 1;
  border-color: rgb(190 242 100 / var(--tw-border-opacity));
}

.border-lime-400 {
  --tw-border-opacity: 1;
  border-color: rgb(163 230 53 / var(--tw-border-opacity));
}

.border-lime-50 {
  --tw-border-opacity: 1;
  border-color: rgb(247 254 231 / var(--tw-border-opacity));
}

.border-lime-500 {
  --tw-border-opacity: 1;
  border-color: rgb(132 204 22 / var(--tw-border-opacity));
}

.border-lime-600 {
  --tw-border-opacity: 1;
  border-color: rgb(101 163 13 / var(--tw-border-opacity));
}

.border-lime-700 {
  --tw-border-opacity: 1;
  border-color: rgb(77 124 15 / var(--tw-border-opacity));
}

.border-lime-800 {
  --tw-border-opacity: 1;
  border-color: rgb(63 98 18 / var(--tw-border-opacity));
}

.border-lime-900 {
  --tw-border-opacity: 1;
  border-color: rgb(54 83 20 / var(--tw-border-opacity));
}

.border-lime-950 {
  --tw-border-opacity: 1;
  border-color: rgb(26 46 5 / var(--tw-border-opacity));
}

.border-neutral-100 {
  --tw-border-opacity: 1;
  border-color: rgb(245 245 245 / var(--tw-border-opacity));
}

.border-neutral-200 {
  --tw-border-opacity: 1;
  border-color: rgb(229 229 229 / var(--tw-border-opacity));
}

.border-neutral-300 {
  --tw-border-opacity: 1;
  border-color: rgb(212 212 212 / var(--tw-border-opacity));
}

.border-neutral-400 {
  --tw-border-opacity: 1;
  border-color: rgb(163 163 163 / var(--tw-border-opacity));
}

.border-neutral-50 {
  --tw-border-opacity: 1;
  border-color: rgb(250 250 250 / var(--tw-border-opacity));
}

.border-neutral-500 {
  --tw-border-opacity: 1;
  border-color: rgb(115 115 115 / var(--tw-border-opacity));
}

.border-neutral-600 {
  --tw-border-opacity: 1;
  border-color: rgb(82 82 82 / var(--tw-border-opacity));
}

.border-neutral-700 {
  --tw-border-opacity: 1;
  border-color: rgb(64 64 64 / var(--tw-border-opacity));
}

.border-neutral-800 {
  --tw-border-opacity: 1;
  border-color: rgb(38 38 38 / var(--tw-border-opacity));
}

.border-neutral-900 {
  --tw-border-opacity: 1;
  border-color: rgb(23 23 23 / var(--tw-border-opacity));
}

.border-neutral-950 {
  --tw-border-opacity: 1;
  border-color: rgb(10 10 10 / var(--tw-border-opacity));
}

.border-orange-100 {
  --tw-border-opacity: 1;
  border-color: rgb(255 237 213 / var(--tw-border-opacity));
}

.border-orange-200 {
  --tw-border-opacity: 1;
  border-color: rgb(254 215 170 / var(--tw-border-opacity));
}

.border-orange-300 {
  --tw-border-opacity: 1;
  border-color: rgb(253 186 116 / var(--tw-border-opacity));
}

.border-orange-400 {
  --tw-border-opacity: 1;
  border-color: rgb(251 146 60 / var(--tw-border-opacity));
}

.border-orange-50 {
  --tw-border-opacity: 1;
  border-color: rgb(255 247 237 / var(--tw-border-opacity));
}

.border-orange-500 {
  --tw-border-opacity: 1;
  border-color: rgb(249 115 22 / var(--tw-border-opacity));
}

.border-orange-600 {
  --tw-border-opacity: 1;
  border-color: rgb(234 88 12 / var(--tw-border-opacity));
}

.border-orange-700 {
  --tw-border-opacity: 1;
  border-color: rgb(194 65 12 / var(--tw-border-opacity));
}

.border-orange-800 {
  --tw-border-opacity: 1;
  border-color: rgb(154 52 18 / var(--tw-border-opacity));
}

.border-orange-900 {
  --tw-border-opacity: 1;
  border-color: rgb(124 45 18 / var(--tw-border-opacity));
}

.border-orange-950 {
  --tw-border-opacity: 1;
  border-color: rgb(67 20 7 / var(--tw-border-opacity));
}

.border-pink-100 {
  --tw-border-opacity: 1;
  border-color: rgb(252 231 243 / var(--tw-border-opacity));
}

.border-pink-200 {
  --tw-border-opacity: 1;
  border-color: rgb(251 207 232 / var(--tw-border-opacity));
}

.border-pink-300 {
  --tw-border-opacity: 1;
  border-color: rgb(249 168 212 / var(--tw-border-opacity));
}

.border-pink-400 {
  --tw-border-opacity: 1;
  border-color: rgb(244 114 182 / var(--tw-border-opacity));
}

.border-pink-50 {
  --tw-border-opacity: 1;
  border-color: rgb(253 242 248 / var(--tw-border-opacity));
}

.border-pink-500 {
  --tw-border-opacity: 1;
  border-color: rgb(236 72 153 / var(--tw-border-opacity));
}

.border-pink-600 {
  --tw-border-opacity: 1;
  border-color: rgb(219 39 119 / var(--tw-border-opacity));
}

.border-pink-700 {
  --tw-border-opacity: 1;
  border-color: rgb(190 24 93 / var(--tw-border-opacity));
}

.border-pink-800 {
  --tw-border-opacity: 1;
  border-color: rgb(157 23 77 / var(--tw-border-opacity));
}

.border-pink-900 {
  --tw-border-opacity: 1;
  border-color: rgb(131 24 67 / var(--tw-border-opacity));
}

.border-pink-950 {
  --tw-border-opacity: 1;
  border-color: rgb(80 7 36 / var(--tw-border-opacity));
}

.border-purple-100 {
  --tw-border-opacity: 1;
  border-color: rgb(243 232 255 / var(--tw-border-opacity));
}

.border-purple-200 {
  --tw-border-opacity: 1;
  border-color: rgb(233 213 255 / var(--tw-border-opacity));
}

.border-purple-300 {
  --tw-border-opacity: 1;
  border-color: rgb(216 180 254 / var(--tw-border-opacity));
}

.border-purple-400 {
  --tw-border-opacity: 1;
  border-color: rgb(192 132 252 / var(--tw-border-opacity));
}

.border-purple-50 {
  --tw-border-opacity: 1;
  border-color: rgb(250 245 255 / var(--tw-border-opacity));
}

.border-purple-500 {
  --tw-border-opacity: 1;
  border-color: rgb(168 85 247 / var(--tw-border-opacity));
}

.border-purple-600 {
  --tw-border-opacity: 1;
  border-color: rgb(147 51 234 / var(--tw-border-opacity));
}

.border-purple-700 {
  --tw-border-opacity: 1;
  border-color: rgb(126 34 206 / var(--tw-border-opacity));
}

.border-purple-800 {
  --tw-border-opacity: 1;
  border-color: rgb(107 33 168 / var(--tw-border-opacity));
}

.border-purple-900 {
  --tw-border-opacity: 1;
  border-color: rgb(88 28 135 / var(--tw-border-opacity));
}

.border-purple-950 {
  --tw-border-opacity: 1;
  border-color: rgb(59 7 100 / var(--tw-border-opacity));
}

.border-red-100 {
  --tw-border-opacity: 1;
  border-color: rgb(254 226 226 / var(--tw-border-opacity));
}

.border-red-200 {
  --tw-border-opacity: 1;
  border-color: rgb(254 202 202 / var(--tw-border-opacity));
}

.border-red-300 {
  --tw-border-opacity: 1;
  border-color: rgb(252 165 165 / var(--tw-border-opacity));
}

.border-red-400 {
  --tw-border-opacity: 1;
  border-color: rgb(248 113 113 / var(--tw-border-opacity));
}

.border-red-50 {
  --tw-border-opacity: 1;
  border-color: rgb(254 242 242 / var(--tw-border-opacity));
}

.border-red-500 {
  --tw-border-opacity: 1;
  border-color: rgb(239 68 68 / var(--tw-border-opacity));
}

.border-red-600 {
  --tw-border-opacity: 1;
  border-color: rgb(220 38 38 / var(--tw-border-opacity));
}

.border-red-700 {
  --tw-border-opacity: 1;
  border-color: rgb(185 28 28 / var(--tw-border-opacity));
}

.border-red-800 {
  --tw-border-opacity: 1;
  border-color: rgb(153 27 27 / var(--tw-border-opacity));
}

.border-red-900 {
  --tw-border-opacity: 1;
  border-color: rgb(127 29 29 / var(--tw-border-opacity));
}

.border-red-950 {
  --tw-border-opacity: 1;
  border-color: rgb(69 10 10 / var(--tw-border-opacity));
}

.border-rose-100 {
  --tw-border-opacity: 1;
  border-color: rgb(255 228 230 / var(--tw-border-opacity));
}

.border-rose-200 {
  --tw-border-opacity: 1;
  border-color: rgb(254 205 211 / var(--tw-border-opacity));
}

.border-rose-300 {
  --tw-border-opacity: 1;
  border-color: rgb(253 164 175 / var(--tw-border-opacity));
}

.border-rose-400 {
  --tw-border-opacity: 1;
  border-color: rgb(251 113 133 / var(--tw-border-opacity));
}

.border-rose-50 {
  --tw-border-opacity: 1;
  border-color: rgb(255 241 242 / var(--tw-border-opacity));
}

.border-rose-500 {
  --tw-border-opacity: 1;
  border-color: rgb(244 63 94 / var(--tw-border-opacity));
}

.border-rose-600 {
  --tw-border-opacity: 1;
  border-color: rgb(225 29 72 / var(--tw-border-opacity));
}

.border-rose-700 {
  --tw-border-opacity: 1;
  border-color: rgb(190 18 60 / var(--tw-border-opacity));
}

.border-rose-800 {
  --tw-border-opacity: 1;
  border-color: rgb(159 18 57 / var(--tw-border-opacity));
}

.border-rose-900 {
  --tw-border-opacity: 1;
  border-color: rgb(136 19 55 / var(--tw-border-opacity));
}

.border-rose-950 {
  --tw-border-opacity: 1;
  border-color: rgb(76 5 25 / var(--tw-border-opacity));
}

.border-sky-100 {
  --tw-border-opacity: 1;
  border-color: rgb(224 242 254 / var(--tw-border-opacity));
}

.border-sky-200 {
  --tw-border-opacity: 1;
  border-color: rgb(186 230 253 / var(--tw-border-opacity));
}

.border-sky-300 {
  --tw-border-opacity: 1;
  border-color: rgb(125 211 252 / var(--tw-border-opacity));
}

.border-sky-400 {
  --tw-border-opacity: 1;
  border-color: rgb(56 189 248 / var(--tw-border-opacity));
}

.border-sky-50 {
  --tw-border-opacity: 1;
  border-color: rgb(240 249 255 / var(--tw-border-opacity));
}

.border-sky-500 {
  --tw-border-opacity: 1;
  border-color: rgb(14 165 233 / var(--tw-border-opacity));
}

.border-sky-600 {
  --tw-border-opacity: 1;
  border-color: rgb(2 132 199 / var(--tw-border-opacity));
}

.border-sky-700 {
  --tw-border-opacity: 1;
  border-color: rgb(3 105 161 / var(--tw-border-opacity));
}

.border-sky-800 {
  --tw-border-opacity: 1;
  border-color: rgb(7 89 133 / var(--tw-border-opacity));
}

.border-sky-900 {
  --tw-border-opacity: 1;
  border-color: rgb(12 74 110 / var(--tw-border-opacity));
}

.border-sky-950 {
  --tw-border-opacity: 1;
  border-color: rgb(8 47 73 / var(--tw-border-opacity));
}

.border-slate-100 {
  --tw-border-opacity: 1;
  border-color: rgb(241 245 249 / var(--tw-border-opacity));
}

.border-slate-200 {
  --tw-border-opacity: 1;
  border-color: rgb(226 232 240 / var(--tw-border-opacity));
}

.border-slate-300 {
  --tw-border-opacity: 1;
  border-color: rgb(203 213 225 / var(--tw-border-opacity));
}

.border-slate-400 {
  --tw-border-opacity: 1;
  border-color: rgb(148 163 184 / var(--tw-border-opacity));
}

.border-slate-50 {
  --tw-border-opacity: 1;
  border-color: rgb(248 250 252 / var(--tw-border-opacity));
}

.border-slate-500 {
  --tw-border-opacity: 1;
  border-color: rgb(100 116 139 / var(--tw-border-opacity));
}

.border-slate-600 {
  --tw-border-opacity: 1;
  border-color: rgb(71 85 105 / var(--tw-border-opacity));
}

.border-slate-700 {
  --tw-border-opacity: 1;
  border-color: rgb(51 65 85 / var(--tw-border-opacity));
}

.border-slate-800 {
  --tw-border-opacity: 1;
  border-color: rgb(30 41 59 / var(--tw-border-opacity));
}

.border-slate-900 {
  --tw-border-opacity: 1;
  border-color: rgb(15 23 42 / var(--tw-border-opacity));
}

.border-slate-950 {
  --tw-border-opacity: 1;
  border-color: rgb(2 6 23 / var(--tw-border-opacity));
}

.border-stone-100 {
  --tw-border-opacity: 1;
  border-color: rgb(245 245 244 / var(--tw-border-opacity));
}

.border-stone-200 {
  --tw-border-opacity: 1;
  border-color: rgb(231 229 228 / var(--tw-border-opacity));
}

.border-stone-300 {
  --tw-border-opacity: 1;
  border-color: rgb(214 211 209 / var(--tw-border-opacity));
}

.border-stone-400 {
  --tw-border-opacity: 1;
  border-color: rgb(168 162 158 / var(--tw-border-opacity));
}

.border-stone-50 {
  --tw-border-opacity: 1;
  border-color: rgb(250 250 249 / var(--tw-border-opacity));
}

.border-stone-500 {
  --tw-border-opacity: 1;
  border-color: rgb(120 113 108 / var(--tw-border-opacity));
}

.border-stone-600 {
  --tw-border-opacity: 1;
  border-color: rgb(87 83 78 / var(--tw-border-opacity));
}

.border-stone-700 {
  --tw-border-opacity: 1;
  border-color: rgb(68 64 60 / var(--tw-border-opacity));
}

.border-stone-800 {
  --tw-border-opacity: 1;
  border-color: rgb(41 37 36 / var(--tw-border-opacity));
}

.border-stone-900 {
  --tw-border-opacity: 1;
  border-color: rgb(28 25 23 / var(--tw-border-opacity));
}

.border-stone-950 {
  --tw-border-opacity: 1;
  border-color: rgb(12 10 9 / var(--tw-border-opacity));
}

.border-teal-100 {
  --tw-border-opacity: 1;
  border-color: rgb(204 251 241 / var(--tw-border-opacity));
}

.border-teal-200 {
  --tw-border-opacity: 1;
  border-color: rgb(153 246 228 / var(--tw-border-opacity));
}

.border-teal-300 {
  --tw-border-opacity: 1;
  border-color: rgb(94 234 212 / var(--tw-border-opacity));
}

.border-teal-400 {
  --tw-border-opacity: 1;
  border-color: rgb(45 212 191 / var(--tw-border-opacity));
}

.border-teal-50 {
  --tw-border-opacity: 1;
  border-color: rgb(240 253 250 / var(--tw-border-opacity));
}

.border-teal-500 {
  --tw-border-opacity: 1;
  border-color: rgb(20 184 166 / var(--tw-border-opacity));
}

.border-teal-600 {
  --tw-border-opacity: 1;
  border-color: rgb(13 148 136 / var(--tw-border-opacity));
}

.border-teal-700 {
  --tw-border-opacity: 1;
  border-color: rgb(15 118 110 / var(--tw-border-opacity));
}

.border-teal-800 {
  --tw-border-opacity: 1;
  border-color: rgb(17 94 89 / var(--tw-border-opacity));
}

.border-teal-900 {
  --tw-border-opacity: 1;
  border-color: rgb(19 78 74 / var(--tw-border-opacity));
}

.border-teal-950 {
  --tw-border-opacity: 1;
  border-color: rgb(4 47 46 / var(--tw-border-opacity));
}

.border-transparent {
  border-color: transparent;
}

.border-violet-100 {
  --tw-border-opacity: 1;
  border-color: rgb(237 233 254 / var(--tw-border-opacity));
}

.border-violet-200 {
  --tw-border-opacity: 1;
  border-color: rgb(221 214 254 / var(--tw-border-opacity));
}

.border-violet-300 {
  --tw-border-opacity: 1;
  border-color: rgb(196 181 253 / var(--tw-border-opacity));
}

.border-violet-400 {
  --tw-border-opacity: 1;
  border-color: rgb(167 139 250 / var(--tw-border-opacity));
}

.border-violet-50 {
  --tw-border-opacity: 1;
  border-color: rgb(245 243 255 / var(--tw-border-opacity));
}

.border-violet-500 {
  --tw-border-opacity: 1;
  border-color: rgb(139 92 246 / var(--tw-border-opacity));
}

.border-violet-600 {
  --tw-border-opacity: 1;
  border-color: rgb(124 58 237 / var(--tw-border-opacity));
}

.border-violet-700 {
  --tw-border-opacity: 1;
  border-color: rgb(109 40 217 / var(--tw-border-opacity));
}

.border-violet-800 {
  --tw-border-opacity: 1;
  border-color: rgb(91 33 182 / var(--tw-border-opacity));
}

.border-violet-900 {
  --tw-border-opacity: 1;
  border-color: rgb(76 29 149 / var(--tw-border-opacity));
}

.border-violet-950 {
  --tw-border-opacity: 1;
  border-color: rgb(46 16 101 / var(--tw-border-opacity));
}

.border-white {
  --tw-border-opacity: 1;
  border-color: rgb(255 255 255 / var(--tw-border-opacity));
}

.border-yellow-100 {
  --tw-border-opacity: 1;
  border-color: rgb(254 249 195 / var(--tw-border-opacity));
}

.border-yellow-200 {
  --tw-border-opacity: 1;
  border-color: rgb(254 240 138 / var(--tw-border-opacity));
}

.border-yellow-300 {
  --tw-border-opacity: 1;
  border-color: rgb(253 224 71 / var(--tw-border-opacity));
}

.border-yellow-400 {
  --tw-border-opacity: 1;
  border-color: rgb(250 204 21 / var(--tw-border-opacity));
}

.border-yellow-50 {
  --tw-border-opacity: 1;
  border-color: rgb(254 252 232 / var(--tw-border-opacity));
}

.border-yellow-500 {
  --tw-border-opacity: 1;
  border-color: rgb(234 179 8 / var(--tw-border-opacity));
}

.border-yellow-600 {
  --tw-border-opacity: 1;
  border-color: rgb(202 138 4 / var(--tw-border-opacity));
}

.border-yellow-700 {
  --tw-border-opacity: 1;
  border-color: rgb(161 98 7 / var(--tw-border-opacity));
}

.border-yellow-800 {
  --tw-border-opacity: 1;
  border-color: rgb(133 77 14 / var(--tw-border-opacity));
}

.border-yellow-900 {
  --tw-border-opacity: 1;
  border-color: rgb(113 63 18 / var(--tw-border-opacity));
}

.border-yellow-950 {
  --tw-border-opacity: 1;
  border-color: rgb(66 32 6 / var(--tw-border-opacity));
}

.border-zinc-100 {
  --tw-border-opacity: 1;
  border-color: rgb(244 244 245 / var(--tw-border-opacity));
}

.border-zinc-200 {
  --tw-border-opacity: 1;
  border-color: rgb(228 228 231 / var(--tw-border-opacity));
}

.border-zinc-300 {
  --tw-border-opacity: 1;
  border-color: rgb(212 212 216 / var(--tw-border-opacity));
}

.border-zinc-400 {
  --tw-border-opacity: 1;
  border-color: rgb(161 161 170 / var(--tw-border-opacity));
}

.border-zinc-50 {
  --tw-border-opacity: 1;
  border-color: rgb(250 250 250 / var(--tw-border-opacity));
}

.border-zinc-500 {
  --tw-border-opacity: 1;
  border-color: rgb(113 113 122 / var(--tw-border-opacity));
}

.border-zinc-600 {
  --tw-border-opacity: 1;
  border-color: rgb(82 82 91 / var(--tw-border-opacity));
}

.border-zinc-700 {
  --tw-border-opacity: 1;
  border-color: rgb(63 63 70 / var(--tw-border-opacity));
}

.border-zinc-800 {
  --tw-border-opacity: 1;
  border-color: rgb(39 39 42 / var(--tw-border-opacity));
}

.border-zinc-900 {
  --tw-border-opacity: 1;
  border-color: rgb(24 24 27 / var(--tw-border-opacity));
}

.border-zinc-950 {
  --tw-border-opacity: 1;
  border-color: rgb(9 9 11 / var(--tw-border-opacity));
}

.border-x-amber-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(254 243 199 / var(--tw-border-opacity));
  border-right-color: rgb(254 243 199 / var(--tw-border-opacity));
}

.border-x-amber-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(253 230 138 / var(--tw-border-opacity));
  border-right-color: rgb(253 230 138 / var(--tw-border-opacity));
}

.border-x-amber-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(252 211 77 / var(--tw-border-opacity));
  border-right-color: rgb(252 211 77 / var(--tw-border-opacity));
}

.border-x-amber-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(251 191 36 / var(--tw-border-opacity));
  border-right-color: rgb(251 191 36 / var(--tw-border-opacity));
}

.border-x-amber-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(255 251 235 / var(--tw-border-opacity));
  border-right-color: rgb(255 251 235 / var(--tw-border-opacity));
}

.border-x-amber-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(245 158 11 / var(--tw-border-opacity));
  border-right-color: rgb(245 158 11 / var(--tw-border-opacity));
}

.border-x-amber-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(217 119 6 / var(--tw-border-opacity));
  border-right-color: rgb(217 119 6 / var(--tw-border-opacity));
}

.border-x-amber-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(180 83 9 / var(--tw-border-opacity));
  border-right-color: rgb(180 83 9 / var(--tw-border-opacity));
}

.border-x-amber-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(146 64 14 / var(--tw-border-opacity));
  border-right-color: rgb(146 64 14 / var(--tw-border-opacity));
}

.border-x-amber-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(120 53 15 / var(--tw-border-opacity));
  border-right-color: rgb(120 53 15 / var(--tw-border-opacity));
}

.border-x-amber-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(69 26 3 / var(--tw-border-opacity));
  border-right-color: rgb(69 26 3 / var(--tw-border-opacity));
}

.border-x-black {
  --tw-border-opacity: 1;
  border-left-color: rgb(0 0 0 / var(--tw-border-opacity));
  border-right-color: rgb(0 0 0 / var(--tw-border-opacity));
}

.border-x-blue-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(219 234 254 / var(--tw-border-opacity));
  border-right-color: rgb(219 234 254 / var(--tw-border-opacity));
}

.border-x-blue-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(191 219 254 / var(--tw-border-opacity));
  border-right-color: rgb(191 219 254 / var(--tw-border-opacity));
}

.border-x-blue-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(147 197 253 / var(--tw-border-opacity));
  border-right-color: rgb(147 197 253 / var(--tw-border-opacity));
}

.border-x-blue-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(96 165 250 / var(--tw-border-opacity));
  border-right-color: rgb(96 165 250 / var(--tw-border-opacity));
}

.border-x-blue-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(239 246 255 / var(--tw-border-opacity));
  border-right-color: rgb(239 246 255 / var(--tw-border-opacity));
}

.border-x-blue-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(59 130 246 / var(--tw-border-opacity));
  border-right-color: rgb(59 130 246 / var(--tw-border-opacity));
}

.border-x-blue-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(37 99 235 / var(--tw-border-opacity));
  border-right-color: rgb(37 99 235 / var(--tw-border-opacity));
}

.border-x-blue-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(29 78 216 / var(--tw-border-opacity));
  border-right-color: rgb(29 78 216 / var(--tw-border-opacity));
}

.border-x-blue-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(30 64 175 / var(--tw-border-opacity));
  border-right-color: rgb(30 64 175 / var(--tw-border-opacity));
}

.border-x-blue-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(30 58 138 / var(--tw-border-opacity));
  border-right-color: rgb(30 58 138 / var(--tw-border-opacity));
}

.border-x-blue-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(23 37 84 / var(--tw-border-opacity));
  border-right-color: rgb(23 37 84 / var(--tw-border-opacity));
}

.border-x-current {
  border-left-color: currentColor;
  border-right-color: currentColor;
}

.border-x-cyan-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(207 250 254 / var(--tw-border-opacity));
  border-right-color: rgb(207 250 254 / var(--tw-border-opacity));
}

.border-x-cyan-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(165 243 252 / var(--tw-border-opacity));
  border-right-color: rgb(165 243 252 / var(--tw-border-opacity));
}

.border-x-cyan-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(103 232 249 / var(--tw-border-opacity));
  border-right-color: rgb(103 232 249 / var(--tw-border-opacity));
}

.border-x-cyan-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(34 211 238 / var(--tw-border-opacity));
  border-right-color: rgb(34 211 238 / var(--tw-border-opacity));
}

.border-x-cyan-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(236 254 255 / var(--tw-border-opacity));
  border-right-color: rgb(236 254 255 / var(--tw-border-opacity));
}

.border-x-cyan-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(6 182 212 / var(--tw-border-opacity));
  border-right-color: rgb(6 182 212 / var(--tw-border-opacity));
}

.border-x-cyan-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(8 145 178 / var(--tw-border-opacity));
  border-right-color: rgb(8 145 178 / var(--tw-border-opacity));
}

.border-x-cyan-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(14 116 144 / var(--tw-border-opacity));
  border-right-color: rgb(14 116 144 / var(--tw-border-opacity));
}

.border-x-cyan-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(21 94 117 / var(--tw-border-opacity));
  border-right-color: rgb(21 94 117 / var(--tw-border-opacity));
}

.border-x-cyan-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(22 78 99 / var(--tw-border-opacity));
  border-right-color: rgb(22 78 99 / var(--tw-border-opacity));
}

.border-x-cyan-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(8 51 68 / var(--tw-border-opacity));
  border-right-color: rgb(8 51 68 / var(--tw-border-opacity));
}

.border-x-emerald-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(209 250 229 / var(--tw-border-opacity));
  border-right-color: rgb(209 250 229 / var(--tw-border-opacity));
}

.border-x-emerald-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(167 243 208 / var(--tw-border-opacity));
  border-right-color: rgb(167 243 208 / var(--tw-border-opacity));
}

.border-x-emerald-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(110 231 183 / var(--tw-border-opacity));
  border-right-color: rgb(110 231 183 / var(--tw-border-opacity));
}

.border-x-emerald-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(52 211 153 / var(--tw-border-opacity));
  border-right-color: rgb(52 211 153 / var(--tw-border-opacity));
}

.border-x-emerald-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(236 253 245 / var(--tw-border-opacity));
  border-right-color: rgb(236 253 245 / var(--tw-border-opacity));
}

.border-x-emerald-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(16 185 129 / var(--tw-border-opacity));
  border-right-color: rgb(16 185 129 / var(--tw-border-opacity));
}

.border-x-emerald-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(5 150 105 / var(--tw-border-opacity));
  border-right-color: rgb(5 150 105 / var(--tw-border-opacity));
}

.border-x-emerald-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(4 120 87 / var(--tw-border-opacity));
  border-right-color: rgb(4 120 87 / var(--tw-border-opacity));
}

.border-x-emerald-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(6 95 70 / var(--tw-border-opacity));
  border-right-color: rgb(6 95 70 / var(--tw-border-opacity));
}

.border-x-emerald-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(6 78 59 / var(--tw-border-opacity));
  border-right-color: rgb(6 78 59 / var(--tw-border-opacity));
}

.border-x-emerald-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(2 44 34 / var(--tw-border-opacity));
  border-right-color: rgb(2 44 34 / var(--tw-border-opacity));
}

.border-x-fuchsia-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(250 232 255 / var(--tw-border-opacity));
  border-right-color: rgb(250 232 255 / var(--tw-border-opacity));
}

.border-x-fuchsia-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(245 208 254 / var(--tw-border-opacity));
  border-right-color: rgb(245 208 254 / var(--tw-border-opacity));
}

.border-x-fuchsia-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(240 171 252 / var(--tw-border-opacity));
  border-right-color: rgb(240 171 252 / var(--tw-border-opacity));
}

.border-x-fuchsia-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(232 121 249 / var(--tw-border-opacity));
  border-right-color: rgb(232 121 249 / var(--tw-border-opacity));
}

.border-x-fuchsia-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(253 244 255 / var(--tw-border-opacity));
  border-right-color: rgb(253 244 255 / var(--tw-border-opacity));
}

.border-x-fuchsia-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(217 70 239 / var(--tw-border-opacity));
  border-right-color: rgb(217 70 239 / var(--tw-border-opacity));
}

.border-x-fuchsia-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(192 38 211 / var(--tw-border-opacity));
  border-right-color: rgb(192 38 211 / var(--tw-border-opacity));
}

.border-x-fuchsia-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(162 28 175 / var(--tw-border-opacity));
  border-right-color: rgb(162 28 175 / var(--tw-border-opacity));
}

.border-x-fuchsia-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(134 25 143 / var(--tw-border-opacity));
  border-right-color: rgb(134 25 143 / var(--tw-border-opacity));
}

.border-x-fuchsia-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(112 26 117 / var(--tw-border-opacity));
  border-right-color: rgb(112 26 117 / var(--tw-border-opacity));
}

.border-x-fuchsia-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(74 4 78 / var(--tw-border-opacity));
  border-right-color: rgb(74 4 78 / var(--tw-border-opacity));
}

.border-x-gray-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(243 244 246 / var(--tw-border-opacity));
  border-right-color: rgb(243 244 246 / var(--tw-border-opacity));
}

.border-x-gray-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(229 231 235 / var(--tw-border-opacity));
  border-right-color: rgb(229 231 235 / var(--tw-border-opacity));
}

.border-x-gray-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(209 213 219 / var(--tw-border-opacity));
  border-right-color: rgb(209 213 219 / var(--tw-border-opacity));
}

.border-x-gray-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(156 163 175 / var(--tw-border-opacity));
  border-right-color: rgb(156 163 175 / var(--tw-border-opacity));
}

.border-x-gray-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(249 250 251 / var(--tw-border-opacity));
  border-right-color: rgb(249 250 251 / var(--tw-border-opacity));
}

.border-x-gray-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(107 114 128 / var(--tw-border-opacity));
  border-right-color: rgb(107 114 128 / var(--tw-border-opacity));
}

.border-x-gray-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(75 85 99 / var(--tw-border-opacity));
  border-right-color: rgb(75 85 99 / var(--tw-border-opacity));
}

.border-x-gray-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(55 65 81 / var(--tw-border-opacity));
  border-right-color: rgb(55 65 81 / var(--tw-border-opacity));
}

.border-x-gray-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(31 41 55 / var(--tw-border-opacity));
  border-right-color: rgb(31 41 55 / var(--tw-border-opacity));
}

.border-x-gray-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(17 24 39 / var(--tw-border-opacity));
  border-right-color: rgb(17 24 39 / var(--tw-border-opacity));
}

.border-x-gray-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(3 7 18 / var(--tw-border-opacity));
  border-right-color: rgb(3 7 18 / var(--tw-border-opacity));
}

.border-x-green-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(220 252 231 / var(--tw-border-opacity));
  border-right-color: rgb(220 252 231 / var(--tw-border-opacity));
}

.border-x-green-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(187 247 208 / var(--tw-border-opacity));
  border-right-color: rgb(187 247 208 / var(--tw-border-opacity));
}

.border-x-green-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(134 239 172 / var(--tw-border-opacity));
  border-right-color: rgb(134 239 172 / var(--tw-border-opacity));
}

.border-x-green-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(74 222 128 / var(--tw-border-opacity));
  border-right-color: rgb(74 222 128 / var(--tw-border-opacity));
}

.border-x-green-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(240 253 244 / var(--tw-border-opacity));
  border-right-color: rgb(240 253 244 / var(--tw-border-opacity));
}

.border-x-green-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(34 197 94 / var(--tw-border-opacity));
  border-right-color: rgb(34 197 94 / var(--tw-border-opacity));
}

.border-x-green-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(22 163 74 / var(--tw-border-opacity));
  border-right-color: rgb(22 163 74 / var(--tw-border-opacity));
}

.border-x-green-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(21 128 61 / var(--tw-border-opacity));
  border-right-color: rgb(21 128 61 / var(--tw-border-opacity));
}

.border-x-green-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(22 101 52 / var(--tw-border-opacity));
  border-right-color: rgb(22 101 52 / var(--tw-border-opacity));
}

.border-x-green-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(20 83 45 / var(--tw-border-opacity));
  border-right-color: rgb(20 83 45 / var(--tw-border-opacity));
}

.border-x-green-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(5 46 22 / var(--tw-border-opacity));
  border-right-color: rgb(5 46 22 / var(--tw-border-opacity));
}

.border-x-indigo-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(224 231 255 / var(--tw-border-opacity));
  border-right-color: rgb(224 231 255 / var(--tw-border-opacity));
}

.border-x-indigo-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(199 210 254 / var(--tw-border-opacity));
  border-right-color: rgb(199 210 254 / var(--tw-border-opacity));
}

.border-x-indigo-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(165 180 252 / var(--tw-border-opacity));
  border-right-color: rgb(165 180 252 / var(--tw-border-opacity));
}

.border-x-indigo-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(129 140 248 / var(--tw-border-opacity));
  border-right-color: rgb(129 140 248 / var(--tw-border-opacity));
}

.border-x-indigo-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(238 242 255 / var(--tw-border-opacity));
  border-right-color: rgb(238 242 255 / var(--tw-border-opacity));
}

.border-x-indigo-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(99 102 241 / var(--tw-border-opacity));
  border-right-color: rgb(99 102 241 / var(--tw-border-opacity));
}

.border-x-indigo-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(79 70 229 / var(--tw-border-opacity));
  border-right-color: rgb(79 70 229 / var(--tw-border-opacity));
}

.border-x-indigo-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(67 56 202 / var(--tw-border-opacity));
  border-right-color: rgb(67 56 202 / var(--tw-border-opacity));
}

.border-x-indigo-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(55 48 163 / var(--tw-border-opacity));
  border-right-color: rgb(55 48 163 / var(--tw-border-opacity));
}

.border-x-indigo-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(49 46 129 / var(--tw-border-opacity));
  border-right-color: rgb(49 46 129 / var(--tw-border-opacity));
}

.border-x-indigo-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(30 27 75 / var(--tw-border-opacity));
  border-right-color: rgb(30 27 75 / var(--tw-border-opacity));
}

.border-x-inherit {
  border-left-color: inherit;
  border-right-color: inherit;
}

.border-x-lime-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(236 252 203 / var(--tw-border-opacity));
  border-right-color: rgb(236 252 203 / var(--tw-border-opacity));
}

.border-x-lime-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(217 249 157 / var(--tw-border-opacity));
  border-right-color: rgb(217 249 157 / var(--tw-border-opacity));
}

.border-x-lime-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(190 242 100 / var(--tw-border-opacity));
  border-right-color: rgb(190 242 100 / var(--tw-border-opacity));
}

.border-x-lime-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(163 230 53 / var(--tw-border-opacity));
  border-right-color: rgb(163 230 53 / var(--tw-border-opacity));
}

.border-x-lime-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(247 254 231 / var(--tw-border-opacity));
  border-right-color: rgb(247 254 231 / var(--tw-border-opacity));
}

.border-x-lime-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(132 204 22 / var(--tw-border-opacity));
  border-right-color: rgb(132 204 22 / var(--tw-border-opacity));
}

.border-x-lime-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(101 163 13 / var(--tw-border-opacity));
  border-right-color: rgb(101 163 13 / var(--tw-border-opacity));
}

.border-x-lime-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(77 124 15 / var(--tw-border-opacity));
  border-right-color: rgb(77 124 15 / var(--tw-border-opacity));
}

.border-x-lime-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(63 98 18 / var(--tw-border-opacity));
  border-right-color: rgb(63 98 18 / var(--tw-border-opacity));
}

.border-x-lime-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(54 83 20 / var(--tw-border-opacity));
  border-right-color: rgb(54 83 20 / var(--tw-border-opacity));
}

.border-x-lime-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(26 46 5 / var(--tw-border-opacity));
  border-right-color: rgb(26 46 5 / var(--tw-border-opacity));
}

.border-x-neutral-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(245 245 245 / var(--tw-border-opacity));
  border-right-color: rgb(245 245 245 / var(--tw-border-opacity));
}

.border-x-neutral-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(229 229 229 / var(--tw-border-opacity));
  border-right-color: rgb(229 229 229 / var(--tw-border-opacity));
}

.border-x-neutral-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(212 212 212 / var(--tw-border-opacity));
  border-right-color: rgb(212 212 212 / var(--tw-border-opacity));
}

.border-x-neutral-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(163 163 163 / var(--tw-border-opacity));
  border-right-color: rgb(163 163 163 / var(--tw-border-opacity));
}

.border-x-neutral-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(250 250 250 / var(--tw-border-opacity));
  border-right-color: rgb(250 250 250 / var(--tw-border-opacity));
}

.border-x-neutral-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(115 115 115 / var(--tw-border-opacity));
  border-right-color: rgb(115 115 115 / var(--tw-border-opacity));
}

.border-x-neutral-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(82 82 82 / var(--tw-border-opacity));
  border-right-color: rgb(82 82 82 / var(--tw-border-opacity));
}

.border-x-neutral-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(64 64 64 / var(--tw-border-opacity));
  border-right-color: rgb(64 64 64 / var(--tw-border-opacity));
}

.border-x-neutral-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(38 38 38 / var(--tw-border-opacity));
  border-right-color: rgb(38 38 38 / var(--tw-border-opacity));
}

.border-x-neutral-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(23 23 23 / var(--tw-border-opacity));
  border-right-color: rgb(23 23 23 / var(--tw-border-opacity));
}

.border-x-neutral-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(10 10 10 / var(--tw-border-opacity));
  border-right-color: rgb(10 10 10 / var(--tw-border-opacity));
}

.border-x-orange-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(255 237 213 / var(--tw-border-opacity));
  border-right-color: rgb(255 237 213 / var(--tw-border-opacity));
}

.border-x-orange-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(254 215 170 / var(--tw-border-opacity));
  border-right-color: rgb(254 215 170 / var(--tw-border-opacity));
}

.border-x-orange-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(253 186 116 / var(--tw-border-opacity));
  border-right-color: rgb(253 186 116 / var(--tw-border-opacity));
}

.border-x-orange-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(251 146 60 / var(--tw-border-opacity));
  border-right-color: rgb(251 146 60 / var(--tw-border-opacity));
}

.border-x-orange-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(255 247 237 / var(--tw-border-opacity));
  border-right-color: rgb(255 247 237 / var(--tw-border-opacity));
}

.border-x-orange-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(249 115 22 / var(--tw-border-opacity));
  border-right-color: rgb(249 115 22 / var(--tw-border-opacity));
}

.border-x-orange-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(234 88 12 / var(--tw-border-opacity));
  border-right-color: rgb(234 88 12 / var(--tw-border-opacity));
}

.border-x-orange-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(194 65 12 / var(--tw-border-opacity));
  border-right-color: rgb(194 65 12 / var(--tw-border-opacity));
}

.border-x-orange-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(154 52 18 / var(--tw-border-opacity));
  border-right-color: rgb(154 52 18 / var(--tw-border-opacity));
}

.border-x-orange-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(124 45 18 / var(--tw-border-opacity));
  border-right-color: rgb(124 45 18 / var(--tw-border-opacity));
}

.border-x-orange-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(67 20 7 / var(--tw-border-opacity));
  border-right-color: rgb(67 20 7 / var(--tw-border-opacity));
}

.border-x-pink-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(252 231 243 / var(--tw-border-opacity));
  border-right-color: rgb(252 231 243 / var(--tw-border-opacity));
}

.border-x-pink-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(251 207 232 / var(--tw-border-opacity));
  border-right-color: rgb(251 207 232 / var(--tw-border-opacity));
}

.border-x-pink-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(249 168 212 / var(--tw-border-opacity));
  border-right-color: rgb(249 168 212 / var(--tw-border-opacity));
}

.border-x-pink-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(244 114 182 / var(--tw-border-opacity));
  border-right-color: rgb(244 114 182 / var(--tw-border-opacity));
}

.border-x-pink-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(253 242 248 / var(--tw-border-opacity));
  border-right-color: rgb(253 242 248 / var(--tw-border-opacity));
}

.border-x-pink-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(236 72 153 / var(--tw-border-opacity));
  border-right-color: rgb(236 72 153 / var(--tw-border-opacity));
}

.border-x-pink-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(219 39 119 / var(--tw-border-opacity));
  border-right-color: rgb(219 39 119 / var(--tw-border-opacity));
}

.border-x-pink-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(190 24 93 / var(--tw-border-opacity));
  border-right-color: rgb(190 24 93 / var(--tw-border-opacity));
}

.border-x-pink-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(157 23 77 / var(--tw-border-opacity));
  border-right-color: rgb(157 23 77 / var(--tw-border-opacity));
}

.border-x-pink-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(131 24 67 / var(--tw-border-opacity));
  border-right-color: rgb(131 24 67 / var(--tw-border-opacity));
}

.border-x-pink-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(80 7 36 / var(--tw-border-opacity));
  border-right-color: rgb(80 7 36 / var(--tw-border-opacity));
}

.border-x-purple-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(243 232 255 / var(--tw-border-opacity));
  border-right-color: rgb(243 232 255 / var(--tw-border-opacity));
}

.border-x-purple-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(233 213 255 / var(--tw-border-opacity));
  border-right-color: rgb(233 213 255 / var(--tw-border-opacity));
}

.border-x-purple-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(216 180 254 / var(--tw-border-opacity));
  border-right-color: rgb(216 180 254 / var(--tw-border-opacity));
}

.border-x-purple-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(192 132 252 / var(--tw-border-opacity));
  border-right-color: rgb(192 132 252 / var(--tw-border-opacity));
}

.border-x-purple-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(250 245 255 / var(--tw-border-opacity));
  border-right-color: rgb(250 245 255 / var(--tw-border-opacity));
}

.border-x-purple-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(168 85 247 / var(--tw-border-opacity));
  border-right-color: rgb(168 85 247 / var(--tw-border-opacity));
}

.border-x-purple-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(147 51 234 / var(--tw-border-opacity));
  border-right-color: rgb(147 51 234 / var(--tw-border-opacity));
}

.border-x-purple-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(126 34 206 / var(--tw-border-opacity));
  border-right-color: rgb(126 34 206 / var(--tw-border-opacity));
}

.border-x-purple-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(107 33 168 / var(--tw-border-opacity));
  border-right-color: rgb(107 33 168 / var(--tw-border-opacity));
}

.border-x-purple-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(88 28 135 / var(--tw-border-opacity));
  border-right-color: rgb(88 28 135 / var(--tw-border-opacity));
}

.border-x-purple-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(59 7 100 / var(--tw-border-opacity));
  border-right-color: rgb(59 7 100 / var(--tw-border-opacity));
}

.border-x-red-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(254 226 226 / var(--tw-border-opacity));
  border-right-color: rgb(254 226 226 / var(--tw-border-opacity));
}

.border-x-red-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(254 202 202 / var(--tw-border-opacity));
  border-right-color: rgb(254 202 202 / var(--tw-border-opacity));
}

.border-x-red-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(252 165 165 / var(--tw-border-opacity));
  border-right-color: rgb(252 165 165 / var(--tw-border-opacity));
}

.border-x-red-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(248 113 113 / var(--tw-border-opacity));
  border-right-color: rgb(248 113 113 / var(--tw-border-opacity));
}

.border-x-red-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(254 242 242 / var(--tw-border-opacity));
  border-right-color: rgb(254 242 242 / var(--tw-border-opacity));
}

.border-x-red-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(239 68 68 / var(--tw-border-opacity));
  border-right-color: rgb(239 68 68 / var(--tw-border-opacity));
}

.border-x-red-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(220 38 38 / var(--tw-border-opacity));
  border-right-color: rgb(220 38 38 / var(--tw-border-opacity));
}

.border-x-red-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(185 28 28 / var(--tw-border-opacity));
  border-right-color: rgb(185 28 28 / var(--tw-border-opacity));
}

.border-x-red-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(153 27 27 / var(--tw-border-opacity));
  border-right-color: rgb(153 27 27 / var(--tw-border-opacity));
}

.border-x-red-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(127 29 29 / var(--tw-border-opacity));
  border-right-color: rgb(127 29 29 / var(--tw-border-opacity));
}

.border-x-red-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(69 10 10 / var(--tw-border-opacity));
  border-right-color: rgb(69 10 10 / var(--tw-border-opacity));
}

.border-x-rose-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(255 228 230 / var(--tw-border-opacity));
  border-right-color: rgb(255 228 230 / var(--tw-border-opacity));
}

.border-x-rose-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(254 205 211 / var(--tw-border-opacity));
  border-right-color: rgb(254 205 211 / var(--tw-border-opacity));
}

.border-x-rose-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(253 164 175 / var(--tw-border-opacity));
  border-right-color: rgb(253 164 175 / var(--tw-border-opacity));
}

.border-x-rose-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(251 113 133 / var(--tw-border-opacity));
  border-right-color: rgb(251 113 133 / var(--tw-border-opacity));
}

.border-x-rose-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(255 241 242 / var(--tw-border-opacity));
  border-right-color: rgb(255 241 242 / var(--tw-border-opacity));
}

.border-x-rose-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(244 63 94 / var(--tw-border-opacity));
  border-right-color: rgb(244 63 94 / var(--tw-border-opacity));
}

.border-x-rose-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(225 29 72 / var(--tw-border-opacity));
  border-right-color: rgb(225 29 72 / var(--tw-border-opacity));
}

.border-x-rose-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(190 18 60 / var(--tw-border-opacity));
  border-right-color: rgb(190 18 60 / var(--tw-border-opacity));
}

.border-x-rose-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(159 18 57 / var(--tw-border-opacity));
  border-right-color: rgb(159 18 57 / var(--tw-border-opacity));
}

.border-x-rose-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(136 19 55 / var(--tw-border-opacity));
  border-right-color: rgb(136 19 55 / var(--tw-border-opacity));
}

.border-x-rose-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(76 5 25 / var(--tw-border-opacity));
  border-right-color: rgb(76 5 25 / var(--tw-border-opacity));
}

.border-x-sky-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(224 242 254 / var(--tw-border-opacity));
  border-right-color: rgb(224 242 254 / var(--tw-border-opacity));
}

.border-x-sky-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(186 230 253 / var(--tw-border-opacity));
  border-right-color: rgb(186 230 253 / var(--tw-border-opacity));
}

.border-x-sky-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(125 211 252 / var(--tw-border-opacity));
  border-right-color: rgb(125 211 252 / var(--tw-border-opacity));
}

.border-x-sky-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(56 189 248 / var(--tw-border-opacity));
  border-right-color: rgb(56 189 248 / var(--tw-border-opacity));
}

.border-x-sky-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(240 249 255 / var(--tw-border-opacity));
  border-right-color: rgb(240 249 255 / var(--tw-border-opacity));
}

.border-x-sky-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(14 165 233 / var(--tw-border-opacity));
  border-right-color: rgb(14 165 233 / var(--tw-border-opacity));
}

.border-x-sky-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(2 132 199 / var(--tw-border-opacity));
  border-right-color: rgb(2 132 199 / var(--tw-border-opacity));
}

.border-x-sky-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(3 105 161 / var(--tw-border-opacity));
  border-right-color: rgb(3 105 161 / var(--tw-border-opacity));
}

.border-x-sky-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(7 89 133 / var(--tw-border-opacity));
  border-right-color: rgb(7 89 133 / var(--tw-border-opacity));
}

.border-x-sky-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(12 74 110 / var(--tw-border-opacity));
  border-right-color: rgb(12 74 110 / var(--tw-border-opacity));
}

.border-x-sky-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(8 47 73 / var(--tw-border-opacity));
  border-right-color: rgb(8 47 73 / var(--tw-border-opacity));
}

.border-x-slate-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(241 245 249 / var(--tw-border-opacity));
  border-right-color: rgb(241 245 249 / var(--tw-border-opacity));
}

.border-x-slate-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(226 232 240 / var(--tw-border-opacity));
  border-right-color: rgb(226 232 240 / var(--tw-border-opacity));
}

.border-x-slate-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(203 213 225 / var(--tw-border-opacity));
  border-right-color: rgb(203 213 225 / var(--tw-border-opacity));
}

.border-x-slate-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(148 163 184 / var(--tw-border-opacity));
  border-right-color: rgb(148 163 184 / var(--tw-border-opacity));
}

.border-x-slate-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(248 250 252 / var(--tw-border-opacity));
  border-right-color: rgb(248 250 252 / var(--tw-border-opacity));
}

.border-x-slate-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(100 116 139 / var(--tw-border-opacity));
  border-right-color: rgb(100 116 139 / var(--tw-border-opacity));
}

.border-x-slate-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(71 85 105 / var(--tw-border-opacity));
  border-right-color: rgb(71 85 105 / var(--tw-border-opacity));
}

.border-x-slate-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(51 65 85 / var(--tw-border-opacity));
  border-right-color: rgb(51 65 85 / var(--tw-border-opacity));
}

.border-x-slate-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(30 41 59 / var(--tw-border-opacity));
  border-right-color: rgb(30 41 59 / var(--tw-border-opacity));
}

.border-x-slate-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(15 23 42 / var(--tw-border-opacity));
  border-right-color: rgb(15 23 42 / var(--tw-border-opacity));
}

.border-x-slate-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(2 6 23 / var(--tw-border-opacity));
  border-right-color: rgb(2 6 23 / var(--tw-border-opacity));
}

.border-x-stone-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(245 245 244 / var(--tw-border-opacity));
  border-right-color: rgb(245 245 244 / var(--tw-border-opacity));
}

.border-x-stone-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(231 229 228 / var(--tw-border-opacity));
  border-right-color: rgb(231 229 228 / var(--tw-border-opacity));
}

.border-x-stone-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(214 211 209 / var(--tw-border-opacity));
  border-right-color: rgb(214 211 209 / var(--tw-border-opacity));
}

.border-x-stone-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(168 162 158 / var(--tw-border-opacity));
  border-right-color: rgb(168 162 158 / var(--tw-border-opacity));
}

.border-x-stone-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(250 250 249 / var(--tw-border-opacity));
  border-right-color: rgb(250 250 249 / var(--tw-border-opacity));
}

.border-x-stone-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(120 113 108 / var(--tw-border-opacity));
  border-right-color: rgb(120 113 108 / var(--tw-border-opacity));
}

.border-x-stone-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(87 83 78 / var(--tw-border-opacity));
  border-right-color: rgb(87 83 78 / var(--tw-border-opacity));
}

.border-x-stone-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(68 64 60 / var(--tw-border-opacity));
  border-right-color: rgb(68 64 60 / var(--tw-border-opacity));
}

.border-x-stone-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(41 37 36 / var(--tw-border-opacity));
  border-right-color: rgb(41 37 36 / var(--tw-border-opacity));
}

.border-x-stone-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(28 25 23 / var(--tw-border-opacity));
  border-right-color: rgb(28 25 23 / var(--tw-border-opacity));
}

.border-x-stone-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(12 10 9 / var(--tw-border-opacity));
  border-right-color: rgb(12 10 9 / var(--tw-border-opacity));
}

.border-x-teal-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(204 251 241 / var(--tw-border-opacity));
  border-right-color: rgb(204 251 241 / var(--tw-border-opacity));
}

.border-x-teal-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(153 246 228 / var(--tw-border-opacity));
  border-right-color: rgb(153 246 228 / var(--tw-border-opacity));
}

.border-x-teal-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(94 234 212 / var(--tw-border-opacity));
  border-right-color: rgb(94 234 212 / var(--tw-border-opacity));
}

.border-x-teal-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(45 212 191 / var(--tw-border-opacity));
  border-right-color: rgb(45 212 191 / var(--tw-border-opacity));
}

.border-x-teal-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(240 253 250 / var(--tw-border-opacity));
  border-right-color: rgb(240 253 250 / var(--tw-border-opacity));
}

.border-x-teal-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(20 184 166 / var(--tw-border-opacity));
  border-right-color: rgb(20 184 166 / var(--tw-border-opacity));
}

.border-x-teal-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(13 148 136 / var(--tw-border-opacity));
  border-right-color: rgb(13 148 136 / var(--tw-border-opacity));
}

.border-x-teal-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(15 118 110 / var(--tw-border-opacity));
  border-right-color: rgb(15 118 110 / var(--tw-border-opacity));
}

.border-x-teal-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(17 94 89 / var(--tw-border-opacity));
  border-right-color: rgb(17 94 89 / var(--tw-border-opacity));
}

.border-x-teal-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(19 78 74 / var(--tw-border-opacity));
  border-right-color: rgb(19 78 74 / var(--tw-border-opacity));
}

.border-x-teal-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(4 47 46 / var(--tw-border-opacity));
  border-right-color: rgb(4 47 46 / var(--tw-border-opacity));
}

.border-x-transparent {
  border-left-color: transparent;
  border-right-color: transparent;
}

.border-x-violet-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(237 233 254 / var(--tw-border-opacity));
  border-right-color: rgb(237 233 254 / var(--tw-border-opacity));
}

.border-x-violet-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(221 214 254 / var(--tw-border-opacity));
  border-right-color: rgb(221 214 254 / var(--tw-border-opacity));
}

.border-x-violet-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(196 181 253 / var(--tw-border-opacity));
  border-right-color: rgb(196 181 253 / var(--tw-border-opacity));
}

.border-x-violet-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(167 139 250 / var(--tw-border-opacity));
  border-right-color: rgb(167 139 250 / var(--tw-border-opacity));
}

.border-x-violet-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(245 243 255 / var(--tw-border-opacity));
  border-right-color: rgb(245 243 255 / var(--tw-border-opacity));
}

.border-x-violet-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(139 92 246 / var(--tw-border-opacity));
  border-right-color: rgb(139 92 246 / var(--tw-border-opacity));
}

.border-x-violet-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(124 58 237 / var(--tw-border-opacity));
  border-right-color: rgb(124 58 237 / var(--tw-border-opacity));
}

.border-x-violet-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(109 40 217 / var(--tw-border-opacity));
  border-right-color: rgb(109 40 217 / var(--tw-border-opacity));
}

.border-x-violet-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(91 33 182 / var(--tw-border-opacity));
  border-right-color: rgb(91 33 182 / var(--tw-border-opacity));
}

.border-x-violet-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(76 29 149 / var(--tw-border-opacity));
  border-right-color: rgb(76 29 149 / var(--tw-border-opacity));
}

.border-x-violet-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(46 16 101 / var(--tw-border-opacity));
  border-right-color: rgb(46 16 101 / var(--tw-border-opacity));
}

.border-x-white {
  --tw-border-opacity: 1;
  border-left-color: rgb(255 255 255 / var(--tw-border-opacity));
  border-right-color: rgb(255 255 255 / var(--tw-border-opacity));
}

.border-x-yellow-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(254 249 195 / var(--tw-border-opacity));
  border-right-color: rgb(254 249 195 / var(--tw-border-opacity));
}

.border-x-yellow-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(254 240 138 / var(--tw-border-opacity));
  border-right-color: rgb(254 240 138 / var(--tw-border-opacity));
}

.border-x-yellow-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(253 224 71 / var(--tw-border-opacity));
  border-right-color: rgb(253 224 71 / var(--tw-border-opacity));
}

.border-x-yellow-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(250 204 21 / var(--tw-border-opacity));
  border-right-color: rgb(250 204 21 / var(--tw-border-opacity));
}

.border-x-yellow-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(254 252 232 / var(--tw-border-opacity));
  border-right-color: rgb(254 252 232 / var(--tw-border-opacity));
}

.border-x-yellow-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(234 179 8 / var(--tw-border-opacity));
  border-right-color: rgb(234 179 8 / var(--tw-border-opacity));
}

.border-x-yellow-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(202 138 4 / var(--tw-border-opacity));
  border-right-color: rgb(202 138 4 / var(--tw-border-opacity));
}

.border-x-yellow-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(161 98 7 / var(--tw-border-opacity));
  border-right-color: rgb(161 98 7 / var(--tw-border-opacity));
}

.border-x-yellow-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(133 77 14 / var(--tw-border-opacity));
  border-right-color: rgb(133 77 14 / var(--tw-border-opacity));
}

.border-x-yellow-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(113 63 18 / var(--tw-border-opacity));
  border-right-color: rgb(113 63 18 / var(--tw-border-opacity));
}

.border-x-yellow-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(66 32 6 / var(--tw-border-opacity));
  border-right-color: rgb(66 32 6 / var(--tw-border-opacity));
}

.border-x-zinc-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(244 244 245 / var(--tw-border-opacity));
  border-right-color: rgb(244 244 245 / var(--tw-border-opacity));
}

.border-x-zinc-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(228 228 231 / var(--tw-border-opacity));
  border-right-color: rgb(228 228 231 / var(--tw-border-opacity));
}

.border-x-zinc-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(212 212 216 / var(--tw-border-opacity));
  border-right-color: rgb(212 212 216 / var(--tw-border-opacity));
}

.border-x-zinc-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(161 161 170 / var(--tw-border-opacity));
  border-right-color: rgb(161 161 170 / var(--tw-border-opacity));
}

.border-x-zinc-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(250 250 250 / var(--tw-border-opacity));
  border-right-color: rgb(250 250 250 / var(--tw-border-opacity));
}

.border-x-zinc-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(113 113 122 / var(--tw-border-opacity));
  border-right-color: rgb(113 113 122 / var(--tw-border-opacity));
}

.border-x-zinc-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(82 82 91 / var(--tw-border-opacity));
  border-right-color: rgb(82 82 91 / var(--tw-border-opacity));
}

.border-x-zinc-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(63 63 70 / var(--tw-border-opacity));
  border-right-color: rgb(63 63 70 / var(--tw-border-opacity));
}

.border-x-zinc-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(39 39 42 / var(--tw-border-opacity));
  border-right-color: rgb(39 39 42 / var(--tw-border-opacity));
}

.border-x-zinc-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(24 24 27 / var(--tw-border-opacity));
  border-right-color: rgb(24 24 27 / var(--tw-border-opacity));
}

.border-x-zinc-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(9 9 11 / var(--tw-border-opacity));
  border-right-color: rgb(9 9 11 / var(--tw-border-opacity));
}

.border-y-amber-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(254 243 199 / var(--tw-border-opacity));
  border-bottom-color: rgb(254 243 199 / var(--tw-border-opacity));
}

.border-y-amber-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(253 230 138 / var(--tw-border-opacity));
  border-bottom-color: rgb(253 230 138 / var(--tw-border-opacity));
}

.border-y-amber-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(252 211 77 / var(--tw-border-opacity));
  border-bottom-color: rgb(252 211 77 / var(--tw-border-opacity));
}

.border-y-amber-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(251 191 36 / var(--tw-border-opacity));
  border-bottom-color: rgb(251 191 36 / var(--tw-border-opacity));
}

.border-y-amber-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(255 251 235 / var(--tw-border-opacity));
  border-bottom-color: rgb(255 251 235 / var(--tw-border-opacity));
}

.border-y-amber-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(245 158 11 / var(--tw-border-opacity));
  border-bottom-color: rgb(245 158 11 / var(--tw-border-opacity));
}

.border-y-amber-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(217 119 6 / var(--tw-border-opacity));
  border-bottom-color: rgb(217 119 6 / var(--tw-border-opacity));
}

.border-y-amber-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(180 83 9 / var(--tw-border-opacity));
  border-bottom-color: rgb(180 83 9 / var(--tw-border-opacity));
}

.border-y-amber-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(146 64 14 / var(--tw-border-opacity));
  border-bottom-color: rgb(146 64 14 / var(--tw-border-opacity));
}

.border-y-amber-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(120 53 15 / var(--tw-border-opacity));
  border-bottom-color: rgb(120 53 15 / var(--tw-border-opacity));
}

.border-y-amber-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(69 26 3 / var(--tw-border-opacity));
  border-bottom-color: rgb(69 26 3 / var(--tw-border-opacity));
}

.border-y-black {
  --tw-border-opacity: 1;
  border-top-color: rgb(0 0 0 / var(--tw-border-opacity));
  border-bottom-color: rgb(0 0 0 / var(--tw-border-opacity));
}

.border-y-blue-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(219 234 254 / var(--tw-border-opacity));
  border-bottom-color: rgb(219 234 254 / var(--tw-border-opacity));
}

.border-y-blue-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(191 219 254 / var(--tw-border-opacity));
  border-bottom-color: rgb(191 219 254 / var(--tw-border-opacity));
}

.border-y-blue-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(147 197 253 / var(--tw-border-opacity));
  border-bottom-color: rgb(147 197 253 / var(--tw-border-opacity));
}

.border-y-blue-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(96 165 250 / var(--tw-border-opacity));
  border-bottom-color: rgb(96 165 250 / var(--tw-border-opacity));
}

.border-y-blue-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(239 246 255 / var(--tw-border-opacity));
  border-bottom-color: rgb(239 246 255 / var(--tw-border-opacity));
}

.border-y-blue-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(59 130 246 / var(--tw-border-opacity));
  border-bottom-color: rgb(59 130 246 / var(--tw-border-opacity));
}

.border-y-blue-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(37 99 235 / var(--tw-border-opacity));
  border-bottom-color: rgb(37 99 235 / var(--tw-border-opacity));
}

.border-y-blue-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(29 78 216 / var(--tw-border-opacity));
  border-bottom-color: rgb(29 78 216 / var(--tw-border-opacity));
}

.border-y-blue-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(30 64 175 / var(--tw-border-opacity));
  border-bottom-color: rgb(30 64 175 / var(--tw-border-opacity));
}

.border-y-blue-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(30 58 138 / var(--tw-border-opacity));
  border-bottom-color: rgb(30 58 138 / var(--tw-border-opacity));
}

.border-y-blue-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(23 37 84 / var(--tw-border-opacity));
  border-bottom-color: rgb(23 37 84 / var(--tw-border-opacity));
}

.border-y-current {
  border-top-color: currentColor;
  border-bottom-color: currentColor;
}

.border-y-cyan-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(207 250 254 / var(--tw-border-opacity));
  border-bottom-color: rgb(207 250 254 / var(--tw-border-opacity));
}

.border-y-cyan-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(165 243 252 / var(--tw-border-opacity));
  border-bottom-color: rgb(165 243 252 / var(--tw-border-opacity));
}

.border-y-cyan-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(103 232 249 / var(--tw-border-opacity));
  border-bottom-color: rgb(103 232 249 / var(--tw-border-opacity));
}

.border-y-cyan-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(34 211 238 / var(--tw-border-opacity));
  border-bottom-color: rgb(34 211 238 / var(--tw-border-opacity));
}

.border-y-cyan-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(236 254 255 / var(--tw-border-opacity));
  border-bottom-color: rgb(236 254 255 / var(--tw-border-opacity));
}

.border-y-cyan-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(6 182 212 / var(--tw-border-opacity));
  border-bottom-color: rgb(6 182 212 / var(--tw-border-opacity));
}

.border-y-cyan-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(8 145 178 / var(--tw-border-opacity));
  border-bottom-color: rgb(8 145 178 / var(--tw-border-opacity));
}

.border-y-cyan-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(14 116 144 / var(--tw-border-opacity));
  border-bottom-color: rgb(14 116 144 / var(--tw-border-opacity));
}

.border-y-cyan-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(21 94 117 / var(--tw-border-opacity));
  border-bottom-color: rgb(21 94 117 / var(--tw-border-opacity));
}

.border-y-cyan-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(22 78 99 / var(--tw-border-opacity));
  border-bottom-color: rgb(22 78 99 / var(--tw-border-opacity));
}

.border-y-cyan-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(8 51 68 / var(--tw-border-opacity));
  border-bottom-color: rgb(8 51 68 / var(--tw-border-opacity));
}

.border-y-emerald-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(209 250 229 / var(--tw-border-opacity));
  border-bottom-color: rgb(209 250 229 / var(--tw-border-opacity));
}

.border-y-emerald-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(167 243 208 / var(--tw-border-opacity));
  border-bottom-color: rgb(167 243 208 / var(--tw-border-opacity));
}

.border-y-emerald-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(110 231 183 / var(--tw-border-opacity));
  border-bottom-color: rgb(110 231 183 / var(--tw-border-opacity));
}

.border-y-emerald-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(52 211 153 / var(--tw-border-opacity));
  border-bottom-color: rgb(52 211 153 / var(--tw-border-opacity));
}

.border-y-emerald-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(236 253 245 / var(--tw-border-opacity));
  border-bottom-color: rgb(236 253 245 / var(--tw-border-opacity));
}

.border-y-emerald-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(16 185 129 / var(--tw-border-opacity));
  border-bottom-color: rgb(16 185 129 / var(--tw-border-opacity));
}

.border-y-emerald-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(5 150 105 / var(--tw-border-opacity));
  border-bottom-color: rgb(5 150 105 / var(--tw-border-opacity));
}

.border-y-emerald-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(4 120 87 / var(--tw-border-opacity));
  border-bottom-color: rgb(4 120 87 / var(--tw-border-opacity));
}

.border-y-emerald-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(6 95 70 / var(--tw-border-opacity));
  border-bottom-color: rgb(6 95 70 / var(--tw-border-opacity));
}

.border-y-emerald-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(6 78 59 / var(--tw-border-opacity));
  border-bottom-color: rgb(6 78 59 / var(--tw-border-opacity));
}

.border-y-emerald-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(2 44 34 / var(--tw-border-opacity));
  border-bottom-color: rgb(2 44 34 / var(--tw-border-opacity));
}

.border-y-fuchsia-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(250 232 255 / var(--tw-border-opacity));
  border-bottom-color: rgb(250 232 255 / var(--tw-border-opacity));
}

.border-y-fuchsia-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(245 208 254 / var(--tw-border-opacity));
  border-bottom-color: rgb(245 208 254 / var(--tw-border-opacity));
}

.border-y-fuchsia-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(240 171 252 / var(--tw-border-opacity));
  border-bottom-color: rgb(240 171 252 / var(--tw-border-opacity));
}

.border-y-fuchsia-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(232 121 249 / var(--tw-border-opacity));
  border-bottom-color: rgb(232 121 249 / var(--tw-border-opacity));
}

.border-y-fuchsia-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(253 244 255 / var(--tw-border-opacity));
  border-bottom-color: rgb(253 244 255 / var(--tw-border-opacity));
}

.border-y-fuchsia-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(217 70 239 / var(--tw-border-opacity));
  border-bottom-color: rgb(217 70 239 / var(--tw-border-opacity));
}

.border-y-fuchsia-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(192 38 211 / var(--tw-border-opacity));
  border-bottom-color: rgb(192 38 211 / var(--tw-border-opacity));
}

.border-y-fuchsia-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(162 28 175 / var(--tw-border-opacity));
  border-bottom-color: rgb(162 28 175 / var(--tw-border-opacity));
}

.border-y-fuchsia-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(134 25 143 / var(--tw-border-opacity));
  border-bottom-color: rgb(134 25 143 / var(--tw-border-opacity));
}

.border-y-fuchsia-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(112 26 117 / var(--tw-border-opacity));
  border-bottom-color: rgb(112 26 117 / var(--tw-border-opacity));
}

.border-y-fuchsia-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(74 4 78 / var(--tw-border-opacity));
  border-bottom-color: rgb(74 4 78 / var(--tw-border-opacity));
}

.border-y-gray-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(243 244 246 / var(--tw-border-opacity));
  border-bottom-color: rgb(243 244 246 / var(--tw-border-opacity));
}

.border-y-gray-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(229 231 235 / var(--tw-border-opacity));
  border-bottom-color: rgb(229 231 235 / var(--tw-border-opacity));
}

.border-y-gray-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(209 213 219 / var(--tw-border-opacity));
  border-bottom-color: rgb(209 213 219 / var(--tw-border-opacity));
}

.border-y-gray-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(156 163 175 / var(--tw-border-opacity));
  border-bottom-color: rgb(156 163 175 / var(--tw-border-opacity));
}

.border-y-gray-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(249 250 251 / var(--tw-border-opacity));
  border-bottom-color: rgb(249 250 251 / var(--tw-border-opacity));
}

.border-y-gray-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(107 114 128 / var(--tw-border-opacity));
  border-bottom-color: rgb(107 114 128 / var(--tw-border-opacity));
}

.border-y-gray-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(75 85 99 / var(--tw-border-opacity));
  border-bottom-color: rgb(75 85 99 / var(--tw-border-opacity));
}

.border-y-gray-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(55 65 81 / var(--tw-border-opacity));
  border-bottom-color: rgb(55 65 81 / var(--tw-border-opacity));
}

.border-y-gray-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(31 41 55 / var(--tw-border-opacity));
  border-bottom-color: rgb(31 41 55 / var(--tw-border-opacity));
}

.border-y-gray-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(17 24 39 / var(--tw-border-opacity));
  border-bottom-color: rgb(17 24 39 / var(--tw-border-opacity));
}

.border-y-gray-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(3 7 18 / var(--tw-border-opacity));
  border-bottom-color: rgb(3 7 18 / var(--tw-border-opacity));
}

.border-y-green-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(220 252 231 / var(--tw-border-opacity));
  border-bottom-color: rgb(220 252 231 / var(--tw-border-opacity));
}

.border-y-green-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(187 247 208 / var(--tw-border-opacity));
  border-bottom-color: rgb(187 247 208 / var(--tw-border-opacity));
}

.border-y-green-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(134 239 172 / var(--tw-border-opacity));
  border-bottom-color: rgb(134 239 172 / var(--tw-border-opacity));
}

.border-y-green-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(74 222 128 / var(--tw-border-opacity));
  border-bottom-color: rgb(74 222 128 / var(--tw-border-opacity));
}

.border-y-green-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(240 253 244 / var(--tw-border-opacity));
  border-bottom-color: rgb(240 253 244 / var(--tw-border-opacity));
}

.border-y-green-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(34 197 94 / var(--tw-border-opacity));
  border-bottom-color: rgb(34 197 94 / var(--tw-border-opacity));
}

.border-y-green-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(22 163 74 / var(--tw-border-opacity));
  border-bottom-color: rgb(22 163 74 / var(--tw-border-opacity));
}

.border-y-green-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(21 128 61 / var(--tw-border-opacity));
  border-bottom-color: rgb(21 128 61 / var(--tw-border-opacity));
}

.border-y-green-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(22 101 52 / var(--tw-border-opacity));
  border-bottom-color: rgb(22 101 52 / var(--tw-border-opacity));
}

.border-y-green-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(20 83 45 / var(--tw-border-opacity));
  border-bottom-color: rgb(20 83 45 / var(--tw-border-opacity));
}

.border-y-green-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(5 46 22 / var(--tw-border-opacity));
  border-bottom-color: rgb(5 46 22 / var(--tw-border-opacity));
}

.border-y-indigo-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(224 231 255 / var(--tw-border-opacity));
  border-bottom-color: rgb(224 231 255 / var(--tw-border-opacity));
}

.border-y-indigo-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(199 210 254 / var(--tw-border-opacity));
  border-bottom-color: rgb(199 210 254 / var(--tw-border-opacity));
}

.border-y-indigo-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(165 180 252 / var(--tw-border-opacity));
  border-bottom-color: rgb(165 180 252 / var(--tw-border-opacity));
}

.border-y-indigo-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(129 140 248 / var(--tw-border-opacity));
  border-bottom-color: rgb(129 140 248 / var(--tw-border-opacity));
}

.border-y-indigo-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(238 242 255 / var(--tw-border-opacity));
  border-bottom-color: rgb(238 242 255 / var(--tw-border-opacity));
}

.border-y-indigo-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(99 102 241 / var(--tw-border-opacity));
  border-bottom-color: rgb(99 102 241 / var(--tw-border-opacity));
}

.border-y-indigo-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(79 70 229 / var(--tw-border-opacity));
  border-bottom-color: rgb(79 70 229 / var(--tw-border-opacity));
}

.border-y-indigo-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(67 56 202 / var(--tw-border-opacity));
  border-bottom-color: rgb(67 56 202 / var(--tw-border-opacity));
}

.border-y-indigo-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(55 48 163 / var(--tw-border-opacity));
  border-bottom-color: rgb(55 48 163 / var(--tw-border-opacity));
}

.border-y-indigo-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(49 46 129 / var(--tw-border-opacity));
  border-bottom-color: rgb(49 46 129 / var(--tw-border-opacity));
}

.border-y-indigo-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(30 27 75 / var(--tw-border-opacity));
  border-bottom-color: rgb(30 27 75 / var(--tw-border-opacity));
}

.border-y-inherit {
  border-top-color: inherit;
  border-bottom-color: inherit;
}

.border-y-lime-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(236 252 203 / var(--tw-border-opacity));
  border-bottom-color: rgb(236 252 203 / var(--tw-border-opacity));
}

.border-y-lime-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(217 249 157 / var(--tw-border-opacity));
  border-bottom-color: rgb(217 249 157 / var(--tw-border-opacity));
}

.border-y-lime-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(190 242 100 / var(--tw-border-opacity));
  border-bottom-color: rgb(190 242 100 / var(--tw-border-opacity));
}

.border-y-lime-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(163 230 53 / var(--tw-border-opacity));
  border-bottom-color: rgb(163 230 53 / var(--tw-border-opacity));
}

.border-y-lime-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(247 254 231 / var(--tw-border-opacity));
  border-bottom-color: rgb(247 254 231 / var(--tw-border-opacity));
}

.border-y-lime-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(132 204 22 / var(--tw-border-opacity));
  border-bottom-color: rgb(132 204 22 / var(--tw-border-opacity));
}

.border-y-lime-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(101 163 13 / var(--tw-border-opacity));
  border-bottom-color: rgb(101 163 13 / var(--tw-border-opacity));
}

.border-y-lime-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(77 124 15 / var(--tw-border-opacity));
  border-bottom-color: rgb(77 124 15 / var(--tw-border-opacity));
}

.border-y-lime-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(63 98 18 / var(--tw-border-opacity));
  border-bottom-color: rgb(63 98 18 / var(--tw-border-opacity));
}

.border-y-lime-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(54 83 20 / var(--tw-border-opacity));
  border-bottom-color: rgb(54 83 20 / var(--tw-border-opacity));
}

.border-y-lime-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(26 46 5 / var(--tw-border-opacity));
  border-bottom-color: rgb(26 46 5 / var(--tw-border-opacity));
}

.border-y-neutral-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(245 245 245 / var(--tw-border-opacity));
  border-bottom-color: rgb(245 245 245 / var(--tw-border-opacity));
}

.border-y-neutral-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(229 229 229 / var(--tw-border-opacity));
  border-bottom-color: rgb(229 229 229 / var(--tw-border-opacity));
}

.border-y-neutral-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(212 212 212 / var(--tw-border-opacity));
  border-bottom-color: rgb(212 212 212 / var(--tw-border-opacity));
}

.border-y-neutral-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(163 163 163 / var(--tw-border-opacity));
  border-bottom-color: rgb(163 163 163 / var(--tw-border-opacity));
}

.border-y-neutral-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(250 250 250 / var(--tw-border-opacity));
  border-bottom-color: rgb(250 250 250 / var(--tw-border-opacity));
}

.border-y-neutral-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(115 115 115 / var(--tw-border-opacity));
  border-bottom-color: rgb(115 115 115 / var(--tw-border-opacity));
}

.border-y-neutral-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(82 82 82 / var(--tw-border-opacity));
  border-bottom-color: rgb(82 82 82 / var(--tw-border-opacity));
}

.border-y-neutral-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(64 64 64 / var(--tw-border-opacity));
  border-bottom-color: rgb(64 64 64 / var(--tw-border-opacity));
}

.border-y-neutral-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(38 38 38 / var(--tw-border-opacity));
  border-bottom-color: rgb(38 38 38 / var(--tw-border-opacity));
}

.border-y-neutral-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(23 23 23 / var(--tw-border-opacity));
  border-bottom-color: rgb(23 23 23 / var(--tw-border-opacity));
}

.border-y-neutral-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(10 10 10 / var(--tw-border-opacity));
  border-bottom-color: rgb(10 10 10 / var(--tw-border-opacity));
}

.border-y-orange-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(255 237 213 / var(--tw-border-opacity));
  border-bottom-color: rgb(255 237 213 / var(--tw-border-opacity));
}

.border-y-orange-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(254 215 170 / var(--tw-border-opacity));
  border-bottom-color: rgb(254 215 170 / var(--tw-border-opacity));
}

.border-y-orange-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(253 186 116 / var(--tw-border-opacity));
  border-bottom-color: rgb(253 186 116 / var(--tw-border-opacity));
}

.border-y-orange-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(251 146 60 / var(--tw-border-opacity));
  border-bottom-color: rgb(251 146 60 / var(--tw-border-opacity));
}

.border-y-orange-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(255 247 237 / var(--tw-border-opacity));
  border-bottom-color: rgb(255 247 237 / var(--tw-border-opacity));
}

.border-y-orange-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(249 115 22 / var(--tw-border-opacity));
  border-bottom-color: rgb(249 115 22 / var(--tw-border-opacity));
}

.border-y-orange-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(234 88 12 / var(--tw-border-opacity));
  border-bottom-color: rgb(234 88 12 / var(--tw-border-opacity));
}

.border-y-orange-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(194 65 12 / var(--tw-border-opacity));
  border-bottom-color: rgb(194 65 12 / var(--tw-border-opacity));
}

.border-y-orange-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(154 52 18 / var(--tw-border-opacity));
  border-bottom-color: rgb(154 52 18 / var(--tw-border-opacity));
}

.border-y-orange-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(124 45 18 / var(--tw-border-opacity));
  border-bottom-color: rgb(124 45 18 / var(--tw-border-opacity));
}

.border-y-orange-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(67 20 7 / var(--tw-border-opacity));
  border-bottom-color: rgb(67 20 7 / var(--tw-border-opacity));
}

.border-y-pink-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(252 231 243 / var(--tw-border-opacity));
  border-bottom-color: rgb(252 231 243 / var(--tw-border-opacity));
}

.border-y-pink-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(251 207 232 / var(--tw-border-opacity));
  border-bottom-color: rgb(251 207 232 / var(--tw-border-opacity));
}

.border-y-pink-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(249 168 212 / var(--tw-border-opacity));
  border-bottom-color: rgb(249 168 212 / var(--tw-border-opacity));
}

.border-y-pink-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(244 114 182 / var(--tw-border-opacity));
  border-bottom-color: rgb(244 114 182 / var(--tw-border-opacity));
}

.border-y-pink-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(253 242 248 / var(--tw-border-opacity));
  border-bottom-color: rgb(253 242 248 / var(--tw-border-opacity));
}

.border-y-pink-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(236 72 153 / var(--tw-border-opacity));
  border-bottom-color: rgb(236 72 153 / var(--tw-border-opacity));
}

.border-y-pink-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(219 39 119 / var(--tw-border-opacity));
  border-bottom-color: rgb(219 39 119 / var(--tw-border-opacity));
}

.border-y-pink-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(190 24 93 / var(--tw-border-opacity));
  border-bottom-color: rgb(190 24 93 / var(--tw-border-opacity));
}

.border-y-pink-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(157 23 77 / var(--tw-border-opacity));
  border-bottom-color: rgb(157 23 77 / var(--tw-border-opacity));
}

.border-y-pink-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(131 24 67 / var(--tw-border-opacity));
  border-bottom-color: rgb(131 24 67 / var(--tw-border-opacity));
}

.border-y-pink-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(80 7 36 / var(--tw-border-opacity));
  border-bottom-color: rgb(80 7 36 / var(--tw-border-opacity));
}

.border-y-purple-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(243 232 255 / var(--tw-border-opacity));
  border-bottom-color: rgb(243 232 255 / var(--tw-border-opacity));
}

.border-y-purple-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(233 213 255 / var(--tw-border-opacity));
  border-bottom-color: rgb(233 213 255 / var(--tw-border-opacity));
}

.border-y-purple-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(216 180 254 / var(--tw-border-opacity));
  border-bottom-color: rgb(216 180 254 / var(--tw-border-opacity));
}

.border-y-purple-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(192 132 252 / var(--tw-border-opacity));
  border-bottom-color: rgb(192 132 252 / var(--tw-border-opacity));
}

.border-y-purple-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(250 245 255 / var(--tw-border-opacity));
  border-bottom-color: rgb(250 245 255 / var(--tw-border-opacity));
}

.border-y-purple-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(168 85 247 / var(--tw-border-opacity));
  border-bottom-color: rgb(168 85 247 / var(--tw-border-opacity));
}

.border-y-purple-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(147 51 234 / var(--tw-border-opacity));
  border-bottom-color: rgb(147 51 234 / var(--tw-border-opacity));
}

.border-y-purple-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(126 34 206 / var(--tw-border-opacity));
  border-bottom-color: rgb(126 34 206 / var(--tw-border-opacity));
}

.border-y-purple-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(107 33 168 / var(--tw-border-opacity));
  border-bottom-color: rgb(107 33 168 / var(--tw-border-opacity));
}

.border-y-purple-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(88 28 135 / var(--tw-border-opacity));
  border-bottom-color: rgb(88 28 135 / var(--tw-border-opacity));
}

.border-y-purple-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(59 7 100 / var(--tw-border-opacity));
  border-bottom-color: rgb(59 7 100 / var(--tw-border-opacity));
}

.border-y-red-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(254 226 226 / var(--tw-border-opacity));
  border-bottom-color: rgb(254 226 226 / var(--tw-border-opacity));
}

.border-y-red-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(254 202 202 / var(--tw-border-opacity));
  border-bottom-color: rgb(254 202 202 / var(--tw-border-opacity));
}

.border-y-red-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(252 165 165 / var(--tw-border-opacity));
  border-bottom-color: rgb(252 165 165 / var(--tw-border-opacity));
}

.border-y-red-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(248 113 113 / var(--tw-border-opacity));
  border-bottom-color: rgb(248 113 113 / var(--tw-border-opacity));
}

.border-y-red-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(254 242 242 / var(--tw-border-opacity));
  border-bottom-color: rgb(254 242 242 / var(--tw-border-opacity));
}

.border-y-red-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(239 68 68 / var(--tw-border-opacity));
  border-bottom-color: rgb(239 68 68 / var(--tw-border-opacity));
}

.border-y-red-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(220 38 38 / var(--tw-border-opacity));
  border-bottom-color: rgb(220 38 38 / var(--tw-border-opacity));
}

.border-y-red-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(185 28 28 / var(--tw-border-opacity));
  border-bottom-color: rgb(185 28 28 / var(--tw-border-opacity));
}

.border-y-red-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(153 27 27 / var(--tw-border-opacity));
  border-bottom-color: rgb(153 27 27 / var(--tw-border-opacity));
}

.border-y-red-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(127 29 29 / var(--tw-border-opacity));
  border-bottom-color: rgb(127 29 29 / var(--tw-border-opacity));
}

.border-y-red-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(69 10 10 / var(--tw-border-opacity));
  border-bottom-color: rgb(69 10 10 / var(--tw-border-opacity));
}

.border-y-rose-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(255 228 230 / var(--tw-border-opacity));
  border-bottom-color: rgb(255 228 230 / var(--tw-border-opacity));
}

.border-y-rose-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(254 205 211 / var(--tw-border-opacity));
  border-bottom-color: rgb(254 205 211 / var(--tw-border-opacity));
}

.border-y-rose-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(253 164 175 / var(--tw-border-opacity));
  border-bottom-color: rgb(253 164 175 / var(--tw-border-opacity));
}

.border-y-rose-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(251 113 133 / var(--tw-border-opacity));
  border-bottom-color: rgb(251 113 133 / var(--tw-border-opacity));
}

.border-y-rose-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(255 241 242 / var(--tw-border-opacity));
  border-bottom-color: rgb(255 241 242 / var(--tw-border-opacity));
}

.border-y-rose-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(244 63 94 / var(--tw-border-opacity));
  border-bottom-color: rgb(244 63 94 / var(--tw-border-opacity));
}

.border-y-rose-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(225 29 72 / var(--tw-border-opacity));
  border-bottom-color: rgb(225 29 72 / var(--tw-border-opacity));
}

.border-y-rose-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(190 18 60 / var(--tw-border-opacity));
  border-bottom-color: rgb(190 18 60 / var(--tw-border-opacity));
}

.border-y-rose-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(159 18 57 / var(--tw-border-opacity));
  border-bottom-color: rgb(159 18 57 / var(--tw-border-opacity));
}

.border-y-rose-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(136 19 55 / var(--tw-border-opacity));
  border-bottom-color: rgb(136 19 55 / var(--tw-border-opacity));
}

.border-y-rose-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(76 5 25 / var(--tw-border-opacity));
  border-bottom-color: rgb(76 5 25 / var(--tw-border-opacity));
}

.border-y-sky-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(224 242 254 / var(--tw-border-opacity));
  border-bottom-color: rgb(224 242 254 / var(--tw-border-opacity));
}

.border-y-sky-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(186 230 253 / var(--tw-border-opacity));
  border-bottom-color: rgb(186 230 253 / var(--tw-border-opacity));
}

.border-y-sky-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(125 211 252 / var(--tw-border-opacity));
  border-bottom-color: rgb(125 211 252 / var(--tw-border-opacity));
}

.border-y-sky-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(56 189 248 / var(--tw-border-opacity));
  border-bottom-color: rgb(56 189 248 / var(--tw-border-opacity));
}

.border-y-sky-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(240 249 255 / var(--tw-border-opacity));
  border-bottom-color: rgb(240 249 255 / var(--tw-border-opacity));
}

.border-y-sky-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(14 165 233 / var(--tw-border-opacity));
  border-bottom-color: rgb(14 165 233 / var(--tw-border-opacity));
}

.border-y-sky-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(2 132 199 / var(--tw-border-opacity));
  border-bottom-color: rgb(2 132 199 / var(--tw-border-opacity));
}

.border-y-sky-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(3 105 161 / var(--tw-border-opacity));
  border-bottom-color: rgb(3 105 161 / var(--tw-border-opacity));
}

.border-y-sky-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(7 89 133 / var(--tw-border-opacity));
  border-bottom-color: rgb(7 89 133 / var(--tw-border-opacity));
}

.border-y-sky-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(12 74 110 / var(--tw-border-opacity));
  border-bottom-color: rgb(12 74 110 / var(--tw-border-opacity));
}

.border-y-sky-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(8 47 73 / var(--tw-border-opacity));
  border-bottom-color: rgb(8 47 73 / var(--tw-border-opacity));
}

.border-y-slate-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(241 245 249 / var(--tw-border-opacity));
  border-bottom-color: rgb(241 245 249 / var(--tw-border-opacity));
}

.border-y-slate-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(226 232 240 / var(--tw-border-opacity));
  border-bottom-color: rgb(226 232 240 / var(--tw-border-opacity));
}

.border-y-slate-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(203 213 225 / var(--tw-border-opacity));
  border-bottom-color: rgb(203 213 225 / var(--tw-border-opacity));
}

.border-y-slate-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(148 163 184 / var(--tw-border-opacity));
  border-bottom-color: rgb(148 163 184 / var(--tw-border-opacity));
}

.border-y-slate-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(248 250 252 / var(--tw-border-opacity));
  border-bottom-color: rgb(248 250 252 / var(--tw-border-opacity));
}

.border-y-slate-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(100 116 139 / var(--tw-border-opacity));
  border-bottom-color: rgb(100 116 139 / var(--tw-border-opacity));
}

.border-y-slate-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(71 85 105 / var(--tw-border-opacity));
  border-bottom-color: rgb(71 85 105 / var(--tw-border-opacity));
}

.border-y-slate-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(51 65 85 / var(--tw-border-opacity));
  border-bottom-color: rgb(51 65 85 / var(--tw-border-opacity));
}

.border-y-slate-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(30 41 59 / var(--tw-border-opacity));
  border-bottom-color: rgb(30 41 59 / var(--tw-border-opacity));
}

.border-y-slate-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(15 23 42 / var(--tw-border-opacity));
  border-bottom-color: rgb(15 23 42 / var(--tw-border-opacity));
}

.border-y-slate-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(2 6 23 / var(--tw-border-opacity));
  border-bottom-color: rgb(2 6 23 / var(--tw-border-opacity));
}

.border-y-stone-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(245 245 244 / var(--tw-border-opacity));
  border-bottom-color: rgb(245 245 244 / var(--tw-border-opacity));
}

.border-y-stone-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(231 229 228 / var(--tw-border-opacity));
  border-bottom-color: rgb(231 229 228 / var(--tw-border-opacity));
}

.border-y-stone-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(214 211 209 / var(--tw-border-opacity));
  border-bottom-color: rgb(214 211 209 / var(--tw-border-opacity));
}

.border-y-stone-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(168 162 158 / var(--tw-border-opacity));
  border-bottom-color: rgb(168 162 158 / var(--tw-border-opacity));
}

.border-y-stone-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(250 250 249 / var(--tw-border-opacity));
  border-bottom-color: rgb(250 250 249 / var(--tw-border-opacity));
}

.border-y-stone-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(120 113 108 / var(--tw-border-opacity));
  border-bottom-color: rgb(120 113 108 / var(--tw-border-opacity));
}

.border-y-stone-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(87 83 78 / var(--tw-border-opacity));
  border-bottom-color: rgb(87 83 78 / var(--tw-border-opacity));
}

.border-y-stone-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(68 64 60 / var(--tw-border-opacity));
  border-bottom-color: rgb(68 64 60 / var(--tw-border-opacity));
}

.border-y-stone-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(41 37 36 / var(--tw-border-opacity));
  border-bottom-color: rgb(41 37 36 / var(--tw-border-opacity));
}

.border-y-stone-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(28 25 23 / var(--tw-border-opacity));
  border-bottom-color: rgb(28 25 23 / var(--tw-border-opacity));
}

.border-y-stone-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(12 10 9 / var(--tw-border-opacity));
  border-bottom-color: rgb(12 10 9 / var(--tw-border-opacity));
}

.border-y-teal-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(204 251 241 / var(--tw-border-opacity));
  border-bottom-color: rgb(204 251 241 / var(--tw-border-opacity));
}

.border-y-teal-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(153 246 228 / var(--tw-border-opacity));
  border-bottom-color: rgb(153 246 228 / var(--tw-border-opacity));
}

.border-y-teal-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(94 234 212 / var(--tw-border-opacity));
  border-bottom-color: rgb(94 234 212 / var(--tw-border-opacity));
}

.border-y-teal-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(45 212 191 / var(--tw-border-opacity));
  border-bottom-color: rgb(45 212 191 / var(--tw-border-opacity));
}

.border-y-teal-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(240 253 250 / var(--tw-border-opacity));
  border-bottom-color: rgb(240 253 250 / var(--tw-border-opacity));
}

.border-y-teal-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(20 184 166 / var(--tw-border-opacity));
  border-bottom-color: rgb(20 184 166 / var(--tw-border-opacity));
}

.border-y-teal-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(13 148 136 / var(--tw-border-opacity));
  border-bottom-color: rgb(13 148 136 / var(--tw-border-opacity));
}

.border-y-teal-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(15 118 110 / var(--tw-border-opacity));
  border-bottom-color: rgb(15 118 110 / var(--tw-border-opacity));
}

.border-y-teal-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(17 94 89 / var(--tw-border-opacity));
  border-bottom-color: rgb(17 94 89 / var(--tw-border-opacity));
}

.border-y-teal-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(19 78 74 / var(--tw-border-opacity));
  border-bottom-color: rgb(19 78 74 / var(--tw-border-opacity));
}

.border-y-teal-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(4 47 46 / var(--tw-border-opacity));
  border-bottom-color: rgb(4 47 46 / var(--tw-border-opacity));
}

.border-y-transparent {
  border-top-color: transparent;
  border-bottom-color: transparent;
}

.border-y-violet-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(237 233 254 / var(--tw-border-opacity));
  border-bottom-color: rgb(237 233 254 / var(--tw-border-opacity));
}

.border-y-violet-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(221 214 254 / var(--tw-border-opacity));
  border-bottom-color: rgb(221 214 254 / var(--tw-border-opacity));
}

.border-y-violet-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(196 181 253 / var(--tw-border-opacity));
  border-bottom-color: rgb(196 181 253 / var(--tw-border-opacity));
}

.border-y-violet-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(167 139 250 / var(--tw-border-opacity));
  border-bottom-color: rgb(167 139 250 / var(--tw-border-opacity));
}

.border-y-violet-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(245 243 255 / var(--tw-border-opacity));
  border-bottom-color: rgb(245 243 255 / var(--tw-border-opacity));
}

.border-y-violet-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(139 92 246 / var(--tw-border-opacity));
  border-bottom-color: rgb(139 92 246 / var(--tw-border-opacity));
}

.border-y-violet-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(124 58 237 / var(--tw-border-opacity));
  border-bottom-color: rgb(124 58 237 / var(--tw-border-opacity));
}

.border-y-violet-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(109 40 217 / var(--tw-border-opacity));
  border-bottom-color: rgb(109 40 217 / var(--tw-border-opacity));
}

.border-y-violet-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(91 33 182 / var(--tw-border-opacity));
  border-bottom-color: rgb(91 33 182 / var(--tw-border-opacity));
}

.border-y-violet-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(76 29 149 / var(--tw-border-opacity));
  border-bottom-color: rgb(76 29 149 / var(--tw-border-opacity));
}

.border-y-violet-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(46 16 101 / var(--tw-border-opacity));
  border-bottom-color: rgb(46 16 101 / var(--tw-border-opacity));
}

.border-y-white {
  --tw-border-opacity: 1;
  border-top-color: rgb(255 255 255 / var(--tw-border-opacity));
  border-bottom-color: rgb(255 255 255 / var(--tw-border-opacity));
}

.border-y-yellow-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(254 249 195 / var(--tw-border-opacity));
  border-bottom-color: rgb(254 249 195 / var(--tw-border-opacity));
}

.border-y-yellow-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(254 240 138 / var(--tw-border-opacity));
  border-bottom-color: rgb(254 240 138 / var(--tw-border-opacity));
}

.border-y-yellow-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(253 224 71 / var(--tw-border-opacity));
  border-bottom-color: rgb(253 224 71 / var(--tw-border-opacity));
}

.border-y-yellow-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(250 204 21 / var(--tw-border-opacity));
  border-bottom-color: rgb(250 204 21 / var(--tw-border-opacity));
}

.border-y-yellow-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(254 252 232 / var(--tw-border-opacity));
  border-bottom-color: rgb(254 252 232 / var(--tw-border-opacity));
}

.border-y-yellow-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(234 179 8 / var(--tw-border-opacity));
  border-bottom-color: rgb(234 179 8 / var(--tw-border-opacity));
}

.border-y-yellow-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(202 138 4 / var(--tw-border-opacity));
  border-bottom-color: rgb(202 138 4 / var(--tw-border-opacity));
}

.border-y-yellow-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(161 98 7 / var(--tw-border-opacity));
  border-bottom-color: rgb(161 98 7 / var(--tw-border-opacity));
}

.border-y-yellow-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(133 77 14 / var(--tw-border-opacity));
  border-bottom-color: rgb(133 77 14 / var(--tw-border-opacity));
}

.border-y-yellow-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(113 63 18 / var(--tw-border-opacity));
  border-bottom-color: rgb(113 63 18 / var(--tw-border-opacity));
}

.border-y-yellow-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(66 32 6 / var(--tw-border-opacity));
  border-bottom-color: rgb(66 32 6 / var(--tw-border-opacity));
}

.border-y-zinc-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(244 244 245 / var(--tw-border-opacity));
  border-bottom-color: rgb(244 244 245 / var(--tw-border-opacity));
}

.border-y-zinc-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(228 228 231 / var(--tw-border-opacity));
  border-bottom-color: rgb(228 228 231 / var(--tw-border-opacity));
}

.border-y-zinc-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(212 212 216 / var(--tw-border-opacity));
  border-bottom-color: rgb(212 212 216 / var(--tw-border-opacity));
}

.border-y-zinc-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(161 161 170 / var(--tw-border-opacity));
  border-bottom-color: rgb(161 161 170 / var(--tw-border-opacity));
}

.border-y-zinc-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(250 250 250 / var(--tw-border-opacity));
  border-bottom-color: rgb(250 250 250 / var(--tw-border-opacity));
}

.border-y-zinc-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(113 113 122 / var(--tw-border-opacity));
  border-bottom-color: rgb(113 113 122 / var(--tw-border-opacity));
}

.border-y-zinc-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(82 82 91 / var(--tw-border-opacity));
  border-bottom-color: rgb(82 82 91 / var(--tw-border-opacity));
}

.border-y-zinc-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(63 63 70 / var(--tw-border-opacity));
  border-bottom-color: rgb(63 63 70 / var(--tw-border-opacity));
}

.border-y-zinc-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(39 39 42 / var(--tw-border-opacity));
  border-bottom-color: rgb(39 39 42 / var(--tw-border-opacity));
}

.border-y-zinc-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(24 24 27 / var(--tw-border-opacity));
  border-bottom-color: rgb(24 24 27 / var(--tw-border-opacity));
}

.border-y-zinc-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(9 9 11 / var(--tw-border-opacity));
  border-bottom-color: rgb(9 9 11 / var(--tw-border-opacity));
}

.border-b-amber-100 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(254 243 199 / var(--tw-border-opacity));
}

.border-b-amber-200 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(253 230 138 / var(--tw-border-opacity));
}

.border-b-amber-300 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(252 211 77 / var(--tw-border-opacity));
}

.border-b-amber-400 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(251 191 36 / var(--tw-border-opacity));
}

.border-b-amber-50 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(255 251 235 / var(--tw-border-opacity));
}

.border-b-amber-500 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(245 158 11 / var(--tw-border-opacity));
}

.border-b-amber-600 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(217 119 6 / var(--tw-border-opacity));
}

.border-b-amber-700 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(180 83 9 / var(--tw-border-opacity));
}

.border-b-amber-800 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(146 64 14 / var(--tw-border-opacity));
}

.border-b-amber-900 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(120 53 15 / var(--tw-border-opacity));
}

.border-b-amber-950 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(69 26 3 / var(--tw-border-opacity));
}

.border-b-black {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(0 0 0 / var(--tw-border-opacity));
}

.border-b-blue-100 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(219 234 254 / var(--tw-border-opacity));
}

.border-b-blue-200 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(191 219 254 / var(--tw-border-opacity));
}

.border-b-blue-300 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(147 197 253 / var(--tw-border-opacity));
}

.border-b-blue-400 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(96 165 250 / var(--tw-border-opacity));
}

.border-b-blue-50 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(239 246 255 / var(--tw-border-opacity));
}

.border-b-blue-500 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(59 130 246 / var(--tw-border-opacity));
}

.border-b-blue-600 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(37 99 235 / var(--tw-border-opacity));
}

.border-b-blue-700 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(29 78 216 / var(--tw-border-opacity));
}

.border-b-blue-800 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(30 64 175 / var(--tw-border-opacity));
}

.border-b-blue-900 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(30 58 138 / var(--tw-border-opacity));
}

.border-b-blue-950 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(23 37 84 / var(--tw-border-opacity));
}

.border-b-current {
  border-bottom-color: currentColor;
}

.border-b-cyan-100 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(207 250 254 / var(--tw-border-opacity));
}

.border-b-cyan-200 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(165 243 252 / var(--tw-border-opacity));
}

.border-b-cyan-300 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(103 232 249 / var(--tw-border-opacity));
}

.border-b-cyan-400 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(34 211 238 / var(--tw-border-opacity));
}

.border-b-cyan-50 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(236 254 255 / var(--tw-border-opacity));
}

.border-b-cyan-500 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(6 182 212 / var(--tw-border-opacity));
}

.border-b-cyan-600 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(8 145 178 / var(--tw-border-opacity));
}

.border-b-cyan-700 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(14 116 144 / var(--tw-border-opacity));
}

.border-b-cyan-800 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(21 94 117 / var(--tw-border-opacity));
}

.border-b-cyan-900 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(22 78 99 / var(--tw-border-opacity));
}

.border-b-cyan-950 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(8 51 68 / var(--tw-border-opacity));
}

.border-b-emerald-100 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(209 250 229 / var(--tw-border-opacity));
}

.border-b-emerald-200 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(167 243 208 / var(--tw-border-opacity));
}

.border-b-emerald-300 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(110 231 183 / var(--tw-border-opacity));
}

.border-b-emerald-400 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(52 211 153 / var(--tw-border-opacity));
}

.border-b-emerald-50 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(236 253 245 / var(--tw-border-opacity));
}

.border-b-emerald-500 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(16 185 129 / var(--tw-border-opacity));
}

.border-b-emerald-600 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(5 150 105 / var(--tw-border-opacity));
}

.border-b-emerald-700 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(4 120 87 / var(--tw-border-opacity));
}

.border-b-emerald-800 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(6 95 70 / var(--tw-border-opacity));
}

.border-b-emerald-900 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(6 78 59 / var(--tw-border-opacity));
}

.border-b-emerald-950 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(2 44 34 / var(--tw-border-opacity));
}

.border-b-fuchsia-100 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(250 232 255 / var(--tw-border-opacity));
}

.border-b-fuchsia-200 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(245 208 254 / var(--tw-border-opacity));
}

.border-b-fuchsia-300 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(240 171 252 / var(--tw-border-opacity));
}

.border-b-fuchsia-400 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(232 121 249 / var(--tw-border-opacity));
}

.border-b-fuchsia-50 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(253 244 255 / var(--tw-border-opacity));
}

.border-b-fuchsia-500 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(217 70 239 / var(--tw-border-opacity));
}

.border-b-fuchsia-600 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(192 38 211 / var(--tw-border-opacity));
}

.border-b-fuchsia-700 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(162 28 175 / var(--tw-border-opacity));
}

.border-b-fuchsia-800 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(134 25 143 / var(--tw-border-opacity));
}

.border-b-fuchsia-900 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(112 26 117 / var(--tw-border-opacity));
}

.border-b-fuchsia-950 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(74 4 78 / var(--tw-border-opacity));
}

.border-b-gray-100 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(243 244 246 / var(--tw-border-opacity));
}

.border-b-gray-200 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(229 231 235 / var(--tw-border-opacity));
}

.border-b-gray-300 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(209 213 219 / var(--tw-border-opacity));
}

.border-b-gray-400 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(156 163 175 / var(--tw-border-opacity));
}

.border-b-gray-50 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(249 250 251 / var(--tw-border-opacity));
}

.border-b-gray-500 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(107 114 128 / var(--tw-border-opacity));
}

.border-b-gray-600 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(75 85 99 / var(--tw-border-opacity));
}

.border-b-gray-700 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(55 65 81 / var(--tw-border-opacity));
}

.border-b-gray-800 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(31 41 55 / var(--tw-border-opacity));
}

.border-b-gray-900 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(17 24 39 / var(--tw-border-opacity));
}

.border-b-gray-950 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(3 7 18 / var(--tw-border-opacity));
}

.border-b-green-100 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(220 252 231 / var(--tw-border-opacity));
}

.border-b-green-200 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(187 247 208 / var(--tw-border-opacity));
}

.border-b-green-300 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(134 239 172 / var(--tw-border-opacity));
}

.border-b-green-400 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(74 222 128 / var(--tw-border-opacity));
}

.border-b-green-50 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(240 253 244 / var(--tw-border-opacity));
}

.border-b-green-500 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(34 197 94 / var(--tw-border-opacity));
}

.border-b-green-600 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(22 163 74 / var(--tw-border-opacity));
}

.border-b-green-700 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(21 128 61 / var(--tw-border-opacity));
}

.border-b-green-800 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(22 101 52 / var(--tw-border-opacity));
}

.border-b-green-900 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(20 83 45 / var(--tw-border-opacity));
}

.border-b-green-950 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(5 46 22 / var(--tw-border-opacity));
}

.border-b-indigo-100 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(224 231 255 / var(--tw-border-opacity));
}

.border-b-indigo-200 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(199 210 254 / var(--tw-border-opacity));
}

.border-b-indigo-300 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(165 180 252 / var(--tw-border-opacity));
}

.border-b-indigo-400 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(129 140 248 / var(--tw-border-opacity));
}

.border-b-indigo-50 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(238 242 255 / var(--tw-border-opacity));
}

.border-b-indigo-500 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(99 102 241 / var(--tw-border-opacity));
}

.border-b-indigo-600 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(79 70 229 / var(--tw-border-opacity));
}

.border-b-indigo-700 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(67 56 202 / var(--tw-border-opacity));
}

.border-b-indigo-800 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(55 48 163 / var(--tw-border-opacity));
}

.border-b-indigo-900 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(49 46 129 / var(--tw-border-opacity));
}

.border-b-indigo-950 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(30 27 75 / var(--tw-border-opacity));
}

.border-b-inherit {
  border-bottom-color: inherit;
}

.border-b-lime-100 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(236 252 203 / var(--tw-border-opacity));
}

.border-b-lime-200 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(217 249 157 / var(--tw-border-opacity));
}

.border-b-lime-300 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(190 242 100 / var(--tw-border-opacity));
}

.border-b-lime-400 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(163 230 53 / var(--tw-border-opacity));
}

.border-b-lime-50 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(247 254 231 / var(--tw-border-opacity));
}

.border-b-lime-500 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(132 204 22 / var(--tw-border-opacity));
}

.border-b-lime-600 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(101 163 13 / var(--tw-border-opacity));
}

.border-b-lime-700 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(77 124 15 / var(--tw-border-opacity));
}

.border-b-lime-800 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(63 98 18 / var(--tw-border-opacity));
}

.border-b-lime-900 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(54 83 20 / var(--tw-border-opacity));
}

.border-b-lime-950 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(26 46 5 / var(--tw-border-opacity));
}

.border-b-neutral-100 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(245 245 245 / var(--tw-border-opacity));
}

.border-b-neutral-200 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(229 229 229 / var(--tw-border-opacity));
}

.border-b-neutral-300 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(212 212 212 / var(--tw-border-opacity));
}

.border-b-neutral-400 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(163 163 163 / var(--tw-border-opacity));
}

.border-b-neutral-50 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(250 250 250 / var(--tw-border-opacity));
}

.border-b-neutral-500 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(115 115 115 / var(--tw-border-opacity));
}

.border-b-neutral-600 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(82 82 82 / var(--tw-border-opacity));
}

.border-b-neutral-700 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(64 64 64 / var(--tw-border-opacity));
}

.border-b-neutral-800 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(38 38 38 / var(--tw-border-opacity));
}

.border-b-neutral-900 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(23 23 23 / var(--tw-border-opacity));
}

.border-b-neutral-950 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(10 10 10 / var(--tw-border-opacity));
}

.border-b-orange-100 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(255 237 213 / var(--tw-border-opacity));
}

.border-b-orange-200 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(254 215 170 / var(--tw-border-opacity));
}

.border-b-orange-300 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(253 186 116 / var(--tw-border-opacity));
}

.border-b-orange-400 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(251 146 60 / var(--tw-border-opacity));
}

.border-b-orange-50 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(255 247 237 / var(--tw-border-opacity));
}

.border-b-orange-500 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(249 115 22 / var(--tw-border-opacity));
}

.border-b-orange-600 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(234 88 12 / var(--tw-border-opacity));
}

.border-b-orange-700 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(194 65 12 / var(--tw-border-opacity));
}

.border-b-orange-800 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(154 52 18 / var(--tw-border-opacity));
}

.border-b-orange-900 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(124 45 18 / var(--tw-border-opacity));
}

.border-b-orange-950 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(67 20 7 / var(--tw-border-opacity));
}

.border-b-pink-100 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(252 231 243 / var(--tw-border-opacity));
}

.border-b-pink-200 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(251 207 232 / var(--tw-border-opacity));
}

.border-b-pink-300 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(249 168 212 / var(--tw-border-opacity));
}

.border-b-pink-400 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(244 114 182 / var(--tw-border-opacity));
}

.border-b-pink-50 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(253 242 248 / var(--tw-border-opacity));
}

.border-b-pink-500 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(236 72 153 / var(--tw-border-opacity));
}

.border-b-pink-600 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(219 39 119 / var(--tw-border-opacity));
}

.border-b-pink-700 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(190 24 93 / var(--tw-border-opacity));
}

.border-b-pink-800 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(157 23 77 / var(--tw-border-opacity));
}

.border-b-pink-900 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(131 24 67 / var(--tw-border-opacity));
}

.border-b-pink-950 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(80 7 36 / var(--tw-border-opacity));
}

.border-b-purple-100 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(243 232 255 / var(--tw-border-opacity));
}

.border-b-purple-200 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(233 213 255 / var(--tw-border-opacity));
}

.border-b-purple-300 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(216 180 254 / var(--tw-border-opacity));
}

.border-b-purple-400 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(192 132 252 / var(--tw-border-opacity));
}

.border-b-purple-50 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(250 245 255 / var(--tw-border-opacity));
}

.border-b-purple-500 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(168 85 247 / var(--tw-border-opacity));
}

.border-b-purple-600 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(147 51 234 / var(--tw-border-opacity));
}

.border-b-purple-700 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(126 34 206 / var(--tw-border-opacity));
}

.border-b-purple-800 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(107 33 168 / var(--tw-border-opacity));
}

.border-b-purple-900 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(88 28 135 / var(--tw-border-opacity));
}

.border-b-purple-950 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(59 7 100 / var(--tw-border-opacity));
}

.border-b-red-100 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(254 226 226 / var(--tw-border-opacity));
}

.border-b-red-200 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(254 202 202 / var(--tw-border-opacity));
}

.border-b-red-300 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(252 165 165 / var(--tw-border-opacity));
}

.border-b-red-400 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(248 113 113 / var(--tw-border-opacity));
}

.border-b-red-50 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(254 242 242 / var(--tw-border-opacity));
}

.border-b-red-500 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(239 68 68 / var(--tw-border-opacity));
}

.border-b-red-600 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(220 38 38 / var(--tw-border-opacity));
}

.border-b-red-700 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(185 28 28 / var(--tw-border-opacity));
}

.border-b-red-800 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(153 27 27 / var(--tw-border-opacity));
}

.border-b-red-900 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(127 29 29 / var(--tw-border-opacity));
}

.border-b-red-950 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(69 10 10 / var(--tw-border-opacity));
}

.border-b-rose-100 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(255 228 230 / var(--tw-border-opacity));
}

.border-b-rose-200 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(254 205 211 / var(--tw-border-opacity));
}

.border-b-rose-300 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(253 164 175 / var(--tw-border-opacity));
}

.border-b-rose-400 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(251 113 133 / var(--tw-border-opacity));
}

.border-b-rose-50 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(255 241 242 / var(--tw-border-opacity));
}

.border-b-rose-500 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(244 63 94 / var(--tw-border-opacity));
}

.border-b-rose-600 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(225 29 72 / var(--tw-border-opacity));
}

.border-b-rose-700 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(190 18 60 / var(--tw-border-opacity));
}

.border-b-rose-800 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(159 18 57 / var(--tw-border-opacity));
}

.border-b-rose-900 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(136 19 55 / var(--tw-border-opacity));
}

.border-b-rose-950 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(76 5 25 / var(--tw-border-opacity));
}

.border-b-sky-100 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(224 242 254 / var(--tw-border-opacity));
}

.border-b-sky-200 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(186 230 253 / var(--tw-border-opacity));
}

.border-b-sky-300 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(125 211 252 / var(--tw-border-opacity));
}

.border-b-sky-400 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(56 189 248 / var(--tw-border-opacity));
}

.border-b-sky-50 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(240 249 255 / var(--tw-border-opacity));
}

.border-b-sky-500 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(14 165 233 / var(--tw-border-opacity));
}

.border-b-sky-600 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(2 132 199 / var(--tw-border-opacity));
}

.border-b-sky-700 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(3 105 161 / var(--tw-border-opacity));
}

.border-b-sky-800 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(7 89 133 / var(--tw-border-opacity));
}

.border-b-sky-900 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(12 74 110 / var(--tw-border-opacity));
}

.border-b-sky-950 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(8 47 73 / var(--tw-border-opacity));
}

.border-b-slate-100 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(241 245 249 / var(--tw-border-opacity));
}

.border-b-slate-200 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(226 232 240 / var(--tw-border-opacity));
}

.border-b-slate-300 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(203 213 225 / var(--tw-border-opacity));
}

.border-b-slate-400 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(148 163 184 / var(--tw-border-opacity));
}

.border-b-slate-50 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(248 250 252 / var(--tw-border-opacity));
}

.border-b-slate-500 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(100 116 139 / var(--tw-border-opacity));
}

.border-b-slate-600 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(71 85 105 / var(--tw-border-opacity));
}

.border-b-slate-700 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(51 65 85 / var(--tw-border-opacity));
}

.border-b-slate-800 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(30 41 59 / var(--tw-border-opacity));
}

.border-b-slate-900 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(15 23 42 / var(--tw-border-opacity));
}

.border-b-slate-950 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(2 6 23 / var(--tw-border-opacity));
}

.border-b-stone-100 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(245 245 244 / var(--tw-border-opacity));
}

.border-b-stone-200 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(231 229 228 / var(--tw-border-opacity));
}

.border-b-stone-300 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(214 211 209 / var(--tw-border-opacity));
}

.border-b-stone-400 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(168 162 158 / var(--tw-border-opacity));
}

.border-b-stone-50 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(250 250 249 / var(--tw-border-opacity));
}

.border-b-stone-500 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(120 113 108 / var(--tw-border-opacity));
}

.border-b-stone-600 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(87 83 78 / var(--tw-border-opacity));
}

.border-b-stone-700 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(68 64 60 / var(--tw-border-opacity));
}

.border-b-stone-800 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(41 37 36 / var(--tw-border-opacity));
}

.border-b-stone-900 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(28 25 23 / var(--tw-border-opacity));
}

.border-b-stone-950 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(12 10 9 / var(--tw-border-opacity));
}

.border-b-teal-100 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(204 251 241 / var(--tw-border-opacity));
}

.border-b-teal-200 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(153 246 228 / var(--tw-border-opacity));
}

.border-b-teal-300 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(94 234 212 / var(--tw-border-opacity));
}

.border-b-teal-400 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(45 212 191 / var(--tw-border-opacity));
}

.border-b-teal-50 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(240 253 250 / var(--tw-border-opacity));
}

.border-b-teal-500 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(20 184 166 / var(--tw-border-opacity));
}

.border-b-teal-600 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(13 148 136 / var(--tw-border-opacity));
}

.border-b-teal-700 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(15 118 110 / var(--tw-border-opacity));
}

.border-b-teal-800 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(17 94 89 / var(--tw-border-opacity));
}

.border-b-teal-900 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(19 78 74 / var(--tw-border-opacity));
}

.border-b-teal-950 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(4 47 46 / var(--tw-border-opacity));
}

.border-b-transparent {
  border-bottom-color: transparent;
}

.border-b-violet-100 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(237 233 254 / var(--tw-border-opacity));
}

.border-b-violet-200 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(221 214 254 / var(--tw-border-opacity));
}

.border-b-violet-300 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(196 181 253 / var(--tw-border-opacity));
}

.border-b-violet-400 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(167 139 250 / var(--tw-border-opacity));
}

.border-b-violet-50 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(245 243 255 / var(--tw-border-opacity));
}

.border-b-violet-500 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(139 92 246 / var(--tw-border-opacity));
}

.border-b-violet-600 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(124 58 237 / var(--tw-border-opacity));
}

.border-b-violet-700 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(109 40 217 / var(--tw-border-opacity));
}

.border-b-violet-800 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(91 33 182 / var(--tw-border-opacity));
}

.border-b-violet-900 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(76 29 149 / var(--tw-border-opacity));
}

.border-b-violet-950 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(46 16 101 / var(--tw-border-opacity));
}

.border-b-white {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(255 255 255 / var(--tw-border-opacity));
}

.border-b-yellow-100 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(254 249 195 / var(--tw-border-opacity));
}

.border-b-yellow-200 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(254 240 138 / var(--tw-border-opacity));
}

.border-b-yellow-300 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(253 224 71 / var(--tw-border-opacity));
}

.border-b-yellow-400 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(250 204 21 / var(--tw-border-opacity));
}

.border-b-yellow-50 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(254 252 232 / var(--tw-border-opacity));
}

.border-b-yellow-500 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(234 179 8 / var(--tw-border-opacity));
}

.border-b-yellow-600 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(202 138 4 / var(--tw-border-opacity));
}

.border-b-yellow-700 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(161 98 7 / var(--tw-border-opacity));
}

.border-b-yellow-800 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(133 77 14 / var(--tw-border-opacity));
}

.border-b-yellow-900 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(113 63 18 / var(--tw-border-opacity));
}

.border-b-yellow-950 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(66 32 6 / var(--tw-border-opacity));
}

.border-b-zinc-100 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(244 244 245 / var(--tw-border-opacity));
}

.border-b-zinc-200 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(228 228 231 / var(--tw-border-opacity));
}

.border-b-zinc-300 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(212 212 216 / var(--tw-border-opacity));
}

.border-b-zinc-400 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(161 161 170 / var(--tw-border-opacity));
}

.border-b-zinc-50 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(250 250 250 / var(--tw-border-opacity));
}

.border-b-zinc-500 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(113 113 122 / var(--tw-border-opacity));
}

.border-b-zinc-600 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(82 82 91 / var(--tw-border-opacity));
}

.border-b-zinc-700 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(63 63 70 / var(--tw-border-opacity));
}

.border-b-zinc-800 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(39 39 42 / var(--tw-border-opacity));
}

.border-b-zinc-900 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(24 24 27 / var(--tw-border-opacity));
}

.border-b-zinc-950 {
  --tw-border-opacity: 1;
  border-bottom-color: rgb(9 9 11 / var(--tw-border-opacity));
}

.border-e-amber-100 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(254 243 199 / var(--tw-border-opacity));
}

.border-e-amber-200 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(253 230 138 / var(--tw-border-opacity));
}

.border-e-amber-300 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(252 211 77 / var(--tw-border-opacity));
}

.border-e-amber-400 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(251 191 36 / var(--tw-border-opacity));
}

.border-e-amber-50 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(255 251 235 / var(--tw-border-opacity));
}

.border-e-amber-500 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(245 158 11 / var(--tw-border-opacity));
}

.border-e-amber-600 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(217 119 6 / var(--tw-border-opacity));
}

.border-e-amber-700 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(180 83 9 / var(--tw-border-opacity));
}

.border-e-amber-800 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(146 64 14 / var(--tw-border-opacity));
}

.border-e-amber-900 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(120 53 15 / var(--tw-border-opacity));
}

.border-e-amber-950 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(69 26 3 / var(--tw-border-opacity));
}

.border-e-black {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(0 0 0 / var(--tw-border-opacity));
}

.border-e-blue-100 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(219 234 254 / var(--tw-border-opacity));
}

.border-e-blue-200 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(191 219 254 / var(--tw-border-opacity));
}

.border-e-blue-300 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(147 197 253 / var(--tw-border-opacity));
}

.border-e-blue-400 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(96 165 250 / var(--tw-border-opacity));
}

.border-e-blue-50 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(239 246 255 / var(--tw-border-opacity));
}

.border-e-blue-500 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(59 130 246 / var(--tw-border-opacity));
}

.border-e-blue-600 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(37 99 235 / var(--tw-border-opacity));
}

.border-e-blue-700 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(29 78 216 / var(--tw-border-opacity));
}

.border-e-blue-800 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(30 64 175 / var(--tw-border-opacity));
}

.border-e-blue-900 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(30 58 138 / var(--tw-border-opacity));
}

.border-e-blue-950 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(23 37 84 / var(--tw-border-opacity));
}

.border-e-current {
  border-inline-end-color: currentColor;
}

.border-e-cyan-100 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(207 250 254 / var(--tw-border-opacity));
}

.border-e-cyan-200 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(165 243 252 / var(--tw-border-opacity));
}

.border-e-cyan-300 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(103 232 249 / var(--tw-border-opacity));
}

.border-e-cyan-400 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(34 211 238 / var(--tw-border-opacity));
}

.border-e-cyan-50 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(236 254 255 / var(--tw-border-opacity));
}

.border-e-cyan-500 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(6 182 212 / var(--tw-border-opacity));
}

.border-e-cyan-600 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(8 145 178 / var(--tw-border-opacity));
}

.border-e-cyan-700 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(14 116 144 / var(--tw-border-opacity));
}

.border-e-cyan-800 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(21 94 117 / var(--tw-border-opacity));
}

.border-e-cyan-900 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(22 78 99 / var(--tw-border-opacity));
}

.border-e-cyan-950 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(8 51 68 / var(--tw-border-opacity));
}

.border-e-emerald-100 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(209 250 229 / var(--tw-border-opacity));
}

.border-e-emerald-200 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(167 243 208 / var(--tw-border-opacity));
}

.border-e-emerald-300 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(110 231 183 / var(--tw-border-opacity));
}

.border-e-emerald-400 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(52 211 153 / var(--tw-border-opacity));
}

.border-e-emerald-50 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(236 253 245 / var(--tw-border-opacity));
}

.border-e-emerald-500 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(16 185 129 / var(--tw-border-opacity));
}

.border-e-emerald-600 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(5 150 105 / var(--tw-border-opacity));
}

.border-e-emerald-700 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(4 120 87 / var(--tw-border-opacity));
}

.border-e-emerald-800 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(6 95 70 / var(--tw-border-opacity));
}

.border-e-emerald-900 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(6 78 59 / var(--tw-border-opacity));
}

.border-e-emerald-950 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(2 44 34 / var(--tw-border-opacity));
}

.border-e-fuchsia-100 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(250 232 255 / var(--tw-border-opacity));
}

.border-e-fuchsia-200 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(245 208 254 / var(--tw-border-opacity));
}

.border-e-fuchsia-300 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(240 171 252 / var(--tw-border-opacity));
}

.border-e-fuchsia-400 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(232 121 249 / var(--tw-border-opacity));
}

.border-e-fuchsia-50 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(253 244 255 / var(--tw-border-opacity));
}

.border-e-fuchsia-500 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(217 70 239 / var(--tw-border-opacity));
}

.border-e-fuchsia-600 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(192 38 211 / var(--tw-border-opacity));
}

.border-e-fuchsia-700 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(162 28 175 / var(--tw-border-opacity));
}

.border-e-fuchsia-800 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(134 25 143 / var(--tw-border-opacity));
}

.border-e-fuchsia-900 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(112 26 117 / var(--tw-border-opacity));
}

.border-e-fuchsia-950 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(74 4 78 / var(--tw-border-opacity));
}

.border-e-gray-100 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(243 244 246 / var(--tw-border-opacity));
}

.border-e-gray-200 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(229 231 235 / var(--tw-border-opacity));
}

.border-e-gray-300 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(209 213 219 / var(--tw-border-opacity));
}

.border-e-gray-400 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(156 163 175 / var(--tw-border-opacity));
}

.border-e-gray-50 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(249 250 251 / var(--tw-border-opacity));
}

.border-e-gray-500 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(107 114 128 / var(--tw-border-opacity));
}

.border-e-gray-600 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(75 85 99 / var(--tw-border-opacity));
}

.border-e-gray-700 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(55 65 81 / var(--tw-border-opacity));
}

.border-e-gray-800 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(31 41 55 / var(--tw-border-opacity));
}

.border-e-gray-900 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(17 24 39 / var(--tw-border-opacity));
}

.border-e-gray-950 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(3 7 18 / var(--tw-border-opacity));
}

.border-e-green-100 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(220 252 231 / var(--tw-border-opacity));
}

.border-e-green-200 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(187 247 208 / var(--tw-border-opacity));
}

.border-e-green-300 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(134 239 172 / var(--tw-border-opacity));
}

.border-e-green-400 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(74 222 128 / var(--tw-border-opacity));
}

.border-e-green-50 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(240 253 244 / var(--tw-border-opacity));
}

.border-e-green-500 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(34 197 94 / var(--tw-border-opacity));
}

.border-e-green-600 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(22 163 74 / var(--tw-border-opacity));
}

.border-e-green-700 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(21 128 61 / var(--tw-border-opacity));
}

.border-e-green-800 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(22 101 52 / var(--tw-border-opacity));
}

.border-e-green-900 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(20 83 45 / var(--tw-border-opacity));
}

.border-e-green-950 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(5 46 22 / var(--tw-border-opacity));
}

.border-e-indigo-100 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(224 231 255 / var(--tw-border-opacity));
}

.border-e-indigo-200 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(199 210 254 / var(--tw-border-opacity));
}

.border-e-indigo-300 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(165 180 252 / var(--tw-border-opacity));
}

.border-e-indigo-400 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(129 140 248 / var(--tw-border-opacity));
}

.border-e-indigo-50 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(238 242 255 / var(--tw-border-opacity));
}

.border-e-indigo-500 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(99 102 241 / var(--tw-border-opacity));
}

.border-e-indigo-600 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(79 70 229 / var(--tw-border-opacity));
}

.border-e-indigo-700 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(67 56 202 / var(--tw-border-opacity));
}

.border-e-indigo-800 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(55 48 163 / var(--tw-border-opacity));
}

.border-e-indigo-900 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(49 46 129 / var(--tw-border-opacity));
}

.border-e-indigo-950 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(30 27 75 / var(--tw-border-opacity));
}

.border-e-inherit {
  border-inline-end-color: inherit;
}

.border-e-lime-100 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(236 252 203 / var(--tw-border-opacity));
}

.border-e-lime-200 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(217 249 157 / var(--tw-border-opacity));
}

.border-e-lime-300 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(190 242 100 / var(--tw-border-opacity));
}

.border-e-lime-400 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(163 230 53 / var(--tw-border-opacity));
}

.border-e-lime-50 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(247 254 231 / var(--tw-border-opacity));
}

.border-e-lime-500 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(132 204 22 / var(--tw-border-opacity));
}

.border-e-lime-600 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(101 163 13 / var(--tw-border-opacity));
}

.border-e-lime-700 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(77 124 15 / var(--tw-border-opacity));
}

.border-e-lime-800 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(63 98 18 / var(--tw-border-opacity));
}

.border-e-lime-900 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(54 83 20 / var(--tw-border-opacity));
}

.border-e-lime-950 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(26 46 5 / var(--tw-border-opacity));
}

.border-e-neutral-100 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(245 245 245 / var(--tw-border-opacity));
}

.border-e-neutral-200 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(229 229 229 / var(--tw-border-opacity));
}

.border-e-neutral-300 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(212 212 212 / var(--tw-border-opacity));
}

.border-e-neutral-400 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(163 163 163 / var(--tw-border-opacity));
}

.border-e-neutral-50 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(250 250 250 / var(--tw-border-opacity));
}

.border-e-neutral-500 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(115 115 115 / var(--tw-border-opacity));
}

.border-e-neutral-600 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(82 82 82 / var(--tw-border-opacity));
}

.border-e-neutral-700 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(64 64 64 / var(--tw-border-opacity));
}

.border-e-neutral-800 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(38 38 38 / var(--tw-border-opacity));
}

.border-e-neutral-900 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(23 23 23 / var(--tw-border-opacity));
}

.border-e-neutral-950 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(10 10 10 / var(--tw-border-opacity));
}

.border-e-orange-100 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(255 237 213 / var(--tw-border-opacity));
}

.border-e-orange-200 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(254 215 170 / var(--tw-border-opacity));
}

.border-e-orange-300 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(253 186 116 / var(--tw-border-opacity));
}

.border-e-orange-400 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(251 146 60 / var(--tw-border-opacity));
}

.border-e-orange-50 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(255 247 237 / var(--tw-border-opacity));
}

.border-e-orange-500 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(249 115 22 / var(--tw-border-opacity));
}

.border-e-orange-600 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(234 88 12 / var(--tw-border-opacity));
}

.border-e-orange-700 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(194 65 12 / var(--tw-border-opacity));
}

.border-e-orange-800 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(154 52 18 / var(--tw-border-opacity));
}

.border-e-orange-900 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(124 45 18 / var(--tw-border-opacity));
}

.border-e-orange-950 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(67 20 7 / var(--tw-border-opacity));
}

.border-e-pink-100 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(252 231 243 / var(--tw-border-opacity));
}

.border-e-pink-200 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(251 207 232 / var(--tw-border-opacity));
}

.border-e-pink-300 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(249 168 212 / var(--tw-border-opacity));
}

.border-e-pink-400 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(244 114 182 / var(--tw-border-opacity));
}

.border-e-pink-50 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(253 242 248 / var(--tw-border-opacity));
}

.border-e-pink-500 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(236 72 153 / var(--tw-border-opacity));
}

.border-e-pink-600 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(219 39 119 / var(--tw-border-opacity));
}

.border-e-pink-700 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(190 24 93 / var(--tw-border-opacity));
}

.border-e-pink-800 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(157 23 77 / var(--tw-border-opacity));
}

.border-e-pink-900 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(131 24 67 / var(--tw-border-opacity));
}

.border-e-pink-950 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(80 7 36 / var(--tw-border-opacity));
}

.border-e-purple-100 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(243 232 255 / var(--tw-border-opacity));
}

.border-e-purple-200 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(233 213 255 / var(--tw-border-opacity));
}

.border-e-purple-300 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(216 180 254 / var(--tw-border-opacity));
}

.border-e-purple-400 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(192 132 252 / var(--tw-border-opacity));
}

.border-e-purple-50 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(250 245 255 / var(--tw-border-opacity));
}

.border-e-purple-500 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(168 85 247 / var(--tw-border-opacity));
}

.border-e-purple-600 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(147 51 234 / var(--tw-border-opacity));
}

.border-e-purple-700 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(126 34 206 / var(--tw-border-opacity));
}

.border-e-purple-800 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(107 33 168 / var(--tw-border-opacity));
}

.border-e-purple-900 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(88 28 135 / var(--tw-border-opacity));
}

.border-e-purple-950 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(59 7 100 / var(--tw-border-opacity));
}

.border-e-red-100 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(254 226 226 / var(--tw-border-opacity));
}

.border-e-red-200 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(254 202 202 / var(--tw-border-opacity));
}

.border-e-red-300 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(252 165 165 / var(--tw-border-opacity));
}

.border-e-red-400 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(248 113 113 / var(--tw-border-opacity));
}

.border-e-red-50 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(254 242 242 / var(--tw-border-opacity));
}

.border-e-red-500 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(239 68 68 / var(--tw-border-opacity));
}

.border-e-red-600 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(220 38 38 / var(--tw-border-opacity));
}

.border-e-red-700 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(185 28 28 / var(--tw-border-opacity));
}

.border-e-red-800 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(153 27 27 / var(--tw-border-opacity));
}

.border-e-red-900 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(127 29 29 / var(--tw-border-opacity));
}

.border-e-red-950 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(69 10 10 / var(--tw-border-opacity));
}

.border-e-rose-100 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(255 228 230 / var(--tw-border-opacity));
}

.border-e-rose-200 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(254 205 211 / var(--tw-border-opacity));
}

.border-e-rose-300 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(253 164 175 / var(--tw-border-opacity));
}

.border-e-rose-400 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(251 113 133 / var(--tw-border-opacity));
}

.border-e-rose-50 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(255 241 242 / var(--tw-border-opacity));
}

.border-e-rose-500 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(244 63 94 / var(--tw-border-opacity));
}

.border-e-rose-600 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(225 29 72 / var(--tw-border-opacity));
}

.border-e-rose-700 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(190 18 60 / var(--tw-border-opacity));
}

.border-e-rose-800 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(159 18 57 / var(--tw-border-opacity));
}

.border-e-rose-900 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(136 19 55 / var(--tw-border-opacity));
}

.border-e-rose-950 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(76 5 25 / var(--tw-border-opacity));
}

.border-e-sky-100 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(224 242 254 / var(--tw-border-opacity));
}

.border-e-sky-200 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(186 230 253 / var(--tw-border-opacity));
}

.border-e-sky-300 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(125 211 252 / var(--tw-border-opacity));
}

.border-e-sky-400 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(56 189 248 / var(--tw-border-opacity));
}

.border-e-sky-50 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(240 249 255 / var(--tw-border-opacity));
}

.border-e-sky-500 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(14 165 233 / var(--tw-border-opacity));
}

.border-e-sky-600 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(2 132 199 / var(--tw-border-opacity));
}

.border-e-sky-700 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(3 105 161 / var(--tw-border-opacity));
}

.border-e-sky-800 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(7 89 133 / var(--tw-border-opacity));
}

.border-e-sky-900 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(12 74 110 / var(--tw-border-opacity));
}

.border-e-sky-950 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(8 47 73 / var(--tw-border-opacity));
}

.border-e-slate-100 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(241 245 249 / var(--tw-border-opacity));
}

.border-e-slate-200 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(226 232 240 / var(--tw-border-opacity));
}

.border-e-slate-300 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(203 213 225 / var(--tw-border-opacity));
}

.border-e-slate-400 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(148 163 184 / var(--tw-border-opacity));
}

.border-e-slate-50 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(248 250 252 / var(--tw-border-opacity));
}

.border-e-slate-500 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(100 116 139 / var(--tw-border-opacity));
}

.border-e-slate-600 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(71 85 105 / var(--tw-border-opacity));
}

.border-e-slate-700 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(51 65 85 / var(--tw-border-opacity));
}

.border-e-slate-800 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(30 41 59 / var(--tw-border-opacity));
}

.border-e-slate-900 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(15 23 42 / var(--tw-border-opacity));
}

.border-e-slate-950 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(2 6 23 / var(--tw-border-opacity));
}

.border-e-stone-100 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(245 245 244 / var(--tw-border-opacity));
}

.border-e-stone-200 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(231 229 228 / var(--tw-border-opacity));
}

.border-e-stone-300 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(214 211 209 / var(--tw-border-opacity));
}

.border-e-stone-400 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(168 162 158 / var(--tw-border-opacity));
}

.border-e-stone-50 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(250 250 249 / var(--tw-border-opacity));
}

.border-e-stone-500 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(120 113 108 / var(--tw-border-opacity));
}

.border-e-stone-600 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(87 83 78 / var(--tw-border-opacity));
}

.border-e-stone-700 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(68 64 60 / var(--tw-border-opacity));
}

.border-e-stone-800 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(41 37 36 / var(--tw-border-opacity));
}

.border-e-stone-900 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(28 25 23 / var(--tw-border-opacity));
}

.border-e-stone-950 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(12 10 9 / var(--tw-border-opacity));
}

.border-e-teal-100 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(204 251 241 / var(--tw-border-opacity));
}

.border-e-teal-200 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(153 246 228 / var(--tw-border-opacity));
}

.border-e-teal-300 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(94 234 212 / var(--tw-border-opacity));
}

.border-e-teal-400 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(45 212 191 / var(--tw-border-opacity));
}

.border-e-teal-50 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(240 253 250 / var(--tw-border-opacity));
}

.border-e-teal-500 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(20 184 166 / var(--tw-border-opacity));
}

.border-e-teal-600 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(13 148 136 / var(--tw-border-opacity));
}

.border-e-teal-700 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(15 118 110 / var(--tw-border-opacity));
}

.border-e-teal-800 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(17 94 89 / var(--tw-border-opacity));
}

.border-e-teal-900 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(19 78 74 / var(--tw-border-opacity));
}

.border-e-teal-950 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(4 47 46 / var(--tw-border-opacity));
}

.border-e-transparent {
  border-inline-end-color: transparent;
}

.border-e-violet-100 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(237 233 254 / var(--tw-border-opacity));
}

.border-e-violet-200 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(221 214 254 / var(--tw-border-opacity));
}

.border-e-violet-300 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(196 181 253 / var(--tw-border-opacity));
}

.border-e-violet-400 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(167 139 250 / var(--tw-border-opacity));
}

.border-e-violet-50 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(245 243 255 / var(--tw-border-opacity));
}

.border-e-violet-500 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(139 92 246 / var(--tw-border-opacity));
}

.border-e-violet-600 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(124 58 237 / var(--tw-border-opacity));
}

.border-e-violet-700 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(109 40 217 / var(--tw-border-opacity));
}

.border-e-violet-800 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(91 33 182 / var(--tw-border-opacity));
}

.border-e-violet-900 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(76 29 149 / var(--tw-border-opacity));
}

.border-e-violet-950 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(46 16 101 / var(--tw-border-opacity));
}

.border-e-white {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(255 255 255 / var(--tw-border-opacity));
}

.border-e-yellow-100 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(254 249 195 / var(--tw-border-opacity));
}

.border-e-yellow-200 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(254 240 138 / var(--tw-border-opacity));
}

.border-e-yellow-300 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(253 224 71 / var(--tw-border-opacity));
}

.border-e-yellow-400 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(250 204 21 / var(--tw-border-opacity));
}

.border-e-yellow-50 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(254 252 232 / var(--tw-border-opacity));
}

.border-e-yellow-500 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(234 179 8 / var(--tw-border-opacity));
}

.border-e-yellow-600 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(202 138 4 / var(--tw-border-opacity));
}

.border-e-yellow-700 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(161 98 7 / var(--tw-border-opacity));
}

.border-e-yellow-800 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(133 77 14 / var(--tw-border-opacity));
}

.border-e-yellow-900 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(113 63 18 / var(--tw-border-opacity));
}

.border-e-yellow-950 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(66 32 6 / var(--tw-border-opacity));
}

.border-e-zinc-100 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(244 244 245 / var(--tw-border-opacity));
}

.border-e-zinc-200 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(228 228 231 / var(--tw-border-opacity));
}

.border-e-zinc-300 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(212 212 216 / var(--tw-border-opacity));
}

.border-e-zinc-400 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(161 161 170 / var(--tw-border-opacity));
}

.border-e-zinc-50 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(250 250 250 / var(--tw-border-opacity));
}

.border-e-zinc-500 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(113 113 122 / var(--tw-border-opacity));
}

.border-e-zinc-600 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(82 82 91 / var(--tw-border-opacity));
}

.border-e-zinc-700 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(63 63 70 / var(--tw-border-opacity));
}

.border-e-zinc-800 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(39 39 42 / var(--tw-border-opacity));
}

.border-e-zinc-900 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(24 24 27 / var(--tw-border-opacity));
}

.border-e-zinc-950 {
  --tw-border-opacity: 1;
  border-inline-end-color: rgb(9 9 11 / var(--tw-border-opacity));
}

.border-l-amber-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(254 243 199 / var(--tw-border-opacity));
}

.border-l-amber-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(253 230 138 / var(--tw-border-opacity));
}

.border-l-amber-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(252 211 77 / var(--tw-border-opacity));
}

.border-l-amber-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(251 191 36 / var(--tw-border-opacity));
}

.border-l-amber-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(255 251 235 / var(--tw-border-opacity));
}

.border-l-amber-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(245 158 11 / var(--tw-border-opacity));
}

.border-l-amber-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(217 119 6 / var(--tw-border-opacity));
}

.border-l-amber-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(180 83 9 / var(--tw-border-opacity));
}

.border-l-amber-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(146 64 14 / var(--tw-border-opacity));
}

.border-l-amber-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(120 53 15 / var(--tw-border-opacity));
}

.border-l-amber-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(69 26 3 / var(--tw-border-opacity));
}

.border-l-black {
  --tw-border-opacity: 1;
  border-left-color: rgb(0 0 0 / var(--tw-border-opacity));
}

.border-l-blue-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(219 234 254 / var(--tw-border-opacity));
}

.border-l-blue-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(191 219 254 / var(--tw-border-opacity));
}

.border-l-blue-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(147 197 253 / var(--tw-border-opacity));
}

.border-l-blue-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(96 165 250 / var(--tw-border-opacity));
}

.border-l-blue-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(239 246 255 / var(--tw-border-opacity));
}

.border-l-blue-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(59 130 246 / var(--tw-border-opacity));
}

.border-l-blue-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(37 99 235 / var(--tw-border-opacity));
}

.border-l-blue-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(29 78 216 / var(--tw-border-opacity));
}

.border-l-blue-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(30 64 175 / var(--tw-border-opacity));
}

.border-l-blue-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(30 58 138 / var(--tw-border-opacity));
}

.border-l-blue-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(23 37 84 / var(--tw-border-opacity));
}

.border-l-current {
  border-left-color: currentColor;
}

.border-l-cyan-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(207 250 254 / var(--tw-border-opacity));
}

.border-l-cyan-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(165 243 252 / var(--tw-border-opacity));
}

.border-l-cyan-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(103 232 249 / var(--tw-border-opacity));
}

.border-l-cyan-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(34 211 238 / var(--tw-border-opacity));
}

.border-l-cyan-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(236 254 255 / var(--tw-border-opacity));
}

.border-l-cyan-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(6 182 212 / var(--tw-border-opacity));
}

.border-l-cyan-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(8 145 178 / var(--tw-border-opacity));
}

.border-l-cyan-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(14 116 144 / var(--tw-border-opacity));
}

.border-l-cyan-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(21 94 117 / var(--tw-border-opacity));
}

.border-l-cyan-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(22 78 99 / var(--tw-border-opacity));
}

.border-l-cyan-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(8 51 68 / var(--tw-border-opacity));
}

.border-l-emerald-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(209 250 229 / var(--tw-border-opacity));
}

.border-l-emerald-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(167 243 208 / var(--tw-border-opacity));
}

.border-l-emerald-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(110 231 183 / var(--tw-border-opacity));
}

.border-l-emerald-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(52 211 153 / var(--tw-border-opacity));
}

.border-l-emerald-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(236 253 245 / var(--tw-border-opacity));
}

.border-l-emerald-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(16 185 129 / var(--tw-border-opacity));
}

.border-l-emerald-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(5 150 105 / var(--tw-border-opacity));
}

.border-l-emerald-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(4 120 87 / var(--tw-border-opacity));
}

.border-l-emerald-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(6 95 70 / var(--tw-border-opacity));
}

.border-l-emerald-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(6 78 59 / var(--tw-border-opacity));
}

.border-l-emerald-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(2 44 34 / var(--tw-border-opacity));
}

.border-l-fuchsia-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(250 232 255 / var(--tw-border-opacity));
}

.border-l-fuchsia-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(245 208 254 / var(--tw-border-opacity));
}

.border-l-fuchsia-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(240 171 252 / var(--tw-border-opacity));
}

.border-l-fuchsia-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(232 121 249 / var(--tw-border-opacity));
}

.border-l-fuchsia-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(253 244 255 / var(--tw-border-opacity));
}

.border-l-fuchsia-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(217 70 239 / var(--tw-border-opacity));
}

.border-l-fuchsia-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(192 38 211 / var(--tw-border-opacity));
}

.border-l-fuchsia-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(162 28 175 / var(--tw-border-opacity));
}

.border-l-fuchsia-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(134 25 143 / var(--tw-border-opacity));
}

.border-l-fuchsia-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(112 26 117 / var(--tw-border-opacity));
}

.border-l-fuchsia-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(74 4 78 / var(--tw-border-opacity));
}

.border-l-gray-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(243 244 246 / var(--tw-border-opacity));
}

.border-l-gray-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(229 231 235 / var(--tw-border-opacity));
}

.border-l-gray-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(209 213 219 / var(--tw-border-opacity));
}

.border-l-gray-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(156 163 175 / var(--tw-border-opacity));
}

.border-l-gray-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(249 250 251 / var(--tw-border-opacity));
}

.border-l-gray-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(107 114 128 / var(--tw-border-opacity));
}

.border-l-gray-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(75 85 99 / var(--tw-border-opacity));
}

.border-l-gray-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(55 65 81 / var(--tw-border-opacity));
}

.border-l-gray-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(31 41 55 / var(--tw-border-opacity));
}

.border-l-gray-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(17 24 39 / var(--tw-border-opacity));
}

.border-l-gray-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(3 7 18 / var(--tw-border-opacity));
}

.border-l-green-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(220 252 231 / var(--tw-border-opacity));
}

.border-l-green-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(187 247 208 / var(--tw-border-opacity));
}

.border-l-green-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(134 239 172 / var(--tw-border-opacity));
}

.border-l-green-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(74 222 128 / var(--tw-border-opacity));
}

.border-l-green-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(240 253 244 / var(--tw-border-opacity));
}

.border-l-green-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(34 197 94 / var(--tw-border-opacity));
}

.border-l-green-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(22 163 74 / var(--tw-border-opacity));
}

.border-l-green-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(21 128 61 / var(--tw-border-opacity));
}

.border-l-green-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(22 101 52 / var(--tw-border-opacity));
}

.border-l-green-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(20 83 45 / var(--tw-border-opacity));
}

.border-l-green-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(5 46 22 / var(--tw-border-opacity));
}

.border-l-indigo-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(224 231 255 / var(--tw-border-opacity));
}

.border-l-indigo-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(199 210 254 / var(--tw-border-opacity));
}

.border-l-indigo-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(165 180 252 / var(--tw-border-opacity));
}

.border-l-indigo-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(129 140 248 / var(--tw-border-opacity));
}

.border-l-indigo-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(238 242 255 / var(--tw-border-opacity));
}

.border-l-indigo-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(99 102 241 / var(--tw-border-opacity));
}

.border-l-indigo-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(79 70 229 / var(--tw-border-opacity));
}

.border-l-indigo-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(67 56 202 / var(--tw-border-opacity));
}

.border-l-indigo-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(55 48 163 / var(--tw-border-opacity));
}

.border-l-indigo-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(49 46 129 / var(--tw-border-opacity));
}

.border-l-indigo-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(30 27 75 / var(--tw-border-opacity));
}

.border-l-inherit {
  border-left-color: inherit;
}

.border-l-lime-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(236 252 203 / var(--tw-border-opacity));
}

.border-l-lime-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(217 249 157 / var(--tw-border-opacity));
}

.border-l-lime-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(190 242 100 / var(--tw-border-opacity));
}

.border-l-lime-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(163 230 53 / var(--tw-border-opacity));
}

.border-l-lime-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(247 254 231 / var(--tw-border-opacity));
}

.border-l-lime-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(132 204 22 / var(--tw-border-opacity));
}

.border-l-lime-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(101 163 13 / var(--tw-border-opacity));
}

.border-l-lime-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(77 124 15 / var(--tw-border-opacity));
}

.border-l-lime-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(63 98 18 / var(--tw-border-opacity));
}

.border-l-lime-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(54 83 20 / var(--tw-border-opacity));
}

.border-l-lime-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(26 46 5 / var(--tw-border-opacity));
}

.border-l-neutral-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(245 245 245 / var(--tw-border-opacity));
}

.border-l-neutral-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(229 229 229 / var(--tw-border-opacity));
}

.border-l-neutral-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(212 212 212 / var(--tw-border-opacity));
}

.border-l-neutral-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(163 163 163 / var(--tw-border-opacity));
}

.border-l-neutral-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(250 250 250 / var(--tw-border-opacity));
}

.border-l-neutral-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(115 115 115 / var(--tw-border-opacity));
}

.border-l-neutral-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(82 82 82 / var(--tw-border-opacity));
}

.border-l-neutral-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(64 64 64 / var(--tw-border-opacity));
}

.border-l-neutral-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(38 38 38 / var(--tw-border-opacity));
}

.border-l-neutral-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(23 23 23 / var(--tw-border-opacity));
}

.border-l-neutral-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(10 10 10 / var(--tw-border-opacity));
}

.border-l-orange-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(255 237 213 / var(--tw-border-opacity));
}

.border-l-orange-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(254 215 170 / var(--tw-border-opacity));
}

.border-l-orange-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(253 186 116 / var(--tw-border-opacity));
}

.border-l-orange-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(251 146 60 / var(--tw-border-opacity));
}

.border-l-orange-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(255 247 237 / var(--tw-border-opacity));
}

.border-l-orange-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(249 115 22 / var(--tw-border-opacity));
}

.border-l-orange-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(234 88 12 / var(--tw-border-opacity));
}

.border-l-orange-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(194 65 12 / var(--tw-border-opacity));
}

.border-l-orange-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(154 52 18 / var(--tw-border-opacity));
}

.border-l-orange-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(124 45 18 / var(--tw-border-opacity));
}

.border-l-orange-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(67 20 7 / var(--tw-border-opacity));
}

.border-l-pink-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(252 231 243 / var(--tw-border-opacity));
}

.border-l-pink-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(251 207 232 / var(--tw-border-opacity));
}

.border-l-pink-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(249 168 212 / var(--tw-border-opacity));
}

.border-l-pink-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(244 114 182 / var(--tw-border-opacity));
}

.border-l-pink-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(253 242 248 / var(--tw-border-opacity));
}

.border-l-pink-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(236 72 153 / var(--tw-border-opacity));
}

.border-l-pink-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(219 39 119 / var(--tw-border-opacity));
}

.border-l-pink-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(190 24 93 / var(--tw-border-opacity));
}

.border-l-pink-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(157 23 77 / var(--tw-border-opacity));
}

.border-l-pink-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(131 24 67 / var(--tw-border-opacity));
}

.border-l-pink-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(80 7 36 / var(--tw-border-opacity));
}

.border-l-purple-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(243 232 255 / var(--tw-border-opacity));
}

.border-l-purple-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(233 213 255 / var(--tw-border-opacity));
}

.border-l-purple-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(216 180 254 / var(--tw-border-opacity));
}

.border-l-purple-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(192 132 252 / var(--tw-border-opacity));
}

.border-l-purple-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(250 245 255 / var(--tw-border-opacity));
}

.border-l-purple-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(168 85 247 / var(--tw-border-opacity));
}

.border-l-purple-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(147 51 234 / var(--tw-border-opacity));
}

.border-l-purple-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(126 34 206 / var(--tw-border-opacity));
}

.border-l-purple-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(107 33 168 / var(--tw-border-opacity));
}

.border-l-purple-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(88 28 135 / var(--tw-border-opacity));
}

.border-l-purple-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(59 7 100 / var(--tw-border-opacity));
}

.border-l-red-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(254 226 226 / var(--tw-border-opacity));
}

.border-l-red-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(254 202 202 / var(--tw-border-opacity));
}

.border-l-red-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(252 165 165 / var(--tw-border-opacity));
}

.border-l-red-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(248 113 113 / var(--tw-border-opacity));
}

.border-l-red-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(254 242 242 / var(--tw-border-opacity));
}

.border-l-red-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(239 68 68 / var(--tw-border-opacity));
}

.border-l-red-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(220 38 38 / var(--tw-border-opacity));
}

.border-l-red-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(185 28 28 / var(--tw-border-opacity));
}

.border-l-red-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(153 27 27 / var(--tw-border-opacity));
}

.border-l-red-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(127 29 29 / var(--tw-border-opacity));
}

.border-l-red-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(69 10 10 / var(--tw-border-opacity));
}

.border-l-rose-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(255 228 230 / var(--tw-border-opacity));
}

.border-l-rose-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(254 205 211 / var(--tw-border-opacity));
}

.border-l-rose-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(253 164 175 / var(--tw-border-opacity));
}

.border-l-rose-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(251 113 133 / var(--tw-border-opacity));
}

.border-l-rose-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(255 241 242 / var(--tw-border-opacity));
}

.border-l-rose-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(244 63 94 / var(--tw-border-opacity));
}

.border-l-rose-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(225 29 72 / var(--tw-border-opacity));
}

.border-l-rose-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(190 18 60 / var(--tw-border-opacity));
}

.border-l-rose-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(159 18 57 / var(--tw-border-opacity));
}

.border-l-rose-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(136 19 55 / var(--tw-border-opacity));
}

.border-l-rose-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(76 5 25 / var(--tw-border-opacity));
}

.border-l-sky-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(224 242 254 / var(--tw-border-opacity));
}

.border-l-sky-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(186 230 253 / var(--tw-border-opacity));
}

.border-l-sky-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(125 211 252 / var(--tw-border-opacity));
}

.border-l-sky-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(56 189 248 / var(--tw-border-opacity));
}

.border-l-sky-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(240 249 255 / var(--tw-border-opacity));
}

.border-l-sky-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(14 165 233 / var(--tw-border-opacity));
}

.border-l-sky-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(2 132 199 / var(--tw-border-opacity));
}

.border-l-sky-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(3 105 161 / var(--tw-border-opacity));
}

.border-l-sky-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(7 89 133 / var(--tw-border-opacity));
}

.border-l-sky-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(12 74 110 / var(--tw-border-opacity));
}

.border-l-sky-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(8 47 73 / var(--tw-border-opacity));
}

.border-l-slate-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(241 245 249 / var(--tw-border-opacity));
}

.border-l-slate-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(226 232 240 / var(--tw-border-opacity));
}

.border-l-slate-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(203 213 225 / var(--tw-border-opacity));
}

.border-l-slate-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(148 163 184 / var(--tw-border-opacity));
}

.border-l-slate-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(248 250 252 / var(--tw-border-opacity));
}

.border-l-slate-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(100 116 139 / var(--tw-border-opacity));
}

.border-l-slate-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(71 85 105 / var(--tw-border-opacity));
}

.border-l-slate-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(51 65 85 / var(--tw-border-opacity));
}

.border-l-slate-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(30 41 59 / var(--tw-border-opacity));
}

.border-l-slate-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(15 23 42 / var(--tw-border-opacity));
}

.border-l-slate-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(2 6 23 / var(--tw-border-opacity));
}

.border-l-stone-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(245 245 244 / var(--tw-border-opacity));
}

.border-l-stone-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(231 229 228 / var(--tw-border-opacity));
}

.border-l-stone-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(214 211 209 / var(--tw-border-opacity));
}

.border-l-stone-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(168 162 158 / var(--tw-border-opacity));
}

.border-l-stone-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(250 250 249 / var(--tw-border-opacity));
}

.border-l-stone-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(120 113 108 / var(--tw-border-opacity));
}

.border-l-stone-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(87 83 78 / var(--tw-border-opacity));
}

.border-l-stone-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(68 64 60 / var(--tw-border-opacity));
}

.border-l-stone-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(41 37 36 / var(--tw-border-opacity));
}

.border-l-stone-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(28 25 23 / var(--tw-border-opacity));
}

.border-l-stone-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(12 10 9 / var(--tw-border-opacity));
}

.border-l-teal-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(204 251 241 / var(--tw-border-opacity));
}

.border-l-teal-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(153 246 228 / var(--tw-border-opacity));
}

.border-l-teal-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(94 234 212 / var(--tw-border-opacity));
}

.border-l-teal-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(45 212 191 / var(--tw-border-opacity));
}

.border-l-teal-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(240 253 250 / var(--tw-border-opacity));
}

.border-l-teal-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(20 184 166 / var(--tw-border-opacity));
}

.border-l-teal-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(13 148 136 / var(--tw-border-opacity));
}

.border-l-teal-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(15 118 110 / var(--tw-border-opacity));
}

.border-l-teal-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(17 94 89 / var(--tw-border-opacity));
}

.border-l-teal-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(19 78 74 / var(--tw-border-opacity));
}

.border-l-teal-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(4 47 46 / var(--tw-border-opacity));
}

.border-l-transparent {
  border-left-color: transparent;
}

.border-l-violet-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(237 233 254 / var(--tw-border-opacity));
}

.border-l-violet-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(221 214 254 / var(--tw-border-opacity));
}

.border-l-violet-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(196 181 253 / var(--tw-border-opacity));
}

.border-l-violet-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(167 139 250 / var(--tw-border-opacity));
}

.border-l-violet-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(245 243 255 / var(--tw-border-opacity));
}

.border-l-violet-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(139 92 246 / var(--tw-border-opacity));
}

.border-l-violet-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(124 58 237 / var(--tw-border-opacity));
}

.border-l-violet-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(109 40 217 / var(--tw-border-opacity));
}

.border-l-violet-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(91 33 182 / var(--tw-border-opacity));
}

.border-l-violet-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(76 29 149 / var(--tw-border-opacity));
}

.border-l-violet-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(46 16 101 / var(--tw-border-opacity));
}

.border-l-white {
  --tw-border-opacity: 1;
  border-left-color: rgb(255 255 255 / var(--tw-border-opacity));
}

.border-l-yellow-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(254 249 195 / var(--tw-border-opacity));
}

.border-l-yellow-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(254 240 138 / var(--tw-border-opacity));
}

.border-l-yellow-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(253 224 71 / var(--tw-border-opacity));
}

.border-l-yellow-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(250 204 21 / var(--tw-border-opacity));
}

.border-l-yellow-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(254 252 232 / var(--tw-border-opacity));
}

.border-l-yellow-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(234 179 8 / var(--tw-border-opacity));
}

.border-l-yellow-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(202 138 4 / var(--tw-border-opacity));
}

.border-l-yellow-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(161 98 7 / var(--tw-border-opacity));
}

.border-l-yellow-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(133 77 14 / var(--tw-border-opacity));
}

.border-l-yellow-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(113 63 18 / var(--tw-border-opacity));
}

.border-l-yellow-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(66 32 6 / var(--tw-border-opacity));
}

.border-l-zinc-100 {
  --tw-border-opacity: 1;
  border-left-color: rgb(244 244 245 / var(--tw-border-opacity));
}

.border-l-zinc-200 {
  --tw-border-opacity: 1;
  border-left-color: rgb(228 228 231 / var(--tw-border-opacity));
}

.border-l-zinc-300 {
  --tw-border-opacity: 1;
  border-left-color: rgb(212 212 216 / var(--tw-border-opacity));
}

.border-l-zinc-400 {
  --tw-border-opacity: 1;
  border-left-color: rgb(161 161 170 / var(--tw-border-opacity));
}

.border-l-zinc-50 {
  --tw-border-opacity: 1;
  border-left-color: rgb(250 250 250 / var(--tw-border-opacity));
}

.border-l-zinc-500 {
  --tw-border-opacity: 1;
  border-left-color: rgb(113 113 122 / var(--tw-border-opacity));
}

.border-l-zinc-600 {
  --tw-border-opacity: 1;
  border-left-color: rgb(82 82 91 / var(--tw-border-opacity));
}

.border-l-zinc-700 {
  --tw-border-opacity: 1;
  border-left-color: rgb(63 63 70 / var(--tw-border-opacity));
}

.border-l-zinc-800 {
  --tw-border-opacity: 1;
  border-left-color: rgb(39 39 42 / var(--tw-border-opacity));
}

.border-l-zinc-900 {
  --tw-border-opacity: 1;
  border-left-color: rgb(24 24 27 / var(--tw-border-opacity));
}

.border-l-zinc-950 {
  --tw-border-opacity: 1;
  border-left-color: rgb(9 9 11 / var(--tw-border-opacity));
}

.border-r-amber-100 {
  --tw-border-opacity: 1;
  border-right-color: rgb(254 243 199 / var(--tw-border-opacity));
}

.border-r-amber-200 {
  --tw-border-opacity: 1;
  border-right-color: rgb(253 230 138 / var(--tw-border-opacity));
}

.border-r-amber-300 {
  --tw-border-opacity: 1;
  border-right-color: rgb(252 211 77 / var(--tw-border-opacity));
}

.border-r-amber-400 {
  --tw-border-opacity: 1;
  border-right-color: rgb(251 191 36 / var(--tw-border-opacity));
}

.border-r-amber-50 {
  --tw-border-opacity: 1;
  border-right-color: rgb(255 251 235 / var(--tw-border-opacity));
}

.border-r-amber-500 {
  --tw-border-opacity: 1;
  border-right-color: rgb(245 158 11 / var(--tw-border-opacity));
}

.border-r-amber-600 {
  --tw-border-opacity: 1;
  border-right-color: rgb(217 119 6 / var(--tw-border-opacity));
}

.border-r-amber-700 {
  --tw-border-opacity: 1;
  border-right-color: rgb(180 83 9 / var(--tw-border-opacity));
}

.border-r-amber-800 {
  --tw-border-opacity: 1;
  border-right-color: rgb(146 64 14 / var(--tw-border-opacity));
}

.border-r-amber-900 {
  --tw-border-opacity: 1;
  border-right-color: rgb(120 53 15 / var(--tw-border-opacity));
}

.border-r-amber-950 {
  --tw-border-opacity: 1;
  border-right-color: rgb(69 26 3 / var(--tw-border-opacity));
}

.border-r-black {
  --tw-border-opacity: 1;
  border-right-color: rgb(0 0 0 / var(--tw-border-opacity));
}

.border-r-blue-100 {
  --tw-border-opacity: 1;
  border-right-color: rgb(219 234 254 / var(--tw-border-opacity));
}

.border-r-blue-200 {
  --tw-border-opacity: 1;
  border-right-color: rgb(191 219 254 / var(--tw-border-opacity));
}

.border-r-blue-300 {
  --tw-border-opacity: 1;
  border-right-color: rgb(147 197 253 / var(--tw-border-opacity));
}

.border-r-blue-400 {
  --tw-border-opacity: 1;
  border-right-color: rgb(96 165 250 / var(--tw-border-opacity));
}

.border-r-blue-50 {
  --tw-border-opacity: 1;
  border-right-color: rgb(239 246 255 / var(--tw-border-opacity));
}

.border-r-blue-500 {
  --tw-border-opacity: 1;
  border-right-color: rgb(59 130 246 / var(--tw-border-opacity));
}

.border-r-blue-600 {
  --tw-border-opacity: 1;
  border-right-color: rgb(37 99 235 / var(--tw-border-opacity));
}

.border-r-blue-700 {
  --tw-border-opacity: 1;
  border-right-color: rgb(29 78 216 / var(--tw-border-opacity));
}

.border-r-blue-800 {
  --tw-border-opacity: 1;
  border-right-color: rgb(30 64 175 / var(--tw-border-opacity));
}

.border-r-blue-900 {
  --tw-border-opacity: 1;
  border-right-color: rgb(30 58 138 / var(--tw-border-opacity));
}

.border-r-blue-950 {
  --tw-border-opacity: 1;
  border-right-color: rgb(23 37 84 / var(--tw-border-opacity));
}

.border-r-current {
  border-right-color: currentColor;
}

.border-r-cyan-100 {
  --tw-border-opacity: 1;
  border-right-color: rgb(207 250 254 / var(--tw-border-opacity));
}

.border-r-cyan-200 {
  --tw-border-opacity: 1;
  border-right-color: rgb(165 243 252 / var(--tw-border-opacity));
}

.border-r-cyan-300 {
  --tw-border-opacity: 1;
  border-right-color: rgb(103 232 249 / var(--tw-border-opacity));
}

.border-r-cyan-400 {
  --tw-border-opacity: 1;
  border-right-color: rgb(34 211 238 / var(--tw-border-opacity));
}

.border-r-cyan-50 {
  --tw-border-opacity: 1;
  border-right-color: rgb(236 254 255 / var(--tw-border-opacity));
}

.border-r-cyan-500 {
  --tw-border-opacity: 1;
  border-right-color: rgb(6 182 212 / var(--tw-border-opacity));
}

.border-r-cyan-600 {
  --tw-border-opacity: 1;
  border-right-color: rgb(8 145 178 / var(--tw-border-opacity));
}

.border-r-cyan-700 {
  --tw-border-opacity: 1;
  border-right-color: rgb(14 116 144 / var(--tw-border-opacity));
}

.border-r-cyan-800 {
  --tw-border-opacity: 1;
  border-right-color: rgb(21 94 117 / var(--tw-border-opacity));
}

.border-r-cyan-900 {
  --tw-border-opacity: 1;
  border-right-color: rgb(22 78 99 / var(--tw-border-opacity));
}

.border-r-cyan-950 {
  --tw-border-opacity: 1;
  border-right-color: rgb(8 51 68 / var(--tw-border-opacity));
}

.border-r-emerald-100 {
  --tw-border-opacity: 1;
  border-right-color: rgb(209 250 229 / var(--tw-border-opacity));
}

.border-r-emerald-200 {
  --tw-border-opacity: 1;
  border-right-color: rgb(167 243 208 / var(--tw-border-opacity));
}

.border-r-emerald-300 {
  --tw-border-opacity: 1;
  border-right-color: rgb(110 231 183 / var(--tw-border-opacity));
}

.border-r-emerald-400 {
  --tw-border-opacity: 1;
  border-right-color: rgb(52 211 153 / var(--tw-border-opacity));
}

.border-r-emerald-50 {
  --tw-border-opacity: 1;
  border-right-color: rgb(236 253 245 / var(--tw-border-opacity));
}

.border-r-emerald-500 {
  --tw-border-opacity: 1;
  border-right-color: rgb(16 185 129 / var(--tw-border-opacity));
}

.border-r-emerald-600 {
  --tw-border-opacity: 1;
  border-right-color: rgb(5 150 105 / var(--tw-border-opacity));
}

.border-r-emerald-700 {
  --tw-border-opacity: 1;
  border-right-color: rgb(4 120 87 / var(--tw-border-opacity));
}

.border-r-emerald-800 {
  --tw-border-opacity: 1;
  border-right-color: rgb(6 95 70 / var(--tw-border-opacity));
}

.border-r-emerald-900 {
  --tw-border-opacity: 1;
  border-right-color: rgb(6 78 59 / var(--tw-border-opacity));
}

.border-r-emerald-950 {
  --tw-border-opacity: 1;
  border-right-color: rgb(2 44 34 / var(--tw-border-opacity));
}

.border-r-fuchsia-100 {
  --tw-border-opacity: 1;
  border-right-color: rgb(250 232 255 / var(--tw-border-opacity));
}

.border-r-fuchsia-200 {
  --tw-border-opacity: 1;
  border-right-color: rgb(245 208 254 / var(--tw-border-opacity));
}

.border-r-fuchsia-300 {
  --tw-border-opacity: 1;
  border-right-color: rgb(240 171 252 / var(--tw-border-opacity));
}

.border-r-fuchsia-400 {
  --tw-border-opacity: 1;
  border-right-color: rgb(232 121 249 / var(--tw-border-opacity));
}

.border-r-fuchsia-50 {
  --tw-border-opacity: 1;
  border-right-color: rgb(253 244 255 / var(--tw-border-opacity));
}

.border-r-fuchsia-500 {
  --tw-border-opacity: 1;
  border-right-color: rgb(217 70 239 / var(--tw-border-opacity));
}

.border-r-fuchsia-600 {
  --tw-border-opacity: 1;
  border-right-color: rgb(192 38 211 / var(--tw-border-opacity));
}

.border-r-fuchsia-700 {
  --tw-border-opacity: 1;
  border-right-color: rgb(162 28 175 / var(--tw-border-opacity));
}

.border-r-fuchsia-800 {
  --tw-border-opacity: 1;
  border-right-color: rgb(134 25 143 / var(--tw-border-opacity));
}

.border-r-fuchsia-900 {
  --tw-border-opacity: 1;
  border-right-color: rgb(112 26 117 / var(--tw-border-opacity));
}

.border-r-fuchsia-950 {
  --tw-border-opacity: 1;
  border-right-color: rgb(74 4 78 / var(--tw-border-opacity));
}

.border-r-gray-100 {
  --tw-border-opacity: 1;
  border-right-color: rgb(243 244 246 / var(--tw-border-opacity));
}

.border-r-gray-200 {
  --tw-border-opacity: 1;
  border-right-color: rgb(229 231 235 / var(--tw-border-opacity));
}

.border-r-gray-300 {
  --tw-border-opacity: 1;
  border-right-color: rgb(209 213 219 / var(--tw-border-opacity));
}

.border-r-gray-400 {
  --tw-border-opacity: 1;
  border-right-color: rgb(156 163 175 / var(--tw-border-opacity));
}

.border-r-gray-50 {
  --tw-border-opacity: 1;
  border-right-color: rgb(249 250 251 / var(--tw-border-opacity));
}

.border-r-gray-500 {
  --tw-border-opacity: 1;
  border-right-color: rgb(107 114 128 / var(--tw-border-opacity));
}

.border-r-gray-600 {
  --tw-border-opacity: 1;
  border-right-color: rgb(75 85 99 / var(--tw-border-opacity));
}

.border-r-gray-700 {
  --tw-border-opacity: 1;
  border-right-color: rgb(55 65 81 / var(--tw-border-opacity));
}

.border-r-gray-800 {
  --tw-border-opacity: 1;
  border-right-color: rgb(31 41 55 / var(--tw-border-opacity));
}

.border-r-gray-900 {
  --tw-border-opacity: 1;
  border-right-color: rgb(17 24 39 / var(--tw-border-opacity));
}

.border-r-gray-950 {
  --tw-border-opacity: 1;
  border-right-color: rgb(3 7 18 / var(--tw-border-opacity));
}

.border-r-green-100 {
  --tw-border-opacity: 1;
  border-right-color: rgb(220 252 231 / var(--tw-border-opacity));
}

.border-r-green-200 {
  --tw-border-opacity: 1;
  border-right-color: rgb(187 247 208 / var(--tw-border-opacity));
}

.border-r-green-300 {
  --tw-border-opacity: 1;
  border-right-color: rgb(134 239 172 / var(--tw-border-opacity));
}

.border-r-green-400 {
  --tw-border-opacity: 1;
  border-right-color: rgb(74 222 128 / var(--tw-border-opacity));
}

.border-r-green-50 {
  --tw-border-opacity: 1;
  border-right-color: rgb(240 253 244 / var(--tw-border-opacity));
}

.border-r-green-500 {
  --tw-border-opacity: 1;
  border-right-color: rgb(34 197 94 / var(--tw-border-opacity));
}

.border-r-green-600 {
  --tw-border-opacity: 1;
  border-right-color: rgb(22 163 74 / var(--tw-border-opacity));
}

.border-r-green-700 {
  --tw-border-opacity: 1;
  border-right-color: rgb(21 128 61 / var(--tw-border-opacity));
}

.border-r-green-800 {
  --tw-border-opacity: 1;
  border-right-color: rgb(22 101 52 / var(--tw-border-opacity));
}

.border-r-green-900 {
  --tw-border-opacity: 1;
  border-right-color: rgb(20 83 45 / var(--tw-border-opacity));
}

.border-r-green-950 {
  --tw-border-opacity: 1;
  border-right-color: rgb(5 46 22 / var(--tw-border-opacity));
}

.border-r-indigo-100 {
  --tw-border-opacity: 1;
  border-right-color: rgb(224 231 255 / var(--tw-border-opacity));
}

.border-r-indigo-200 {
  --tw-border-opacity: 1;
  border-right-color: rgb(199 210 254 / var(--tw-border-opacity));
}

.border-r-indigo-300 {
  --tw-border-opacity: 1;
  border-right-color: rgb(165 180 252 / var(--tw-border-opacity));
}

.border-r-indigo-400 {
  --tw-border-opacity: 1;
  border-right-color: rgb(129 140 248 / var(--tw-border-opacity));
}

.border-r-indigo-50 {
  --tw-border-opacity: 1;
  border-right-color: rgb(238 242 255 / var(--tw-border-opacity));
}

.border-r-indigo-500 {
  --tw-border-opacity: 1;
  border-right-color: rgb(99 102 241 / var(--tw-border-opacity));
}

.border-r-indigo-600 {
  --tw-border-opacity: 1;
  border-right-color: rgb(79 70 229 / var(--tw-border-opacity));
}

.border-r-indigo-700 {
  --tw-border-opacity: 1;
  border-right-color: rgb(67 56 202 / var(--tw-border-opacity));
}

.border-r-indigo-800 {
  --tw-border-opacity: 1;
  border-right-color: rgb(55 48 163 / var(--tw-border-opacity));
}

.border-r-indigo-900 {
  --tw-border-opacity: 1;
  border-right-color: rgb(49 46 129 / var(--tw-border-opacity));
}

.border-r-indigo-950 {
  --tw-border-opacity: 1;
  border-right-color: rgb(30 27 75 / var(--tw-border-opacity));
}

.border-r-inherit {
  border-right-color: inherit;
}

.border-r-lime-100 {
  --tw-border-opacity: 1;
  border-right-color: rgb(236 252 203 / var(--tw-border-opacity));
}

.border-r-lime-200 {
  --tw-border-opacity: 1;
  border-right-color: rgb(217 249 157 / var(--tw-border-opacity));
}

.border-r-lime-300 {
  --tw-border-opacity: 1;
  border-right-color: rgb(190 242 100 / var(--tw-border-opacity));
}

.border-r-lime-400 {
  --tw-border-opacity: 1;
  border-right-color: rgb(163 230 53 / var(--tw-border-opacity));
}

.border-r-lime-50 {
  --tw-border-opacity: 1;
  border-right-color: rgb(247 254 231 / var(--tw-border-opacity));
}

.border-r-lime-500 {
  --tw-border-opacity: 1;
  border-right-color: rgb(132 204 22 / var(--tw-border-opacity));
}

.border-r-lime-600 {
  --tw-border-opacity: 1;
  border-right-color: rgb(101 163 13 / var(--tw-border-opacity));
}

.border-r-lime-700 {
  --tw-border-opacity: 1;
  border-right-color: rgb(77 124 15 / var(--tw-border-opacity));
}

.border-r-lime-800 {
  --tw-border-opacity: 1;
  border-right-color: rgb(63 98 18 / var(--tw-border-opacity));
}

.border-r-lime-900 {
  --tw-border-opacity: 1;
  border-right-color: rgb(54 83 20 / var(--tw-border-opacity));
}

.border-r-lime-950 {
  --tw-border-opacity: 1;
  border-right-color: rgb(26 46 5 / var(--tw-border-opacity));
}

.border-r-neutral-100 {
  --tw-border-opacity: 1;
  border-right-color: rgb(245 245 245 / var(--tw-border-opacity));
}

.border-r-neutral-200 {
  --tw-border-opacity: 1;
  border-right-color: rgb(229 229 229 / var(--tw-border-opacity));
}

.border-r-neutral-300 {
  --tw-border-opacity: 1;
  border-right-color: rgb(212 212 212 / var(--tw-border-opacity));
}

.border-r-neutral-400 {
  --tw-border-opacity: 1;
  border-right-color: rgb(163 163 163 / var(--tw-border-opacity));
}

.border-r-neutral-50 {
  --tw-border-opacity: 1;
  border-right-color: rgb(250 250 250 / var(--tw-border-opacity));
}

.border-r-neutral-500 {
  --tw-border-opacity: 1;
  border-right-color: rgb(115 115 115 / var(--tw-border-opacity));
}

.border-r-neutral-600 {
  --tw-border-opacity: 1;
  border-right-color: rgb(82 82 82 / var(--tw-border-opacity));
}

.border-r-neutral-700 {
  --tw-border-opacity: 1;
  border-right-color: rgb(64 64 64 / var(--tw-border-opacity));
}

.border-r-neutral-800 {
  --tw-border-opacity: 1;
  border-right-color: rgb(38 38 38 / var(--tw-border-opacity));
}

.border-r-neutral-900 {
  --tw-border-opacity: 1;
  border-right-color: rgb(23 23 23 / var(--tw-border-opacity));
}

.border-r-neutral-950 {
  --tw-border-opacity: 1;
  border-right-color: rgb(10 10 10 / var(--tw-border-opacity));
}

.border-r-orange-100 {
  --tw-border-opacity: 1;
  border-right-color: rgb(255 237 213 / var(--tw-border-opacity));
}

.border-r-orange-200 {
  --tw-border-opacity: 1;
  border-right-color: rgb(254 215 170 / var(--tw-border-opacity));
}

.border-r-orange-300 {
  --tw-border-opacity: 1;
  border-right-color: rgb(253 186 116 / var(--tw-border-opacity));
}

.border-r-orange-400 {
  --tw-border-opacity: 1;
  border-right-color: rgb(251 146 60 / var(--tw-border-opacity));
}

.border-r-orange-50 {
  --tw-border-opacity: 1;
  border-right-color: rgb(255 247 237 / var(--tw-border-opacity));
}

.border-r-orange-500 {
  --tw-border-opacity: 1;
  border-right-color: rgb(249 115 22 / var(--tw-border-opacity));
}

.border-r-orange-600 {
  --tw-border-opacity: 1;
  border-right-color: rgb(234 88 12 / var(--tw-border-opacity));
}

.border-r-orange-700 {
  --tw-border-opacity: 1;
  border-right-color: rgb(194 65 12 / var(--tw-border-opacity));
}

.border-r-orange-800 {
  --tw-border-opacity: 1;
  border-right-color: rgb(154 52 18 / var(--tw-border-opacity));
}

.border-r-orange-900 {
  --tw-border-opacity: 1;
  border-right-color: rgb(124 45 18 / var(--tw-border-opacity));
}

.border-r-orange-950 {
  --tw-border-opacity: 1;
  border-right-color: rgb(67 20 7 / var(--tw-border-opacity));
}

.border-r-pink-100 {
  --tw-border-opacity: 1;
  border-right-color: rgb(252 231 243 / var(--tw-border-opacity));
}

.border-r-pink-200 {
  --tw-border-opacity: 1;
  border-right-color: rgb(251 207 232 / var(--tw-border-opacity));
}

.border-r-pink-300 {
  --tw-border-opacity: 1;
  border-right-color: rgb(249 168 212 / var(--tw-border-opacity));
}

.border-r-pink-400 {
  --tw-border-opacity: 1;
  border-right-color: rgb(244 114 182 / var(--tw-border-opacity));
}

.border-r-pink-50 {
  --tw-border-opacity: 1;
  border-right-color: rgb(253 242 248 / var(--tw-border-opacity));
}

.border-r-pink-500 {
  --tw-border-opacity: 1;
  border-right-color: rgb(236 72 153 / var(--tw-border-opacity));
}

.border-r-pink-600 {
  --tw-border-opacity: 1;
  border-right-color: rgb(219 39 119 / var(--tw-border-opacity));
}

.border-r-pink-700 {
  --tw-border-opacity: 1;
  border-right-color: rgb(190 24 93 / var(--tw-border-opacity));
}

.border-r-pink-800 {
  --tw-border-opacity: 1;
  border-right-color: rgb(157 23 77 / var(--tw-border-opacity));
}

.border-r-pink-900 {
  --tw-border-opacity: 1;
  border-right-color: rgb(131 24 67 / var(--tw-border-opacity));
}

.border-r-pink-950 {
  --tw-border-opacity: 1;
  border-right-color: rgb(80 7 36 / var(--tw-border-opacity));
}

.border-r-purple-100 {
  --tw-border-opacity: 1;
  border-right-color: rgb(243 232 255 / var(--tw-border-opacity));
}

.border-r-purple-200 {
  --tw-border-opacity: 1;
  border-right-color: rgb(233 213 255 / var(--tw-border-opacity));
}

.border-r-purple-300 {
  --tw-border-opacity: 1;
  border-right-color: rgb(216 180 254 / var(--tw-border-opacity));
}

.border-r-purple-400 {
  --tw-border-opacity: 1;
  border-right-color: rgb(192 132 252 / var(--tw-border-opacity));
}

.border-r-purple-50 {
  --tw-border-opacity: 1;
  border-right-color: rgb(250 245 255 / var(--tw-border-opacity));
}

.border-r-purple-500 {
  --tw-border-opacity: 1;
  border-right-color: rgb(168 85 247 / var(--tw-border-opacity));
}

.border-r-purple-600 {
  --tw-border-opacity: 1;
  border-right-color: rgb(147 51 234 / var(--tw-border-opacity));
}

.border-r-purple-700 {
  --tw-border-opacity: 1;
  border-right-color: rgb(126 34 206 / var(--tw-border-opacity));
}

.border-r-purple-800 {
  --tw-border-opacity: 1;
  border-right-color: rgb(107 33 168 / var(--tw-border-opacity));
}

.border-r-purple-900 {
  --tw-border-opacity: 1;
  border-right-color: rgb(88 28 135 / var(--tw-border-opacity));
}

.border-r-purple-950 {
  --tw-border-opacity: 1;
  border-right-color: rgb(59 7 100 / var(--tw-border-opacity));
}

.border-r-red-100 {
  --tw-border-opacity: 1;
  border-right-color: rgb(254 226 226 / var(--tw-border-opacity));
}

.border-r-red-200 {
  --tw-border-opacity: 1;
  border-right-color: rgb(254 202 202 / var(--tw-border-opacity));
}

.border-r-red-300 {
  --tw-border-opacity: 1;
  border-right-color: rgb(252 165 165 / var(--tw-border-opacity));
}

.border-r-red-400 {
  --tw-border-opacity: 1;
  border-right-color: rgb(248 113 113 / var(--tw-border-opacity));
}

.border-r-red-50 {
  --tw-border-opacity: 1;
  border-right-color: rgb(254 242 242 / var(--tw-border-opacity));
}

.border-r-red-500 {
  --tw-border-opacity: 1;
  border-right-color: rgb(239 68 68 / var(--tw-border-opacity));
}

.border-r-red-600 {
  --tw-border-opacity: 1;
  border-right-color: rgb(220 38 38 / var(--tw-border-opacity));
}

.border-r-red-700 {
  --tw-border-opacity: 1;
  border-right-color: rgb(185 28 28 / var(--tw-border-opacity));
}

.border-r-red-800 {
  --tw-border-opacity: 1;
  border-right-color: rgb(153 27 27 / var(--tw-border-opacity));
}

.border-r-red-900 {
  --tw-border-opacity: 1;
  border-right-color: rgb(127 29 29 / var(--tw-border-opacity));
}

.border-r-red-950 {
  --tw-border-opacity: 1;
  border-right-color: rgb(69 10 10 / var(--tw-border-opacity));
}

.border-r-rose-100 {
  --tw-border-opacity: 1;
  border-right-color: rgb(255 228 230 / var(--tw-border-opacity));
}

.border-r-rose-200 {
  --tw-border-opacity: 1;
  border-right-color: rgb(254 205 211 / var(--tw-border-opacity));
}

.border-r-rose-300 {
  --tw-border-opacity: 1;
  border-right-color: rgb(253 164 175 / var(--tw-border-opacity));
}

.border-r-rose-400 {
  --tw-border-opacity: 1;
  border-right-color: rgb(251 113 133 / var(--tw-border-opacity));
}

.border-r-rose-50 {
  --tw-border-opacity: 1;
  border-right-color: rgb(255 241 242 / var(--tw-border-opacity));
}

.border-r-rose-500 {
  --tw-border-opacity: 1;
  border-right-color: rgb(244 63 94 / var(--tw-border-opacity));
}

.border-r-rose-600 {
  --tw-border-opacity: 1;
  border-right-color: rgb(225 29 72 / var(--tw-border-opacity));
}

.border-r-rose-700 {
  --tw-border-opacity: 1;
  border-right-color: rgb(190 18 60 / var(--tw-border-opacity));
}

.border-r-rose-800 {
  --tw-border-opacity: 1;
  border-right-color: rgb(159 18 57 / var(--tw-border-opacity));
}

.border-r-rose-900 {
  --tw-border-opacity: 1;
  border-right-color: rgb(136 19 55 / var(--tw-border-opacity));
}

.border-r-rose-950 {
  --tw-border-opacity: 1;
  border-right-color: rgb(76 5 25 / var(--tw-border-opacity));
}

.border-r-sky-100 {
  --tw-border-opacity: 1;
  border-right-color: rgb(224 242 254 / var(--tw-border-opacity));
}

.border-r-sky-200 {
  --tw-border-opacity: 1;
  border-right-color: rgb(186 230 253 / var(--tw-border-opacity));
}

.border-r-sky-300 {
  --tw-border-opacity: 1;
  border-right-color: rgb(125 211 252 / var(--tw-border-opacity));
}

.border-r-sky-400 {
  --tw-border-opacity: 1;
  border-right-color: rgb(56 189 248 / var(--tw-border-opacity));
}

.border-r-sky-50 {
  --tw-border-opacity: 1;
  border-right-color: rgb(240 249 255 / var(--tw-border-opacity));
}

.border-r-sky-500 {
  --tw-border-opacity: 1;
  border-right-color: rgb(14 165 233 / var(--tw-border-opacity));
}

.border-r-sky-600 {
  --tw-border-opacity: 1;
  border-right-color: rgb(2 132 199 / var(--tw-border-opacity));
}

.border-r-sky-700 {
  --tw-border-opacity: 1;
  border-right-color: rgb(3 105 161 / var(--tw-border-opacity));
}

.border-r-sky-800 {
  --tw-border-opacity: 1;
  border-right-color: rgb(7 89 133 / var(--tw-border-opacity));
}

.border-r-sky-900 {
  --tw-border-opacity: 1;
  border-right-color: rgb(12 74 110 / var(--tw-border-opacity));
}

.border-r-sky-950 {
  --tw-border-opacity: 1;
  border-right-color: rgb(8 47 73 / var(--tw-border-opacity));
}

.border-r-slate-100 {
  --tw-border-opacity: 1;
  border-right-color: rgb(241 245 249 / var(--tw-border-opacity));
}

.border-r-slate-200 {
  --tw-border-opacity: 1;
  border-right-color: rgb(226 232 240 / var(--tw-border-opacity));
}

.border-r-slate-300 {
  --tw-border-opacity: 1;
  border-right-color: rgb(203 213 225 / var(--tw-border-opacity));
}

.border-r-slate-400 {
  --tw-border-opacity: 1;
  border-right-color: rgb(148 163 184 / var(--tw-border-opacity));
}

.border-r-slate-50 {
  --tw-border-opacity: 1;
  border-right-color: rgb(248 250 252 / var(--tw-border-opacity));
}

.border-r-slate-500 {
  --tw-border-opacity: 1;
  border-right-color: rgb(100 116 139 / var(--tw-border-opacity));
}

.border-r-slate-600 {
  --tw-border-opacity: 1;
  border-right-color: rgb(71 85 105 / var(--tw-border-opacity));
}

.border-r-slate-700 {
  --tw-border-opacity: 1;
  border-right-color: rgb(51 65 85 / var(--tw-border-opacity));
}

.border-r-slate-800 {
  --tw-border-opacity: 1;
  border-right-color: rgb(30 41 59 / var(--tw-border-opacity));
}

.border-r-slate-900 {
  --tw-border-opacity: 1;
  border-right-color: rgb(15 23 42 / var(--tw-border-opacity));
}

.border-r-slate-950 {
  --tw-border-opacity: 1;
  border-right-color: rgb(2 6 23 / var(--tw-border-opacity));
}

.border-r-stone-100 {
  --tw-border-opacity: 1;
  border-right-color: rgb(245 245 244 / var(--tw-border-opacity));
}

.border-r-stone-200 {
  --tw-border-opacity: 1;
  border-right-color: rgb(231 229 228 / var(--tw-border-opacity));
}

.border-r-stone-300 {
  --tw-border-opacity: 1;
  border-right-color: rgb(214 211 209 / var(--tw-border-opacity));
}

.border-r-stone-400 {
  --tw-border-opacity: 1;
  border-right-color: rgb(168 162 158 / var(--tw-border-opacity));
}

.border-r-stone-50 {
  --tw-border-opacity: 1;
  border-right-color: rgb(250 250 249 / var(--tw-border-opacity));
}

.border-r-stone-500 {
  --tw-border-opacity: 1;
  border-right-color: rgb(120 113 108 / var(--tw-border-opacity));
}

.border-r-stone-600 {
  --tw-border-opacity: 1;
  border-right-color: rgb(87 83 78 / var(--tw-border-opacity));
}

.border-r-stone-700 {
  --tw-border-opacity: 1;
  border-right-color: rgb(68 64 60 / var(--tw-border-opacity));
}

.border-r-stone-800 {
  --tw-border-opacity: 1;
  border-right-color: rgb(41 37 36 / var(--tw-border-opacity));
}

.border-r-stone-900 {
  --tw-border-opacity: 1;
  border-right-color: rgb(28 25 23 / var(--tw-border-opacity));
}

.border-r-stone-950 {
  --tw-border-opacity: 1;
  border-right-color: rgb(12 10 9 / var(--tw-border-opacity));
}

.border-r-teal-100 {
  --tw-border-opacity: 1;
  border-right-color: rgb(204 251 241 / var(--tw-border-opacity));
}

.border-r-teal-200 {
  --tw-border-opacity: 1;
  border-right-color: rgb(153 246 228 / var(--tw-border-opacity));
}

.border-r-teal-300 {
  --tw-border-opacity: 1;
  border-right-color: rgb(94 234 212 / var(--tw-border-opacity));
}

.border-r-teal-400 {
  --tw-border-opacity: 1;
  border-right-color: rgb(45 212 191 / var(--tw-border-opacity));
}

.border-r-teal-50 {
  --tw-border-opacity: 1;
  border-right-color: rgb(240 253 250 / var(--tw-border-opacity));
}

.border-r-teal-500 {
  --tw-border-opacity: 1;
  border-right-color: rgb(20 184 166 / var(--tw-border-opacity));
}

.border-r-teal-600 {
  --tw-border-opacity: 1;
  border-right-color: rgb(13 148 136 / var(--tw-border-opacity));
}

.border-r-teal-700 {
  --tw-border-opacity: 1;
  border-right-color: rgb(15 118 110 / var(--tw-border-opacity));
}

.border-r-teal-800 {
  --tw-border-opacity: 1;
  border-right-color: rgb(17 94 89 / var(--tw-border-opacity));
}

.border-r-teal-900 {
  --tw-border-opacity: 1;
  border-right-color: rgb(19 78 74 / var(--tw-border-opacity));
}

.border-r-teal-950 {
  --tw-border-opacity: 1;
  border-right-color: rgb(4 47 46 / var(--tw-border-opacity));
}

.border-r-transparent {
  border-right-color: transparent;
}

.border-r-violet-100 {
  --tw-border-opacity: 1;
  border-right-color: rgb(237 233 254 / var(--tw-border-opacity));
}

.border-r-violet-200 {
  --tw-border-opacity: 1;
  border-right-color: rgb(221 214 254 / var(--tw-border-opacity));
}

.border-r-violet-300 {
  --tw-border-opacity: 1;
  border-right-color: rgb(196 181 253 / var(--tw-border-opacity));
}

.border-r-violet-400 {
  --tw-border-opacity: 1;
  border-right-color: rgb(167 139 250 / var(--tw-border-opacity));
}

.border-r-violet-50 {
  --tw-border-opacity: 1;
  border-right-color: rgb(245 243 255 / var(--tw-border-opacity));
}

.border-r-violet-500 {
  --tw-border-opacity: 1;
  border-right-color: rgb(139 92 246 / var(--tw-border-opacity));
}

.border-r-violet-600 {
  --tw-border-opacity: 1;
  border-right-color: rgb(124 58 237 / var(--tw-border-opacity));
}

.border-r-violet-700 {
  --tw-border-opacity: 1;
  border-right-color: rgb(109 40 217 / var(--tw-border-opacity));
}

.border-r-violet-800 {
  --tw-border-opacity: 1;
  border-right-color: rgb(91 33 182 / var(--tw-border-opacity));
}

.border-r-violet-900 {
  --tw-border-opacity: 1;
  border-right-color: rgb(76 29 149 / var(--tw-border-opacity));
}

.border-r-violet-950 {
  --tw-border-opacity: 1;
  border-right-color: rgb(46 16 101 / var(--tw-border-opacity));
}

.border-r-white {
  --tw-border-opacity: 1;
  border-right-color: rgb(255 255 255 / var(--tw-border-opacity));
}

.border-r-yellow-100 {
  --tw-border-opacity: 1;
  border-right-color: rgb(254 249 195 / var(--tw-border-opacity));
}

.border-r-yellow-200 {
  --tw-border-opacity: 1;
  border-right-color: rgb(254 240 138 / var(--tw-border-opacity));
}

.border-r-yellow-300 {
  --tw-border-opacity: 1;
  border-right-color: rgb(253 224 71 / var(--tw-border-opacity));
}

.border-r-yellow-400 {
  --tw-border-opacity: 1;
  border-right-color: rgb(250 204 21 / var(--tw-border-opacity));
}

.border-r-yellow-50 {
  --tw-border-opacity: 1;
  border-right-color: rgb(254 252 232 / var(--tw-border-opacity));
}

.border-r-yellow-500 {
  --tw-border-opacity: 1;
  border-right-color: rgb(234 179 8 / var(--tw-border-opacity));
}

.border-r-yellow-600 {
  --tw-border-opacity: 1;
  border-right-color: rgb(202 138 4 / var(--tw-border-opacity));
}

.border-r-yellow-700 {
  --tw-border-opacity: 1;
  border-right-color: rgb(161 98 7 / var(--tw-border-opacity));
}

.border-r-yellow-800 {
  --tw-border-opacity: 1;
  border-right-color: rgb(133 77 14 / var(--tw-border-opacity));
}

.border-r-yellow-900 {
  --tw-border-opacity: 1;
  border-right-color: rgb(113 63 18 / var(--tw-border-opacity));
}

.border-r-yellow-950 {
  --tw-border-opacity: 1;
  border-right-color: rgb(66 32 6 / var(--tw-border-opacity));
}

.border-r-zinc-100 {
  --tw-border-opacity: 1;
  border-right-color: rgb(244 244 245 / var(--tw-border-opacity));
}

.border-r-zinc-200 {
  --tw-border-opacity: 1;
  border-right-color: rgb(228 228 231 / var(--tw-border-opacity));
}

.border-r-zinc-300 {
  --tw-border-opacity: 1;
  border-right-color: rgb(212 212 216 / var(--tw-border-opacity));
}

.border-r-zinc-400 {
  --tw-border-opacity: 1;
  border-right-color: rgb(161 161 170 / var(--tw-border-opacity));
}

.border-r-zinc-50 {
  --tw-border-opacity: 1;
  border-right-color: rgb(250 250 250 / var(--tw-border-opacity));
}

.border-r-zinc-500 {
  --tw-border-opacity: 1;
  border-right-color: rgb(113 113 122 / var(--tw-border-opacity));
}

.border-r-zinc-600 {
  --tw-border-opacity: 1;
  border-right-color: rgb(82 82 91 / var(--tw-border-opacity));
}

.border-r-zinc-700 {
  --tw-border-opacity: 1;
  border-right-color: rgb(63 63 70 / var(--tw-border-opacity));
}

.border-r-zinc-800 {
  --tw-border-opacity: 1;
  border-right-color: rgb(39 39 42 / var(--tw-border-opacity));
}

.border-r-zinc-900 {
  --tw-border-opacity: 1;
  border-right-color: rgb(24 24 27 / var(--tw-border-opacity));
}

.border-r-zinc-950 {
  --tw-border-opacity: 1;
  border-right-color: rgb(9 9 11 / var(--tw-border-opacity));
}

.border-s-amber-100 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(254 243 199 / var(--tw-border-opacity));
}

.border-s-amber-200 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(253 230 138 / var(--tw-border-opacity));
}

.border-s-amber-300 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(252 211 77 / var(--tw-border-opacity));
}

.border-s-amber-400 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(251 191 36 / var(--tw-border-opacity));
}

.border-s-amber-50 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(255 251 235 / var(--tw-border-opacity));
}

.border-s-amber-500 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(245 158 11 / var(--tw-border-opacity));
}

.border-s-amber-600 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(217 119 6 / var(--tw-border-opacity));
}

.border-s-amber-700 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(180 83 9 / var(--tw-border-opacity));
}

.border-s-amber-800 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(146 64 14 / var(--tw-border-opacity));
}

.border-s-amber-900 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(120 53 15 / var(--tw-border-opacity));
}

.border-s-amber-950 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(69 26 3 / var(--tw-border-opacity));
}

.border-s-black {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(0 0 0 / var(--tw-border-opacity));
}

.border-s-blue-100 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(219 234 254 / var(--tw-border-opacity));
}

.border-s-blue-200 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(191 219 254 / var(--tw-border-opacity));
}

.border-s-blue-300 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(147 197 253 / var(--tw-border-opacity));
}

.border-s-blue-400 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(96 165 250 / var(--tw-border-opacity));
}

.border-s-blue-50 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(239 246 255 / var(--tw-border-opacity));
}

.border-s-blue-500 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(59 130 246 / var(--tw-border-opacity));
}

.border-s-blue-600 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(37 99 235 / var(--tw-border-opacity));
}

.border-s-blue-700 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(29 78 216 / var(--tw-border-opacity));
}

.border-s-blue-800 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(30 64 175 / var(--tw-border-opacity));
}

.border-s-blue-900 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(30 58 138 / var(--tw-border-opacity));
}

.border-s-blue-950 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(23 37 84 / var(--tw-border-opacity));
}

.border-s-current {
  border-inline-start-color: currentColor;
}

.border-s-cyan-100 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(207 250 254 / var(--tw-border-opacity));
}

.border-s-cyan-200 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(165 243 252 / var(--tw-border-opacity));
}

.border-s-cyan-300 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(103 232 249 / var(--tw-border-opacity));
}

.border-s-cyan-400 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(34 211 238 / var(--tw-border-opacity));
}

.border-s-cyan-50 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(236 254 255 / var(--tw-border-opacity));
}

.border-s-cyan-500 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(6 182 212 / var(--tw-border-opacity));
}

.border-s-cyan-600 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(8 145 178 / var(--tw-border-opacity));
}

.border-s-cyan-700 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(14 116 144 / var(--tw-border-opacity));
}

.border-s-cyan-800 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(21 94 117 / var(--tw-border-opacity));
}

.border-s-cyan-900 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(22 78 99 / var(--tw-border-opacity));
}

.border-s-cyan-950 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(8 51 68 / var(--tw-border-opacity));
}

.border-s-emerald-100 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(209 250 229 / var(--tw-border-opacity));
}

.border-s-emerald-200 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(167 243 208 / var(--tw-border-opacity));
}

.border-s-emerald-300 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(110 231 183 / var(--tw-border-opacity));
}

.border-s-emerald-400 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(52 211 153 / var(--tw-border-opacity));
}

.border-s-emerald-50 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(236 253 245 / var(--tw-border-opacity));
}

.border-s-emerald-500 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(16 185 129 / var(--tw-border-opacity));
}

.border-s-emerald-600 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(5 150 105 / var(--tw-border-opacity));
}

.border-s-emerald-700 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(4 120 87 / var(--tw-border-opacity));
}

.border-s-emerald-800 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(6 95 70 / var(--tw-border-opacity));
}

.border-s-emerald-900 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(6 78 59 / var(--tw-border-opacity));
}

.border-s-emerald-950 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(2 44 34 / var(--tw-border-opacity));
}

.border-s-fuchsia-100 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(250 232 255 / var(--tw-border-opacity));
}

.border-s-fuchsia-200 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(245 208 254 / var(--tw-border-opacity));
}

.border-s-fuchsia-300 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(240 171 252 / var(--tw-border-opacity));
}

.border-s-fuchsia-400 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(232 121 249 / var(--tw-border-opacity));
}

.border-s-fuchsia-50 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(253 244 255 / var(--tw-border-opacity));
}

.border-s-fuchsia-500 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(217 70 239 / var(--tw-border-opacity));
}

.border-s-fuchsia-600 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(192 38 211 / var(--tw-border-opacity));
}

.border-s-fuchsia-700 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(162 28 175 / var(--tw-border-opacity));
}

.border-s-fuchsia-800 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(134 25 143 / var(--tw-border-opacity));
}

.border-s-fuchsia-900 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(112 26 117 / var(--tw-border-opacity));
}

.border-s-fuchsia-950 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(74 4 78 / var(--tw-border-opacity));
}

.border-s-gray-100 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(243 244 246 / var(--tw-border-opacity));
}

.border-s-gray-200 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(229 231 235 / var(--tw-border-opacity));
}

.border-s-gray-300 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(209 213 219 / var(--tw-border-opacity));
}

.border-s-gray-400 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(156 163 175 / var(--tw-border-opacity));
}

.border-s-gray-50 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(249 250 251 / var(--tw-border-opacity));
}

.border-s-gray-500 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(107 114 128 / var(--tw-border-opacity));
}

.border-s-gray-600 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(75 85 99 / var(--tw-border-opacity));
}

.border-s-gray-700 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(55 65 81 / var(--tw-border-opacity));
}

.border-s-gray-800 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(31 41 55 / var(--tw-border-opacity));
}

.border-s-gray-900 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(17 24 39 / var(--tw-border-opacity));
}

.border-s-gray-950 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(3 7 18 / var(--tw-border-opacity));
}

.border-s-green-100 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(220 252 231 / var(--tw-border-opacity));
}

.border-s-green-200 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(187 247 208 / var(--tw-border-opacity));
}

.border-s-green-300 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(134 239 172 / var(--tw-border-opacity));
}

.border-s-green-400 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(74 222 128 / var(--tw-border-opacity));
}

.border-s-green-50 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(240 253 244 / var(--tw-border-opacity));
}

.border-s-green-500 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(34 197 94 / var(--tw-border-opacity));
}

.border-s-green-600 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(22 163 74 / var(--tw-border-opacity));
}

.border-s-green-700 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(21 128 61 / var(--tw-border-opacity));
}

.border-s-green-800 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(22 101 52 / var(--tw-border-opacity));
}

.border-s-green-900 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(20 83 45 / var(--tw-border-opacity));
}

.border-s-green-950 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(5 46 22 / var(--tw-border-opacity));
}

.border-s-indigo-100 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(224 231 255 / var(--tw-border-opacity));
}

.border-s-indigo-200 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(199 210 254 / var(--tw-border-opacity));
}

.border-s-indigo-300 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(165 180 252 / var(--tw-border-opacity));
}

.border-s-indigo-400 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(129 140 248 / var(--tw-border-opacity));
}

.border-s-indigo-50 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(238 242 255 / var(--tw-border-opacity));
}

.border-s-indigo-500 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(99 102 241 / var(--tw-border-opacity));
}

.border-s-indigo-600 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(79 70 229 / var(--tw-border-opacity));
}

.border-s-indigo-700 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(67 56 202 / var(--tw-border-opacity));
}

.border-s-indigo-800 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(55 48 163 / var(--tw-border-opacity));
}

.border-s-indigo-900 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(49 46 129 / var(--tw-border-opacity));
}

.border-s-indigo-950 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(30 27 75 / var(--tw-border-opacity));
}

.border-s-inherit {
  border-inline-start-color: inherit;
}

.border-s-lime-100 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(236 252 203 / var(--tw-border-opacity));
}

.border-s-lime-200 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(217 249 157 / var(--tw-border-opacity));
}

.border-s-lime-300 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(190 242 100 / var(--tw-border-opacity));
}

.border-s-lime-400 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(163 230 53 / var(--tw-border-opacity));
}

.border-s-lime-50 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(247 254 231 / var(--tw-border-opacity));
}

.border-s-lime-500 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(132 204 22 / var(--tw-border-opacity));
}

.border-s-lime-600 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(101 163 13 / var(--tw-border-opacity));
}

.border-s-lime-700 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(77 124 15 / var(--tw-border-opacity));
}

.border-s-lime-800 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(63 98 18 / var(--tw-border-opacity));
}

.border-s-lime-900 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(54 83 20 / var(--tw-border-opacity));
}

.border-s-lime-950 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(26 46 5 / var(--tw-border-opacity));
}

.border-s-neutral-100 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(245 245 245 / var(--tw-border-opacity));
}

.border-s-neutral-200 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(229 229 229 / var(--tw-border-opacity));
}

.border-s-neutral-300 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(212 212 212 / var(--tw-border-opacity));
}

.border-s-neutral-400 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(163 163 163 / var(--tw-border-opacity));
}

.border-s-neutral-50 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(250 250 250 / var(--tw-border-opacity));
}

.border-s-neutral-500 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(115 115 115 / var(--tw-border-opacity));
}

.border-s-neutral-600 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(82 82 82 / var(--tw-border-opacity));
}

.border-s-neutral-700 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(64 64 64 / var(--tw-border-opacity));
}

.border-s-neutral-800 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(38 38 38 / var(--tw-border-opacity));
}

.border-s-neutral-900 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(23 23 23 / var(--tw-border-opacity));
}

.border-s-neutral-950 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(10 10 10 / var(--tw-border-opacity));
}

.border-s-orange-100 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(255 237 213 / var(--tw-border-opacity));
}

.border-s-orange-200 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(254 215 170 / var(--tw-border-opacity));
}

.border-s-orange-300 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(253 186 116 / var(--tw-border-opacity));
}

.border-s-orange-400 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(251 146 60 / var(--tw-border-opacity));
}

.border-s-orange-50 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(255 247 237 / var(--tw-border-opacity));
}

.border-s-orange-500 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(249 115 22 / var(--tw-border-opacity));
}

.border-s-orange-600 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(234 88 12 / var(--tw-border-opacity));
}

.border-s-orange-700 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(194 65 12 / var(--tw-border-opacity));
}

.border-s-orange-800 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(154 52 18 / var(--tw-border-opacity));
}

.border-s-orange-900 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(124 45 18 / var(--tw-border-opacity));
}

.border-s-orange-950 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(67 20 7 / var(--tw-border-opacity));
}

.border-s-pink-100 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(252 231 243 / var(--tw-border-opacity));
}

.border-s-pink-200 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(251 207 232 / var(--tw-border-opacity));
}

.border-s-pink-300 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(249 168 212 / var(--tw-border-opacity));
}

.border-s-pink-400 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(244 114 182 / var(--tw-border-opacity));
}

.border-s-pink-50 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(253 242 248 / var(--tw-border-opacity));
}

.border-s-pink-500 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(236 72 153 / var(--tw-border-opacity));
}

.border-s-pink-600 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(219 39 119 / var(--tw-border-opacity));
}

.border-s-pink-700 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(190 24 93 / var(--tw-border-opacity));
}

.border-s-pink-800 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(157 23 77 / var(--tw-border-opacity));
}

.border-s-pink-900 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(131 24 67 / var(--tw-border-opacity));
}

.border-s-pink-950 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(80 7 36 / var(--tw-border-opacity));
}

.border-s-purple-100 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(243 232 255 / var(--tw-border-opacity));
}

.border-s-purple-200 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(233 213 255 / var(--tw-border-opacity));
}

.border-s-purple-300 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(216 180 254 / var(--tw-border-opacity));
}

.border-s-purple-400 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(192 132 252 / var(--tw-border-opacity));
}

.border-s-purple-50 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(250 245 255 / var(--tw-border-opacity));
}

.border-s-purple-500 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(168 85 247 / var(--tw-border-opacity));
}

.border-s-purple-600 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(147 51 234 / var(--tw-border-opacity));
}

.border-s-purple-700 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(126 34 206 / var(--tw-border-opacity));
}

.border-s-purple-800 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(107 33 168 / var(--tw-border-opacity));
}

.border-s-purple-900 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(88 28 135 / var(--tw-border-opacity));
}

.border-s-purple-950 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(59 7 100 / var(--tw-border-opacity));
}

.border-s-red-100 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(254 226 226 / var(--tw-border-opacity));
}

.border-s-red-200 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(254 202 202 / var(--tw-border-opacity));
}

.border-s-red-300 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(252 165 165 / var(--tw-border-opacity));
}

.border-s-red-400 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(248 113 113 / var(--tw-border-opacity));
}

.border-s-red-50 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(254 242 242 / var(--tw-border-opacity));
}

.border-s-red-500 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(239 68 68 / var(--tw-border-opacity));
}

.border-s-red-600 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(220 38 38 / var(--tw-border-opacity));
}

.border-s-red-700 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(185 28 28 / var(--tw-border-opacity));
}

.border-s-red-800 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(153 27 27 / var(--tw-border-opacity));
}

.border-s-red-900 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(127 29 29 / var(--tw-border-opacity));
}

.border-s-red-950 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(69 10 10 / var(--tw-border-opacity));
}

.border-s-rose-100 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(255 228 230 / var(--tw-border-opacity));
}

.border-s-rose-200 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(254 205 211 / var(--tw-border-opacity));
}

.border-s-rose-300 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(253 164 175 / var(--tw-border-opacity));
}

.border-s-rose-400 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(251 113 133 / var(--tw-border-opacity));
}

.border-s-rose-50 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(255 241 242 / var(--tw-border-opacity));
}

.border-s-rose-500 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(244 63 94 / var(--tw-border-opacity));
}

.border-s-rose-600 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(225 29 72 / var(--tw-border-opacity));
}

.border-s-rose-700 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(190 18 60 / var(--tw-border-opacity));
}

.border-s-rose-800 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(159 18 57 / var(--tw-border-opacity));
}

.border-s-rose-900 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(136 19 55 / var(--tw-border-opacity));
}

.border-s-rose-950 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(76 5 25 / var(--tw-border-opacity));
}

.border-s-sky-100 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(224 242 254 / var(--tw-border-opacity));
}

.border-s-sky-200 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(186 230 253 / var(--tw-border-opacity));
}

.border-s-sky-300 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(125 211 252 / var(--tw-border-opacity));
}

.border-s-sky-400 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(56 189 248 / var(--tw-border-opacity));
}

.border-s-sky-50 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(240 249 255 / var(--tw-border-opacity));
}

.border-s-sky-500 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(14 165 233 / var(--tw-border-opacity));
}

.border-s-sky-600 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(2 132 199 / var(--tw-border-opacity));
}

.border-s-sky-700 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(3 105 161 / var(--tw-border-opacity));
}

.border-s-sky-800 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(7 89 133 / var(--tw-border-opacity));
}

.border-s-sky-900 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(12 74 110 / var(--tw-border-opacity));
}

.border-s-sky-950 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(8 47 73 / var(--tw-border-opacity));
}

.border-s-slate-100 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(241 245 249 / var(--tw-border-opacity));
}

.border-s-slate-200 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(226 232 240 / var(--tw-border-opacity));
}

.border-s-slate-300 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(203 213 225 / var(--tw-border-opacity));
}

.border-s-slate-400 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(148 163 184 / var(--tw-border-opacity));
}

.border-s-slate-50 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(248 250 252 / var(--tw-border-opacity));
}

.border-s-slate-500 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(100 116 139 / var(--tw-border-opacity));
}

.border-s-slate-600 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(71 85 105 / var(--tw-border-opacity));
}

.border-s-slate-700 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(51 65 85 / var(--tw-border-opacity));
}

.border-s-slate-800 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(30 41 59 / var(--tw-border-opacity));
}

.border-s-slate-900 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(15 23 42 / var(--tw-border-opacity));
}

.border-s-slate-950 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(2 6 23 / var(--tw-border-opacity));
}

.border-s-stone-100 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(245 245 244 / var(--tw-border-opacity));
}

.border-s-stone-200 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(231 229 228 / var(--tw-border-opacity));
}

.border-s-stone-300 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(214 211 209 / var(--tw-border-opacity));
}

.border-s-stone-400 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(168 162 158 / var(--tw-border-opacity));
}

.border-s-stone-50 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(250 250 249 / var(--tw-border-opacity));
}

.border-s-stone-500 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(120 113 108 / var(--tw-border-opacity));
}

.border-s-stone-600 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(87 83 78 / var(--tw-border-opacity));
}

.border-s-stone-700 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(68 64 60 / var(--tw-border-opacity));
}

.border-s-stone-800 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(41 37 36 / var(--tw-border-opacity));
}

.border-s-stone-900 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(28 25 23 / var(--tw-border-opacity));
}

.border-s-stone-950 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(12 10 9 / var(--tw-border-opacity));
}

.border-s-teal-100 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(204 251 241 / var(--tw-border-opacity));
}

.border-s-teal-200 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(153 246 228 / var(--tw-border-opacity));
}

.border-s-teal-300 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(94 234 212 / var(--tw-border-opacity));
}

.border-s-teal-400 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(45 212 191 / var(--tw-border-opacity));
}

.border-s-teal-50 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(240 253 250 / var(--tw-border-opacity));
}

.border-s-teal-500 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(20 184 166 / var(--tw-border-opacity));
}

.border-s-teal-600 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(13 148 136 / var(--tw-border-opacity));
}

.border-s-teal-700 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(15 118 110 / var(--tw-border-opacity));
}

.border-s-teal-800 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(17 94 89 / var(--tw-border-opacity));
}

.border-s-teal-900 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(19 78 74 / var(--tw-border-opacity));
}

.border-s-teal-950 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(4 47 46 / var(--tw-border-opacity));
}

.border-s-transparent {
  border-inline-start-color: transparent;
}

.border-s-violet-100 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(237 233 254 / var(--tw-border-opacity));
}

.border-s-violet-200 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(221 214 254 / var(--tw-border-opacity));
}

.border-s-violet-300 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(196 181 253 / var(--tw-border-opacity));
}

.border-s-violet-400 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(167 139 250 / var(--tw-border-opacity));
}

.border-s-violet-50 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(245 243 255 / var(--tw-border-opacity));
}

.border-s-violet-500 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(139 92 246 / var(--tw-border-opacity));
}

.border-s-violet-600 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(124 58 237 / var(--tw-border-opacity));
}

.border-s-violet-700 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(109 40 217 / var(--tw-border-opacity));
}

.border-s-violet-800 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(91 33 182 / var(--tw-border-opacity));
}

.border-s-violet-900 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(76 29 149 / var(--tw-border-opacity));
}

.border-s-violet-950 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(46 16 101 / var(--tw-border-opacity));
}

.border-s-white {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(255 255 255 / var(--tw-border-opacity));
}

.border-s-yellow-100 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(254 249 195 / var(--tw-border-opacity));
}

.border-s-yellow-200 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(254 240 138 / var(--tw-border-opacity));
}

.border-s-yellow-300 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(253 224 71 / var(--tw-border-opacity));
}

.border-s-yellow-400 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(250 204 21 / var(--tw-border-opacity));
}

.border-s-yellow-50 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(254 252 232 / var(--tw-border-opacity));
}

.border-s-yellow-500 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(234 179 8 / var(--tw-border-opacity));
}

.border-s-yellow-600 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(202 138 4 / var(--tw-border-opacity));
}

.border-s-yellow-700 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(161 98 7 / var(--tw-border-opacity));
}

.border-s-yellow-800 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(133 77 14 / var(--tw-border-opacity));
}

.border-s-yellow-900 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(113 63 18 / var(--tw-border-opacity));
}

.border-s-yellow-950 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(66 32 6 / var(--tw-border-opacity));
}

.border-s-zinc-100 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(244 244 245 / var(--tw-border-opacity));
}

.border-s-zinc-200 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(228 228 231 / var(--tw-border-opacity));
}

.border-s-zinc-300 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(212 212 216 / var(--tw-border-opacity));
}

.border-s-zinc-400 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(161 161 170 / var(--tw-border-opacity));
}

.border-s-zinc-50 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(250 250 250 / var(--tw-border-opacity));
}

.border-s-zinc-500 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(113 113 122 / var(--tw-border-opacity));
}

.border-s-zinc-600 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(82 82 91 / var(--tw-border-opacity));
}

.border-s-zinc-700 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(63 63 70 / var(--tw-border-opacity));
}

.border-s-zinc-800 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(39 39 42 / var(--tw-border-opacity));
}

.border-s-zinc-900 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(24 24 27 / var(--tw-border-opacity));
}

.border-s-zinc-950 {
  --tw-border-opacity: 1;
  border-inline-start-color: rgb(9 9 11 / var(--tw-border-opacity));
}

.border-t-amber-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(254 243 199 / var(--tw-border-opacity));
}

.border-t-amber-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(253 230 138 / var(--tw-border-opacity));
}

.border-t-amber-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(252 211 77 / var(--tw-border-opacity));
}

.border-t-amber-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(251 191 36 / var(--tw-border-opacity));
}

.border-t-amber-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(255 251 235 / var(--tw-border-opacity));
}

.border-t-amber-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(245 158 11 / var(--tw-border-opacity));
}

.border-t-amber-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(217 119 6 / var(--tw-border-opacity));
}

.border-t-amber-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(180 83 9 / var(--tw-border-opacity));
}

.border-t-amber-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(146 64 14 / var(--tw-border-opacity));
}

.border-t-amber-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(120 53 15 / var(--tw-border-opacity));
}

.border-t-amber-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(69 26 3 / var(--tw-border-opacity));
}

.border-t-black {
  --tw-border-opacity: 1;
  border-top-color: rgb(0 0 0 / var(--tw-border-opacity));
}

.border-t-blue-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(219 234 254 / var(--tw-border-opacity));
}

.border-t-blue-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(191 219 254 / var(--tw-border-opacity));
}

.border-t-blue-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(147 197 253 / var(--tw-border-opacity));
}

.border-t-blue-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(96 165 250 / var(--tw-border-opacity));
}

.border-t-blue-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(239 246 255 / var(--tw-border-opacity));
}

.border-t-blue-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(59 130 246 / var(--tw-border-opacity));
}

.border-t-blue-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(37 99 235 / var(--tw-border-opacity));
}

.border-t-blue-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(29 78 216 / var(--tw-border-opacity));
}

.border-t-blue-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(30 64 175 / var(--tw-border-opacity));
}

.border-t-blue-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(30 58 138 / var(--tw-border-opacity));
}

.border-t-blue-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(23 37 84 / var(--tw-border-opacity));
}

.border-t-current {
  border-top-color: currentColor;
}

.border-t-cyan-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(207 250 254 / var(--tw-border-opacity));
}

.border-t-cyan-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(165 243 252 / var(--tw-border-opacity));
}

.border-t-cyan-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(103 232 249 / var(--tw-border-opacity));
}

.border-t-cyan-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(34 211 238 / var(--tw-border-opacity));
}

.border-t-cyan-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(236 254 255 / var(--tw-border-opacity));
}

.border-t-cyan-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(6 182 212 / var(--tw-border-opacity));
}

.border-t-cyan-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(8 145 178 / var(--tw-border-opacity));
}

.border-t-cyan-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(14 116 144 / var(--tw-border-opacity));
}

.border-t-cyan-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(21 94 117 / var(--tw-border-opacity));
}

.border-t-cyan-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(22 78 99 / var(--tw-border-opacity));
}

.border-t-cyan-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(8 51 68 / var(--tw-border-opacity));
}

.border-t-emerald-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(209 250 229 / var(--tw-border-opacity));
}

.border-t-emerald-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(167 243 208 / var(--tw-border-opacity));
}

.border-t-emerald-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(110 231 183 / var(--tw-border-opacity));
}

.border-t-emerald-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(52 211 153 / var(--tw-border-opacity));
}

.border-t-emerald-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(236 253 245 / var(--tw-border-opacity));
}

.border-t-emerald-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(16 185 129 / var(--tw-border-opacity));
}

.border-t-emerald-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(5 150 105 / var(--tw-border-opacity));
}

.border-t-emerald-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(4 120 87 / var(--tw-border-opacity));
}

.border-t-emerald-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(6 95 70 / var(--tw-border-opacity));
}

.border-t-emerald-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(6 78 59 / var(--tw-border-opacity));
}

.border-t-emerald-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(2 44 34 / var(--tw-border-opacity));
}

.border-t-fuchsia-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(250 232 255 / var(--tw-border-opacity));
}

.border-t-fuchsia-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(245 208 254 / var(--tw-border-opacity));
}

.border-t-fuchsia-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(240 171 252 / var(--tw-border-opacity));
}

.border-t-fuchsia-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(232 121 249 / var(--tw-border-opacity));
}

.border-t-fuchsia-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(253 244 255 / var(--tw-border-opacity));
}

.border-t-fuchsia-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(217 70 239 / var(--tw-border-opacity));
}

.border-t-fuchsia-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(192 38 211 / var(--tw-border-opacity));
}

.border-t-fuchsia-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(162 28 175 / var(--tw-border-opacity));
}

.border-t-fuchsia-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(134 25 143 / var(--tw-border-opacity));
}

.border-t-fuchsia-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(112 26 117 / var(--tw-border-opacity));
}

.border-t-fuchsia-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(74 4 78 / var(--tw-border-opacity));
}

.border-t-gray-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(243 244 246 / var(--tw-border-opacity));
}

.border-t-gray-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(229 231 235 / var(--tw-border-opacity));
}

.border-t-gray-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(209 213 219 / var(--tw-border-opacity));
}

.border-t-gray-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(156 163 175 / var(--tw-border-opacity));
}

.border-t-gray-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(249 250 251 / var(--tw-border-opacity));
}

.border-t-gray-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(107 114 128 / var(--tw-border-opacity));
}

.border-t-gray-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(75 85 99 / var(--tw-border-opacity));
}

.border-t-gray-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(55 65 81 / var(--tw-border-opacity));
}

.border-t-gray-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(31 41 55 / var(--tw-border-opacity));
}

.border-t-gray-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(17 24 39 / var(--tw-border-opacity));
}

.border-t-gray-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(3 7 18 / var(--tw-border-opacity));
}

.border-t-green-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(220 252 231 / var(--tw-border-opacity));
}

.border-t-green-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(187 247 208 / var(--tw-border-opacity));
}

.border-t-green-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(134 239 172 / var(--tw-border-opacity));
}

.border-t-green-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(74 222 128 / var(--tw-border-opacity));
}

.border-t-green-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(240 253 244 / var(--tw-border-opacity));
}

.border-t-green-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(34 197 94 / var(--tw-border-opacity));
}

.border-t-green-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(22 163 74 / var(--tw-border-opacity));
}

.border-t-green-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(21 128 61 / var(--tw-border-opacity));
}

.border-t-green-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(22 101 52 / var(--tw-border-opacity));
}

.border-t-green-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(20 83 45 / var(--tw-border-opacity));
}

.border-t-green-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(5 46 22 / var(--tw-border-opacity));
}

.border-t-indigo-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(224 231 255 / var(--tw-border-opacity));
}

.border-t-indigo-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(199 210 254 / var(--tw-border-opacity));
}

.border-t-indigo-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(165 180 252 / var(--tw-border-opacity));
}

.border-t-indigo-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(129 140 248 / var(--tw-border-opacity));
}

.border-t-indigo-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(238 242 255 / var(--tw-border-opacity));
}

.border-t-indigo-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(99 102 241 / var(--tw-border-opacity));
}

.border-t-indigo-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(79 70 229 / var(--tw-border-opacity));
}

.border-t-indigo-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(67 56 202 / var(--tw-border-opacity));
}

.border-t-indigo-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(55 48 163 / var(--tw-border-opacity));
}

.border-t-indigo-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(49 46 129 / var(--tw-border-opacity));
}

.border-t-indigo-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(30 27 75 / var(--tw-border-opacity));
}

.border-t-inherit {
  border-top-color: inherit;
}

.border-t-lime-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(236 252 203 / var(--tw-border-opacity));
}

.border-t-lime-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(217 249 157 / var(--tw-border-opacity));
}

.border-t-lime-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(190 242 100 / var(--tw-border-opacity));
}

.border-t-lime-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(163 230 53 / var(--tw-border-opacity));
}

.border-t-lime-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(247 254 231 / var(--tw-border-opacity));
}

.border-t-lime-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(132 204 22 / var(--tw-border-opacity));
}

.border-t-lime-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(101 163 13 / var(--tw-border-opacity));
}

.border-t-lime-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(77 124 15 / var(--tw-border-opacity));
}

.border-t-lime-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(63 98 18 / var(--tw-border-opacity));
}

.border-t-lime-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(54 83 20 / var(--tw-border-opacity));
}

.border-t-lime-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(26 46 5 / var(--tw-border-opacity));
}

.border-t-neutral-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(245 245 245 / var(--tw-border-opacity));
}

.border-t-neutral-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(229 229 229 / var(--tw-border-opacity));
}

.border-t-neutral-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(212 212 212 / var(--tw-border-opacity));
}

.border-t-neutral-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(163 163 163 / var(--tw-border-opacity));
}

.border-t-neutral-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(250 250 250 / var(--tw-border-opacity));
}

.border-t-neutral-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(115 115 115 / var(--tw-border-opacity));
}

.border-t-neutral-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(82 82 82 / var(--tw-border-opacity));
}

.border-t-neutral-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(64 64 64 / var(--tw-border-opacity));
}

.border-t-neutral-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(38 38 38 / var(--tw-border-opacity));
}

.border-t-neutral-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(23 23 23 / var(--tw-border-opacity));
}

.border-t-neutral-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(10 10 10 / var(--tw-border-opacity));
}

.border-t-orange-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(255 237 213 / var(--tw-border-opacity));
}

.border-t-orange-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(254 215 170 / var(--tw-border-opacity));
}

.border-t-orange-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(253 186 116 / var(--tw-border-opacity));
}

.border-t-orange-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(251 146 60 / var(--tw-border-opacity));
}

.border-t-orange-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(255 247 237 / var(--tw-border-opacity));
}

.border-t-orange-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(249 115 22 / var(--tw-border-opacity));
}

.border-t-orange-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(234 88 12 / var(--tw-border-opacity));
}

.border-t-orange-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(194 65 12 / var(--tw-border-opacity));
}

.border-t-orange-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(154 52 18 / var(--tw-border-opacity));
}

.border-t-orange-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(124 45 18 / var(--tw-border-opacity));
}

.border-t-orange-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(67 20 7 / var(--tw-border-opacity));
}

.border-t-pink-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(252 231 243 / var(--tw-border-opacity));
}

.border-t-pink-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(251 207 232 / var(--tw-border-opacity));
}

.border-t-pink-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(249 168 212 / var(--tw-border-opacity));
}

.border-t-pink-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(244 114 182 / var(--tw-border-opacity));
}

.border-t-pink-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(253 242 248 / var(--tw-border-opacity));
}

.border-t-pink-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(236 72 153 / var(--tw-border-opacity));
}

.border-t-pink-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(219 39 119 / var(--tw-border-opacity));
}

.border-t-pink-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(190 24 93 / var(--tw-border-opacity));
}

.border-t-pink-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(157 23 77 / var(--tw-border-opacity));
}

.border-t-pink-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(131 24 67 / var(--tw-border-opacity));
}

.border-t-pink-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(80 7 36 / var(--tw-border-opacity));
}

.border-t-purple-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(243 232 255 / var(--tw-border-opacity));
}

.border-t-purple-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(233 213 255 / var(--tw-border-opacity));
}

.border-t-purple-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(216 180 254 / var(--tw-border-opacity));
}

.border-t-purple-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(192 132 252 / var(--tw-border-opacity));
}

.border-t-purple-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(250 245 255 / var(--tw-border-opacity));
}

.border-t-purple-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(168 85 247 / var(--tw-border-opacity));
}

.border-t-purple-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(147 51 234 / var(--tw-border-opacity));
}

.border-t-purple-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(126 34 206 / var(--tw-border-opacity));
}

.border-t-purple-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(107 33 168 / var(--tw-border-opacity));
}

.border-t-purple-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(88 28 135 / var(--tw-border-opacity));
}

.border-t-purple-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(59 7 100 / var(--tw-border-opacity));
}

.border-t-red-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(254 226 226 / var(--tw-border-opacity));
}

.border-t-red-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(254 202 202 / var(--tw-border-opacity));
}

.border-t-red-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(252 165 165 / var(--tw-border-opacity));
}

.border-t-red-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(248 113 113 / var(--tw-border-opacity));
}

.border-t-red-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(254 242 242 / var(--tw-border-opacity));
}

.border-t-red-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(239 68 68 / var(--tw-border-opacity));
}

.border-t-red-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(220 38 38 / var(--tw-border-opacity));
}

.border-t-red-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(185 28 28 / var(--tw-border-opacity));
}

.border-t-red-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(153 27 27 / var(--tw-border-opacity));
}

.border-t-red-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(127 29 29 / var(--tw-border-opacity));
}

.border-t-red-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(69 10 10 / var(--tw-border-opacity));
}

.border-t-rose-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(255 228 230 / var(--tw-border-opacity));
}

.border-t-rose-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(254 205 211 / var(--tw-border-opacity));
}

.border-t-rose-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(253 164 175 / var(--tw-border-opacity));
}

.border-t-rose-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(251 113 133 / var(--tw-border-opacity));
}

.border-t-rose-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(255 241 242 / var(--tw-border-opacity));
}

.border-t-rose-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(244 63 94 / var(--tw-border-opacity));
}

.border-t-rose-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(225 29 72 / var(--tw-border-opacity));
}

.border-t-rose-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(190 18 60 / var(--tw-border-opacity));
}

.border-t-rose-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(159 18 57 / var(--tw-border-opacity));
}

.border-t-rose-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(136 19 55 / var(--tw-border-opacity));
}

.border-t-rose-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(76 5 25 / var(--tw-border-opacity));
}

.border-t-sky-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(224 242 254 / var(--tw-border-opacity));
}

.border-t-sky-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(186 230 253 / var(--tw-border-opacity));
}

.border-t-sky-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(125 211 252 / var(--tw-border-opacity));
}

.border-t-sky-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(56 189 248 / var(--tw-border-opacity));
}

.border-t-sky-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(240 249 255 / var(--tw-border-opacity));
}

.border-t-sky-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(14 165 233 / var(--tw-border-opacity));
}

.border-t-sky-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(2 132 199 / var(--tw-border-opacity));
}

.border-t-sky-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(3 105 161 / var(--tw-border-opacity));
}

.border-t-sky-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(7 89 133 / var(--tw-border-opacity));
}

.border-t-sky-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(12 74 110 / var(--tw-border-opacity));
}

.border-t-sky-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(8 47 73 / var(--tw-border-opacity));
}

.border-t-slate-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(241 245 249 / var(--tw-border-opacity));
}

.border-t-slate-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(226 232 240 / var(--tw-border-opacity));
}

.border-t-slate-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(203 213 225 / var(--tw-border-opacity));
}

.border-t-slate-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(148 163 184 / var(--tw-border-opacity));
}

.border-t-slate-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(248 250 252 / var(--tw-border-opacity));
}

.border-t-slate-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(100 116 139 / var(--tw-border-opacity));
}

.border-t-slate-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(71 85 105 / var(--tw-border-opacity));
}

.border-t-slate-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(51 65 85 / var(--tw-border-opacity));
}

.border-t-slate-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(30 41 59 / var(--tw-border-opacity));
}

.border-t-slate-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(15 23 42 / var(--tw-border-opacity));
}

.border-t-slate-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(2 6 23 / var(--tw-border-opacity));
}

.border-t-stone-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(245 245 244 / var(--tw-border-opacity));
}

.border-t-stone-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(231 229 228 / var(--tw-border-opacity));
}

.border-t-stone-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(214 211 209 / var(--tw-border-opacity));
}

.border-t-stone-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(168 162 158 / var(--tw-border-opacity));
}

.border-t-stone-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(250 250 249 / var(--tw-border-opacity));
}

.border-t-stone-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(120 113 108 / var(--tw-border-opacity));
}

.border-t-stone-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(87 83 78 / var(--tw-border-opacity));
}

.border-t-stone-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(68 64 60 / var(--tw-border-opacity));
}

.border-t-stone-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(41 37 36 / var(--tw-border-opacity));
}

.border-t-stone-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(28 25 23 / var(--tw-border-opacity));
}

.border-t-stone-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(12 10 9 / var(--tw-border-opacity));
}

.border-t-teal-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(204 251 241 / var(--tw-border-opacity));
}

.border-t-teal-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(153 246 228 / var(--tw-border-opacity));
}

.border-t-teal-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(94 234 212 / var(--tw-border-opacity));
}

.border-t-teal-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(45 212 191 / var(--tw-border-opacity));
}

.border-t-teal-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(240 253 250 / var(--tw-border-opacity));
}

.border-t-teal-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(20 184 166 / var(--tw-border-opacity));
}

.border-t-teal-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(13 148 136 / var(--tw-border-opacity));
}

.border-t-teal-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(15 118 110 / var(--tw-border-opacity));
}

.border-t-teal-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(17 94 89 / var(--tw-border-opacity));
}

.border-t-teal-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(19 78 74 / var(--tw-border-opacity));
}

.border-t-teal-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(4 47 46 / var(--tw-border-opacity));
}

.border-t-transparent {
  border-top-color: transparent;
}

.border-t-violet-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(237 233 254 / var(--tw-border-opacity));
}

.border-t-violet-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(221 214 254 / var(--tw-border-opacity));
}

.border-t-violet-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(196 181 253 / var(--tw-border-opacity));
}

.border-t-violet-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(167 139 250 / var(--tw-border-opacity));
}

.border-t-violet-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(245 243 255 / var(--tw-border-opacity));
}

.border-t-violet-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(139 92 246 / var(--tw-border-opacity));
}

.border-t-violet-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(124 58 237 / var(--tw-border-opacity));
}

.border-t-violet-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(109 40 217 / var(--tw-border-opacity));
}

.border-t-violet-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(91 33 182 / var(--tw-border-opacity));
}

.border-t-violet-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(76 29 149 / var(--tw-border-opacity));
}

.border-t-violet-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(46 16 101 / var(--tw-border-opacity));
}

.border-t-white {
  --tw-border-opacity: 1;
  border-top-color: rgb(255 255 255 / var(--tw-border-opacity));
}

.border-t-yellow-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(254 249 195 / var(--tw-border-opacity));
}

.border-t-yellow-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(254 240 138 / var(--tw-border-opacity));
}

.border-t-yellow-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(253 224 71 / var(--tw-border-opacity));
}

.border-t-yellow-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(250 204 21 / var(--tw-border-opacity));
}

.border-t-yellow-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(254 252 232 / var(--tw-border-opacity));
}

.border-t-yellow-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(234 179 8 / var(--tw-border-opacity));
}

.border-t-yellow-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(202 138 4 / var(--tw-border-opacity));
}

.border-t-yellow-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(161 98 7 / var(--tw-border-opacity));
}

.border-t-yellow-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(133 77 14 / var(--tw-border-opacity));
}

.border-t-yellow-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(113 63 18 / var(--tw-border-opacity));
}

.border-t-yellow-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(66 32 6 / var(--tw-border-opacity));
}

.border-t-zinc-100 {
  --tw-border-opacity: 1;
  border-top-color: rgb(244 244 245 / var(--tw-border-opacity));
}

.border-t-zinc-200 {
  --tw-border-opacity: 1;
  border-top-color: rgb(228 228 231 / var(--tw-border-opacity));
}

.border-t-zinc-300 {
  --tw-border-opacity: 1;
  border-top-color: rgb(212 212 216 / var(--tw-border-opacity));
}

.border-t-zinc-400 {
  --tw-border-opacity: 1;
  border-top-color: rgb(161 161 170 / var(--tw-border-opacity));
}

.border-t-zinc-50 {
  --tw-border-opacity: 1;
  border-top-color: rgb(250 250 250 / var(--tw-border-opacity));
}

.border-t-zinc-500 {
  --tw-border-opacity: 1;
  border-top-color: rgb(113 113 122 / var(--tw-border-opacity));
}

.border-t-zinc-600 {
  --tw-border-opacity: 1;
  border-top-color: rgb(82 82 91 / var(--tw-border-opacity));
}

.border-t-zinc-700 {
  --tw-border-opacity: 1;
  border-top-color: rgb(63 63 70 / var(--tw-border-opacity));
}

.border-t-zinc-800 {
  --tw-border-opacity: 1;
  border-top-color: rgb(39 39 42 / var(--tw-border-opacity));
}

.border-t-zinc-900 {
  --tw-border-opacity: 1;
  border-top-color: rgb(24 24 27 / var(--tw-border-opacity));
}

.border-t-zinc-950 {
  --tw-border-opacity: 1;
  border-top-color: rgb(9 9 11 / var(--tw-border-opacity));
}

.bg-amber-100 {
  --tw-bg-opacity: 1;
  background-color: rgb(254 243 199 / var(--tw-bg-opacity));
}

.bg-amber-200 {
  --tw-bg-opacity: 1;
  background-color: rgb(253 230 138 / var(--tw-bg-opacity));
}

.bg-amber-300 {
  --tw-bg-opacity: 1;
  background-color: rgb(252 211 77 / var(--tw-bg-opacity));
}

.bg-amber-400 {
  --tw-bg-opacity: 1;
  background-color: rgb(251 191 36 / var(--tw-bg-opacity));
}

.bg-amber-50 {
  --tw-bg-opacity: 1;
  background-color: rgb(255 251 235 / var(--tw-bg-opacity));
}

.bg-amber-500 {
  --tw-bg-opacity: 1;
  background-color: rgb(245 158 11 / var(--tw-bg-opacity));
}

.bg-amber-600 {
  --tw-bg-opacity: 1;
  background-color: rgb(217 119 6 / var(--tw-bg-opacity));
}

.bg-amber-700 {
  --tw-bg-opacity: 1;
  background-color: rgb(180 83 9 / var(--tw-bg-opacity));
}

.bg-amber-800 {
  --tw-bg-opacity: 1;
  background-color: rgb(146 64 14 / var(--tw-bg-opacity));
}

.bg-amber-900 {
  --tw-bg-opacity: 1;
  background-color: rgb(120 53 15 / var(--tw-bg-opacity));
}

.bg-amber-950 {
  --tw-bg-opacity: 1;
  background-color: rgb(69 26 3 / var(--tw-bg-opacity));
}

.bg-black {
  --tw-bg-opacity: 1;
  background-color: rgb(0 0 0 / var(--tw-bg-opacity));
}

.bg-blue-100 {
  --tw-bg-opacity: 1;
  background-color: rgb(219 234 254 / var(--tw-bg-opacity));
}

.bg-blue-200 {
  --tw-bg-opacity: 1;
  background-color: rgb(191 219 254 / var(--tw-bg-opacity));
}

.bg-blue-300 {
  --tw-bg-opacity: 1;
  background-color: rgb(147 197 253 / var(--tw-bg-opacity));
}

.bg-blue-400 {
  --tw-bg-opacity: 1;
  background-color: rgb(96 165 250 / var(--tw-bg-opacity));
}

.bg-blue-50 {
  --tw-bg-opacity: 1;
  background-color: rgb(239 246 255 / var(--tw-bg-opacity));
}

.bg-blue-500 {
  --tw-bg-opacity: 1;
  background-color: rgb(59 130 246 / var(--tw-bg-opacity));
}

.bg-blue-600 {
  --tw-bg-opacity: 1;
  background-color: rgb(37 99 235 / var(--tw-bg-opacity));
}

.bg-blue-700 {
  --tw-bg-opacity: 1;
  background-color: rgb(29 78 216 / var(--tw-bg-opacity));
}

.bg-blue-800 {
  --tw-bg-opacity: 1;
  background-color: rgb(30 64 175 / var(--tw-bg-opacity));
}

.bg-blue-900 {
  --tw-bg-opacity: 1;
  background-color: rgb(30 58 138 / var(--tw-bg-opacity));
}

.bg-blue-950 {
  --tw-bg-opacity: 1;
  background-color: rgb(23 37 84 / var(--tw-bg-opacity));
}

.bg-current {
  background-color: currentColor;
}

.bg-cyan-100 {
  --tw-bg-opacity: 1;
  background-color: rgb(207 250 254 / var(--tw-bg-opacity));
}

.bg-cyan-200 {
  --tw-bg-opacity: 1;
  background-color: rgb(165 243 252 / var(--tw-bg-opacity));
}

.bg-cyan-300 {
  --tw-bg-opacity: 1;
  background-color: rgb(103 232 249 / var(--tw-bg-opacity));
}

.bg-cyan-400 {
  --tw-bg-opacity: 1;
  background-color: rgb(34 211 238 / var(--tw-bg-opacity));
}

.bg-cyan-50 {
  --tw-bg-opacity: 1;
  background-color: rgb(236 254 255 / var(--tw-bg-opacity));
}

.bg-cyan-500 {
  --tw-bg-opacity: 1;
  background-color: rgb(6 182 212 / var(--tw-bg-opacity));
}

.bg-cyan-600 {
  --tw-bg-opacity: 1;
  background-color: rgb(8 145 178 / var(--tw-bg-opacity));
}

.bg-cyan-700 {
  --tw-bg-opacity: 1;
  background-color: rgb(14 116 144 / var(--tw-bg-opacity));
}

.bg-cyan-800 {
  --tw-bg-opacity: 1;
  background-color: rgb(21 94 117 / var(--tw-bg-opacity));
}

.bg-cyan-900 {
  --tw-bg-opacity: 1;
  background-color: rgb(22 78 99 / var(--tw-bg-opacity));
}

.bg-cyan-950 {
  --tw-bg-opacity: 1;
  background-color: rgb(8 51 68 / var(--tw-bg-opacity));
}

.bg-emerald-100 {
  --tw-bg-opacity: 1;
  background-color: rgb(209 250 229 / var(--tw-bg-opacity));
}

.bg-emerald-200 {
  --tw-bg-opacity: 1;
  background-color: rgb(167 243 208 / var(--tw-bg-opacity));
}

.bg-emerald-300 {
  --tw-bg-opacity: 1;
  background-color: rgb(110 231 183 / var(--tw-bg-opacity));
}

.bg-emerald-400 {
  --tw-bg-opacity: 1;
  background-color: rgb(52 211 153 / var(--tw-bg-opacity));
}

.bg-emerald-50 {
  --tw-bg-opacity: 1;
  background-color: rgb(236 253 245 / var(--tw-bg-opacity));
}

.bg-emerald-500 {
  --tw-bg-opacity: 1;
  background-color: rgb(16 185 129 / var(--tw-bg-opacity));
}

.bg-emerald-600 {
  --tw-bg-opacity: 1;
  background-color: rgb(5 150 105 / var(--tw-bg-opacity));
}

.bg-emerald-700 {
  --tw-bg-opacity: 1;
  background-color: rgb(4 120 87 / var(--tw-bg-opacity));
}

.bg-emerald-800 {
  --tw-bg-opacity: 1;
  background-color: rgb(6 95 70 / var(--tw-bg-opacity));
}

.bg-emerald-900 {
  --tw-bg-opacity: 1;
  background-color: rgb(6 78 59 / var(--tw-bg-opacity));
}

.bg-emerald-950 {
  --tw-bg-opacity: 1;
  background-color: rgb(2 44 34 / var(--tw-bg-opacity));
}

.bg-fuchsia-100 {
  --tw-bg-opacity: 1;
  background-color: rgb(250 232 255 / var(--tw-bg-opacity));
}

.bg-fuchsia-200 {
  --tw-bg-opacity: 1;
  background-color: rgb(245 208 254 / var(--tw-bg-opacity));
}

.bg-fuchsia-300 {
  --tw-bg-opacity: 1;
  background-color: rgb(240 171 252 / var(--tw-bg-opacity));
}

.bg-fuchsia-400 {
  --tw-bg-opacity: 1;
  background-color: rgb(232 121 249 / var(--tw-bg-opacity));
}

.bg-fuchsia-50 {
  --tw-bg-opacity: 1;
  background-color: rgb(253 244 255 / var(--tw-bg-opacity));
}

.bg-fuchsia-500 {
  --tw-bg-opacity: 1;
  background-color: rgb(217 70 239 / var(--tw-bg-opacity));
}

.bg-fuchsia-600 {
  --tw-bg-opacity: 1;
  background-color: rgb(192 38 211 / var(--tw-bg-opacity));
}

.bg-fuchsia-700 {
  --tw-bg-opacity: 1;
  background-color: rgb(162 28 175 / var(--tw-bg-opacity));
}

.bg-fuchsia-800 {
  --tw-bg-opacity: 1;
  background-color: rgb(134 25 143 / var(--tw-bg-opacity));
}

.bg-fuchsia-900 {
  --tw-bg-opacity: 1;
  background-color: rgb(112 26 117 / var(--tw-bg-opacity));
}

.bg-fuchsia-950 {
  --tw-bg-opacity: 1;
  background-color: rgb(74 4 78 / var(--tw-bg-opacity));
}

.bg-gray-100 {
  --tw-bg-opacity: 1;
  background-color: rgb(243 244 246 / var(--tw-bg-opacity));
}

.bg-gray-200 {
  --tw-bg-opacity: 1;
  background-color: rgb(229 231 235 / var(--tw-bg-opacity));
}

.bg-gray-300 {
  --tw-bg-opacity: 1;
  background-color: rgb(209 213 219 / var(--tw-bg-opacity));
}

.bg-gray-400 {
  --tw-bg-opacity: 1;
  background-color: rgb(156 163 175 / var(--tw-bg-opacity));
}

.bg-gray-50 {
  --tw-bg-opacity: 1;
  background-color: rgb(249 250 251 / var(--tw-bg-opacity));
}

.bg-gray-500 {
  --tw-bg-opacity: 1;
  background-color: rgb(107 114 128 / var(--tw-bg-opacity));
}

.bg-gray-600 {
  --tw-bg-opacity: 1;
  background-color: rgb(75 85 99 / var(--tw-bg-opacity));
}

.bg-gray-700 {
  --tw-bg-opacity: 1;
  background-color: rgb(55 65 81 / var(--tw-bg-opacity));
}

.bg-gray-800 {
  --tw-bg-opacity: 1;
  background-color: rgb(31 41 55 / var(--tw-bg-opacity));
}

.bg-gray-900 {
  --tw-bg-opacity: 1;
  background-color: rgb(17 24 39 / var(--tw-bg-opacity));
}

.bg-gray-950 {
  --tw-bg-opacity: 1;
  background-color: rgb(3 7 18 / var(--tw-bg-opacity));
}

.bg-green-100 {
  --tw-bg-opacity: 1;
  background-color: rgb(220 252 231 / var(--tw-bg-opacity));
}

.bg-green-200 {
  --tw-bg-opacity: 1;
  background-color: rgb(187 247 208 / var(--tw-bg-opacity));
}

.bg-green-300 {
  --tw-bg-opacity: 1;
  background-color: rgb(134 239 172 / var(--tw-bg-opacity));
}

.bg-green-400 {
  --tw-bg-opacity: 1;
  background-color: rgb(74 222 128 / var(--tw-bg-opacity));
}

.bg-green-50 {
  --tw-bg-opacity: 1;
  background-color: rgb(240 253 244 / var(--tw-bg-opacity));
}

.bg-green-500 {
  --tw-bg-opacity: 1;
  background-color: rgb(34 197 94 / var(--tw-bg-opacity));
}

.bg-green-600 {
  --tw-bg-opacity: 1;
  background-color: rgb(22 163 74 / var(--tw-bg-opacity));
}

.bg-green-700 {
  --tw-bg-opacity: 1;
  background-color: rgb(21 128 61 / var(--tw-bg-opacity));
}

.bg-green-800 {
  --tw-bg-opacity: 1;
  background-color: rgb(22 101 52 / var(--tw-bg-opacity));
}

.bg-green-900 {
  --tw-bg-opacity: 1;
  background-color: rgb(20 83 45 / var(--tw-bg-opacity));
}

.bg-green-950 {
  --tw-bg-opacity: 1;
  background-color: rgb(5 46 22 / var(--tw-bg-opacity));
}

.bg-indigo-100 {
  --tw-bg-opacity: 1;
  background-color: rgb(224 231 255 / var(--tw-bg-opacity));
}

.bg-indigo-200 {
  --tw-bg-opacity: 1;
  background-color: rgb(199 210 254 / var(--tw-bg-opacity));
}

.bg-indigo-300 {
  --tw-bg-opacity: 1;
  background-color: rgb(165 180 252 / var(--tw-bg-opacity));
}

.bg-indigo-400 {
  --tw-bg-opacity: 1;
  background-color: rgb(129 140 248 / var(--tw-bg-opacity));
}

.bg-indigo-50 {
  --tw-bg-opacity: 1;
  background-color: rgb(238 242 255 / var(--tw-bg-opacity));
}

.bg-indigo-500 {
  --tw-bg-opacity: 1;
  background-color: rgb(99 102 241 / var(--tw-bg-opacity));
}

.bg-indigo-600 {
  --tw-bg-opacity: 1;
  background-color: rgb(79 70 229 / var(--tw-bg-opacity));
}

.bg-indigo-700 {
  --tw-bg-opacity: 1;
  background-color: rgb(67 56 202 / var(--tw-bg-opacity));
}

.bg-indigo-800 {
  --tw-bg-opacity: 1;
  background-color: rgb(55 48 163 / var(--tw-bg-opacity));
}

.bg-indigo-900 {
  --tw-bg-opacity: 1;
  background-color: rgb(49 46 129 / var(--tw-bg-opacity));
}

.bg-indigo-950 {
  --tw-bg-opacity: 1;
  background-color: rgb(30 27 75 / var(--tw-bg-opacity));
}

.bg-inherit {
  background-color: inherit;
}

.bg-lime-100 {
  --tw-bg-opacity: 1;
  background-color: rgb(236 252 203 / var(--tw-bg-opacity));
}

.bg-lime-200 {
  --tw-bg-opacity: 1;
  background-color: rgb(217 249 157 / var(--tw-bg-opacity));
}

.bg-lime-300 {
  --tw-bg-opacity: 1;
  background-color: rgb(190 242 100 / var(--tw-bg-opacity));
}

.bg-lime-400 {
  --tw-bg-opacity: 1;
  background-color: rgb(163 230 53 / var(--tw-bg-opacity));
}

.bg-lime-50 {
  --tw-bg-opacity: 1;
  background-color: rgb(247 254 231 / var(--tw-bg-opacity));
}

.bg-lime-500 {
  --tw-bg-opacity: 1;
  background-color: rgb(132 204 22 / var(--tw-bg-opacity));
}

.bg-lime-600 {
  --tw-bg-opacity: 1;
  background-color: rgb(101 163 13 / var(--tw-bg-opacity));
}

.bg-lime-700 {
  --tw-bg-opacity: 1;
  background-color: rgb(77 124 15 / var(--tw-bg-opacity));
}

.bg-lime-800 {
  --tw-bg-opacity: 1;
  background-color: rgb(63 98 18 / var(--tw-bg-opacity));
}

.bg-lime-900 {
  --tw-bg-opacity: 1;
  background-color: rgb(54 83 20 / var(--tw-bg-opacity));
}

.bg-lime-950 {
  --tw-bg-opacity: 1;
  background-color: rgb(26 46 5 / var(--tw-bg-opacity));
}

.bg-neutral-100 {
  --tw-bg-opacity: 1;
  background-color: rgb(245 245 245 / var(--tw-bg-opacity));
}

.bg-neutral-200 {
  --tw-bg-opacity: 1;
  background-color: rgb(229 229 229 / var(--tw-bg-opacity));
}

.bg-neutral-300 {
  --tw-bg-opacity: 1;
  background-color: rgb(212 212 212 / var(--tw-bg-opacity));
}

.bg-neutral-400 {
  --tw-bg-opacity: 1;
  background-color: rgb(163 163 163 / var(--tw-bg-opacity));
}

.bg-neutral-50 {
  --tw-bg-opacity: 1;
  background-color: rgb(250 250 250 / var(--tw-bg-opacity));
}

.bg-neutral-500 {
  --tw-bg-opacity: 1;
  background-color: rgb(115 115 115 / var(--tw-bg-opacity));
}

.bg-neutral-600 {
  --tw-bg-opacity: 1;
  background-color: rgb(82 82 82 / var(--tw-bg-opacity));
}

.bg-neutral-700 {
  --tw-bg-opacity: 1;
  background-color: rgb(64 64 64 / var(--tw-bg-opacity));
}

.bg-neutral-800 {
  --tw-bg-opacity: 1;
  background-color: rgb(38 38 38 / var(--tw-bg-opacity));
}

.bg-neutral-900 {
  --tw-bg-opacity: 1;
  background-color: rgb(23 23 23 / var(--tw-bg-opacity));
}

.bg-neutral-950 {
  --tw-bg-opacity: 1;
  background-color: rgb(10 10 10 / var(--tw-bg-opacity));
}

.bg-orange-100 {
  --tw-bg-opacity: 1;
  background-color: rgb(255 237 213 / var(--tw-bg-opacity));
}

.bg-orange-200 {
  --tw-bg-opacity: 1;
  background-color: rgb(254 215 170 / var(--tw-bg-opacity));
}

.bg-orange-300 {
  --tw-bg-opacity: 1;
  background-color: rgb(253 186 116 / var(--tw-bg-opacity));
}

.bg-orange-400 {
  --tw-bg-opacity: 1;
  background-color: rgb(251 146 60 / var(--tw-bg-opacity));
}

.bg-orange-50 {
  --tw-bg-opacity: 1;
  background-color: rgb(255 247 237 / var(--tw-bg-opacity));
}

.bg-orange-500 {
  --tw-bg-opacity: 1;
  background-color: rgb(249 115 22 / var(--tw-bg-opacity));
}

.bg-orange-600 {
  --tw-bg-opacity: 1;
  background-color: rgb(234 88 12 / var(--tw-bg-opacity));
}

.bg-orange-700 {
  --tw-bg-opacity: 1;
  background-color: rgb(194 65 12 / var(--tw-bg-opacity));
}

.bg-orange-800 {
  --tw-bg-opacity: 1;
  background-color: rgb(154 52 18 / var(--tw-bg-opacity));
}

.bg-orange-900 {
  --tw-bg-opacity: 1;
  background-color: rgb(124 45 18 / var(--tw-bg-opacity));
}

.bg-orange-950 {
  --tw-bg-opacity: 1;
  background-color: rgb(67 20 7 / var(--tw-bg-opacity));
}

.bg-pink-100 {
  --tw-bg-opacity: 1;
  background-color: rgb(252 231 243 / var(--tw-bg-opacity));
}

.bg-pink-200 {
  --tw-bg-opacity: 1;
  background-color: rgb(251 207 232 / var(--tw-bg-opacity));
}

.bg-pink-300 {
  --tw-bg-opacity: 1;
  background-color: rgb(249 168 212 / var(--tw-bg-opacity));
}

.bg-pink-400 {
  --tw-bg-opacity: 1;
  background-color: rgb(244 114 182 / var(--tw-bg-opacity));
}

.bg-pink-50 {
  --tw-bg-opacity: 1;
  background-color: rgb(253 242 248 / var(--tw-bg-opacity));
}

.bg-pink-500 {
  --tw-bg-opacity: 1;
  background-color: rgb(236 72 153 / var(--tw-bg-opacity));
}

.bg-pink-600 {
  --tw-bg-opacity: 1;
  background-color: rgb(219 39 119 / var(--tw-bg-opacity));
}

.bg-pink-700 {
  --tw-bg-opacity: 1;
  background-color: rgb(190 24 93 / var(--tw-bg-opacity));
}

.bg-pink-800 {
  --tw-bg-opacity: 1;
  background-color: rgb(157 23 77 / var(--tw-bg-opacity));
}

.bg-pink-900 {
  --tw-bg-opacity: 1;
  background-color: rgb(131 24 67 / var(--tw-bg-opacity));
}

.bg-pink-950 {
  --tw-bg-opacity: 1;
  background-color: rgb(80 7 36 / var(--tw-bg-opacity));
}

.bg-purple-100 {
  --tw-bg-opacity: 1;
  background-color: rgb(243 232 255 / var(--tw-bg-opacity));
}

.bg-purple-200 {
  --tw-bg-opacity: 1;
  background-color: rgb(233 213 255 / var(--tw-bg-opacity));
}

.bg-purple-300 {
  --tw-bg-opacity: 1;
  background-color: rgb(216 180 254 / var(--tw-bg-opacity));
}

.bg-purple-400 {
  --tw-bg-opacity: 1;
  background-color: rgb(192 132 252 / var(--tw-bg-opacity));
}

.bg-purple-50 {
  --tw-bg-opacity: 1;
  background-color: rgb(250 245 255 / var(--tw-bg-opacity));
}

.bg-purple-500 {
  --tw-bg-opacity: 1;
  background-color: rgb(168 85 247 / var(--tw-bg-opacity));
}

.bg-purple-600 {
  --tw-bg-opacity: 1;
  background-color: rgb(147 51 234 / var(--tw-bg-opacity));
}

.bg-purple-700 {
  --tw-bg-opacity: 1;
  background-color: rgb(126 34 206 / var(--tw-bg-opacity));
}

.bg-purple-800 {
  --tw-bg-opacity: 1;
  background-color: rgb(107 33 168 / var(--tw-bg-opacity));
}

.bg-purple-900 {
  --tw-bg-opacity: 1;
  background-color: rgb(88 28 135 / var(--tw-bg-opacity));
}

.bg-purple-950 {
  --tw-bg-opacity: 1;
  background-color: rgb(59 7 100 / var(--tw-bg-opacity));
}

.bg-red-100 {
  --tw-bg-opacity: 1;
  background-color: rgb(254 226 226 / var(--tw-bg-opacity));
}

.bg-red-200 {
  --tw-bg-opacity: 1;
  background-color: rgb(254 202 202 / var(--tw-bg-opacity));
}

.bg-red-300 {
  --tw-bg-opacity: 1;
  background-color: rgb(252 165 165 / var(--tw-bg-opacity));
}

.bg-red-400 {
  --tw-bg-opacity: 1;
  background-color: rgb(248 113 113 / var(--tw-bg-opacity));
}

.bg-red-50 {
  --tw-bg-opacity: 1;
  background-color: rgb(254 242 242 / var(--tw-bg-opacity));
}

.bg-red-500 {
  --tw-bg-opacity: 1;
  background-color: rgb(239 68 68 / var(--tw-bg-opacity));
}

.bg-red-600 {
  --tw-bg-opacity: 1;
  background-color: rgb(220 38 38 / var(--tw-bg-opacity));
}

.bg-red-700 {
  --tw-bg-opacity: 1;
  background-color: rgb(185 28 28 / var(--tw-bg-opacity));
}

.bg-red-800 {
  --tw-bg-opacity: 1;
  background-color: rgb(153 27 27 / var(--tw-bg-opacity));
}

.bg-red-900 {
  --tw-bg-opacity: 1;
  background-color: rgb(127 29 29 / var(--tw-bg-opacity));
}

.bg-red-950 {
  --tw-bg-opacity: 1;
  background-color: rgb(69 10 10 / var(--tw-bg-opacity));
}

.bg-rose-100 {
  --tw-bg-opacity: 1;
  background-color: rgb(255 228 230 / var(--tw-bg-opacity));
}

.bg-rose-200 {
  --tw-bg-opacity: 1;
  background-color: rgb(254 205 211 / var(--tw-bg-opacity));
}

.bg-rose-300 {
  --tw-bg-opacity: 1;
  background-color: rgb(253 164 175 / var(--tw-bg-opacity));
}

.bg-rose-400 {
  --tw-bg-opacity: 1;
  background-color: rgb(251 113 133 / var(--tw-bg-opacity));
}

.bg-rose-50 {
  --tw-bg-opacity: 1;
  background-color: rgb(255 241 242 / var(--tw-bg-opacity));
}

.bg-rose-500 {
  --tw-bg-opacity: 1;
  background-color: rgb(244 63 94 / var(--tw-bg-opacity));
}

.bg-rose-600 {
  --tw-bg-opacity: 1;
  background-color: rgb(225 29 72 / var(--tw-bg-opacity));
}

.bg-rose-700 {
  --tw-bg-opacity: 1;
  background-color: rgb(190 18 60 / var(--tw-bg-opacity));
}

.bg-rose-800 {
  --tw-bg-opacity: 1;
  background-color: rgb(159 18 57 / var(--tw-bg-opacity));
}

.bg-rose-900 {
  --tw-bg-opacity: 1;
  background-color: rgb(136 19 55 / var(--tw-bg-opacity));
}

.bg-rose-950 {
  --tw-bg-opacity: 1;
  background-color: rgb(76 5 25 / var(--tw-bg-opacity));
}

.bg-sky-100 {
  --tw-bg-opacity: 1;
  background-color: rgb(224 242 254 / var(--tw-bg-opacity));
}

.bg-sky-200 {
  --tw-bg-opacity: 1;
  background-color: rgb(186 230 253 / var(--tw-bg-opacity));
}

.bg-sky-300 {
  --tw-bg-opacity: 1;
  background-color: rgb(125 211 252 / var(--tw-bg-opacity));
}

.bg-sky-400 {
  --tw-bg-opacity: 1;
  background-color: rgb(56 189 248 / var(--tw-bg-opacity));
}

.bg-sky-50 {
  --tw-bg-opacity: 1;
  background-color: rgb(240 249 255 / var(--tw-bg-opacity));
}

.bg-sky-500 {
  --tw-bg-opacity: 1;
  background-color: rgb(14 165 233 / var(--tw-bg-opacity));
}

.bg-sky-600 {
  --tw-bg-opacity: 1;
  background-color: rgb(2 132 199 / var(--tw-bg-opacity));
}

.bg-sky-700 {
  --tw-bg-opacity: 1;
  background-color: rgb(3 105 161 / var(--tw-bg-opacity));
}

.bg-sky-800 {
  --tw-bg-opacity: 1;
  background-color: rgb(7 89 133 / var(--tw-bg-opacity));
}

.bg-sky-900 {
  --tw-bg-opacity: 1;
  background-color: rgb(12 74 110 / var(--tw-bg-opacity));
}

.bg-sky-950 {
  --tw-bg-opacity: 1;
  background-color: rgb(8 47 73 / var(--tw-bg-opacity));
}

.bg-slate-100 {
  --tw-bg-opacity: 1;
  background-color: rgb(241 245 249 / var(--tw-bg-opacity));
}

.bg-slate-200 {
  --tw-bg-opacity: 1;
  background-color: rgb(226 232 240 / var(--tw-bg-opacity));
}

.bg-slate-300 {
  --tw-bg-opacity: 1;
  background-color: rgb(203 213 225 / var(--tw-bg-opacity));
}

.bg-slate-400 {
  --tw-bg-opacity: 1;
  background-color: rgb(148 163 184 / var(--tw-bg-opacity));
}

.bg-slate-50 {
  --tw-bg-opacity: 1;
  background-color: rgb(248 250 252 / var(--tw-bg-opacity));
}

.bg-slate-500 {
  --tw-bg-opacity: 1;
  background-color: rgb(100 116 139 / var(--tw-bg-opacity));
}

.bg-slate-600 {
  --tw-bg-opacity: 1;
  background-color: rgb(71 85 105 / var(--tw-bg-opacity));
}

.bg-slate-700 {
  --tw-bg-opacity: 1;
  background-color: rgb(51 65 85 / var(--tw-bg-opacity));
}

.bg-slate-800 {
  --tw-bg-opacity: 1;
  background-color: rgb(30 41 59 / var(--tw-bg-opacity));
}

.bg-slate-900 {
  --tw-bg-opacity: 1;
  background-color: rgb(15 23 42 / var(--tw-bg-opacity));
}

.bg-slate-950 {
  --tw-bg-opacity: 1;
  background-color: rgb(2 6 23 / var(--tw-bg-opacity));
}

.bg-stone-100 {
  --tw-bg-opacity: 1;
  background-color: rgb(245 245 244 / var(--tw-bg-opacity));
}

.bg-stone-200 {
  --tw-bg-opacity: 1;
  background-color: rgb(231 229 228 / var(--tw-bg-opacity));
}

.bg-stone-300 {
  --tw-bg-opacity: 1;
  background-color: rgb(214 211 209 / var(--tw-bg-opacity));
}

.bg-stone-400 {
  --tw-bg-opacity: 1;
  background-color: rgb(168 162 158 / var(--tw-bg-opacity));
}

.bg-stone-50 {
  --tw-bg-opacity: 1;
  background-color: rgb(250 250 249 / var(--tw-bg-opacity));
}

.bg-stone-500 {
  --tw-bg-opacity: 1;
  background-color: rgb(120 113 108 / var(--tw-bg-opacity));
}

.bg-stone-600 {
  --tw-bg-opacity: 1;
  background-color: rgb(87 83 78 / var(--tw-bg-opacity));
}

.bg-stone-700 {
  --tw-bg-opacity: 1;
  background-color: rgb(68 64 60 / var(--tw-bg-opacity));
}

.bg-stone-800 {
  --tw-bg-opacity: 1;
  background-color: rgb(41 37 36 / var(--tw-bg-opacity));
}

.bg-stone-900 {
  --tw-bg-opacity: 1;
  background-color: rgb(28 25 23 / var(--tw-bg-opacity));
}

.bg-stone-950 {
  --tw-bg-opacity: 1;
  background-color: rgb(12 10 9 / var(--tw-bg-opacity));
}

.bg-teal-100 {
  --tw-bg-opacity: 1;
  background-color: rgb(204 251 241 / var(--tw-bg-opacity));
}

.bg-teal-200 {
  --tw-bg-opacity: 1;
  background-color: rgb(153 246 228 / var(--tw-bg-opacity));
}

.bg-teal-300 {
  --tw-bg-opacity: 1;
  background-color: rgb(94 234 212 / var(--tw-bg-opacity));
}

.bg-teal-400 {
  --tw-bg-opacity: 1;
  background-color: rgb(45 212 191 / var(--tw-bg-opacity));
}

.bg-teal-50 {
  --tw-bg-opacity: 1;
  background-color: rgb(240 253 250 / var(--tw-bg-opacity));
}

.bg-teal-500 {
  --tw-bg-opacity: 1;
  background-color: rgb(20 184 166 / var(--tw-bg-opacity));
}

.bg-teal-600 {
  --tw-bg-opacity: 1;
  background-color: rgb(13 148 136 / var(--tw-bg-opacity));
}

.bg-teal-700 {
  --tw-bg-opacity: 1;
  background-color: rgb(15 118 110 / var(--tw-bg-opacity));
}

.bg-teal-800 {
  --tw-bg-opacity: 1;
  background-color: rgb(17 94 89 / var(--tw-bg-opacity));
}

.bg-teal-900 {
  --tw-bg-opacity: 1;
  background-color: rgb(19 78 74 / var(--tw-bg-opacity));
}

.bg-teal-950 {
  --tw-bg-opacity: 1;
  background-color: rgb(4 47 46 / var(--tw-bg-opacity));
}

.bg-transparent {
  background-color: transparent;
}

.bg-violet-100 {
  --tw-bg-opacity: 1;
  background-color: rgb(237 233 254 / var(--tw-bg-opacity));
}

.bg-violet-200 {
  --tw-bg-opacity: 1;
  background-color: rgb(221 214 254 / var(--tw-bg-opacity));
}

.bg-violet-300 {
  --tw-bg-opacity: 1;
  background-color: rgb(196 181 253 / var(--tw-bg-opacity));
}

.bg-violet-400 {
  --tw-bg-opacity: 1;
  background-color: rgb(167 139 250 / var(--tw-bg-opacity));
}

.bg-violet-50 {
  --tw-bg-opacity: 1;
  background-color: rgb(245 243 255 / var(--tw-bg-opacity));
}

.bg-violet-500 {
  --tw-bg-opacity: 1;
  background-color: rgb(139 92 246 / var(--tw-bg-opacity));
}

.bg-violet-600 {
  --tw-bg-opacity: 1;
  background-color: rgb(124 58 237 / var(--tw-bg-opacity));
}

.bg-violet-700 {
  --tw-bg-opacity: 1;
  background-color: rgb(109 40 217 / var(--tw-bg-opacity));
}

.bg-violet-800 {
  --tw-bg-opacity: 1;
  background-color: rgb(91 33 182 / var(--tw-bg-opacity));
}

.bg-violet-900 {
  --tw-bg-opacity: 1;
  background-color: rgb(76 29 149 / var(--tw-bg-opacity));
}

.bg-violet-950 {
  --tw-bg-opacity: 1;
  background-color: rgb(46 16 101 / var(--tw-bg-opacity));
}

.bg-white {
  --tw-bg-opacity: 1;
  background-color: rgb(255 255 255 / var(--tw-bg-opacity));
}

.bg-yellow-100 {
  --tw-bg-opacity: 1;
  background-color: rgb(254 249 195 / var(--tw-bg-opacity));
}

.bg-yellow-200 {
  --tw-bg-opacity: 1;
  background-color: rgb(254 240 138 / var(--tw-bg-opacity));
}

.bg-yellow-300 {
  --tw-bg-opacity: 1;
  background-color: rgb(253 224 71 / var(--tw-bg-opacity));
}

.bg-yellow-400 {
  --tw-bg-opacity: 1;
  background-color: rgb(250 204 21 / var(--tw-bg-opacity));
}

.bg-yellow-50 {
  --tw-bg-opacity: 1;
  background-color: rgb(254 252 232 / var(--tw-bg-opacity));
}

.bg-yellow-500 {
  --tw-bg-opacity: 1;
  background-color: rgb(234 179 8 / var(--tw-bg-opacity));
}

.bg-yellow-600 {
  --tw-bg-opacity: 1;
  background-color: rgb(202 138 4 / var(--tw-bg-opacity));
}

.bg-yellow-700 {
  --tw-bg-opacity: 1;
  background-color: rgb(161 98 7 / var(--tw-bg-opacity));
}

.bg-yellow-800 {
  --tw-bg-opacity: 1;
  background-color: rgb(133 77 14 / var(--tw-bg-opacity));
}

.bg-yellow-900 {
  --tw-bg-opacity: 1;
  background-color: rgb(113 63 18 / var(--tw-bg-opacity));
}

.bg-yellow-950 {
  --tw-bg-opacity: 1;
  background-color: rgb(66 32 6 / var(--tw-bg-opacity));
}

.bg-zinc-100 {
  --tw-bg-opacity: 1;
  background-color: rgb(244 244 245 / var(--tw-bg-opacity));
}

.bg-zinc-200 {
  --tw-bg-opacity: 1;
  background-color: rgb(228 228 231 / var(--tw-bg-opacity));
}

.bg-zinc-300 {
  --tw-bg-opacity: 1;
  background-color: rgb(212 212 216 / var(--tw-bg-opacity));
}

.bg-zinc-400 {
  --tw-bg-opacity: 1;
  background-color: rgb(161 161 170 / var(--tw-bg-opacity));
}

.bg-zinc-50 {
  --tw-bg-opacity: 1;
  background-color: rgb(250 250 250 / var(--tw-bg-opacity));
}

.bg-zinc-500 {
  --tw-bg-opacity: 1;
  background-color: rgb(113 113 122 / var(--tw-bg-opacity));
}

.bg-zinc-600 {
  --tw-bg-opacity: 1;
  background-color: rgb(82 82 91 / var(--tw-bg-opacity));
}

.bg-zinc-700 {
  --tw-bg-opacity: 1;
  background-color: rgb(63 63 70 / var(--tw-bg-opacity));
}

.bg-zinc-800 {
  --tw-bg-opacity: 1;
  background-color: rgb(39 39 42 / var(--tw-bg-opacity));
}

.bg-zinc-900 {
  --tw-bg-opacity: 1;
  background-color: rgb(24 24 27 / var(--tw-bg-opacity));
}

.bg-zinc-950 {
  --tw-bg-opacity: 1;
  background-color: rgb(9 9 11 / var(--tw-bg-opacity));
}

.bg-gradient-to-b {
  background-image: linear-gradient(to bottom, var(--tw-gradient-stops));
}

.bg-gradient-to-bl {
  background-image: linear-gradient(to bottom left, var(--tw-gradient-stops));
}

.bg-gradient-to-br {
  background-image: linear-gradient(to bottom right, var(--tw-gradient-stops));
}

.bg-gradient-to-l {
  background-image: linear-gradient(to left, var(--tw-gradient-stops));
}

.bg-gradient-to-r {
  background-image: linear-gradient(to right, var(--tw-gradient-stops));
}

.bg-gradient-to-t {
  background-image: linear-gradient(to top, var(--tw-gradient-stops));
}

.bg-gradient-to-tl {
  background-image: linear-gradient(to top left, var(--tw-gradient-stops));
}

.bg-gradient-to-tr {
  background-image: linear-gradient(to top right, var(--tw-gradient-stops));
}

.bg-none {
  background-image: none;
}

.from-black {
  --tw-gradient-from: #000 var(--tw-gradient-from-position);
  --tw-gradient-to: rgb(0 0 0 / 0) var(--tw-gradient-to-position);
  --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
}

.from-current {
  --tw-gradient-from: currentColor var(--tw-gradient-from-position);
  --tw-gradient-to: rgb(255 255 255 / 0) var(--tw-gradient-to-position);
  --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
}

.from-inherit {
  --tw-gradient-from: inherit var(--tw-gradient-from-position);
  --tw-gradient-to: rgb(255 255 255 / 0) var(--tw-gradient-to-position);
  --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
}

.from-transparent {
  --tw-gradient-from: transparent var(--tw-gradient-from-position);
  --tw-gradient-to: rgb(0 0 0 / 0) var(--tw-gradient-to-position);
  --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
}

.box-decoration-slice {
  -webkit-box-decoration-break: slice;
          box-decoration-break: slice;
}

.box-decoration-clone {
  -webkit-box-decoration-break: clone;
          box-decoration-break: clone;
}

.bg-auto {
  background-size: auto;
}

.bg-contain {
  background-size: contain;
}

.bg-cover {
  background-size: cover;
}

.bg-fixed {
  background-attachment: fixed;
}

.bg-local {
  background-attachment: local;
}

.bg-scroll {
  background-attachment: scroll;
}

.bg-clip-border {
  background-clip: border-box;
}

.bg-clip-padding {
  background-clip: padding-box;
}

.bg-clip-content {
  background-clip: content-box;
}

.bg-clip-text {
  -webkit-background-clip: text;
          background-clip: text;
}

.bg-bottom {
  background-position: bottom;
}

.bg-center {
  background-position: center;
}

.bg-left {
  background-position: left;
}

.bg-left-bottom {
  background-position: left bottom;
}

.bg-left-top {
  background-position: left top;
}

.bg-right {
  background-position: right;
}

.bg-right-bottom {
  background-position: right bottom;
}

.bg-right-top {
  background-position: right top;
}

.bg-top {
  background-position: top;
}

.bg-repeat {
  background-repeat: repeat;
}

.bg-no-repeat {
  background-repeat: no-repeat;
}

.bg-repeat-x {
  background-repeat: repeat-x;
}

.bg-repeat-y {
  background-repeat: repeat-y;
}

.bg-repeat-round {
  background-repeat: round;
}

.bg-repeat-space {
  background-repeat: space;
}

.bg-origin-border {
  background-origin: border-box;
}

.bg-origin-padding {
  background-origin: padding-box;
}

.bg-origin-content {
  background-origin: content-box;
}

.fill-amber-100 {
  fill: #fef3c7;
}

.fill-amber-200 {
  fill: #fde68a;
}

.fill-amber-300 {
  fill: #fcd34d;
}

.fill-amber-400 {
  fill: #fbbf24;
}

.fill-amber-50 {
  fill: #fffbeb;
}

.fill-amber-500 {
  fill: #f59e0b;
}

.fill-amber-600 {
  fill: #d97706;
}

.fill-amber-700 {
  fill: #b45309;
}

.fill-amber-800 {
  fill: #92400e;
}

.fill-amber-900 {
  fill: #78350f;
}

.fill-amber-950 {
  fill: #451a03;
}

.fill-black {
  fill: #000;
}

.fill-blue-100 {
  fill: #dbeafe;
}

.fill-blue-200 {
  fill: #bfdbfe;
}

.fill-blue-300 {
  fill: #93c5fd;
}

.fill-blue-400 {
  fill: #60a5fa;
}

.fill-blue-50 {
  fill: #eff6ff;
}

.fill-blue-500 {
  fill: #3b82f6;
}

.fill-blue-600 {
  fill: #2563eb;
}

.fill-blue-700 {
  fill: #1d4ed8;
}

.fill-blue-800 {
  fill: #1e40af;
}

.fill-blue-900 {
  fill: #1e3a8a;
}

.fill-blue-950 {
  fill: #172554;
}

.fill-current {
  fill: currentColor;
}

.fill-cyan-100 {
  fill: #cffafe;
}

.fill-cyan-200 {
  fill: #a5f3fc;
}

.fill-cyan-300 {
  fill: #67e8f9;
}

.fill-cyan-400 {
  fill: #22d3ee;
}

.fill-cyan-50 {
  fill: #ecfeff;
}

.fill-cyan-500 {
  fill: #06b6d4;
}

.fill-cyan-600 {
  fill: #0891b2;
}

.fill-cyan-700 {
  fill: #0e7490;
}

.fill-cyan-800 {
  fill: #155e75;
}

.fill-cyan-900 {
  fill: #164e63;
}

.fill-cyan-950 {
  fill: #083344;
}

.fill-emerald-100 {
  fill: #d1fae5;
}

.fill-emerald-200 {
  fill: #a7f3d0;
}

.fill-emerald-300 {
  fill: #6ee7b7;
}

.fill-emerald-400 {
  fill: #34d399;
}

.fill-emerald-50 {
  fill: #ecfdf5;
}

.fill-emerald-500 {
  fill: #10b981;
}

.fill-emerald-600 {
  fill: #059669;
}

.fill-emerald-700 {
  fill: #047857;
}

.fill-emerald-800 {
  fill: #065f46;
}

.fill-emerald-900 {
  fill: #064e3b;
}

.fill-emerald-950 {
  fill: #022c22;
}

.fill-fuchsia-100 {
  fill: #fae8ff;
}

.fill-fuchsia-200 {
  fill: #f5d0fe;
}

.fill-fuchsia-300 {
  fill: #f0abfc;
}

.fill-fuchsia-400 {
  fill: #e879f9;
}

.fill-fuchsia-50 {
  fill: #fdf4ff;
}

.fill-fuchsia-500 {
  fill: #d946ef;
}

.fill-fuchsia-600 {
  fill: #c026d3;
}

.fill-fuchsia-700 {
  fill: #a21caf;
}

.fill-fuchsia-800 {
  fill: #86198f;
}

.fill-fuchsia-900 {
  fill: #701a75;
}

.fill-fuchsia-950 {
  fill: #4a044e;
}

.fill-gray-100 {
  fill: #f3f4f6;
}

.fill-gray-200 {
  fill: #e5e7eb;
}

.fill-gray-300 {
  fill: #d1d5db;
}

.fill-gray-400 {
  fill: #9ca3af;
}

.fill-gray-50 {
  fill: #f9fafb;
}

.fill-gray-500 {
  fill: #6b7280;
}

.fill-gray-600 {
  fill: #4b5563;
}

.fill-gray-700 {
  fill: #374151;
}

.fill-gray-800 {
  fill: #1f2937;
}

.fill-gray-900 {
  fill: #111827;
}

.fill-gray-950 {
  fill: #030712;
}

.fill-green-100 {
  fill: #dcfce7;
}

.fill-green-200 {
  fill: #bbf7d0;
}

.fill-green-300 {
  fill: #86efac;
}

.fill-green-400 {
  fill: #4ade80;
}

.fill-green-50 {
  fill: #f0fdf4;
}

.fill-green-500 {
  fill: #22c55e;
}

.fill-green-600 {
  fill: #16a34a;
}

.fill-green-700 {
  fill: #15803d;
}

.fill-green-800 {
  fill: #166534;
}

.fill-green-900 {
  fill: #14532d;
}

.fill-green-950 {
  fill: #052e16;
}

.fill-indigo-100 {
  fill: #e0e7ff;
}

.fill-indigo-200 {
  fill: #c7d2fe;
}

.fill-indigo-300 {
  fill: #a5b4fc;
}

.fill-indigo-400 {
  fill: #818cf8;
}

.fill-indigo-50 {
  fill: #eef2ff;
}

.fill-indigo-500 {
  fill: #6366f1;
}

.fill-indigo-600 {
  fill: #4f46e5;
}

.fill-indigo-700 {
  fill: #4338ca;
}

.fill-indigo-800 {
  fill: #3730a3;
}

.fill-indigo-900 {
  fill: #312e81;
}

.fill-indigo-950 {
  fill: #1e1b4b;
}

.fill-inherit {
  fill: inherit;
}

.fill-lime-100 {
  fill: #ecfccb;
}

.fill-lime-200 {
  fill: #d9f99d;
}

.fill-lime-300 {
  fill: #bef264;
}

.fill-lime-400 {
  fill: #a3e635;
}

.fill-lime-50 {
  fill: #f7fee7;
}

.fill-lime-500 {
  fill: #84cc16;
}

.fill-lime-600 {
  fill: #65a30d;
}

.fill-lime-700 {
  fill: #4d7c0f;
}

.fill-lime-800 {
  fill: #3f6212;
}

.fill-lime-900 {
  fill: #365314;
}

.fill-lime-950 {
  fill: #1a2e05;
}

.fill-neutral-100 {
  fill: #f5f5f5;
}

.fill-neutral-200 {
  fill: #e5e5e5;
}

.fill-neutral-300 {
  fill: #d4d4d4;
}

.fill-neutral-400 {
  fill: #a3a3a3;
}

.fill-neutral-50 {
  fill: #fafafa;
}

.fill-neutral-500 {
  fill: #737373;
}

.fill-neutral-600 {
  fill: #525252;
}

.fill-neutral-700 {
  fill: #404040;
}

.fill-neutral-800 {
  fill: #262626;
}

.fill-neutral-900 {
  fill: #171717;
}

.fill-neutral-950 {
  fill: #0a0a0a;
}

.fill-none {
  fill: none;
}

.fill-orange-100 {
  fill: #ffedd5;
}

.fill-orange-200 {
  fill: #fed7aa;
}

.fill-orange-300 {
  fill: #fdba74;
}

.fill-orange-400 {
  fill: #fb923c;
}

.fill-orange-50 {
  fill: #fff7ed;
}

.fill-orange-500 {
  fill: #f97316;
}

.fill-orange-600 {
  fill: #ea580c;
}

.fill-orange-700 {
  fill: #c2410c;
}

.fill-orange-800 {
  fill: #9a3412;
}

.fill-orange-900 {
  fill: #7c2d12;
}

.fill-orange-950 {
  fill: #431407;
}

.fill-pink-100 {
  fill: #fce7f3;
}

.fill-pink-200 {
  fill: #fbcfe8;
}

.fill-pink-300 {
  fill: #f9a8d4;
}

.fill-pink-400 {
  fill: #f472b6;
}

.fill-pink-50 {
  fill: #fdf2f8;
}

.fill-pink-500 {
  fill: #ec4899;
}

.fill-pink-600 {
  fill: #db2777;
}

.fill-pink-700 {
  fill: #be185d;
}

.fill-pink-800 {
  fill: #9d174d;
}

.fill-pink-900 {
  fill: #831843;
}

.fill-pink-950 {
  fill: #500724;
}

.fill-purple-100 {
  fill: #f3e8ff;
}

.fill-purple-200 {
  fill: #e9d5ff;
}

.fill-purple-300 {
  fill: #d8b4fe;
}

.fill-purple-400 {
  fill: #c084fc;
}

.fill-purple-50 {
  fill: #faf5ff;
}

.fill-purple-500 {
  fill: #a855f7;
}

.fill-purple-600 {
  fill: #9333ea;
}

.fill-purple-700 {
  fill: #7e22ce;
}

.fill-purple-800 {
  fill: #6b21a8;
}

.fill-purple-900 {
  fill: #581c87;
}

.fill-purple-950 {
  fill: #3b0764;
}

.fill-red-100 {
  fill: #fee2e2;
}

.fill-red-200 {
  fill: #fecaca;
}

.fill-red-300 {
  fill: #fca5a5;
}

.fill-red-400 {
  fill: #f87171;
}

.fill-red-50 {
  fill: #fef2f2;
}

.fill-red-500 {
  fill: #ef4444;
}

.fill-red-600 {
  fill: #dc2626;
}

.fill-red-700 {
  fill: #b91c1c;
}

.fill-red-800 {
  fill: #991b1b;
}

.fill-red-900 {
  fill: #7f1d1d;
}

.fill-red-950 {
  fill: #450a0a;
}

.fill-rose-100 {
  fill: #ffe4e6;
}

.fill-rose-200 {
  fill: #fecdd3;
}

.fill-rose-300 {
  fill: #fda4af;
}

.fill-rose-400 {
  fill: #fb7185;
}

.fill-rose-50 {
  fill: #fff1f2;
}

.fill-rose-500 {
  fill: #f43f5e;
}

.fill-rose-600 {
  fill: #e11d48;
}

.fill-rose-700 {
  fill: #be123c;
}

.fill-rose-800 {
  fill: #9f1239;
}

.fill-rose-900 {
  fill: #881337;
}

.fill-rose-950 {
  fill: #4c0519;
}

.fill-sky-100 {
  fill: #e0f2fe;
}

.fill-sky-200 {
  fill: #bae6fd;
}

.fill-sky-300 {
  fill: #7dd3fc;
}

.fill-sky-400 {
  fill: #38bdf8;
}

.fill-sky-50 {
  fill: #f0f9ff;
}

.fill-sky-500 {
  fill: #0ea5e9;
}

.fill-sky-600 {
  fill: #0284c7;
}

.fill-sky-700 {
  fill: #0369a1;
}

.fill-sky-800 {
  fill: #075985;
}

.fill-sky-900 {
  fill: #0c4a6e;
}

.fill-sky-950 {
  fill: #082f49;
}

.fill-slate-100 {
  fill: #f1f5f9;
}

.fill-slate-200 {
  fill: #e2e8f0;
}

.fill-slate-300 {
  fill: #cbd5e1;
}

.fill-slate-400 {
  fill: #94a3b8;
}

.fill-slate-50 {
  fill: #f8fafc;
}

.fill-slate-500 {
  fill: #64748b;
}

.fill-slate-600 {
  fill: #475569;
}

.fill-slate-700 {
  fill: #334155;
}

.fill-slate-800 {
  fill: #1e293b;
}

.fill-slate-900 {
  fill: #0f172a;
}

.fill-slate-950 {
  fill: #020617;
}

.fill-stone-100 {
  fill: #f5f5f4;
}

.fill-stone-200 {
  fill: #e7e5e4;
}

.fill-stone-300 {
  fill: #d6d3d1;
}

.fill-stone-400 {
  fill: #a8a29e;
}

.fill-stone-50 {
  fill: #fafaf9;
}

.fill-stone-500 {
  fill: #78716c;
}

.fill-stone-600 {
  fill: #57534e;
}

.fill-stone-700 {
  fill: #44403c;
}

.fill-stone-800 {
  fill: #292524;
}

.fill-stone-900 {
  fill: #1c1917;
}

.fill-stone-950 {
  fill: #0c0a09;
}

.fill-teal-100 {
  fill: #ccfbf1;
}

.fill-teal-200 {
  fill: #99f6e4;
}

.fill-teal-300 {
  fill: #5eead4;
}

.fill-teal-400 {
  fill: #2dd4bf;
}

.fill-teal-50 {
  fill: #f0fdfa;
}

.fill-teal-500 {
  fill: #14b8a6;
}

.fill-teal-600 {
  fill: #0d9488;
}

.fill-teal-700 {
  fill: #0f766e;
}

.fill-teal-800 {
  fill: #115e59;
}

.fill-teal-900 {
  fill: #134e4a;
}

.fill-teal-950 {
  fill: #042f2e;
}

.fill-transparent {
  fill: transparent;
}

.fill-violet-100 {
  fill: #ede9fe;
}

.fill-violet-200 {
  fill: #ddd6fe;
}

.fill-violet-300 {
  fill: #c4b5fd;
}

.fill-violet-400 {
  fill: #a78bfa;
}

.fill-violet-50 {
  fill: #f5f3ff;
}

.fill-violet-500 {
  fill: #8b5cf6;
}

.fill-violet-600 {
  fill: #7c3aed;
}

.fill-violet-700 {
  fill: #6d28d9;
}

.fill-violet-800 {
  fill: #5b21b6;
}

.fill-violet-900 {
  fill: #4c1d95;
}

.fill-violet-950 {
  fill: #2e1065;
}

.fill-white {
  fill: #fff;
}

.fill-yellow-100 {
  fill: #fef9c3;
}

.fill-yellow-200 {
  fill: #fef08a;
}

.fill-yellow-300 {
  fill: #fde047;
}

.fill-yellow-400 {
  fill: #facc15;
}

.fill-yellow-50 {
  fill: #fefce8;
}

.fill-yellow-500 {
  fill: #eab308;
}

.fill-yellow-600 {
  fill: #ca8a04;
}

.fill-yellow-700 {
  fill: #a16207;
}

.fill-yellow-800 {
  fill: #854d0e;
}

.fill-yellow-900 {
  fill: #713f12;
}

.fill-yellow-950 {
  fill: #422006;
}

.fill-zinc-100 {
  fill: #f4f4f5;
}

.fill-zinc-200 {
  fill: #e4e4e7;
}

.fill-zinc-300 {
  fill: #d4d4d8;
}

.fill-zinc-400 {
  fill: #a1a1aa;
}

.fill-zinc-50 {
  fill: #fafafa;
}

.fill-zinc-500 {
  fill: #71717a;
}

.fill-zinc-600 {
  fill: #52525b;
}

.fill-zinc-700 {
  fill: #3f3f46;
}

.fill-zinc-800 {
  fill: #27272a;
}

.fill-zinc-900 {
  fill: #18181b;
}

.fill-zinc-950 {
  fill: #09090b;
}

.stroke-amber-100 {
  stroke: #fef3c7;
}

.stroke-amber-200 {
  stroke: #fde68a;
}

.stroke-amber-300 {
  stroke: #fcd34d;
}

.stroke-amber-400 {
  stroke: #fbbf24;
}

.stroke-amber-50 {
  stroke: #fffbeb;
}

.stroke-amber-500 {
  stroke: #f59e0b;
}

.stroke-amber-600 {
  stroke: #d97706;
}

.stroke-amber-700 {
  stroke: #b45309;
}

.stroke-amber-800 {
  stroke: #92400e;
}

.stroke-amber-900 {
  stroke: #78350f;
}

.stroke-amber-950 {
  stroke: #451a03;
}

.stroke-black {
  stroke: #000;
}

.stroke-blue-100 {
  stroke: #dbeafe;
}

.stroke-blue-200 {
  stroke: #bfdbfe;
}

.stroke-blue-300 {
  stroke: #93c5fd;
}

.stroke-blue-400 {
  stroke: #60a5fa;
}

.stroke-blue-50 {
  stroke: #eff6ff;
}

.stroke-blue-500 {
  stroke: #3b82f6;
}

.stroke-blue-600 {
  stroke: #2563eb;
}

.stroke-blue-700 {
  stroke: #1d4ed8;
}

.stroke-blue-800 {
  stroke: #1e40af;
}

.stroke-blue-900 {
  stroke: #1e3a8a;
}

.stroke-blue-950 {
  stroke: #172554;
}

.stroke-current {
  stroke: currentColor;
}

.stroke-cyan-100 {
  stroke: #cffafe;
}

.stroke-cyan-200 {
  stroke: #a5f3fc;
}

.stroke-cyan-300 {
  stroke: #67e8f9;
}

.stroke-cyan-400 {
  stroke: #22d3ee;
}

.stroke-cyan-50 {
  stroke: #ecfeff;
}

.stroke-cyan-500 {
  stroke: #06b6d4;
}

.stroke-cyan-600 {
  stroke: #0891b2;
}

.stroke-cyan-700 {
  stroke: #0e7490;
}

.stroke-cyan-800 {
  stroke: #155e75;
}

.stroke-cyan-900 {
  stroke: #164e63;
}

.stroke-cyan-950 {
  stroke: #083344;
}

.stroke-emerald-100 {
  stroke: #d1fae5;
}

.stroke-emerald-200 {
  stroke: #a7f3d0;
}

.stroke-emerald-300 {
  stroke: #6ee7b7;
}

.stroke-emerald-400 {
  stroke: #34d399;
}

.stroke-emerald-50 {
  stroke: #ecfdf5;
}

.stroke-emerald-500 {
  stroke: #10b981;
}

.stroke-emerald-600 {
  stroke: #059669;
}

.stroke-emerald-700 {
  stroke: #047857;
}

.stroke-emerald-800 {
  stroke: #065f46;
}

.stroke-emerald-900 {
  stroke: #064e3b;
}

.stroke-emerald-950 {
  stroke: #022c22;
}

.stroke-fuchsia-100 {
  stroke: #fae8ff;
}

.stroke-fuchsia-200 {
  stroke: #f5d0fe;
}

.stroke-fuchsia-300 {
  stroke: #f0abfc;
}

.stroke-fuchsia-400 {
  stroke: #e879f9;
}

.stroke-fuchsia-50 {
  stroke: #fdf4ff;
}

.stroke-fuchsia-500 {
  stroke: #d946ef;
}

.stroke-fuchsia-600 {
  stroke: #c026d3;
}

.stroke-fuchsia-700 {
  stroke: #a21caf;
}

.stroke-fuchsia-800 {
  stroke: #86198f;
}

.stroke-fuchsia-900 {
  stroke: #701a75;
}

.stroke-fuchsia-950 {
  stroke: #4a044e;
}

.stroke-gray-100 {
  stroke: #f3f4f6;
}

.stroke-gray-200 {
  stroke: #e5e7eb;
}

.stroke-gray-300 {
  stroke: #d1d5db;
}

.stroke-gray-400 {
  stroke: #9ca3af;
}

.stroke-gray-50 {
  stroke: #f9fafb;
}

.stroke-gray-500 {
  stroke: #6b7280;
}

.stroke-gray-600 {
  stroke: #4b5563;
}

.stroke-gray-700 {
  stroke: #374151;
}

.stroke-gray-800 {
  stroke: #1f2937;
}

.stroke-gray-900 {
  stroke: #111827;
}

.stroke-gray-950 {
  stroke: #030712;
}

.stroke-green-100 {
  stroke: #dcfce7;
}

.stroke-green-200 {
  stroke: #bbf7d0;
}

.stroke-green-300 {
  stroke: #86efac;
}

.stroke-green-400 {
  stroke: #4ade80;
}

.stroke-green-50 {
  stroke: #f0fdf4;
}

.stroke-green-500 {
  stroke: #22c55e;
}

.stroke-green-600 {
  stroke: #16a34a;
}

.stroke-green-700 {
  stroke: #15803d;
}

.stroke-green-800 {
  stroke: #166534;
}

.stroke-green-900 {
  stroke: #14532d;
}

.stroke-green-950 {
  stroke: #052e16;
}

.stroke-indigo-100 {
  stroke: #e0e7ff;
}

.stroke-indigo-200 {
  stroke: #c7d2fe;
}

.stroke-indigo-300 {
  stroke: #a5b4fc;
}

.stroke-indigo-400 {
  stroke: #818cf8;
}

.stroke-indigo-50 {
  stroke: #eef2ff;
}

.stroke-indigo-500 {
  stroke: #6366f1;
}

.stroke-indigo-600 {
  stroke: #4f46e5;
}

.stroke-indigo-700 {
  stroke: #4338ca;
}

.stroke-indigo-800 {
  stroke: #3730a3;
}

.stroke-indigo-900 {
  stroke: #312e81;
}

.stroke-indigo-950 {
  stroke: #1e1b4b;
}

.stroke-inherit {
  stroke: inherit;
}

.stroke-lime-100 {
  stroke: #ecfccb;
}

.stroke-lime-200 {
  stroke: #d9f99d;
}

.stroke-lime-300 {
  stroke: #bef264;
}

.stroke-lime-400 {
  stroke: #a3e635;
}

.stroke-lime-50 {
  stroke: #f7fee7;
}

.stroke-lime-500 {
  stroke: #84cc16;
}

.stroke-lime-600 {
  stroke: #65a30d;
}

.stroke-lime-700 {
  stroke: #4d7c0f;
}

.stroke-lime-800 {
  stroke: #3f6212;
}

.stroke-lime-900 {
  stroke: #365314;
}

.stroke-lime-950 {
  stroke: #1a2e05;
}

.stroke-neutral-100 {
  stroke: #f5f5f5;
}

.stroke-neutral-200 {
  stroke: #e5e5e5;
}

.stroke-neutral-300 {
  stroke: #d4d4d4;
}

.stroke-neutral-400 {
  stroke: #a3a3a3;
}

.stroke-neutral-50 {
  stroke: #fafafa;
}

.stroke-neutral-500 {
  stroke: #737373;
}

.stroke-neutral-600 {
  stroke: #525252;
}

.stroke-neutral-700 {
  stroke: #404040;
}

.stroke-neutral-800 {
  stroke: #262626;
}

.stroke-neutral-900 {
  stroke: #171717;
}

.stroke-neutral-950 {
  stroke: #0a0a0a;
}

.stroke-none {
  stroke: none;
}

.stroke-orange-100 {
  stroke: #ffedd5;
}

.stroke-orange-200 {
  stroke: #fed7aa;
}

.stroke-orange-300 {
  stroke: #fdba74;
}

.stroke-orange-400 {
  stroke: #fb923c;
}

.stroke-orange-50 {
  stroke: #fff7ed;
}

.stroke-orange-500 {
  stroke: #f97316;
}

.stroke-orange-600 {
  stroke: #ea580c;
}

.stroke-orange-700 {
  stroke: #c2410c;
}

.stroke-orange-800 {
  stroke: #9a3412;
}

.stroke-orange-900 {
  stroke: #7c2d12;
}

.stroke-orange-950 {
  stroke: #431407;
}

.stroke-pink-100 {
  stroke: #fce7f3;
}

.stroke-pink-200 {
  stroke: #fbcfe8;
}

.stroke-pink-300 {
  stroke: #f9a8d4;
}

.stroke-pink-400 {
  stroke: #f472b6;
}

.stroke-pink-50 {
  stroke: #fdf2f8;
}

.stroke-pink-500 {
  stroke: #ec4899;
}

.stroke-pink-600 {
  stroke: #db2777;
}

.stroke-pink-700 {
  stroke: #be185d;
}

.stroke-pink-800 {
  stroke: #9d174d;
}

.stroke-pink-900 {
  stroke: #831843;
}

.stroke-pink-950 {
  stroke: #500724;
}

.stroke-purple-100 {
  stroke: #f3e8ff;
}

.stroke-purple-200 {
  stroke: #e9d5ff;
}

.stroke-purple-300 {
  stroke: #d8b4fe;
}

.stroke-purple-400 {
  stroke: #c084fc;
}

.stroke-purple-50 {
  stroke: #faf5ff;
}

.stroke-purple-500 {
  stroke: #a855f7;
}

.stroke-purple-600 {
  stroke: #9333ea;
}

.stroke-purple-700 {
  stroke: #7e22ce;
}

.stroke-purple-800 {
  stroke: #6b21a8;
}

.stroke-purple-900 {
  stroke: #581c87;
}

.stroke-purple-950 {
  stroke: #3b0764;
}

.stroke-red-100 {
  stroke: #fee2e2;
}

.stroke-red-200 {
  stroke: #fecaca;
}

.stroke-red-300 {
  stroke: #fca5a5;
}

.stroke-red-400 {
  stroke: #f87171;
}

.stroke-red-50 {
  stroke: #fef2f2;
}

.stroke-red-500 {
  stroke: #ef4444;
}

.stroke-red-600 {
  stroke: #dc2626;
}

.stroke-red-700 {
  stroke: #b91c1c;
}

.stroke-red-800 {
  stroke: #991b1b;
}

.stroke-red-900 {
  stroke: #7f1d1d;
}

.stroke-red-950 {
  stroke: #450a0a;
}

.stroke-rose-100 {
  stroke: #ffe4e6;
}

.stroke-rose-200 {
  stroke: #fecdd3;
}

.stroke-rose-300 {
  stroke: #fda4af;
}

.stroke-rose-400 {
  stroke: #fb7185;
}

.stroke-rose-50 {
  stroke: #fff1f2;
}

.stroke-rose-500 {
  stroke: #f43f5e;
}

.stroke-rose-600 {
  stroke: #e11d48;
}

.stroke-rose-700 {
  stroke: #be123c;
}

.stroke-rose-800 {
  stroke: #9f1239;
}

.stroke-rose-900 {
  stroke: #881337;
}

.stroke-rose-950 {
  stroke: #4c0519;
}

.stroke-sky-100 {
  stroke: #e0f2fe;
}

.stroke-sky-200 {
  stroke: #bae6fd;
}

.stroke-sky-300 {
  stroke: #7dd3fc;
}

.stroke-sky-400 {
  stroke: #38bdf8;
}

.stroke-sky-50 {
  stroke: #f0f9ff;
}

.stroke-sky-500 {
  stroke: #0ea5e9;
}

.stroke-sky-600 {
  stroke: #0284c7;
}

.stroke-sky-700 {
  stroke: #0369a1;
}

.stroke-sky-800 {
  stroke: #075985;
}

.stroke-sky-900 {
  stroke: #0c4a6e;
}

.stroke-sky-950 {
  stroke: #082f49;
}

.stroke-slate-100 {
  stroke: #f1f5f9;
}

.stroke-slate-200 {
  stroke: #e2e8f0;
}

.stroke-slate-300 {
  stroke: #cbd5e1;
}

.stroke-slate-400 {
  stroke: #94a3b8;
}

.stroke-slate-50 {
  stroke: #f8fafc;
}

.stroke-slate-500 {
  stroke: #64748b;
}

.stroke-slate-600 {
  stroke: #475569;
}

.stroke-slate-700 {
  stroke: #334155;
}

.stroke-slate-800 {
  stroke: #1e293b;
}

.stroke-slate-900 {
  stroke: #0f172a;
}

.stroke-slate-950 {
  stroke: #020617;
}

.stroke-stone-100 {
  stroke: #f5f5f4;
}

.stroke-stone-200 {
  stroke: #e7e5e4;
}

.stroke-stone-300 {
  stroke: #d6d3d1;
}

.stroke-stone-400 {
  stroke: #a8a29e;
}

.stroke-stone-50 {
  stroke: #fafaf9;
}

.stroke-stone-500 {
  stroke: #78716c;
}

.stroke-stone-600 {
  stroke: #57534e;
}

.stroke-stone-700 {
  stroke: #44403c;
}

.stroke-stone-800 {
  stroke: #292524;
}

.stroke-stone-900 {
  stroke: #1c1917;
}

.stroke-stone-950 {
  stroke: #0c0a09;
}

.stroke-teal-100 {
  stroke: #ccfbf1;
}

.stroke-teal-200 {
  stroke: #99f6e4;
}

.stroke-teal-300 {
  stroke: #5eead4;
}

.stroke-teal-400 {
  stroke: #2dd4bf;
}

.stroke-teal-50 {
  stroke: #f0fdfa;
}

.stroke-teal-500 {
  stroke: #14b8a6;
}

.stroke-teal-600 {
  stroke: #0d9488;
}

.stroke-teal-700 {
  stroke: #0f766e;
}

.stroke-teal-800 {
  stroke: #115e59;
}

.stroke-teal-900 {
  stroke: #134e4a;
}

.stroke-teal-950 {
  stroke: #042f2e;
}

.stroke-transparent {
  stroke: transparent;
}

.stroke-violet-100 {
  stroke: #ede9fe;
}

.stroke-violet-200 {
  stroke: #ddd6fe;
}

.stroke-violet-300 {
  stroke: #c4b5fd;
}

.stroke-violet-400 {
  stroke: #a78bfa;
}

.stroke-violet-50 {
  stroke: #f5f3ff;
}

.stroke-violet-500 {
  stroke: #8b5cf6;
}

.stroke-violet-600 {
  stroke: #7c3aed;
}

.stroke-violet-700 {
  stroke: #6d28d9;
}

.stroke-violet-800 {
  stroke: #5b21b6;
}

.stroke-violet-900 {
  stroke: #4c1d95;
}

.stroke-violet-950 {
  stroke: #2e1065;
}

.stroke-white {
  stroke: #fff;
}

.stroke-yellow-100 {
  stroke: #fef9c3;
}

.stroke-yellow-200 {
  stroke: #fef08a;
}

.stroke-yellow-300 {
  stroke: #fde047;
}

.stroke-yellow-400 {
  stroke: #facc15;
}

.stroke-yellow-50 {
  stroke: #fefce8;
}

.stroke-yellow-500 {
  stroke: #eab308;
}

.stroke-yellow-600 {
  stroke: #ca8a04;
}

.stroke-yellow-700 {
  stroke: #a16207;
}

.stroke-yellow-800 {
  stroke: #854d0e;
}

.stroke-yellow-900 {
  stroke: #713f12;
}

.stroke-yellow-950 {
  stroke: #422006;
}

.stroke-zinc-100 {
  stroke: #f4f4f5;
}

.stroke-zinc-200 {
  stroke: #e4e4e7;
}

.stroke-zinc-300 {
  stroke: #d4d4d8;
}

.stroke-zinc-400 {
  stroke: #a1a1aa;
}

.stroke-zinc-50 {
  stroke: #fafafa;
}

.stroke-zinc-500 {
  stroke: #71717a;
}

.stroke-zinc-600 {
  stroke: #52525b;
}

.stroke-zinc-700 {
  stroke: #3f3f46;
}

.stroke-zinc-800 {
  stroke: #27272a;
}

.stroke-zinc-900 {
  stroke: #18181b;
}

.stroke-zinc-950 {
  stroke: #09090b;
}

.stroke-0 {
  stroke-width: 0;
}

.stroke-1 {
  stroke-width: 1;
}

.stroke-2 {
  stroke-width: 2;
}

.object-contain {
  -o-object-fit: contain;
     object-fit: contain;
}

.object-cover {
  -o-object-fit: cover;
     object-fit: cover;
}

.object-fill {
  -o-object-fit: fill;
     object-fit: fill;
}

.object-none {
  -o-object-fit: none;
     object-fit: none;
}

.object-scale-down {
  -o-object-fit: scale-down;
     object-fit: scale-down;
}

.object-bottom {
  -o-object-position: bottom;
     object-position: bottom;
}

.object-center {
  -o-object-position: center;
     object-position: center;
}

.object-left {
  -o-object-position: left;
     object-position: left;
}

.object-left-bottom {
  -o-object-position: left bottom;
     object-position: left bottom;
}

.object-left-top {
  -o-object-position: left top;
     object-position: left top;
}

.object-right {
  -o-object-position: right;
     object-position: right;
}

.object-right-bottom {
  -o-object-position: right bottom;
     object-position: right bottom;
}

.object-right-top {
  -o-object-position: right top;
     object-position: right top;
}

.object-top {
  -o-object-position: top;
     object-position: top;
}

.p-0 {
  padding: 0px;
}

.p-0.5 {
  padding: 0.125rem;
}

.p-1 {
  padding: 0.25rem;
}

.p-1.5 {
  padding: 0.375rem;
}

.p-10 {
  padding: 2.5rem;
}

.p-11 {
  padding: 2.75rem;
}

.p-12 {
  padding: 3rem;
}

.p-14 {
  padding: 3.5rem;
}

.p-16 {
  padding: 4rem;
}

.p-2 {
  padding: 0.5rem;
}

.p-2.5 {
  padding: 0.625rem;
}

.p-20 {
  padding: 5rem;
}

.p-24 {
  padding: 6rem;
}

.p-28 {
  padding: 7rem;
}

.p-3 {
  padding: 0.75rem;
}

.p-3.5 {
  padding: 0.875rem;
}

.p-32 {
  padding: 8rem;
}

.p-36 {
  padding: 9rem;
}

.p-4 {
  padding: 1rem;
}

.p-40 {
  padding: 10rem;
}

.p-44 {
  padding: 11rem;
}

.p-48 {
  padding: 12rem;
}

.p-5 {
  padding: 1.25rem;
}

.p-52 {
  padding: 13rem;
}

.p-56 {
  padding: 14rem;
}

.p-6 {
  padding: 1.5rem;
}

.p-60 {
  padding: 15rem;
}

.p-64 {
  padding: 16rem;
}

.p-7 {
  padding: 1.75rem;
}

.p-72 {
  padding: 18rem;
}

.p-8 {
  padding: 2rem;
}

.p-80 {
  padding: 20rem;
}

.p-9 {
  padding: 2.25rem;
}

.p-96 {
  padding: 24rem;
}

.p-px {
  padding: 1px;
}

.px-0 {
  padding-left: 0px;
  padding-right: 0px;
}

.px-0.5 {
  padding-left: 0.125rem;
  padding-right: 0.125rem;
}

.px-1 {
  padding-left: 0.25rem;
  padding-right: 0.25rem;
}

.px-1.5 {
  padding-left: 0.375rem;
  padding-right: 0.375rem;
}

.px-10 {
  padding-left: 2.5rem;
  padding-right: 2.5rem;
}

.px-11 {
  padding-left: 2.75rem;
  padding-right: 2.75rem;
}

.px-12 {
  padding-left: 3rem;
  padding-right: 3rem;
}

.px-14 {
  padding-left: 3.5rem;
  padding-right: 3.5rem;
}

.px-16 {
  padding-left: 4rem;
  padding-right: 4rem;
}

.px-2 {
  padding-left: 0.5rem;
  padding-right: 0.5rem;
}

.px-2.5 {
  padding-left: 0.625rem;
  padding-right: 0.625rem;
}

.px-20 {
  padding-left: 5rem;
  padding-right: 5rem;
}

.px-24 {
  padding-left: 6rem;
  padding-right: 6rem;
}

.px-28 {
  padding-left: 7rem;
  padding-right: 7rem;
}

.px-3 {
  padding-left: 0.75rem;
  padding-right: 0.75rem;
}

.px-3.5 {
  padding-left: 0.875rem;
  padding-right: 0.875rem;
}

.px-32 {
  padding-left: 8rem;
  padding-right: 8rem;
}

.px-36 {
  padding-left: 9rem;
  padding-right: 9rem;
}

.px-4 {
  padding-left: 1rem;
  padding-right: 1rem;
}

.px-40 {
  padding-left: 10rem;
  padding-right: 10rem;
}

.px-44 {
  padding-left: 11rem;
  padding-right: 11rem;
}

.px-48 {
  padding-left: 12rem;
  padding-right: 12rem;
}

.px-5 {
  padding-left: 1.25rem;
  padding-right: 1.25rem;
}

.px-52 {
  padding-left: 13rem;
  padding-right: 13rem;
}

.px-56 {
  padding-left: 14rem;
  padding-right: 14rem;
}

.px-6 {
  padding-left: 1.5rem;
  padding-right: 1.5rem;
}

.px-60 {
  padding-left: 15rem;
  padding-right: 15rem;
}

.px-64 {
  padding-left: 16rem;
  padding-right: 16rem;
}

.px-7 {
  padding-left: 1.75rem;
  padding-right: 1.75rem;
}

.px-72 {
  padding-left: 18rem;
  padding-right: 18rem;
}

.px-8 {
  padding-left: 2rem;
  padding-right: 2rem;
}

.px-80 {
  padding-left: 20rem;
  padding-right: 20rem;
}

.px-9 {
  padding-left: 2.25rem;
  padding-right: 2.25rem;
}

.px-96 {
  padding-left: 24rem;
  padding-right: 24rem;
}

.px-px {
  padding-left: 1px;
  padding-right: 1px;
}

.py-0 {
  padding-top: 0px;
  padding-bottom: 0px;
}

.py-0.5 {
  padding-top: 0.125rem;
  padding-bottom: 0.125rem;
}

.py-1 {
  padding-top: 0.25rem;
  padding-bottom: 0.25rem;
}

.py-1.5 {
  padding-top: 0.375rem;
  padding-bottom: 0.375rem;
}

.py-10 {
  padding-top: 2.5rem;
  padding-bottom: 2.5rem;
}

.py-11 {
  padding-top: 2.75rem;
  padding-bottom: 2.75rem;
}

.py-12 {
  padding-top: 3rem;
  padding-bottom: 3rem;
}

.py-14 {
  padding-top: 3.5rem;
  padding-bottom: 3.5rem;
}

.py-16 {
  padding-top: 4rem;
  padding-bottom: 4rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.py-2.5 {
  padding-top: 0.625rem;
  padding-bottom: 0.625rem;
}

.py-20 {
  padding-top: 5rem;
  padding-bottom: 5rem;
}

.py-24 {
  padding-top: 6rem;
  padding-bottom: 6rem;
}

.py-28 {
  padding-top: 7rem;
  padding-bottom: 7rem;
}

.py-3 {
  padding-top: 0.75rem;
  padding-bottom: 0.75rem;
}

.py-3.5 {
  padding-top: 0.875rem;
  padding-bottom: 0.875rem;
}

.py-32 {
  padding-top: 8rem;
  padding-bottom: 8rem;
}

.py-36 {
  padding-top: 9rem;
  padding-bottom: 9rem;
}

.py-4 {
  padding-top: 1rem;
  padding-bottom: 1rem;
}

.py-40 {
  padding-top: 10rem;
  padding-bottom: 10rem;
}

.py-44 {
  padding-top: 11rem;
  padding-bottom: 11rem;
}

.py-48 {
  padding-top: 12rem;
  padding-bottom: 12rem;
}

.py-5 {
  padding-top: 1.25rem;
  padding-bottom: 1.25rem;
}

.py-52 {
  padding-top: 13rem;
  padding-bottom: 13rem;
}

.py-56 {
  padding-top: 14rem;
  padding-bottom: 14rem;
}

.py-6 {
  padding-top: 1.5rem;
  padding-bottom: 1.5rem;
}

.py-60 {
  padding-top: 15rem;
  padding-bottom: 15rem;
}

.py-64 {
  padding-top: 16rem;
  padding-bottom: 16rem;
}

.py-7 {
  padding-top: 1.75rem;
  padding-bottom: 1.75rem;
}

.py-72 {
  padding-top: 18rem;
  padding-bottom: 18rem;
}

.py-8 {
  padding-top: 2rem;
  padding-bottom: 2rem;
}

.py-80 {
  padding-top: 20rem;
  padding-bottom: 20rem;
}

.py-9 {
  padding-top: 2.25rem;
  padding-bottom: 2.25rem;
}

.py-96 {
  padding-top: 24rem;
  padding-bottom: 24rem;
}

.py-px {
  padding-top: 1px;
  padding-bottom: 1px;
}

.pb-0 {
  padding-bottom: 0px;
}

.pb-0.5 {
  padding-bottom: 0.125rem;
}

.pb-1 {
  padding-bottom: 0.25rem;
}

.pb-1.5 {
  padding-bottom: 0.375rem;
}

.pb-10 {
  padding-bottom: 2.5rem;
}

.pb-11 {
  padding-bottom: 2.75rem;
}

.pb-12 {
  padding-bottom: 3rem;
}

.pb-14 {
  padding-bottom: 3.5rem;
}

.pb-16 {
  padding-bottom: 4rem;
}

.pb-2 {
  padding-bottom: 0.5rem;
}

.pb-2.5 {
  padding-bottom: 0.625rem;
}

.pb-20 {
  padding-bottom: 5rem;
}

.pb-24 {
  padding-bottom: 6rem;
}

.pb-28 {
  padding-bottom: 7rem;
}

.pb-3 {
  padding-bottom: 0.75rem;
}

.pb-3.5 {
  padding-bottom: 0.875rem;
}

.pb-32 {
  padding-bottom: 8rem;
}

.pb-36 {
  padding-bottom: 9rem;
}

.pb-4 {
  padding-bottom: 1rem;
}

.pb-40 {
  padding-bottom: 10rem;
}

.pb-44 {
  padding-bottom: 11rem;
}

.pb-48 {
  padding-bottom: 12rem;
}

.pb-5 {
  padding-bottom: 1.25rem;
}

.pb-52 {
  padding-bottom: 13rem;
}

.pb-56 {
  padding-bottom: 14rem;
}

.pb-6 {
  padding-bottom: 1.5rem;
}

.pb-60 {
  padding-bottom: 15rem;
}

.pb-64 {
  padding-bottom: 16rem;
}

.pb-7 {
  padding-bottom: 1.75rem;
}

.pb-72 {
  padding-bottom: 18rem;
}

.pb-8 {
  padding-bottom: 2rem;
}

.pb-80 {
  padding-bottom: 20rem;
}

.pb-9 {
  padding-bottom: 2.25rem;
}

.pb-96 {
  padding-bottom: 24rem;
}

.pb-px {
  padding-bottom: 1px;
}

.pe-0 {
  padding-inline-end: 0px;
}

.pe-0.5 {
  padding-inline-end: 0.125rem;
}

.pe-1 {
  padding-inline-end: 0.25rem;
}

.pe-1.5 {
  padding-inline-end: 0.375rem;
}

.pe-10 {
  padding-inline-end: 2.5rem;
}

.pe-11 {
  padding-inline-end: 2.75rem;
}

.pe-12 {
  padding-inline-end: 3rem;
}

.pe-14 {
  padding-inline-end: 3.5rem;
}

.pe-16 {
  padding-inline-end: 4rem;
}

.pe-2 {
  padding-inline-end: 0.5rem;
}

.pe-2.5 {
  padding-inline-end: 0.625rem;
}

.pe-20 {
  padding-inline-end: 5rem;
}

.pe-24 {
  padding-inline-end: 6rem;
}

.pe-28 {
  padding-inline-end: 7rem;
}

.pe-3 {
  padding-inline-end: 0.75rem;
}

.pe-3.5 {
  padding-inline-end: 0.875rem;
}

.pe-32 {
  padding-inline-end: 8rem;
}

.pe-36 {
  padding-inline-end: 9rem;
}

.pe-4 {
  padding-inline-end: 1rem;
}

.pe-40 {
  padding-inline-end: 10rem;
}

.pe-44 {
  padding-inline-end: 11rem;
}

.pe-48 {
  padding-inline-end: 12rem;
}

.pe-5 {
  padding-inline-end: 1.25rem;
}

.pe-52 {
  padding-inline-end: 13rem;
}

.pe-56 {
  padding-inline-end: 14rem;
}

.pe-6 {
  padding-inline-end: 1.5rem;
}

.pe-60 {
  padding-inline-end: 15rem;
}

.pe-64 {
  padding-inline-end: 16rem;
}

.pe-7 {
  padding-inline-end: 1.75rem;
}

.pe-72 {
  padding-inline-end: 18rem;
}

.pe-8 {
  padding-inline-end: 2rem;
}

.pe-80 {
  padding-inline-end: 20rem;
}

.pe-9 {
  padding-inline-end: 2.25rem;
}

.pe-96 {
  padding-inline-end: 24rem;
}

.pe-px {
  padding-inline-end: 1px;
}

.pl-0 {
  padding-left: 0px;
}

.pl-0.5 {
  padding-left: 0.125rem;
}

.pl-1 {
  padding-left: 0.25rem;
}

.pl-1.5 {
  padding-left: 0.375rem;
}

.pl-10 {
  padding-left: 2.5rem;
}

.pl-11 {
  padding-left: 2.75rem;
}

.pl-12 {
  padding-left: 3rem;
}

.pl-14 {
  padding-left: 3.5rem;
}

.pl-16 {
  padding-left: 4rem;
}

.pl-2 {
  padding-left: 0.5rem;
}

.pl-2.5 {
  padding-left: 0.625rem;
}

.pl-20 {
  padding-left: 5rem;
}

.pl-24 {
  padding-left: 6rem;
}

.pl-28 {
  padding-left: 7rem;
}

.pl-3 {
  padding-left: 0.75rem;
}

.pl-3.5 {
  padding-left: 0.875rem;
}

.pl-32 {
  padding-left: 8rem;
}

.pl-36 {
  padding-left: 9rem;
}

.pl-4 {
  padding-left: 1rem;
}

.pl-40 {
  padding-left: 10rem;
}

.pl-44 {
  padding-left: 11rem;
}

.pl-48 {
  padding-left: 12rem;
}

.pl-5 {
  padding-left: 1.25rem;
}

.pl-52 {
  padding-left: 13rem;
}

.pl-56 {
  padding-left: 14rem;
}

.pl-6 {
  padding-left: 1.5rem;
}

.pl-60 {
  padding-left: 15rem;
}

.pl-64 {
  padding-left: 16rem;
}

.pl-7 {
  padding-left: 1.75rem;
}

.pl-72 {
  padding-left: 18rem;
}

.pl-8 {
  padding-left: 2rem;
}

.pl-80 {
  padding-left: 20rem;
}

.pl-9 {
  padding-left: 2.25rem;
}

.pl-96 {
  padding-left: 24rem;
}

.pl-px {
  padding-left: 1px;
}

.pr-0 {
  padding-right: 0px;
}

.pr-0.5 {
  padding-right: 0.125rem;
}

.pr-1 {
  padding-right: 0.25rem;
}

.pr-1.5 {
  padding-right: 0.375rem;
}

.pr-10 {
  padding-right: 2.5rem;
}

.pr-11 {
  padding-right: 2.75rem;
}

.pr-12 {
  padding-right: 3rem;
}

.pr-14 {
  padding-right: 3.5rem;
}

.pr-16 {
  padding-right: 4rem;
}

.pr-2 {
  padding-right: 0.5rem;
}

.pr-2.5 {
  padding-right: 0.625rem;
}

.pr-20 {
  padding-right: 5rem;
}

.pr-24 {
  padding-right: 6rem;
}

.pr-28 {
  padding-right: 7rem;
}

.pr-3 {
  padding-right: 0.75rem;
}

.pr-3.5 {
  padding-right: 0.875rem;
}

.pr-32 {
  padding-right: 8rem;
}

.pr-36 {
  padding-right: 9rem;
}

.pr-4 {
  padding-right: 1rem;
}

.pr-40 {
  padding-right: 10rem;
}

.pr-44 {
  padding-right: 11rem;
}

.pr-48 {
  padding-right: 12rem;
}

.pr-5 {
  padding-right: 1.25rem;
}

.pr-52 {
  padding-right: 13rem;
}

.pr-56 {
  padding-right: 14rem;
}

.pr-6 {
  padding-right: 1.5rem;
}

.pr-60 {
  padding-right: 15rem;
}

.pr-64 {
  padding-right: 16rem;
}

.pr-7 {
  padding-right: 1.75rem;
}

.pr-72 {
  padding-right: 18rem;
}

.pr-8 {
  padding-right: 2rem;
}

.pr-80 {
  padding-right: 20rem;
}

.pr-9 {
  padding-right: 2.25rem;
}

.pr-96 {
  padding-right: 24rem;
}

.pr-px {
  padding-right: 1px;
}

.ps-0 {
  padding-inline-start: 0px;
}

.ps-0.5 {
  padding-inline-start: 0.125rem;
}

.ps-1 {
  padding-inline-start: 0.25rem;
}

.ps-1.5 {
  padding-inline-start: 0.375rem;
}

.ps-10 {
  padding-inline-start: 2.5rem;
}

.ps-11 {
  padding-inline-start: 2.75rem;
}

.ps-12 {
  padding-inline-start: 3rem;
}

.ps-14 {
  padding-inline-start: 3.5rem;
}

.ps-16 {
  padding-inline-start: 4rem;
}

.ps-2 {
  padding-inline-start: 0.5rem;
}

.ps-2.5 {
  padding-inline-start: 0.625rem;
}

.ps-20 {
  padding-inline-start: 5rem;
}

.ps-24 {
  padding-inline-start: 6rem;
}

.ps-28 {
  padding-inline-start: 7rem;
}

.ps-3 {
  padding-inline-start: 0.75rem;
}

.ps-3.5 {
  padding-inline-start: 0.875rem;
}

.ps-32 {
  padding-inline-start: 8rem;
}

.ps-36 {
  padding-inline-start: 9rem;
}

.ps-4 {
  padding-inline-start: 1rem;
}

.ps-40 {
  padding-inline-start: 10rem;
}

.ps-44 {
  padding-inline-start: 11rem;
}

.ps-48 {
  padding-inline-start: 12rem;
}

.ps-5 {
  padding-inline-start: 1.25rem;
}

.ps-52 {
  padding-inline-start: 13rem;
}

.ps-56 {
  padding-inline-start: 14rem;
}

.ps-6 {
  padding-inline-start: 1.5rem;
}

.ps-60 {
  padding-inline-start: 15rem;
}

.ps-64 {
  padding-inline-start: 16rem;
}

.ps-7 {
  padding-inline-start: 1.75rem;
}

.ps-72 {
  padding-inline-start: 18rem;
}

.ps-8 {
  padding-inline-start: 2rem;
}

.ps-80 {
  padding-inline-start: 20rem;
}

.ps-9 {
  padding-inline-start: 2.25rem;
}

.ps-96 {
  padding-inline-start: 24rem;
}

.ps-px {
  padding-inline-start: 1px;
}

.pt-0 {
  padding-top: 0px;
}

.pt-0.5 {
  padding-top: 0.125rem;
}

.pt-1 {
  padding-top: 0.25rem;
}

.pt-1.5 {
  padding-top: 0.375rem;
}

.pt-10 {
  padding-top: 2.5rem;
}

.pt-11 {
  padding-top: 2.75rem;
}

.pt-12 {
  padding-top: 3rem;
}

.pt-14 {
  padding-top: 3.5rem;
}

.pt-16 {
  padding-top: 4rem;
}

.pt-2 {
  padding-top: 0.5rem;
}

.pt-2.5 {
  padding-top: 0.625rem;
}

.pt-20 {
  padding-top: 5rem;
}

.pt-24 {
  padding-top: 6rem;
}

.pt-28 {
  padding-top: 7rem;
}

.pt-3 {
  padding-top: 0.75rem;
}

.pt-3.5 {
  padding-top: 0.875rem;
}

.pt-32 {
  padding-top: 8rem;
}

.pt-36 {
  padding-top: 9rem;
}

.pt-4 {
  padding-top: 1rem;
}

.pt-40 {
  padding-top: 10rem;
}

.pt-44 {
  padding-top: 11rem;
}

.pt-48 {
  padding-top: 12rem;
}

.pt-5 {
  padding-top: 1.25rem;
}

.pt-52 {
  padding-top: 13rem;
}

.pt-56 {
  padding-top: 14rem;
}

.pt-6 {
  padding-top: 1.5rem;
}

.pt-60 {
  padding-top: 15rem;
}

.pt-64 {
  padding-top: 16rem;
}

.pt-7 {
  padding-top: 1.75rem;
}

.pt-72 {
  padding-top: 18rem;
}

.pt-8 {
  padding-top: 2rem;
}

.pt-80 {
  padding-top: 20rem;
}

.pt-9 {
  padding-top: 2.25rem;
}

.pt-96 {
  padding-top: 24rem;
}

.pt-px {
  padding-top: 1px;
}

.text-left {
  text-align: left;
}

.text-center {
  text-align: center;
}

.text-right {
  text-align: right;
}

.text-justify {
  text-align: justify;
}

.text-start {
  text-align: start;
}

.text-end {
  text-align: end;
}

.-indent-0 {
  text-indent: -0px;
}

.-indent-0.5 {
  text-indent: -0.125rem;
}

.-indent-1 {
  text-indent: -0.25rem;
}

.-indent-1.5 {
  text-indent: -0.375rem;
}

.-indent-10 {
  text-indent: -2.5rem;
}

.-indent-11 {
  text-indent: -2.75rem;
}

.-indent-12 {
  text-indent: -3rem;
}

.-indent-14 {
  text-indent: -3.5rem;
}

.-indent-16 {
  text-indent: -4rem;
}

.-indent-2 {
  text-indent: -0.5rem;
}

.-indent-2.5 {
  text-indent: -0.625rem;
}

.-indent-20 {
  text-indent: -5rem;
}

.-indent-24 {
  text-indent: -6rem;
}

.-indent-28 {
  text-indent: -7rem;
}

.-indent-3 {
  text-indent: -0.75rem;
}

.-indent-3.5 {
  text-indent: -0.875rem;
}

.-indent-32 {
  text-indent: -8rem;
}

.-indent-36 {
  text-indent: -9rem;
}

.-indent-4 {
  text-indent: -1rem;
}

.-indent-40 {
  text-indent: -10rem;
}

.-indent-44 {
  text-indent: -11rem;
}

.-indent-48 {
  text-indent: -12rem;
}

.-indent-5 {
  text-indent: -1.25rem;
}

.-indent-52 {
  text-indent: -13rem;
}

.-indent-56 {
  text-indent: -14rem;
}

.-indent-6 {
  text-indent: -1.5rem;
}

.-indent-60 {
  text-indent: -15rem;
}

.-indent-64 {
  text-indent: -16rem;
}

.-indent-7 {
  text-indent: -1.75rem;
}

.-indent-72 {
  text-indent: -18rem;
}

.-indent-8 {
  text-indent: -2rem;
}

.-indent-80 {
  text-indent: -20rem;
}

.-indent-9 {
  text-indent: -2.25rem;
}

.-indent-96 {
  text-indent: -24rem;
}

.-indent-px {
  text-indent: -1px;
}

.indent-0 {
  text-indent: 0px;
}

.indent-0.5 {
  text-indent: 0.125rem;
}

.indent-1 {
  text-indent: 0.25rem;
}

.indent-1.5 {
  text-indent: 0.375rem;
}

.indent-10 {
  text-indent: 2.5rem;
}

.indent-11 {
  text-indent: 2.75rem;
}

.indent-12 {
  text-indent: 3rem;
}

.indent-14 {
  text-indent: 3.5rem;
}

.indent-16 {
  text-indent: 4rem;
}

.indent-2 {
  text-indent: 0.5rem;
}

.indent-2.5 {
  text-indent: 0.625rem;
}

.indent-20 {
  text-indent: 5rem;
}

.indent-24 {
  text-indent: 6rem;
}

.indent-28 {
  text-indent: 7rem;
}

.indent-3 {
  text-indent: 0.75rem;
}

.indent-3.5 {
  text-indent: 0.875rem;
}

.indent-32 {
  text-indent: 8rem;
}

.indent-36 {
  text-indent: 9rem;
}

.indent-4 {
  text-indent: 1rem;
}

.indent-40 {
  text-indent: 10rem;
}

.indent-44 {
  text-indent: 11rem;
}

.indent-48 {
  text-indent: 12rem;
}

.indent-5 {
  text-indent: 1.25rem;
}

.indent-52 {
  text-indent: 13rem;
}

.indent-56 {
  text-indent: 14rem;
}

.indent-6 {
  text-indent: 1.5rem;
}

.indent-60 {
  text-indent: 15rem;
}

.indent-64 {
  text-indent: 16rem;
}

.indent-7 {
  text-indent: 1.75rem;
}

.indent-72 {
  text-indent: 18rem;
}

.indent-8 {
  text-indent: 2rem;
}

.indent-80 {
  text-indent: 20rem;
}

.indent-9 {
  text-indent: 2.25rem;
}

.indent-96 {
  text-indent: 24rem;
}

.indent-px {
  text-indent: 1px;
}

.align-baseline {
  vertical-align: baseline;
}

.align-top {
  vertical-align: top;
}

.align-middle {
  vertical-align: middle;
}

.align-bottom {
  vertical-align: bottom;
}

.align-text-top {
  vertical-align: text-top;
}

.align-text-bottom {
  vertical-align: text-bottom;
}

.align-sub {
  vertical-align: sub;
}

.align-super {
  vertical-align: super;
}

.font-mono {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}

.font-sans {
  font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
}

.font-serif {
  font-family: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2rem;
}

.text-3xl {
  font-size: 1.875rem;
  line-height: 2.25rem;
}

.text-4xl {
  font-size: 2.25rem;
  line-height: 2.5rem;
}

.text-5xl {
  font-size: 3rem;
  line-height: 1;
}

.text-6xl {
  font-size: 3.75rem;
  line-height: 1;
}

.text-7xl {
  font-size: 4.5rem;
  line-height: 1;
}

.text-8xl {
  font-size: 6rem;
  line-height: 1;
}

.text-9xl {
  font-size: 8rem;
  line-height: 1;
}

.text-base {
  font-size: 1rem;
  line-height: 1.5rem;
}

.text-lg {
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.text-sm {
  font-size: 0.875rem;
  line-height: 1.25rem;
}

.text-xl {
  font-size: 1.25rem;
  line-height: 1.75rem;
}

.text-xs {
  font-size: 0.75rem;
  line-height: 1rem;
}

.font-black {
  font-weight: 900;
}

.font-bold {
  font-weight: 700;
}

.font-extrabold {
  font-weight: 800;
}

.font-extralight {
  font-weight: 200;
}

.font-light {
  font-weight: 300;
}

.font-medium {
  font-weight: 500;
}

.font-normal {
  font-weight: 400;
}

.font-semibold {
  font-weight: 600;
}

.font-thin {
  font-weight: 100;
}

.uppercase {
  text-transform: uppercase;
}

.lowercase {
  text-transform: lowercase;
}

.capitalize {
  text-transform: capitalize;
}

.normal-case {
  text-transform: none;
}

.italic {
  font-style: italic;
}

.not-italic {
  font-style: normal;
}

.normal-nums {
  font-variant-numeric: normal;
}

.ordinal {
  --tw-ordinal: ordinal;
  font-variant-numeric: var(--tw-ordinal) var(--tw-slashed-zero) var(--tw-numeric-figure) var(--tw-numeric-spacing) var(--tw-numeric-fraction);
}

.slashed-zero {
  --tw-slashed-zero: slashed-zero;
  font-variant-numeric: var(--tw-ordinal) var(--tw-slashed-zero) var(--tw-numeric-figure) var(--tw-numeric-spacing) var(--tw-numeric-fraction);
}

.lining-nums {
  --tw-numeric-figure: lining-nums;
  font-variant-numeric: var(--tw-ordinal) var(--tw-slashed-zero) var(--tw-numeric-figure) var(--tw-numeric-spacing) var(--tw-numeric-fraction);
}

.oldstyle-nums {
  --tw-numeric-figure: oldstyle-nums;
  font-variant-numeric: var(--tw-ordinal) var(--tw-slashed-zero) var(--tw-numeric-figure) var(--tw-numeric-spacing) var(--tw-numeric-fraction);
}

.proportional-nums {
  --tw-numeric-spacing: proportional-nums;
  font-variant-numeric: var(--tw-ordinal) var(--tw-slashed-zero) var(--tw-numeric-figure) var(--tw-numeric-spacing) var(--tw-numeric-fraction);
}

.tabular-nums {
  --tw-numeric-spacing: tabular-nums;
  font-variant-numeric: var(--tw-ordinal) var(--tw-slashed-zero) var(--tw-numeric-figure) var(--tw-numeric-spacing) var(--tw-numeric-fraction);
}

.diagonal-fractions {
  --tw-numeric-fraction: diagonal-fractions;
  font-variant-numeric: var(--tw-ordinal) var(--tw-slashed-zero) var(--tw-numeric-figure) var(--tw-numeric-spacing) var(--tw-numeric-fraction);
}

.stacked-fractions {
  --tw-numeric-fraction: stacked-fractions;
  font-variant-numeric: var(--tw-ordinal) var(--tw-slashed-zero) var(--tw-numeric-figure) var(--tw-numeric-spacing) var(--tw-numeric-fraction);
}

.leading-10 {
  line-height: 2.5rem;
}

.leading-3 {
  line-height: .75rem;
}

.leading-4 {
  line-height: 1rem;
}

.leading-5 {
  line-height: 1.25rem;
}

.leading-6 {
  line-height: 1.5rem;
}

.leading-7 {
  line-height: 1.75rem;
}

.leading-8 {
  line-height: 2rem;
}

.leading-9 {
  line-height: 2.25rem;
}

.leading-loose {
  line-height: 2;
}

.leading-none {
  line-height: 1;
}

.leading-normal {
  line-height: 1.5;
}

.leading-relaxed {
  line-height: 1.625;
}

.leading-snug {
  line-height: 1.375;
}

.leading-tight {
  line-height: 1.25;
}

.-tracking-normal {
  letter-spacing: -0em;
}

.-tracking-tight {
  letter-spacing: 0.025em;
}

.-tracking-tighter {
  letter-spacing: 0.05em;
}

.-tracking-wide {
  letter-spacing: -0.025em;
}

.-tracking-wider {
  letter-spacing: -0.05em;
}

.-tracking-widest {
  letter-spacing: -0.1em;
}

.tracking-normal {
  letter-spacing: 0em;
}

.tracking-tight {
  letter-spacing: -0.025em;
}

.tracking-tighter {
  letter-spacing: -0.05em;
}

.tracking-wide {
  letter-spacing: 0.025em;
}

.tracking-wider {
  letter-spacing: 0.05em;
}

.tracking-widest {
  letter-spacing: 0.1em;
}

.text-amber-100 {
  --tw-text-opacity: 1;
  color: rgb(254 243 199 / var(--tw-text-opacity));
}

.text-amber-200 {
  --tw-text-opacity: 1;
  color: rgb(253 230 138 / var(--tw-text-opacity));
}

.text-amber-300 {
  --tw-text-opacity: 1;
  color: rgb(252 211 77 / var(--tw-text-opacity));
}

.text-amber-400 {
  --tw-text-opacity: 1;
  color: rgb(251 191 36 / var(--tw-text-opacity));
}

.text-amber-50 {
  --tw-text-opacity: 1;
  color: rgb(255 251 235 / var(--tw-text-opacity));
}

.text-amber-500 {
  --tw-text-opacity: 1;
  color: rgb(245 158 11 / var(--tw-text-opacity));
}

.text-amber-600 {
  --tw-text-opacity: 1;
  color: rgb(217 119 6 / var(--tw-text-opacity));
}

.text-amber-700 {
  --tw-text-opacity: 1;
  color: rgb(180 83 9 / var(--tw-text-opacity));
}

.text-amber-800 {
  --tw-text-opacity: 1;
  color: rgb(146 64 14 / var(--tw-text-opacity));
}

.text-amber-900 {
  --tw-text-opacity: 1;
  color: rgb(120 53 15 / var(--tw-text-opacity));
}

.text-amber-950 {
  --tw-text-opacity: 1;
  color: rgb(69 26 3 / var(--tw-text-opacity));
}

.text-black {
  --tw-text-opacity: 1;
  color: rgb(0 0 0 / var(--tw-text-opacity));
}

.text-blue-100 {
  --tw-text-opacity: 1;
  color: rgb(219 234 254 / var(--tw-text-opacity));
}

.text-blue-200 {
  --tw-text-opacity: 1;
  color: rgb(191 219 254 / var(--tw-text-opacity));
}

.text-blue-300 {
  --tw-text-opacity: 1;
  color: rgb(147 197 253 / var(--tw-text-opacity));
}

.text-blue-400 {
  --tw-text-opacity: 1;
  color: rgb(96 165 250 / var(--tw-text-opacity));
}

.text-blue-50 {
  --tw-text-opacity: 1;
  color: rgb(239 246 255 / var(--tw-text-opacity));
}

.text-blue-500 {
  --tw-text-opacity: 1;
  color: rgb(59 130 246 / var(--tw-text-opacity));
}

.text-blue-600 {
  --tw-text-opacity: 1;
  color: rgb(37 99 235 / var(--tw-text-opacity));
}

.text-blue-700 {
  --tw-text-opacity: 1;
  color: rgb(29 78 216 / var(--tw-text-opacity));
}

.text-blue-800 {
  --tw-text-opacity: 1;
  color: rgb(30 64 175 / var(--tw-text-opacity));
}

.text-blue-900 {
  --tw-text-opacity: 1;
  color: rgb(30 58 138 / var(--tw-text-opacity));
}

.text-blue-950 {
  --tw-text-opacity: 1;
  color: rgb(23 37 84 / var(--tw-text-opacity));
}

.text-current {
  color: currentColor;
}

.text-cyan-100 {
  --tw-text-opacity: 1;
  color: rgb(207 250 254 / var(--tw-text-opacity));
}

.text-cyan-200 {
  --tw-text-opacity: 1;
  color: rgb(165 243 252 / var(--tw-text-opacity));
}

.text-cyan-300 {
  --tw-text-opacity: 1;
  color: rgb(103 232 249 / var(--tw-text-opacity));
}

.text-cyan-400 {
  --tw-text-opacity: 1;
  color: rgb(34 211 238 / var(--tw-text-opacity));
}

.text-cyan-50 {
  --tw-text-opacity: 1;
  color: rgb(236 254 255 / var(--tw-text-opacity));
}

.text-cyan-500 {
  --tw-text-opacity: 1;
  color: rgb(6 182 212 / var(--tw-text-opacity));
}

.text-cyan-600 {
  --tw-text-opacity: 1;
  color: rgb(8 145 178 / var(--tw-text-opacity));
}

.text-cyan-700 {
  --tw-text-opacity: 1;
  color: rgb(14 116 144 / var(--tw-text-opacity));
}

.text-cyan-800 {
  --tw-text-opacity: 1;
  color: rgb(21 94 117 / var(--tw-text-opacity));
}

.text-cyan-900 {
  --tw-text-opacity: 1;
  color: rgb(22 78 99 / var(--tw-text-opacity));
}

.text-cyan-950 {
  --tw-text-opacity: 1;
  color: rgb(8 51 68 / var(--tw-text-opacity));
}

.text-emerald-100 {
  --tw-text-opacity: 1;
  color: rgb(209 250 229 / var(--tw-text-opacity));
}

.text-emerald-200 {
  --tw-text-opacity: 1;
  color: rgb(167 243 208 / var(--tw-text-opacity));
}

.text-emerald-300 {
  --tw-text-opacity: 1;
  color: rgb(110 231 183 / var(--tw-text-opacity));
}

.text-emerald-400 {
  --tw-text-opacity: 1;
  color: rgb(52 211 153 / var(--tw-text-opacity));
}

.text-emerald-50 {
  --tw-text-opacity: 1;
  color: rgb(236 253 245 / var(--tw-text-opacity));
}

.text-emerald-500 {
  --tw-text-opacity: 1;
  color: rgb(16 185 129 / var(--tw-text-opacity));
}

.text-emerald-600 {
  --tw-text-opacity: 1;
  color: rgb(5 150 105 / var(--tw-text-opacity));
}

.text-emerald-700 {
  --tw-text-opacity: 1;
  color: rgb(4 120 87 / var(--tw-text-opacity));
}

.text-emerald-800 {
  --tw-text-opacity: 1;
  color: rgb(6 95 70 / var(--tw-text-opacity));
}

.text-emerald-900 {
  --tw-text-opacity: 1;
  color: rgb(6 78 59 / var(--tw-text-opacity));
}

.text-emerald-950 {
  --tw-text-opacity: 1;
  color: rgb(2 44 34 / var(--tw-text-opacity));
}

.text-fuchsia-100 {
  --tw-text-opacity: 1;
  color: rgb(250 232 255 / var(--tw-text-opacity));
}

.text-fuchsia-200 {
  --tw-text-opacity: 1;
  color: rgb(245 208 254 / var(--tw-text-opacity));
}

.text-fuchsia-300 {
  --tw-text-opacity: 1;
  color: rgb(240 171 252 / var(--tw-text-opacity));
}

.text-fuchsia-400 {
  --tw-text-opacity: 1;
  color: rgb(232 121 249 / var(--tw-text-opacity));
}

.text-fuchsia-50 {
  --tw-text-opacity: 1;
  color: rgb(253 244 255 / var(--tw-text-opacity));
}

.text-fuchsia-500 {
  --tw-text-opacity: 1;
  color: rgb(217 70 239 / var(--tw-text-opacity));
}

.text-fuchsia-600 {
  --tw-text-opacity: 1;
  color: rgb(192 38 211 / var(--tw-text-opacity));
}

.text-fuchsia-700 {
  --tw-text-opacity: 1;
  color: rgb(162 28 175 / var(--tw-text-opacity));
}

.text-fuchsia-800 {
  --tw-text-opacity: 1;
  color: rgb(134 25 143 / var(--tw-text-opacity));
}

.text-fuchsia-900 {
  --tw-text-opacity: 1;
  color: rgb(112 26 117 / var(--tw-text-opacity));
}

.text-fuchsia-950 {
  --tw-text-opacity: 1;
  color: rgb(74 4 78 / var(--tw-text-opacity));
}

.text-gray-100 {
  --tw-text-opacity: 1;
  color: rgb(243 244 246 / var(--tw-text-opacity));
}

.text-gray-200 {
  --tw-text-opacity: 1;
  color: rgb(229 231 235 / var(--tw-text-opacity));
}

.text-gray-300 {
  --tw-text-opacity: 1;
  color: rgb(209 213 219 / var(--tw-text-opacity));
}

.text-gray-400 {
  --tw-text-opacity: 1;
  color: rgb(156 163 175 / var(--tw-text-opacity));
}

.text-gray-50 {
  --tw-text-opacity: 1;
  color: rgb(249 250 251 / var(--tw-text-opacity));
}

.text-gray-500 {
  --tw-text-opacity: 1;
  color: rgb(107 114 128 / var(--tw-text-opacity));
}

.text-gray-600 {
  --tw-text-opacity: 1;
  color: rgb(75 85 99 / var(--tw-text-opacity));
}

.text-gray-700 {
  --tw-text-opacity: 1;
  color: rgb(55 65 81 / var(--tw-text-opacity));
}

.text-gray-800 {
  --tw-text-opacity: 1;
  color: rgb(31 41 55 / var(--tw-text-opacity));
}

.text-gray-900 {
  --tw-text-opacity: 1;
  color: rgb(17 24 39 / var(--tw-text-opacity));
}

.text-gray-950 {
  --tw-text-opacity: 1;
  color: rgb(3 7 18 / var(--tw-text-opacity));
}

.text-green-100 {
  --tw-text-opacity: 1;
  color: rgb(220 252 231 / var(--tw-text-opacity));
}

.text-green-200 {
  --tw-text-opacity: 1;
  color: rgb(187 247 208 / var(--tw-text-opacity));
}

.text-green-300 {
  --tw-text-opacity: 1;
  color: rgb(134 239 172 / var(--tw-text-opacity));
}

.text-green-400 {
  --tw-text-opacity: 1;
  color: rgb(74 222 128 / var(--tw-text-opacity));
}

.text-green-50 {
  --tw-text-opacity: 1;
  color: rgb(240 253 244 / var(--tw-text-opacity));
}

.text-green-500 {
  --tw-text-opacity: 1;
  color: rgb(34 197 94 / var(--tw-text-opacity));
}

.text-green-600 {
  --tw-text-opacity: 1;
  color: rgb(22 163 74 / var(--tw-text-opacity));
}

.text-green-700 {
  --tw-text-opacity: 1;
  color: rgb(21 128 61 / var(--tw-text-opacity));
}

.text-green-800 {
  --tw-text-opacity: 1;
  color: rgb(22 101 52 / var(--tw-text-opacity));
}

.text-green-900 {
  --tw-text-opacity: 1;
  color: rgb(20 83 45 / var(--tw-text-opacity));
}

.text-green-950 {
  --tw-text-opacity: 1;
  color: rgb(5 46 22 / var(--tw-text-opacity));
}

.text-indigo-100 {
  --tw-text-opacity: 1;
  color: rgb(224 231 255 / var(--tw-text-opacity));
}

.text-indigo-200 {
  --tw-text-opacity: 1;
  color: rgb(199 210 254 / var(--tw-text-opacity));
}

.text-indigo-300 {
  --tw-text-opacity: 1;
  color: rgb(165 180 252 / var(--tw-text-opacity));
}

.text-indigo-400 {
  --tw-text-opacity: 1;
  color: rgb(129 140 248 / var(--tw-text-opacity));
}

.text-indigo-50 {
  --tw-text-opacity: 1;
  color: rgb(238 242 255 / var(--tw-text-opacity));
}

.text-indigo-500 {
  --tw-text-opacity: 1;
  color: rgb(99 102 241 / var(--tw-text-opacity));
}

.text-indigo-600 {
  --tw-text-opacity: 1;
  color: rgb(79 70 229 / var(--tw-text-opacity));
}

.text-indigo-700 {
  --tw-text-opacity: 1;
  color: rgb(67 56 202 / var(--tw-text-opacity));
}

.text-indigo-800 {
  --tw-text-opacity: 1;
  color: rgb(55 48 163 / var(--tw-text-opacity));
}

.text-indigo-900 {
  --tw-text-opacity: 1;
  color: rgb(49 46 129 / var(--tw-text-opacity));
}

.text-indigo-950 {
  --tw-text-opacity: 1;
  color: rgb(30 27 75 / var(--tw-text-opacity));
}

.text-inherit {
  color: inherit;
}

.text-lime-100 {
  --tw-text-opacity: 1;
  color: rgb(236 252 203 / var(--tw-text-opacity));
}

.text-lime-200 {
  --tw-text-opacity: 1;
  color: rgb(217 249 157 / var(--tw-text-opacity));
}

.text-lime-300 {
  --tw-text-opacity: 1;
  color: rgb(190 242 100 / var(--tw-text-opacity));
}

.text-lime-400 {
  --tw-text-opacity: 1;
  color: rgb(163 230 53 / var(--tw-text-opacity));
}

.text-lime-50 {
  --tw-text-opacity: 1;
  color: rgb(247 254 231 / var(--tw-text-opacity));
}

.text-lime-500 {
  --tw-text-opacity: 1;
  color: rgb(132 204 22 / var(--tw-text-opacity));
}

.text-lime-600 {
  --tw-text-opacity: 1;
  color: rgb(101 163 13 / var(--tw-text-opacity));
}

.text-lime-700 {
  --tw-text-opacity: 1;
  color: rgb(77 124 15 / var(--tw-text-opacity));
}

.text-lime-800 {
  --tw-text-opacity: 1;
  color: rgb(63 98 18 / var(--tw-text-opacity));
}

.text-lime-900 {
  --tw-text-opacity: 1;
  color: rgb(54 83 20 / var(--tw-text-opacity));
}

.text-lime-950 {
  --tw-text-opacity: 1;
  color: rgb(26 46 5 / var(--tw-text-opacity));
}

.text-neutral-100 {
  --tw-text-opacity: 1;
  color: rgb(245 245 245 / var(--tw-text-opacity));
}

.text-neutral-200 {
  --tw-text-opacity: 1;
  color: rgb(229 229 229 / var(--tw-text-opacity));
}

.text-neutral-300 {
  --tw-text-opacity: 1;
  color: rgb(212 212 212 / var(--tw-text-opacity));
}

.text-neutral-400 {
  --tw-text-opacity: 1;
  color: rgb(163 163 163 / var(--tw-text-opacity));
}

.text-neutral-50 {
  --tw-text-opacity: 1;
  color: rgb(250 250 250 / var(--tw-text-opacity));
}

.text-neutral-500 {
  --tw-text-opacity: 1;
  color: rgb(115 115 115 / var(--tw-text-opacity));
}

.text-neutral-600 {
  --tw-text-opacity: 1;
  color: rgb(82 82 82 / var(--tw-text-opacity));
}

.text-neutral-700 {
  --tw-text-opacity: 1;
  color: rgb(64 64 64 / var(--tw-text-opacity));
}

.text-neutral-800 {
  --tw-text-opacity: 1;
  color: rgb(38 38 38 / var(--tw-text-opacity));
}

.text-neutral-900 {
  --tw-text-opacity: 1;
  color: rgb(23 23 23 / var(--tw-text-opacity));
}

.text-neutral-950 {
  --tw-text-opacity: 1;
  color: rgb(10 10 10 / var(--tw-text-opacity));
}

.text-orange-100 {
  --tw-text-opacity: 1;
  color: rgb(255 237 213 / var(--tw-text-opacity));
}

.text-orange-200 {
  --tw-text-opacity: 1;
  color: rgb(254 215 170 / var(--tw-text-opacity));
}

.text-orange-300 {
  --tw-text-opacity: 1;
  color: rgb(253 186 116 / var(--tw-text-opacity));
}

.text-orange-400 {
  --tw-text-opacity: 1;
  color: rgb(251 146 60 / var(--tw-text-opacity));
}

.text-orange-50 {
  --tw-text-opacity: 1;
  color: rgb(255 247 237 / var(--tw-text-opacity));
}

.text-orange-500 {
  --tw-text-opacity: 1;
  color: rgb(249 115 22 / var(--tw-text-opacity));
}

.text-orange-600 {
  --tw-text-opacity: 1;
  color: rgb(234 88 12 / var(--tw-text-opacity));
}

.text-orange-700 {
  --tw-text-opacity: 1;
  color: rgb(194 65 12 / var(--tw-text-opacity));
}

.text-orange-800 {
  --tw-text-opacity: 1;
  color: rgb(154 52 18 / var(--tw-text-opacity));
}

.text-orange-900 {
  --tw-text-opacity: 1;
  color: rgb(124 45 18 / var(--tw-text-opacity));
}

.text-orange-950 {
  --tw-text-opacity: 1;
  color: rgb(67 20 7 / var(--tw-text-opacity));
}

.text-pink-100 {
  --tw-text-opacity: 1;
  color: rgb(252 231 243 / var(--tw-text-opacity));
}

.text-pink-200 {
  --tw-text-opacity: 1;
  color: rgb(251 207 232 / var(--tw-text-opacity));
}

.text-pink-300 {
  --tw-text-opacity: 1;
  color: rgb(249 168 212 / var(--tw-text-opacity));
}

.text-pink-400 {
  --tw-text-opacity: 1;
  color: rgb(244 114 182 / var(--tw-text-opacity));
}

.text-pink-50 {
  --tw-text-opacity: 1;
  color: rgb(253 242 248 / var(--tw-text-opacity));
}

.text-pink-500 {
  --tw-text-opacity: 1;
  color: rgb(236 72 153 / var(--tw-text-opacity));
}

.text-pink-600 {
  --tw-text-opacity: 1;
  color: rgb(219 39 119 / var(--tw-text-opacity));
}

.text-pink-700 {
  --tw-text-opacity: 1;
  color: rgb(190 24 93 / var(--tw-text-opacity));
}

.text-pink-800 {
  --tw-text-opacity: 1;
  color: rgb(157 23 77 / var(--tw-text-opacity));
}

.text-pink-900 {
  --tw-text-opacity: 1;
  color: rgb(131 24 67 / var(--tw-text-opacity));
}

.text-pink-950 {
  --tw-text-opacity: 1;
  color: rgb(80 7 36 / var(--tw-text-opacity));
}

.text-purple-100 {
  --tw-text-opacity: 1;
  color: rgb(243 232 255 / var(--tw-text-opacity));
}

.text-purple-200 {
  --tw-text-opacity: 1;
  color: rgb(233 213 255 / var(--tw-text-opacity));
}

.text-purple-300 {
  --tw-text-opacity: 1;
  color: rgb(216 180 254 / var(--tw-text-opacity));
}

.text-purple-400 {
  --tw-text-opacity: 1;
  color: rgb(192 132 252 / var(--tw-text-opacity));
}

.text-purple-50 {
  --tw-text-opacity: 1;
  color: rgb(250 245 255 / var(--tw-text-opacity));
}

.text-purple-500 {
  --tw-text-opacity: 1;
  color: rgb(168 85 247 / var(--tw-text-opacity));
}

.text-purple-600 {
  --tw-text-opacity: 1;
  color: rgb(147 51 234 / var(--tw-text-opacity));
}

.text-purple-700 {
  --tw-text-opacity: 1;
  color: rgb(126 34 206 / var(--tw-text-opacity));
}

.text-purple-800 {
  --tw-text-opacity: 1;
  color: rgb(107 33 168 / var(--tw-text-opacity));
}

.text-purple-900 {
  --tw-text-opacity: 1;
  color: rgb(88 28 135 / var(--tw-text-opacity));
}

.text-purple-950 {
  --tw-text-opacity: 1;
  color: rgb(59 7 100 / var(--tw-text-opacity));
}

.text-red-100 {
  --tw-text-opacity: 1;
  color: rgb(254 226 226 / var(--tw-text-opacity));
}

.text-red-200 {
  --tw-text-opacity: 1;
  color: rgb(254 202 202 / var(--tw-text-opacity));
}

.text-red-300 {
  --tw-text-opacity: 1;
  color: rgb(252 165 165 / var(--tw-text-opacity));
}

.text-red-400 {
  --tw-text-opacity: 1;
  color: rgb(248 113 113 / var(--tw-text-opacity));
}

.text-red-50 {
  --tw-text-opacity: 1;
  color: rgb(254 242 242 / var(--tw-text-opacity));
}

.text-red-500 {
  --tw-text-opacity: 1;
  color: rgb(239 68 68 / var(--tw-text-opacity));
}

.text-red-600 {
  --tw-text-opacity: 1;
  color: rgb(220 38 38 / var(--tw-text-opacity));
}

.text-red-700 {
  --tw-text-opacity: 1;
  color: rgb(185 28 28 / var(--tw-text-opacity));
}

.text-red-800 {
  --tw-text-opacity: 1;
  color: rgb(153 27 27 / var(--tw-text-opacity));
}

.text-red-900 {
  --tw-text-opacity: 1;
  color: rgb(127 29 29 / var(--tw-text-opacity));
}

.text-red-950 {
  --tw-text-opacity: 1;
  color: rgb(69 10 10 / var(--tw-text-opacity));
}

.text-rose-100 {
  --tw-text-opacity: 1;
  color: rgb(255 228 230 / var(--tw-text-opacity));
}

.text-rose-200 {
  --tw-text-opacity: 1;
  color: rgb(254 205 211 / var(--tw-text-opacity));
}

.text-rose-300 {
  --tw-text-opacity: 1;
  color: rgb(253 164 175 / var(--tw-text-opacity));
}

.text-rose-400 {
  --tw-text-opacity: 1;
  color: rgb(251 113 133 / var(--tw-text-opacity));
}

.text-rose-50 {
  --tw-text-opacity: 1;
  color: rgb(255 241 242 / var(--tw-text-opacity));
}

.text-rose-500 {
  --tw-text-opacity: 1;
  color: rgb(244 63 94 / var(--tw-text-opacity));
}

.text-rose-600 {
  --tw-text-opacity: 1;
  color: rgb(225 29 72 / var(--tw-text-opacity));
}

.text-rose-700 {
  --tw-text-opacity: 1;
  color: rgb(190 18 60 / var(--tw-text-opacity));
}

.text-rose-800 {
  --tw-text-opacity: 1;
  color: rgb(159 18 57 / var(--tw-text-opacity));
}

.text-rose-900 {
  --tw-text-opacity: 1;
  color: rgb(136 19 55 / var(--tw-text-opacity));
}

.text-rose-950 {
  --tw-text-opacity: 1;
  color: rgb(76 5 25 / var(--tw-text-opacity));
}

.text-sky-100 {
  --tw-text-opacity: 1;
  color: rgb(224 242 254 / var(--tw-text-opacity));
}

.text-sky-200 {
  --tw-text-opacity: 1;
  color: rgb(186 230 253 / var(--tw-text-opacity));
}

.text-sky-300 {
  --tw-text-opacity: 1;
  color: rgb(125 211 252 / var(--tw-text-opacity));
}

.text-sky-400 {
  --tw-text-opacity: 1;
  color: rgb(56 189 248 / var(--tw-text-opacity));
}

.text-sky-50 {
  --tw-text-opacity: 1;
  color: rgb(240 249 255 / var(--tw-text-opacity));
}

.text-sky-500 {
  --tw-text-opacity: 1;
  color: rgb(14 165 233 / var(--tw-text-opacity));
}

.text-sky-600 {
  --tw-text-opacity: 1;
  color: rgb(2 132 199 / var(--tw-text-opacity));
}

.text-sky-700 {
  --tw-text-opacity: 1;
  color: rgb(3 105 161 / var(--tw-text-opacity));
}

.text-sky-800 {
  --tw-text-opacity: 1;
  color: rgb(7 89 133 / var(--tw-text-opacity));
}

.text-sky-900 {
  --tw-text-opacity: 1;
  color: rgb(12 74 110 / var(--tw-text-opacity));
}

.text-sky-950 {
  --tw-text-opacity: 1;
  color: rgb(8 47 73 / var(--tw-text-opacity));
}

.text-slate-100 {
  --tw-text-opacity: 1;
  color: rgb(241 245 249 / var(--tw-text-opacity));
}

.text-slate-200 {
  --tw-text-opacity: 1;
  color: rgb(226 232 240 / var(--tw-text-opacity));
}

.text-slate-300 {
  --tw-text-opacity: 1;
  color: rgb(203 213 225 / var(--tw-text-opacity));
}

.text-slate-400 {
  --tw-text-opacity: 1;
  color: rgb(148 163 184 / var(--tw-text-opacity));
}

.text-slate-50 {
  --tw-text-opacity: 1;
  color: rgb(248 250 252 / var(--tw-text-opacity));
}

.text-slate-500 {
  --tw-text-opacity: 1;
  color: rgb(100 116 139 / var(--tw-text-opacity));
}

.text-slate-600 {
  --tw-text-opacity: 1;
  color: rgb(71 85 105 / var(--tw-text-opacity));
}

.text-slate-700 {
  --tw-text-opacity: 1;
  color: rgb(51 65 85 / var(--tw-text-opacity));
}

.text-slate-800 {
  --tw-text-opacity: 1;
  color: rgb(30 41 59 / var(--tw-text-opacity));
}

.text-slate-900 {
  --tw-text-opacity: 1;
  color: rgb(15 23 42 / var(--tw-text-opacity));
}

.text-slate-950 {
  --tw-text-opacity: 1;
  color: rgb(2 6 23 / var(--tw-text-opacity));
}

.text-stone-100 {
  --tw-text-opacity: 1;
  color: rgb(245 245 244 / var(--tw-text-opacity));
}

.text-stone-200 {
  --tw-text-opacity: 1;
  color: rgb(231 229 228 / var(--tw-text-opacity));
}

.text-stone-300 {
  --tw-text-opacity: 1;
  color: rgb(214 211 209 / var(--tw-text-opacity));
}

.text-stone-400 {
  --tw-text-opacity: 1;
  color: rgb(168 162 158 / var(--tw-text-opacity));
}

.text-stone-50 {
  --tw-text-opacity: 1;
  color: rgb(250 250 249 / var(--tw-text-opacity));
}

.text-stone-500 {
  --tw-text-opacity: 1;
  color: rgb(120 113 108 / var(--tw-text-opacity));
}

.text-stone-600 {
  --tw-text-opacity: 1;
  color: rgb(87 83 78 / var(--tw-text-opacity));
}

.text-stone-700 {
  --tw-text-opacity: 1;
  color: rgb(68 64 60 / var(--tw-text-opacity));
}

.text-stone-800 {
  --tw-text-opacity: 1;
  color: rgb(41 37 36 / var(--tw-text-opacity));
}

.text-stone-900 {
  --tw-text-opacity: 1;
  color: rgb(28 25 23 / var(--tw-text-opacity));
}

.text-stone-950 {
  --tw-text-opacity: 1;
  color: rgb(12 10 9 / var(--tw-text-opacity));
}

.text-teal-100 {
  --tw-text-opacity: 1;
  color: rgb(204 251 241 / var(--tw-text-opacity));
}

.text-teal-200 {
  --tw-text-opacity: 1;
  color: rgb(153 246 228 / var(--tw-text-opacity));
}

.text-teal-300 {
  --tw-text-opacity: 1;
  color: rgb(94 234 212 / var(--tw-text-opacity));
}

.text-teal-400 {
  --tw-text-opacity: 1;
  color: rgb(45 212 191 / var(--tw-text-opacity));
}

.text-teal-50 {
  --tw-text-opacity: 1;
  color: rgb(240 253 250 / var(--tw-text-opacity));
}

.text-teal-500 {
  --tw-text-opacity: 1;
  color: rgb(20 184 166 / var(--tw-text-opacity));
}

.text-teal-600 {
  --tw-text-opacity: 1;
  color: rgb(13 148 136 / var(--tw-text-opacity));
}

.text-teal-700 {
  --tw-text-opacity: 1;
  color: rgb(15 118 110 / var(--tw-text-opacity));
}

.text-teal-800 {
  --tw-text-opacity: 1;
  color: rgb(17 94 89 / var(--tw-text-opacity));
}

.text-teal-900 {
  --tw-text-opacity: 1;
  color: rgb(19 78 74 / var(--tw-text-opacity));
}

.text-teal-950 {
  --tw-text-opacity: 1;
  color: rgb(4 47 46 / var(--tw-text-opacity));
}

.text-transparent {
  color: transparent;
}

.text-violet-100 {
  --tw-text-opacity: 1;
  color: rgb(237 233 254 / var(--tw-text-opacity));
}

.text-violet-200 {
  --tw-text-opacity: 1;
  color: rgb(221 214 254 / var(--tw-text-opacity));
}

.text-violet-300 {
  --tw-text-opacity: 1;
  color: rgb(196 181 253 / var(--tw-text-opacity));
}

.text-violet-400 {
  --tw-text-opacity: 1;
  color: rgb(167 139 250 / var(--tw-text-opacity));
}

.text-violet-50 {
  --tw-text-opacity: 1;
  color: rgb(245 243 255 / var(--tw-text-opacity));
}

.text-violet-500 {
  --tw-text-opacity: 1;
  color: rgb(139 92 246 / var(--tw-text-opacity));
}

.text-violet-600 {
  --tw-text-opacity: 1;
  color: rgb(124 58 237 / var(--tw-text-opacity));
}

.text-violet-700 {
  --tw-text-opacity: 1;
  color: rgb(109 40 217 / var(--tw-text-opacity));
}

.text-violet-800 {
  --tw-text-opacity: 1;
  color: rgb(91 33 182 / var(--tw-text-opacity));
}

.text-violet-900 {
  --tw-text-opacity: 1;
  color: rgb(76 29 149 / var(--tw-text-opacity));
}

.text-violet-950 {
  --tw-text-opacity: 1;
  color: rgb(46 16 101 / var(--tw-text-opacity));
}

.text-white {
  --tw-text-opacity: 1;
  color: rgb(255 255 255 / var(--tw-text-opacity));
}

.text-yellow-100 {
  --tw-text-opacity: 1;
  color: rgb(254 249 195 / var(--tw-text-opacity));
}

.text-yellow-200 {
  --tw-text-opacity: 1;
  color: rgb(254 240 138 / var(--tw-text-opacity));
}

.text-yellow-300 {
  --tw-text-opacity: 1;
  color: rgb(253 224 71 / var(--tw-text-opacity));
}

.text-yellow-400 {
  --tw-text-opacity: 1;
  color: rgb(250 204 21 / var(--tw-text-opacity));
}

.text-yellow-50 {
  --tw-text-opacity: 1;
  color: rgb(254 252 232 / var(--tw-text-opacity));
}

.text-yellow-500 {
  --tw-text-opacity: 1;
  color: rgb(234 179 8 / var(--tw-text-opacity));
}

.text-yellow-600 {
  --tw-text-opacity: 1;
  color: rgb(202 138 4 / var(--tw-text-opacity));
}

.text-yellow-700 {
  --tw-text-opacity: 1;
  color: rgb(161 98 7 / var(--tw-text-opacity));
}

.text-yellow-800 {
  --tw-text-opacity: 1;
  color: rgb(133 77 14 / var(--tw-text-opacity));
}

.text-yellow-900 {
  --tw-text-opacity: 1;
  color: rgb(113 63 18 / var(--tw-text-opacity));
}

.text-yellow-950 {
  --tw-text-opacity: 1;
  color: rgb(66 32 6 / var(--tw-text-opacity));
}

.text-zinc-100 {
  --tw-text-opacity: 1;
  color: rgb(244 244 245 / var(--tw-text-opacity));
}

.text-zinc-200 {
  --tw-text-opacity: 1;
  color: rgb(228 228 231 / var(--tw-text-opacity));
}

.text-zinc-300 {
  --tw-text-opacity: 1;
  color: rgb(212 212 216 / var(--tw-text-opacity));
}

.text-zinc-400 {
  --tw-text-opacity: 1;
  color: rgb(161 161 170 / var(--tw-text-opacity));
}

.text-zinc-50 {
  --tw-text-opacity: 1;
  color: rgb(250 250 250 / var(--tw-text-opacity));
}

.text-zinc-500 {
  --tw-text-opacity: 1;
  color: rgb(113 113 122 / var(--tw-text-opacity));
}

.text-zinc-600 {
  --tw-text-opacity: 1;
  color: rgb(82 82 91 / var(--tw-text-opacity));
}

.text-zinc-700 {
  --tw-text-opacity: 1;
  color: rgb(63 63 70 / var(--tw-text-opacity));
}

.text-zinc-800 {
  --tw-text-opacity: 1;
  color: rgb(39 39 42 / var(--tw-text-opacity));
}

.text-zinc-900 {
  --tw-text-opacity: 1;
  color: rgb(24 24 27 / var(--tw-text-opacity));
}

.text-zinc-950 {
  --tw-text-opacity: 1;
  color: rgb(9 9 11 / var(--tw-text-opacity));
}

.underline {
  text-decoration-line: underline;
}

.overline {
  text-decoration-line: overline;
}

.line-through {
  text-decoration-line: line-through;
}

.no-underline {
  text-decoration-line: none;
}

.decoration-amber-100 {
  text-decoration-color: #fef3c7;
}

.decoration-amber-200 {
  text-decoration-color: #fde68a;
}

.decoration-amber-300 {
  text-decoration-color: #fcd34d;
}

.decoration-amber-400 {
  text-decoration-color: #fbbf24;
}

.decoration-amber-50 {
  text-decoration-color: #fffbeb;
}

.decoration-amber-500 {
  text-decoration-color: #f59e0b;
}

.decoration-amber-600 {
  text-decoration-color: #d97706;
}

.decoration-amber-700 {
  text-decoration-color: #b45309;
}

.decoration-amber-800 {
  text-decoration-color: #92400e;
}

.decoration-amber-900 {
  text-decoration-color: #78350f;
}

.decoration-amber-950 {
  text-decoration-color: #451a03;
}

.decoration-black {
  text-decoration-color: #000;
}

.decoration-blue-100 {
  text-decoration-color: #dbeafe;
}

.decoration-blue-200 {
  text-decoration-color: #bfdbfe;
}

.decoration-blue-300 {
  text-decoration-color: #93c5fd;
}

.decoration-blue-400 {
  text-decoration-color: #60a5fa;
}

.decoration-blue-50 {
  text-decoration-color: #eff6ff;
}

.decoration-blue-500 {
  text-decoration-color: #3b82f6;
}

.decoration-blue-600 {
  text-decoration-color: #2563eb;
}

.decoration-blue-700 {
  text-decoration-color: #1d4ed8;
}

.decoration-blue-800 {
  text-decoration-color: #1e40af;
}

.decoration-blue-900 {
  text-decoration-color: #1e3a8a;
}

.decoration-blue-950 {
  text-decoration-color: #172554;
}

.decoration-current {
  text-decoration-color: currentColor;
}

.decoration-cyan-100 {
  text-decoration-color: #cffafe;
}

.decoration-cyan-200 {
  text-decoration-color: #a5f3fc;
}

.decoration-cyan-300 {
  text-decoration-color: #67e8f9;
}

.decoration-cyan-400 {
  text-decoration-color: #22d3ee;
}

.decoration-cyan-50 {
  text-decoration-color: #ecfeff;
}

.decoration-cyan-500 {
  text-decoration-color: #06b6d4;
}

.decoration-cyan-600 {
  text-decoration-color: #0891b2;
}

.decoration-cyan-700 {
  text-decoration-color: #0e7490;
}

.decoration-cyan-800 {
  text-decoration-color: #155e75;
}

.decoration-cyan-900 {
  text-decoration-color: #164e63;
}

.decoration-cyan-950 {
  text-decoration-color: #083344;
}

.decoration-emerald-100 {
  text-decoration-color: #d1fae5;
}

.decoration-emerald-200 {
  text-decoration-color: #a7f3d0;
}

.decoration-emerald-300 {
  text-decoration-color: #6ee7b7;
}

.decoration-emerald-400 {
  text-decoration-color: #34d399;
}

.decoration-emerald-50 {
  text-decoration-color: #ecfdf5;
}

.decoration-emerald-500 {
  text-decoration-color: #10b981;
}

.decoration-emerald-600 {
  text-decoration-color: #059669;
}

.decoration-emerald-700 {
  text-decoration-color: #047857;
}

.decoration-emerald-800 {
  text-decoration-color: #065f46;
}

.decoration-emerald-900 {
  text-decoration-color: #064e3b;
}

.decoration-emerald-950 {
  text-decoration-color: #022c22;
}

.decoration-fuchsia-100 {
  text-decoration-color: #fae8ff;
}

.decoration-fuchsia-200 {
  text-decoration-color: #f5d0fe;
}

.decoration-fuchsia-300 {
  text-decoration-color: #f0abfc;
}

.decoration-fuchsia-400 {
  text-decoration-color: #e879f9;
}

.decoration-fuchsia-50 {
  text-decoration-color: #fdf4ff;
}

.decoration-fuchsia-500 {
  text-decoration-color: #d946ef;
}

.decoration-fuchsia-600 {
  text-decoration-color: #c026d3;
}

.decoration-fuchsia-700 {
  text-decoration-color: #a21caf;
}

.decoration-fuchsia-800 {
  text-decoration-color: #86198f;
}

.decoration-fuchsia-900 {
  text-decoration-color: #701a75;
}

.decoration-fuchsia-950 {
  text-decoration-color: #4a044e;
}

.decoration-gray-100 {
  text-decoration-color: #f3f4f6;
}

.decoration-gray-200 {
  text-decoration-color: #e5e7eb;
}

.decoration-gray-300 {
  text-decoration-color: #d1d5db;
}

.decoration-gray-400 {
  text-decoration-color: #9ca3af;
}

.decoration-gray-50 {
  text-decoration-color: #f9fafb;
}

.decoration-gray-500 {
  text-decoration-color: #6b7280;
}

.decoration-gray-600 {
  text-decoration-color: #4b5563;
}

.decoration-gray-700 {
  text-decoration-color: #374151;
}

.decoration-gray-800 {
  text-decoration-color: #1f2937;
}

.decoration-gray-900 {
  text-decoration-color: #111827;
}

.decoration-gray-950 {
  text-decoration-color: #030712;
}

.decoration-green-100 {
  text-decoration-color: #dcfce7;
}

.decoration-green-200 {
  text-decoration-color: #bbf7d0;
}

.decoration-green-300 {
  text-decoration-color: #86efac;
}

.decoration-green-400 {
  text-decoration-color: #4ade80;
}

.decoration-green-50 {
  text-decoration-color: #f0fdf4;
}

.decoration-green-500 {
  text-decoration-color: #22c55e;
}

.decoration-green-600 {
  text-decoration-color: #16a34a;
}

.decoration-green-700 {
  text-decoration-color: #15803d;
}

.decoration-green-800 {
  text-decoration-color: #166534;
}

.decoration-green-900 {
  text-decoration-color: #14532d;
}

.decoration-green-950 {
  text-decoration-color: #052e16;
}

.decoration-indigo-100 {
  text-decoration-color: #e0e7ff;
}

.decoration-indigo-200 {
  text-decoration-color: #c7d2fe;
}

.decoration-indigo-300 {
  text-decoration-color: #a5b4fc;
}

.decoration-indigo-400 {
  text-decoration-color: #818cf8;
}

.decoration-indigo-50 {
  text-decoration-color: #eef2ff;
}

.decoration-indigo-500 {
  text-decoration-color: #6366f1;
}

.decoration-indigo-600 {
  text-decoration-color: #4f46e5;
}

.decoration-indigo-700 {
  text-decoration-color: #4338ca;
}

.decoration-indigo-800 {
  text-decoration-color: #3730a3;
}

.decoration-indigo-900 {
  text-decoration-color: #312e81;
}

.decoration-indigo-950 {
  text-decoration-color: #1e1b4b;
}

.decoration-inherit {
  text-decoration-color: inherit;
}

.decoration-lime-100 {
  text-decoration-color: #ecfccb;
}

.decoration-lime-200 {
  text-decoration-color: #d9f99d;
}

.decoration-lime-300 {
  text-decoration-color: #bef264;
}

.decoration-lime-400 {
  text-decoration-color: #a3e635;
}

.decoration-lime-50 {
  text-decoration-color: #f7fee7;
}

.decoration-lime-500 {
  text-decoration-color: #84cc16;
}

.decoration-lime-600 {
  text-decoration-color: #65a30d;
}

.decoration-lime-700 {
  text-decoration-color: #4d7c0f;
}

.decoration-lime-800 {
  text-decoration-color: #3f6212;
}

.decoration-lime-900 {
  text-decoration-color: #365314;
}

.decoration-lime-950 {
  text-decoration-color: #1a2e05;
}

.decoration-neutral-100 {
  text-decoration-color: #f5f5f5;
}

.decoration-neutral-200 {
  text-decoration-color: #e5e5e5;
}

.decoration-neutral-300 {
  text-decoration-color: #d4d4d4;
}

.decoration-neutral-400 {
  text-decoration-color: #a3a3a3;
}

.decoration-neutral-50 {
  text-decoration-color: #fafafa;
}

.decoration-neutral-500 {
  text-decoration-color: #737373;
}

.decoration-neutral-600 {
  text-decoration-color: #525252;
}

.decoration-neutral-700 {
  text-decoration-color: #404040;
}

.decoration-neutral-800 {
  text-decoration-color: #262626;
}

.decoration-neutral-900 {
  text-decoration-color: #171717;
}

.decoration-neutral-950 {
  text-decoration-color: #0a0a0a;
}

.decoration-orange-100 {
  text-decoration-color: #ffedd5;
}

.decoration-orange-200 {
  text-decoration-color: #fed7aa;
}

.decoration-orange-300 {
  text-decoration-color: #fdba74;
}

.decoration-orange-400 {
  text-decoration-color: #fb923c;
}

.decoration-orange-50 {
  text-decoration-color: #fff7ed;
}

.decoration-orange-500 {
  text-decoration-color: #f97316;
}

.decoration-orange-600 {
  text-decoration-color: #ea580c;
}

.decoration-orange-700 {
  text-decoration-color: #c2410c;
}

.decoration-orange-800 {
  text-decoration-color: #9a3412;
}

.decoration-orange-900 {
  text-decoration-color: #7c2d12;
}

.decoration-orange-950 {
  text-decoration-color: #431407;
}

.decoration-pink-100 {
  text-decoration-color: #fce7f3;
}

.decoration-pink-200 {
  text-decoration-color: #fbcfe8;
}

.decoration-pink-300 {
  text-decoration-color: #f9a8d4;
}

.decoration-pink-400 {
  text-decoration-color: #f472b6;
}

.decoration-pink-50 {
  text-decoration-color: #fdf2f8;
}

.decoration-pink-500 {
  text-decoration-color: #ec4899;
}

.decoration-pink-600 {
  text-decoration-color: #db2777;
}

.decoration-pink-700 {
  text-decoration-color: #be185d;
}

.decoration-pink-800 {
  text-decoration-color: #9d174d;
}

.decoration-pink-900 {
  text-decoration-color: #831843;
}

.decoration-pink-950 {
  text-decoration-color: #500724;
}

.decoration-purple-100 {
  text-decoration-color: #f3e8ff;
}

.decoration-purple-200 {
  text-decoration-color: #e9d5ff;
}

.decoration-purple-300 {
  text-decoration-color: #d8b4fe;
}

.decoration-purple-400 {
  text-decoration-color: #c084fc;
}

.decoration-purple-50 {
  text-decoration-color: #faf5ff;
}

.decoration-purple-500 {
  text-decoration-color: #a855f7;
}

.decoration-purple-600 {
  text-decoration-color: #9333ea;
}

.decoration-purple-700 {
  text-decoration-color: #7e22ce;
}

.decoration-purple-800 {
  text-decoration-color: #6b21a8;
}

.decoration-purple-900 {
  text-decoration-color: #581c87;
}

.decoration-purple-950 {
  text-decoration-color: #3b0764;
}

.decoration-red-100 {
  text-decoration-color: #fee2e2;
}

.decoration-red-200 {
  text-decoration-color: #fecaca;
}

.decoration-red-300 {
  text-decoration-color: #fca5a5;
}

.decoration-red-400 {
  text-decoration-color: #f87171;
}

.decoration-red-50 {
  text-decoration-color: #fef2f2;
}

.decoration-red-500 {
  text-decoration-color: #ef4444;
}

.decoration-red-600 {
  text-decoration-color: #dc2626;
}

.decoration-red-700 {
  text-decoration-color: #b91c1c;
}

.decoration-red-800 {
  text-decoration-color: #991b1b;
}

.decoration-red-900 {
  text-decoration-color: #7f1d1d;
}

.decoration-red-950 {
  text-decoration-color: #450a0a;
}

.decoration-rose-100 {
  text-decoration-color: #ffe4e6;
}

.decoration-rose-200 {
  text-decoration-color: #fecdd3;
}

.decoration-rose-300 {
  text-decoration-color: #fda4af;
}

.decoration-rose-400 {
  text-decoration-color: #fb7185;
}

.decoration-rose-50 {
  text-decoration-color: #fff1f2;
}

.decoration-rose-500 {
  text-decoration-color: #f43f5e;
}

.decoration-rose-600 {
  text-decoration-color: #e11d48;
}

.decoration-rose-700 {
  text-decoration-color: #be123c;
}

.decoration-rose-800 {
  text-decoration-color: #9f1239;
}

.decoration-rose-900 {
  text-decoration-color: #881337;
}

.decoration-rose-950 {
  text-decoration-color: #4c0519;
}

.decoration-sky-100 {
  text-decoration-color: #e0f2fe;
}

.decoration-sky-200 {
  text-decoration-color: #bae6fd;
}

.decoration-sky-300 {
  text-decoration-color: #7dd3fc;
}

.decoration-sky-400 {
  text-decoration-color: #38bdf8;
}

.decoration-sky-50 {
  text-decoration-color: #f0f9ff;
}

.decoration-sky-500 {
  text-decoration-color: #0ea5e9;
}

.decoration-sky-600 {
  text-decoration-color: #0284c7;
}

.decoration-sky-700 {
  text-decoration-color: #0369a1;
}

.decoration-sky-800 {
  text-decoration-color: #075985;
}

.decoration-sky-900 {
  text-decoration-color: #0c4a6e;
}

.decoration-sky-950 {
  text-decoration-color: #082f49;
}

.decoration-slate-100 {
  text-decoration-color: #f1f5f9;
}

.decoration-slate-200 {
  text-decoration-color: #e2e8f0;
}

.decoration-slate-300 {
  text-decoration-color: #cbd5e1;
}

.decoration-slate-400 {
  text-decoration-color: #94a3b8;
}

.decoration-slate-50 {
  text-decoration-color: #f8fafc;
}

.decoration-slate-500 {
  text-decoration-color: #64748b;
}

.decoration-slate-600 {
  text-decoration-color: #475569;
}

.decoration-slate-700 {
  text-decoration-color: #334155;
}

.decoration-slate-800 {
  text-decoration-color: #1e293b;
}

.decoration-slate-900 {
  text-decoration-color: #0f172a;
}

.decoration-slate-950 {
  text-decoration-color: #020617;
}

.decoration-stone-100 {
  text-decoration-color: #f5f5f4;
}

.decoration-stone-200 {
  text-decoration-color: #e7e5e4;
}

.decoration-stone-300 {
  text-decoration-color: #d6d3d1;
}

.decoration-stone-400 {
  text-decoration-color: #a8a29e;
}

.decoration-stone-50 {
  text-decoration-color: #fafaf9;
}

.decoration-stone-500 {
  text-decoration-color: #78716c;
}

.decoration-stone-600 {
  text-decoration-color: #57534e;
}

.decoration-stone-700 {
  text-decoration-color: #44403c;
}

.decoration-stone-800 {
  text-decoration-color: #292524;
}

.decoration-stone-900 {
  text-decoration-color: #1c1917;
}

.decoration-stone-950 {
  text-decoration-color: #0c0a09;
}

.decoration-teal-100 {
  text-decoration-color: #ccfbf1;
}

.decoration-teal-200 {
  text-decoration-color: #99f6e4;
}

.decoration-teal-300 {
  text-decoration-color: #5eead4;
}

.decoration-teal-400 {
  text-decoration-color: #2dd4bf;
}

.decoration-teal-50 {
  text-decoration-color: #f0fdfa;
}

.decoration-teal-500 {
  text-decoration-color: #14b8a6;
}

.decoration-teal-600 {
  text-decoration-color: #0d9488;
}

.decoration-teal-700 {
  text-decoration-color: #0f766e;
}

.decoration-teal-800 {
  text-decoration-color: #115e59;
}

.decoration-teal-900 {
  text-decoration-color: #134e4a;
}

.decoration-teal-950 {
  text-decoration-color: #042f2e;
}

.decoration-transparent {
  text-decoration-color: transparent;
}

.decoration-violet-100 {
  text-decoration-color: #ede9fe;
}

.decoration-violet-200 {
  text-decoration-color: #ddd6fe;
}

.decoration-violet-300 {
  text-decoration-color: #c4b5fd;
}

.decoration-violet-400 {
  text-decoration-color: #a78bfa;
}

.decoration-violet-50 {
  text-decoration-color: #f5f3ff;
}

.decoration-violet-500 {
  text-decoration-color: #8b5cf6;
}

.decoration-violet-600 {
  text-decoration-color: #7c3aed;
}

.decoration-violet-700 {
  text-decoration-color: #6d28d9;
}

.decoration-violet-800 {
  text-decoration-color: #5b21b6;
}

.decoration-violet-900 {
  text-decoration-color: #4c1d95;
}

.decoration-violet-950 {
  text-decoration-color: #2e1065;
}

.decoration-white {
  text-decoration-color: #fff;
}

.decoration-yellow-100 {
  text-decoration-color: #fef9c3;
}

.decoration-yellow-200 {
  text-decoration-color: #fef08a;
}

.decoration-yellow-300 {
  text-decoration-color: #fde047;
}

.decoration-yellow-400 {
  text-decoration-color: #facc15;
}

.decoration-yellow-50 {
  text-decoration-color: #fefce8;
}

.decoration-yellow-500 {
  text-decoration-color: #eab308;
}

.decoration-yellow-600 {
  text-decoration-color: #ca8a04;
}

.decoration-yellow-700 {
  text-decoration-color: #a16207;
}

.decoration-yellow-800 {
  text-decoration-color: #854d0e;
}

.decoration-yellow-900 {
  text-decoration-color: #713f12;
}

.decoration-yellow-950 {
  text-decoration-color: #422006;
}

.decoration-zinc-100 {
  text-decoration-color: #f4f4f5;
}

.decoration-zinc-200 {
  text-decoration-color: #e4e4e7;
}

.decoration-zinc-300 {
  text-decoration-color: #d4d4d8;
}

.decoration-zinc-400 {
  text-decoration-color: #a1a1aa;
}

.decoration-zinc-50 {
  text-decoration-color: #fafafa;
}

.decoration-zinc-500 {
  text-decoration-color: #71717a;
}

.decoration-zinc-600 {
  text-decoration-color: #52525b;
}

.decoration-zinc-700 {
  text-decoration-color: #3f3f46;
}

.decoration-zinc-800 {
  text-decoration-color: #27272a;
}

.decoration-zinc-900 {
  text-decoration-color: #18181b;
}

.decoration-zinc-950 {
  text-decoration-color: #09090b;
}

.decoration-solid {
  text-decoration-style: solid;
}

.decoration-double {
  text-decoration-style: double;
}

.decoration-dotted {
  text-decoration-style: dotted;
}

.decoration-dashed {
  text-decoration-style: dashed;
}

.decoration-wavy {
  text-decoration-style: wavy;
}

.decoration-0 {
  text-decoration-thickness: 0px;
}

.decoration-1 {
  text-decoration-thickness: 1px;
}

.decoration-2 {
  text-decoration-thickness: 2px;
}

.decoration-4 {
  text-decoration-thickness: 4px;
}

.decoration-8 {
  text-decoration-thickness: 8px;
}

.decoration-auto {
  text-decoration-thickness: auto;
}

.decoration-from-font {
  text-decoration-thickness: from-font;
}

.underline-offset-0 {
  text-underline-offset: 0px;
}

.underline-offset-1 {
  text-underline-offset: 1px;
}

.underline-offset-2 {
  text-underline-offset: 2px;
}

.underline-offset-4 {
  text-underline-offset: 4px;
}

.underline-offset-8 {
  text-underline-offset: 8px;
}

.underline-offset-auto {
  text-underline-offset: auto;
}

.antialiased {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.subpixel-antialiased {
  -webkit-font-smoothing: auto;
  -moz-osx-font-smoothing: auto;
}

.caret-amber-100 {
  caret-color: #fef3c7;
}

.caret-amber-200 {
  caret-color: #fde68a;
}

.caret-amber-300 {
  caret-color: #fcd34d;
}

.caret-amber-400 {
  caret-color: #fbbf24;
}

.caret-amber-50 {
  caret-color: #fffbeb;
}

.caret-amber-500 {
  caret-color: #f59e0b;
}

.caret-amber-600 {
  caret-color: #d97706;
}

.caret-amber-700 {
  caret-color: #b45309;
}

.caret-amber-800 {
  caret-color: #92400e;
}

.caret-amber-900 {
  caret-color: #78350f;
}

.caret-amber-950 {
  caret-color: #451a03;
}

.caret-black {
  caret-color: #000;
}

.caret-blue-100 {
  caret-color: #dbeafe;
}

.caret-blue-200 {
  caret-color: #bfdbfe;
}

.caret-blue-300 {
  caret-color: #93c5fd;
}

.caret-blue-400 {
  caret-color: #60a5fa;
}

.caret-blue-50 {
  caret-color: #eff6ff;
}

.caret-blue-500 {
  caret-color: #3b82f6;
}

.caret-blue-600 {
  caret-color: #2563eb;
}

.caret-blue-700 {
  caret-color: #1d4ed8;
}

.caret-blue-800 {
  caret-color: #1e40af;
}

.caret-blue-900 {
  caret-color: #1e3a8a;
}

.caret-blue-950 {
  caret-color: #172554;
}

.caret-current {
  caret-color: currentColor;
}

.caret-cyan-100 {
  caret-color: #cffafe;
}

.caret-cyan-200 {
  caret-color: #a5f3fc;
}

.caret-cyan-300 {
  caret-color: #67e8f9;
}

.caret-cyan-400 {
  caret-color: #22d3ee;
}

.caret-cyan-50 {
  caret-color: #ecfeff;
}

.caret-cyan-500 {
  caret-color: #06b6d4;
}

.caret-cyan-600 {
  caret-color: #0891b2;
}

.caret-cyan-700 {
  caret-color: #0e7490;
}

.caret-cyan-800 {
  caret-color: #155e75;
}

.caret-cyan-900 {
  caret-color: #164e63;
}

.caret-cyan-950 {
  caret-color: #083344;
}

.caret-emerald-100 {
  caret-color: #d1fae5;
}

.caret-emerald-200 {
  caret-color: #a7f3d0;
}

.caret-emerald-300 {
  caret-color: #6ee7b7;
}

.caret-emerald-400 {
  caret-color: #34d399;
}

.caret-emerald-50 {
  caret-color: #ecfdf5;
}

.caret-emerald-500 {
  caret-color: #10b981;
}

.caret-emerald-600 {
  caret-color: #059669;
}

.caret-emerald-700 {
  caret-color: #047857;
}

.caret-emerald-800 {
  caret-color: #065f46;
}

.caret-emerald-900 {
  caret-color: #064e3b;
}

.caret-emerald-950 {
  caret-color: #022c22;
}

.caret-fuchsia-100 {
  caret-color: #fae8ff;
}

.caret-fuchsia-200 {
  caret-color: #f5d0fe;
}

.caret-fuchsia-300 {
  caret-color: #f0abfc;
}

.caret-fuchsia-400 {
  caret-color: #e879f9;
}

.caret-fuchsia-50 {
  caret-color: #fdf4ff;
}

.caret-fuchsia-500 {
  caret-color: #d946ef;
}

.caret-fuchsia-600 {
  caret-color: #c026d3;
}

.caret-fuchsia-700 {
  caret-color: #a21caf;
}

.caret-fuchsia-800 {
  caret-color: #86198f;
}

.caret-fuchsia-900 {
  caret-color: #701a75;
}

.caret-fuchsia-950 {
  caret-color: #4a044e;
}

.caret-gray-100 {
  caret-color: #f3f4f6;
}

.caret-gray-200 {
  caret-color: #e5e7eb;
}

.caret-gray-300 {
  caret-color: #d1d5db;
}

.caret-gray-400 {
  caret-color: #9ca3af;
}

.caret-gray-50 {
  caret-color: #f9fafb;
}

.caret-gray-500 {
  caret-color: #6b7280;
}

.caret-gray-600 {
  caret-color: #4b5563;
}

.caret-gray-700 {
  caret-color: #374151;
}

.caret-gray-800 {
  caret-color: #1f2937;
}

.caret-gray-900 {
  caret-color: #111827;
}

.caret-gray-950 {
  caret-color: #030712;
}

.caret-green-100 {
  caret-color: #dcfce7;
}

.caret-green-200 {
  caret-color: #bbf7d0;
}

.caret-green-300 {
  caret-color: #86efac;
}

.caret-green-400 {
  caret-color: #4ade80;
}

.caret-green-50 {
  caret-color: #f0fdf4;
}

.caret-green-500 {
  caret-color: #22c55e;
}

.caret-green-600 {
  caret-color: #16a34a;
}

.caret-green-700 {
  caret-color: #15803d;
}

.caret-green-800 {
  caret-color: #166534;
}

.caret-green-900 {
  caret-color: #14532d;
}

.caret-green-950 {
  caret-color: #052e16;
}

.caret-indigo-100 {
  caret-color: #e0e7ff;
}

.caret-indigo-200 {
  caret-color: #c7d2fe;
}

.caret-indigo-300 {
  caret-color: #a5b4fc;
}

.caret-indigo-400 {
  caret-color: #818cf8;
}

.caret-indigo-50 {
  caret-color: #eef2ff;
}

.caret-indigo-500 {
  caret-color: #6366f1;
}

.caret-indigo-600 {
  caret-color: #4f46e5;
}

.caret-indigo-700 {
  caret-color: #4338ca;
}

.caret-indigo-800 {
  caret-color: #3730a3;
}

.caret-indigo-900 {
  caret-color: #312e81;
}

.caret-indigo-950 {
  caret-color: #1e1b4b;
}

.caret-inherit {
  caret-color: inherit;
}

.caret-lime-100 {
  caret-color: #ecfccb;
}

.caret-lime-200 {
  caret-color: #d9f99d;
}

.caret-lime-300 {
  caret-color: #bef264;
}

.caret-lime-400 {
  caret-color: #a3e635;
}

.caret-lime-50 {
  caret-color: #f7fee7;
}

.caret-lime-500 {
  caret-color: #84cc16;
}

.caret-lime-600 {
  caret-color: #65a30d;
}

.caret-lime-700 {
  caret-color: #4d7c0f;
}

.caret-lime-800 {
  caret-color: #3f6212;
}

.caret-lime-900 {
  caret-color: #365314;
}

.caret-lime-950 {
  caret-color: #1a2e05;
}

.caret-neutral-100 {
  caret-color: #f5f5f5;
}

.caret-neutral-200 {
  caret-color: #e5e5e5;
}

.caret-neutral-300 {
  caret-color: #d4d4d4;
}

.caret-neutral-400 {
  caret-color: #a3a3a3;
}

.caret-neutral-50 {
  caret-color: #fafafa;
}

.caret-neutral-500 {
  caret-color: #737373;
}

.caret-neutral-600 {
  caret-color: #525252;
}

.caret-neutral-700 {
  caret-color: #404040;
}

.caret-neutral-800 {
  caret-color: #262626;
}

.caret-neutral-900 {
  caret-color: #171717;
}

.caret-neutral-950 {
  caret-color: #0a0a0a;
}

.caret-orange-100 {
  caret-color: #ffedd5;
}

.caret-orange-200 {
  caret-color: #fed7aa;
}

.caret-orange-300 {
  caret-color: #fdba74;
}

.caret-orange-400 {
  caret-color: #fb923c;
}

.caret-orange-50 {
  caret-color: #fff7ed;
}

.caret-orange-500 {
  caret-color: #f97316;
}

.caret-orange-600 {
  caret-color: #ea580c;
}

.caret-orange-700 {
  caret-color: #c2410c;
}

.caret-orange-800 {
  caret-color: #9a3412;
}

.caret-orange-900 {
  caret-color: #7c2d12;
}

.caret-orange-950 {
  caret-color: #431407;
}

.caret-pink-100 {
  caret-color: #fce7f3;
}

.caret-pink-200 {
  caret-color: #fbcfe8;
}

.caret-pink-300 {
  caret-color: #f9a8d4;
}

.caret-pink-400 {
  caret-color: #f472b6;
}

.caret-pink-50 {
  caret-color: #fdf2f8;
}

.caret-pink-500 {
  caret-color: #ec4899;
}

.caret-pink-600 {
  caret-color: #db2777;
}

.caret-pink-700 {
  caret-color: #be185d;
}

.caret-pink-800 {
  caret-color: #9d174d;
}

.caret-pink-900 {
  caret-color: #831843;
}

.caret-pink-950 {
  caret-color: #500724;
}

.caret-purple-100 {
  caret-color: #f3e8ff;
}

.caret-purple-200 {
  caret-color: #e9d5ff;
}

.caret-purple-300 {
  caret-color: #d8b4fe;
}

.caret-purple-400 {
  caret-color: #c084fc;
}

.caret-purple-50 {
  caret-color: #faf5ff;
}

.caret-purple-500 {
  caret-color: #a855f7;
}

.caret-purple-600 {
  caret-color: #9333ea;
}

.caret-purple-700 {
  caret-color: #7e22ce;
}

.caret-purple-800 {
  caret-color: #6b21a8;
}

.caret-purple-900 {
  caret-color: #581c87;
}

.caret-purple-950 {
  caret-color: #3b0764;
}

.caret-red-100 {
  caret-color: #fee2e2;
}

.caret-red-200 {
  caret-color: #fecaca;
}

.caret-red-300 {
  caret-color: #fca5a5;
}

.caret-red-400 {
  caret-color: #f87171;
}

.caret-red-50 {
  caret-color: #fef2f2;
}

.caret-red-500 {
  caret-color: #ef4444;
}

.caret-red-600 {
  caret-color: #dc2626;
}

.caret-red-700 {
  caret-color: #b91c1c;
}

.caret-red-800 {
  caret-color: #991b1b;
}

.caret-red-900 {
  caret-color: #7f1d1d;
}

.caret-red-950 {
  caret-color: #450a0a;
}

.caret-rose-100 {
  caret-color: #ffe4e6;
}

.caret-rose-200 {
  caret-color: #fecdd3;
}

.caret-rose-300 {
  caret-color: #fda4af;
}

.caret-rose-400 {
  caret-color: #fb7185;
}

.caret-rose-50 {
  caret-color: #fff1f2;
}

.caret-rose-500 {
  caret-color: #f43f5e;
}

.caret-rose-600 {
  caret-color: #e11d48;
}

.caret-rose-700 {
  caret-color: #be123c;
}

.caret-rose-800 {
  caret-color: #9f1239;
}

.caret-rose-900 {
  caret-color: #881337;
}

.caret-rose-950 {
  caret-color: #4c0519;
}

.caret-sky-100 {
  caret-color: #e0f2fe;
}

.caret-sky-200 {
  caret-color: #bae6fd;
}

.caret-sky-300 {
  caret-color: #7dd3fc;
}

.caret-sky-400 {
  caret-color: #38bdf8;
}

.caret-sky-50 {
  caret-color: #f0f9ff;
}

.caret-sky-500 {
  caret-color: #0ea5e9;
}

.caret-sky-600 {
  caret-color: #0284c7;
}

.caret-sky-700 {
  caret-color: #0369a1;
}

.caret-sky-800 {
  caret-color: #075985;
}

.caret-sky-900 {
  caret-color: #0c4a6e;
}

.caret-sky-950 {
  caret-color: #082f49;
}

.caret-slate-100 {
  caret-color: #f1f5f9;
}

.caret-slate-200 {
  caret-color: #e2e8f0;
}

.caret-slate-300 {
  caret-color: #cbd5e1;
}

.caret-slate-400 {
  caret-color: #94a3b8;
}

.caret-slate-50 {
  caret-color: #f8fafc;
}

.caret-slate-500 {
  caret-color: #64748b;
}

.caret-slate-600 {
  caret-color: #475569;
}

.caret-slate-700 {
  caret-color: #334155;
}

.caret-slate-800 {
  caret-color: #1e293b;
}

.caret-slate-900 {
  caret-color: #0f172a;
}

.caret-slate-950 {
  caret-color: #020617;
}

.caret-stone-100 {
  caret-color: #f5f5f4;
}

.caret-stone-200 {
  caret-color: #e7e5e4;
}

.caret-stone-300 {
  caret-color: #d6d3d1;
}

.caret-stone-400 {
  caret-color: #a8a29e;
}

.caret-stone-50 {
  caret-color: #fafaf9;
}

.caret-stone-500 {
  caret-color: #78716c;
}

.caret-stone-600 {
  caret-color: #57534e;
}

.caret-stone-700 {
  caret-color: #44403c;
}

.caret-stone-800 {
  caret-color: #292524;
}

.caret-stone-900 {
  caret-color: #1c1917;
}

.caret-stone-950 {
  caret-color: #0c0a09;
}

.caret-teal-100 {
  caret-color: #ccfbf1;
}

.caret-teal-200 {
  caret-color: #99f6e4;
}

.caret-teal-300 {
  caret-color: #5eead4;
}

.caret-teal-400 {
  caret-color: #2dd4bf;
}

.caret-teal-50 {
  caret-color: #f0fdfa;
}

.caret-teal-500 {
  caret-color: #14b8a6;
}

.caret-teal-600 {
  caret-color: #0d9488;
}

.caret-teal-700 {
  caret-color: #0f766e;
}

.caret-teal-800 {
  caret-color: #115e59;
}

.caret-teal-900 {
  caret-color: #134e4a;
}

.caret-teal-950 {
  caret-color: #042f2e;
}

.caret-transparent {
  caret-color: transparent;
}

.caret-violet-100 {
  caret-color: #ede9fe;
}

.caret-violet-200 {
  caret-color: #ddd6fe;
}

.caret-violet-300 {
  caret-color: #c4b5fd;
}

.caret-violet-400 {
  caret-color: #a78bfa;
}

.caret-violet-50 {
  caret-color: #f5f3ff;
}

.caret-violet-500 {
  caret-color: #8b5cf6;
}

.caret-violet-600 {
  caret-color: #7c3aed;
}

.caret-violet-700 {
  caret-color: #6d28d9;
}

.caret-violet-800 {
  caret-color: #5b21b6;
}

.caret-violet-900 {
  caret-color: #4c1d95;
}

.caret-violet-950 {
  caret-color: #2e1065;
}

.caret-white {
  caret-color: #fff;
}

.caret-yellow-100 {
  caret-color: #fef9c3;
}

.caret-yellow-200 {
  caret-color: #fef08a;
}

.caret-yellow-300 {
  caret-color: #fde047;
}

.caret-yellow-400 {
  caret-color: #facc15;
}

.caret-yellow-50 {
  caret-color: #fefce8;
}

.caret-yellow-500 {
  caret-color: #eab308;
}

.caret-yellow-600 {
  caret-color: #ca8a04;
}

.caret-yellow-700 {
  caret-color: #a16207;
}

.caret-yellow-800 {
  caret-color: #854d0e;
}

.caret-yellow-900 {
  caret-color: #713f12;
}

.caret-yellow-950 {
  caret-color: #422006;
}

.caret-zinc-100 {
  caret-color: #f4f4f5;
}

.caret-zinc-200 {
  caret-color: #e4e4e7;
}

.caret-zinc-300 {
  caret-color: #d4d4d8;
}

.caret-zinc-400 {
  caret-color: #a1a1aa;
}

.caret-zinc-50 {
  caret-color: #fafafa;
}

.caret-zinc-500 {
  caret-color: #71717a;
}

.caret-zinc-600 {
  caret-color: #52525b;
}

.caret-zinc-700 {
  caret-color: #3f3f46;
}

.caret-zinc-800 {
  caret-color: #27272a;
}

.caret-zinc-900 {
  caret-color: #18181b;
}

.caret-zinc-950 {
  caret-color: #09090b;
}

.accent-amber-100 {
  accent-color: #fef3c7;
}

.accent-amber-200 {
  accent-color: #fde68a;
}

.accent-amber-300 {
  accent-color: #fcd34d;
}

.accent-amber-400 {
  accent-color: #fbbf24;
}

.accent-amber-50 {
  accent-color: #fffbeb;
}

.accent-amber-500 {
  accent-color: #f59e0b;
}

.accent-amber-600 {
  accent-color: #d97706;
}

.accent-amber-700 {
  accent-color: #b45309;
}

.accent-amber-800 {
  accent-color: #92400e;
}

.accent-amber-900 {
  accent-color: #78350f;
}

.accent-amber-950 {
  accent-color: #451a03;
}

.accent-auto {
  accent-color: auto;
}

.accent-black {
  accent-color: #000;
}

.accent-blue-100 {
  accent-color: #dbeafe;
}

.accent-blue-200 {
  accent-color: #bfdbfe;
}

.accent-blue-300 {
  accent-color: #93c5fd;
}

.accent-blue-400 {
  accent-color: #60a5fa;
}

.accent-blue-50 {
  accent-color: #eff6ff;
}

.accent-blue-500 {
  accent-color: #3b82f6;
}

.accent-blue-600 {
  accent-color: #2563eb;
}

.accent-blue-700 {
  accent-color: #1d4ed8;
}

.accent-blue-800 {
  accent-color: #1e40af;
}

.accent-blue-900 {
  accent-color: #1e3a8a;
}

.accent-blue-950 {
  accent-color: #172554;
}

.accent-current {
  accent-color: currentColor;
}

.accent-cyan-100 {
  accent-color: #cffafe;
}

.accent-cyan-200 {
  accent-color: #a5f3fc;
}

.accent-cyan-300 {
  accent-color: #67e8f9;
}

.accent-cyan-400 {
  accent-color: #22d3ee;
}

.accent-cyan-50 {
  accent-color: #ecfeff;
}

.accent-cyan-500 {
  accent-color: #06b6d4;
}

.accent-cyan-600 {
  accent-color: #0891b2;
}

.accent-cyan-700 {
  accent-color: #0e7490;
}

.accent-cyan-800 {
  accent-color: #155e75;
}

.accent-cyan-900 {
  accent-color: #164e63;
}

.accent-cyan-950 {
  accent-color: #083344;
}

.accent-emerald-100 {
  accent-color: #d1fae5;
}

.accent-emerald-200 {
  accent-color: #a7f3d0;
}

.accent-emerald-300 {
  accent-color: #6ee7b7;
}

.accent-emerald-400 {
  accent-color: #34d399;
}

.accent-emerald-50 {
  accent-color: #ecfdf5;
}

.accent-emerald-500 {
  accent-color: #10b981;
}

.accent-emerald-600 {
  accent-color: #059669;
}

.accent-emerald-700 {
  accent-color: #047857;
}

.accent-emerald-800 {
  accent-color: #065f46;
}

.accent-emerald-900 {
  accent-color: #064e3b;
}

.accent-emerald-950 {
  accent-color: #022c22;
}

.accent-fuchsia-100 {
  accent-color: #fae8ff;
}

.accent-fuchsia-200 {
  accent-color: #f5d0fe;
}

.accent-fuchsia-300 {
  accent-color: #f0abfc;
}

.accent-fuchsia-400 {
  accent-color: #e879f9;
}

.accent-fuchsia-50 {
  accent-color: #fdf4ff;
}

.accent-fuchsia-500 {
  accent-color: #d946ef;
}

.accent-fuchsia-600 {
  accent-color: #c026d3;
}

.accent-fuchsia-700 {
  accent-color: #a21caf;
}

.accent-fuchsia-800 {
  accent-color: #86198f;
}

.accent-fuchsia-900 {
  accent-color: #701a75;
}

.accent-fuchsia-950 {
  accent-color: #4a044e;
}

.accent-gray-100 {
  accent-color: #f3f4f6;
}

.accent-gray-200 {
  accent-color: #e5e7eb;
}

.accent-gray-300 {
  accent-color: #d1d5db;
}

.accent-gray-400 {
  accent-color: #9ca3af;
}

.accent-gray-50 {
  accent-color: #f9fafb;
}

.accent-gray-500 {
  accent-color: #6b7280;
}

.accent-gray-600 {
  accent-color: #4b5563;
}

.accent-gray-700 {
  accent-color: #374151;
}

.accent-gray-800 {
  accent-color: #1f2937;
}

.accent-gray-900 {
  accent-color: #111827;
}

.accent-gray-950 {
  accent-color: #030712;
}

.accent-green-100 {
  accent-color: #dcfce7;
}

.accent-green-200 {
  accent-color: #bbf7d0;
}

.accent-green-300 {
  accent-color: #86efac;
}

.accent-green-400 {
  accent-color: #4ade80;
}

.accent-green-50 {
  accent-color: #f0fdf4;
}

.accent-green-500 {
  accent-color: #22c55e;
}

.accent-green-600 {
  accent-color: #16a34a;
}

.accent-green-700 {
  accent-color: #15803d;
}

.accent-green-800 {
  accent-color: #166534;
}

.accent-green-900 {
  accent-color: #14532d;
}

.accent-green-950 {
  accent-color: #052e16;
}

.accent-indigo-100 {
  accent-color: #e0e7ff;
}

.accent-indigo-200 {
  accent-color: #c7d2fe;
}

.accent-indigo-300 {
  accent-color: #a5b4fc;
}

.accent-indigo-400 {
  accent-color: #818cf8;
}

.accent-indigo-50 {
  accent-color: #eef2ff;
}

.accent-indigo-500 {
  accent-color: #6366f1;
}

.accent-indigo-600 {
  accent-color: #4f46e5;
}

.accent-indigo-700 {
  accent-color: #4338ca;
}

.accent-indigo-800 {
  accent-color: #3730a3;
}

.accent-indigo-900 {
  accent-color: #312e81;
}

.accent-indigo-950 {
  accent-color: #1e1b4b;
}

.accent-inherit {
  accent-color: inherit;
}

.accent-lime-100 {
  accent-color: #ecfccb;
}

.accent-lime-200 {
  accent-color: #d9f99d;
}

.accent-lime-300 {
  accent-color: #bef264;
}

.accent-lime-400 {
  accent-color: #a3e635;
}

.accent-lime-50 {
  accent-color: #f7fee7;
}

.accent-lime-500 {
  accent-color: #84cc16;
}

.accent-lime-600 {
  accent-color: #65a30d;
}

.accent-lime-700 {
  accent-color: #4d7c0f;
}

.accent-lime-800 {
  accent-color: #3f6212;
}

.accent-lime-900 {
  accent-color: #365314;
}

.accent-lime-950 {
  accent-color: #1a2e05;
}

.accent-neutral-100 {
  accent-color: #f5f5f5;
}

.accent-neutral-200 {
  accent-color: #e5e5e5;
}

.accent-neutral-300 {
  accent-color: #d4d4d4;
}

.accent-neutral-400 {
  accent-color: #a3a3a3;
}

.accent-neutral-50 {
  accent-color: #fafafa;
}

.accent-neutral-500 {
  accent-color: #737373;
}

.accent-neutral-600 {
  accent-color: #525252;
}

.accent-neutral-700 {
  accent-color: #404040;
}

.accent-neutral-800 {
  accent-color: #262626;
}

.accent-neutral-900 {
  accent-color: #171717;
}

.accent-neutral-950 {
  accent-color: #0a0a0a;
}

.accent-orange-100 {
  accent-color: #ffedd5;
}

.accent-orange-200 {
  accent-color: #fed7aa;
}

.accent-orange-300 {
  accent-color: #fdba74;
}

.accent-orange-400 {
  accent-color: #fb923c;
}

.accent-orange-50 {
  accent-color: #fff7ed;
}

.accent-orange-500 {
  accent-color: #f97316;
}

.accent-orange-600 {
  accent-color: #ea580c;
}

.accent-orange-700 {
  accent-color: #c2410c;
}

.accent-orange-800 {
  accent-color: #9a3412;
}

.accent-orange-900 {
  accent-color: #7c2d12;
}

.accent-orange-950 {
  accent-color: #431407;
}

.accent-pink-100 {
  accent-color: #fce7f3;
}

.accent-pink-200 {
  accent-color: #fbcfe8;
}

.accent-pink-300 {
  accent-color: #f9a8d4;
}

.accent-pink-400 {
  accent-color: #f472b6;
}

.accent-pink-50 {
  accent-color: #fdf2f8;
}

.accent-pink-500 {
  accent-color: #ec4899;
}

.accent-pink-600 {
  accent-color: #db2777;
}

.accent-pink-700 {
  accent-color: #be185d;
}

.accent-pink-800 {
  accent-color: #9d174d;
}

.accent-pink-900 {
  accent-color: #831843;
}

.accent-pink-950 {
  accent-color: #500724;
}

.accent-purple-100 {
  accent-color: #f3e8ff;
}

.accent-purple-200 {
  accent-color: #e9d5ff;
}

.accent-purple-300 {
  accent-color: #d8b4fe;
}

.accent-purple-400 {
  accent-color: #c084fc;
}

.accent-purple-50 {
  accent-color: #faf5ff;
}

.accent-purple-500 {
  accent-color: #a855f7;
}

.accent-purple-600 {
  accent-color: #9333ea;
}

.accent-purple-700 {
  accent-color: #7e22ce;
}

.accent-purple-800 {
  accent-color: #6b21a8;
}

.accent-purple-900 {
  accent-color: #581c87;
}

.accent-purple-950 {
  accent-color: #3b0764;
}

.accent-red-100 {
  accent-color: #fee2e2;
}

.accent-red-200 {
  accent-color: #fecaca;
}

.accent-red-300 {
  accent-color: #fca5a5;
}

.accent-red-400 {
  accent-color: #f87171;
}

.accent-red-50 {
  accent-color: #fef2f2;
}

.accent-red-500 {
  accent-color: #ef4444;
}

.accent-red-600 {
  accent-color: #dc2626;
}

.accent-red-700 {
  accent-color: #b91c1c;
}

.accent-red-800 {
  accent-color: #991b1b;
}

.accent-red-900 {
  accent-color: #7f1d1d;
}

.accent-red-950 {
  accent-color: #450a0a;
}

.accent-rose-100 {
  accent-color: #ffe4e6;
}

.accent-rose-200 {
  accent-color: #fecdd3;
}

.accent-rose-300 {
  accent-color: #fda4af;
}

.accent-rose-400 {
  accent-color: #fb7185;
}

.accent-rose-50 {
  accent-color: #fff1f2;
}

.accent-rose-500 {
  accent-color: #f43f5e;
}

.accent-rose-600 {
  accent-color: #e11d48;
}

.accent-rose-700 {
  accent-color: #be123c;
}

.accent-rose-800 {
  accent-color: #9f1239;
}

.accent-rose-900 {
  accent-color: #881337;
}

.accent-rose-950 {
  accent-color: #4c0519;
}

.accent-sky-100 {
  accent-color: #e0f2fe;
}

.accent-sky-200 {
  accent-color: #bae6fd;
}

.accent-sky-300 {
  accent-color: #7dd3fc;
}

.accent-sky-400 {
  accent-color: #38bdf8;
}

.accent-sky-50 {
  accent-color: #f0f9ff;
}

.accent-sky-500 {
  accent-color: #0ea5e9;
}

.accent-sky-600 {
  accent-color: #0284c7;
}

.accent-sky-700 {
  accent-color: #0369a1;
}

.accent-sky-800 {
  accent-color: #075985;
}

.accent-sky-900 {
  accent-color: #0c4a6e;
}

.accent-sky-950 {
  accent-color: #082f49;
}

.accent-slate-100 {
  accent-color: #f1f5f9;
}

.accent-slate-200 {
  accent-color: #e2e8f0;
}

.accent-slate-300 {
  accent-color: #cbd5e1;
}

.accent-slate-400 {
  accent-color: #94a3b8;
}

.accent-slate-50 {
  accent-color: #f8fafc;
}

.accent-slate-500 {
  accent-color: #64748b;
}

.accent-slate-600 {
  accent-color: #475569;
}

.accent-slate-700 {
  accent-color: #334155;
}

.accent-slate-800 {
  accent-color: #1e293b;
}

.accent-slate-900 {
  accent-color: #0f172a;
}

.accent-slate-950 {
  accent-color: #020617;
}

.accent-stone-100 {
  accent-color: #f5f5f4;
}

.accent-stone-200 {
  accent-color: #e7e5e4;
}

.accent-stone-300 {
  accent-color: #d6d3d1;
}

.accent-stone-400 {
  accent-color: #a8a29e;
}

.accent-stone-50 {
  accent-color: #fafaf9;
}

.accent-stone-500 {
  accent-color: #78716c;
}

.accent-stone-600 {
  accent-color: #57534e;
}

.accent-stone-700 {
  accent-color: #44403c;
}

.accent-stone-800 {
  accent-color: #292524;
}

.accent-stone-900 {
  accent-color: #1c1917;
}

.accent-stone-950 {
  accent-color: #0c0a09;
}

.accent-teal-100 {
  accent-color: #ccfbf1;
}

.accent-teal-200 {
  accent-color: #99f6e4;
}

.accent-teal-300 {
  accent-color: #5eead4;
}

.accent-teal-400 {
  accent-color: #2dd4bf;
}

.accent-teal-50 {
  accent-color: #f0fdfa;
}

.accent-teal-500 {
  accent-color: #14b8a6;
}

.accent-teal-600 {
  accent-color: #0d9488;
}

.accent-teal-700 {
  accent-color: #0f766e;
}

.accent-teal-800 {
  accent-color: #115e59;
}

.accent-teal-900 {
  accent-color: #134e4a;
}

.accent-teal-950 {
  accent-color: #042f2e;
}

.accent-transparent {
  accent-color: transparent;
}

.accent-violet-100 {
  accent-color: #ede9fe;
}

.accent-violet-200 {
  accent-color: #ddd6fe;
}

.accent-violet-300 {
  accent-color: #c4b5fd;
}

.accent-violet-400 {
  accent-color: #a78bfa;
}

.accent-violet-50 {
  accent-color: #f5f3ff;
}

.accent-violet-500 {
  accent-color: #8b5cf6;
}

.accent-violet-600 {
  accent-color: #7c3aed;
}

.accent-violet-700 {
  accent-color: #6d28d9;
}

.accent-violet-800 {
  accent-color: #5b21b6;
}

.accent-violet-900 {
  accent-color: #4c1d95;
}

.accent-violet-950 {
  accent-color: #2e1065;
}

.accent-white {
  accent-color: #fff;
}

.accent-yellow-100 {
  accent-color: #fef9c3;
}

.accent-yellow-200 {
  accent-color: #fef08a;
}

.accent-yellow-300 {
  accent-color: #fde047;
}

.accent-yellow-400 {
  accent-color: #facc15;
}

.accent-yellow-50 {
  accent-color: #fefce8;
}

.accent-yellow-500 {
  accent-color: #eab308;
}

.accent-yellow-600 {
  accent-color: #ca8a04;
}

.accent-yellow-700 {
  accent-color: #a16207;
}

.accent-yellow-800 {
  accent-color: #854d0e;
}

.accent-yellow-900 {
  accent-color: #713f12;
}

.accent-yellow-950 {
  accent-color: #422006;
}

.accent-zinc-100 {
  accent-color: #f4f4f5;
}

.accent-zinc-200 {
  accent-color: #e4e4e7;
}

.accent-zinc-300 {
  accent-color: #d4d4d8;
}

.accent-zinc-400 {
  accent-color: #a1a1aa;
}

.accent-zinc-50 {
  accent-color: #fafafa;
}

.accent-zinc-500 {
  accent-color: #71717a;
}

.accent-zinc-600 {
  accent-color: #52525b;
}

.accent-zinc-700 {
  accent-color: #3f3f46;
}

.accent-zinc-800 {
  accent-color: #27272a;
}

.accent-zinc-900 {
  accent-color: #18181b;
}

.accent-zinc-950 {
  accent-color: #09090b;
}

.opacity-0 {
  opacity: 0;
}

.opacity-10 {
  opacity: 0.1;
}

.opacity-100 {
  opacity: 1;
}

.opacity-20 {
  opacity: 0.2;
}

.opacity-25 {
  opacity: 0.25;
}

.opacity-30 {
  opacity: 0.3;
}

.opacity-40 {
  opacity: 0.4;
}

.opacity-5 {
  opacity: 0.05;
}

.opacity-50 {
  opacity: 0.5;
}

.opacity-60 {
  opacity: 0.6;
}

.opacity-70 {
  opacity: 0.7;
}

.opacity-75 {
  opacity: 0.75;
}

.opacity-80 {
  opacity: 0.8;
}

.opacity-90 {
  opacity: 0.9;
}

.opacity-95 {
  opacity: 0.95;
}

.bg-blend-normal {
  background-blend-mode: normal;
}

.bg-blend-multiply {
  background-blend-mode: multiply;
}

.bg-blend-screen {
  background-blend-mode: screen;
}

.bg-blend-overlay {
  background-blend-mode: overlay;
}

.bg-blend-darken {
  background-blend-mode: darken;
}

.bg-blend-lighten {
  background-blend-mode: lighten;
}

.bg-blend-color-dodge {
  background-blend-mode: color-dodge;
}

.bg-blend-color-burn {
  background-blend-mode: color-burn;
}

.bg-blend-hard-light {
  background-blend-mode: hard-light;
}

.bg-blend-soft-light {
  background-blend-mode: soft-light;
}

.bg-blend-difference {
  background-blend-mode: difference;
}

.bg-blend-exclusion {
  background-blend-mode: exclusion;
}

.bg-blend-hue {
  background-blend-mode: hue;
}

.bg-blend-saturation {
  background-blend-mode: saturation;
}

.bg-blend-color {
  background-blend-mode: color;
}

.bg-blend-luminosity {
  background-blend-mode: luminosity;
}

.mix-blend-normal {
  mix-blend-mode: normal;
}

.mix-blend-multiply {
  mix-blend-mode: multiply;
}

.mix-blend-screen {
  mix-blend-mode: screen;
}

.mix-blend-overlay {
  mix-blend-mode: overlay;
}

.mix-blend-darken {
  mix-blend-mode: darken;
}

.mix-blend-lighten {
  mix-blend-mode: lighten;
}

.mix-blend-color-dodge {
  mix-blend-mode: color-dodge;
}

.mix-blend-color-burn {
  mix-blend-mode: color-burn;
}

.mix-blend-hard-light {
  mix-blend-mode: hard-light;
}

.mix-blend-soft-light {
  mix-blend-mode: soft-light;
}

.mix-blend-difference {
  mix-blend-mode: difference;
}

.mix-blend-exclusion {
  mix-blend-mode: exclusion;
}

.mix-blend-hue {
  mix-blend-mode: hue;
}

.mix-blend-saturation {
  mix-blend-mode: saturation;
}

.mix-blend-color {
  mix-blend-mode: color;
}

.mix-blend-luminosity {
  mix-blend-mode: luminosity;
}

.mix-blend-plus-lighter {
  mix-blend-mode: plus-lighter;
}

.shadow {
  --tw-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);
  --tw-shadow-colored: 0 1px 3px 0 var(--tw-shadow-color), 0 1px 2px -1px var(--tw-shadow-color);
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}

.shadow-2xl {
  --tw-shadow: 0 25px 50px -12px rgb(0 0 0 / 0.25);
  --tw-shadow-colored: 0 25px 50px -12px var(--tw-shadow-color);
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}

.shadow-inner {
  --tw-shadow: inset 0 2px 4px 0 rgb(0 0 0 / 0.05);
  --tw-shadow-colored: inset 0 2px 4px 0 var(--tw-shadow-color);
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}

.shadow-lg {
  --tw-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
  --tw-shadow-colored: 0 10px 15px -3px var(--tw-shadow-color), 0 4px 6px -4px var(--tw-shadow-color);
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}

.shadow-md {
  --tw-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
  --tw-shadow-colored: 0 4px 6px -1px var(--tw-shadow-color), 0 2px 4px -2px var(--tw-shadow-color);
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}

.shadow-none {
  --tw-shadow: 0 0 #0000;
  --tw-shadow-colored: 0 0 #0000;
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}

.shadow-sm {
  --tw-shadow: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --tw-shadow-colored: 0 1px 2px 0 var(--tw-shadow-color);
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}

.shadow-xl {
  --tw-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
  --tw-shadow-colored: 0 20px 25px -5px var(--tw-shadow-color), 0 8px 10px -6px var(--tw-shadow-color);
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}

.shadow-amber-100 {
  --tw-shadow-color: #fef3c7;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-amber-200 {
  --tw-shadow-color: #fde68a;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-amber-300 {
  --tw-shadow-color: #fcd34d;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-amber-400 {
  --tw-shadow-color: #fbbf24;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-amber-50 {
  --tw-shadow-color: #fffbeb;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-amber-500 {
  --tw-shadow-color: #f59e0b;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-amber-600 {
  --tw-shadow-color: #d97706;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-amber-700 {
  --tw-shadow-color: #b45309;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-amber-800 {
  --tw-shadow-color: #92400e;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-amber-900 {
  --tw-shadow-color: #78350f;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-amber-950 {
  --tw-shadow-color: #451a03;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-black {
  --tw-shadow-color: #000;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-blue-100 {
  --tw-shadow-color: #dbeafe;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-blue-200 {
  --tw-shadow-color: #bfdbfe;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-blue-300 {
  --tw-shadow-color: #93c5fd;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-blue-400 {
  --tw-shadow-color: #60a5fa;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-blue-50 {
  --tw-shadow-color: #eff6ff;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-blue-500 {
  --tw-shadow-color: #3b82f6;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-blue-600 {
  --tw-shadow-color: #2563eb;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-blue-700 {
  --tw-shadow-color: #1d4ed8;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-blue-800 {
  --tw-shadow-color: #1e40af;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-blue-900 {
  --tw-shadow-color: #1e3a8a;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-blue-950 {
  --tw-shadow-color: #172554;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-current {
  --tw-shadow-color: currentColor;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-cyan-100 {
  --tw-shadow-color: #cffafe;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-cyan-200 {
  --tw-shadow-color: #a5f3fc;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-cyan-300 {
  --tw-shadow-color: #67e8f9;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-cyan-400 {
  --tw-shadow-color: #22d3ee;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-cyan-50 {
  --tw-shadow-color: #ecfeff;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-cyan-500 {
  --tw-shadow-color: #06b6d4;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-cyan-600 {
  --tw-shadow-color: #0891b2;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-cyan-700 {
  --tw-shadow-color: #0e7490;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-cyan-800 {
  --tw-shadow-color: #155e75;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-cyan-900 {
  --tw-shadow-color: #164e63;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-cyan-950 {
  --tw-shadow-color: #083344;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-emerald-100 {
  --tw-shadow-color: #d1fae5;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-emerald-200 {
  --tw-shadow-color: #a7f3d0;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-emerald-300 {
  --tw-shadow-color: #6ee7b7;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-emerald-400 {
  --tw-shadow-color: #34d399;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-emerald-50 {
  --tw-shadow-color: #ecfdf5;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-emerald-500 {
  --tw-shadow-color: #10b981;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-emerald-600 {
  --tw-shadow-color: #059669;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-emerald-700 {
  --tw-shadow-color: #047857;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-emerald-800 {
  --tw-shadow-color: #065f46;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-emerald-900 {
  --tw-shadow-color: #064e3b;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-emerald-950 {
  --tw-shadow-color: #022c22;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-fuchsia-100 {
  --tw-shadow-color: #fae8ff;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-fuchsia-200 {
  --tw-shadow-color: #f5d0fe;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-fuchsia-300 {
  --tw-shadow-color: #f0abfc;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-fuchsia-400 {
  --tw-shadow-color: #e879f9;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-fuchsia-50 {
  --tw-shadow-color: #fdf4ff;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-fuchsia-500 {
  --tw-shadow-color: #d946ef;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-fuchsia-600 {
  --tw-shadow-color: #c026d3;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-fuchsia-700 {
  --tw-shadow-color: #a21caf;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-fuchsia-800 {
  --tw-shadow-color: #86198f;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-fuchsia-900 {
  --tw-shadow-color: #701a75;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-fuchsia-950 {
  --tw-shadow-color: #4a044e;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-gray-100 {
  --tw-shadow-color: #f3f4f6;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-gray-200 {
  --tw-shadow-color: #e5e7eb;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-gray-300 {
  --tw-shadow-color: #d1d5db;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-gray-400 {
  --tw-shadow-color: #9ca3af;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-gray-50 {
  --tw-shadow-color: #f9fafb;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-gray-500 {
  --tw-shadow-color: #6b7280;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-gray-600 {
  --tw-shadow-color: #4b5563;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-gray-700 {
  --tw-shadow-color: #374151;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-gray-800 {
  --tw-shadow-color: #1f2937;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-gray-900 {
  --tw-shadow-color: #111827;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-gray-950 {
  --tw-shadow-color: #030712;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-green-100 {
  --tw-shadow-color: #dcfce7;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-green-200 {
  --tw-shadow-color: #bbf7d0;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-green-300 {
  --tw-shadow-color: #86efac;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-green-400 {
  --tw-shadow-color: #4ade80;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-green-50 {
  --tw-shadow-color: #f0fdf4;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-green-500 {
  --tw-shadow-color: #22c55e;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-green-600 {
  --tw-shadow-color: #16a34a;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-green-700 {
  --tw-shadow-color: #15803d;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-green-800 {
  --tw-shadow-color: #166534;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-green-900 {
  --tw-shadow-color: #14532d;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-green-950 {
  --tw-shadow-color: #052e16;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-indigo-100 {
  --tw-shadow-color: #e0e7ff;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-indigo-200 {
  --tw-shadow-color: #c7d2fe;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-indigo-300 {
  --tw-shadow-color: #a5b4fc;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-indigo-400 {
  --tw-shadow-color: #818cf8;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-indigo-50 {
  --tw-shadow-color: #eef2ff;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-indigo-500 {
  --tw-shadow-color: #6366f1;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-indigo-600 {
  --tw-shadow-color: #4f46e5;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-indigo-700 {
  --tw-shadow-color: #4338ca;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-indigo-800 {
  --tw-shadow-color: #3730a3;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-indigo-900 {
  --tw-shadow-color: #312e81;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-indigo-950 {
  --tw-shadow-color: #1e1b4b;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-inherit {
  --tw-shadow-color: inherit;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-lime-100 {
  --tw-shadow-color: #ecfccb;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-lime-200 {
  --tw-shadow-color: #d9f99d;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-lime-300 {
  --tw-shadow-color: #bef264;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-lime-400 {
  --tw-shadow-color: #a3e635;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-lime-50 {
  --tw-shadow-color: #f7fee7;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-lime-500 {
  --tw-shadow-color: #84cc16;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-lime-600 {
  --tw-shadow-color: #65a30d;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-lime-700 {
  --tw-shadow-color: #4d7c0f;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-lime-800 {
  --tw-shadow-color: #3f6212;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-lime-900 {
  --tw-shadow-color: #365314;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-lime-950 {
  --tw-shadow-color: #1a2e05;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-neutral-100 {
  --tw-shadow-color: #f5f5f5;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-neutral-200 {
  --tw-shadow-color: #e5e5e5;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-neutral-300 {
  --tw-shadow-color: #d4d4d4;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-neutral-400 {
  --tw-shadow-color: #a3a3a3;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-neutral-50 {
  --tw-shadow-color: #fafafa;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-neutral-500 {
  --tw-shadow-color: #737373;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-neutral-600 {
  --tw-shadow-color: #525252;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-neutral-700 {
  --tw-shadow-color: #404040;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-neutral-800 {
  --tw-shadow-color: #262626;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-neutral-900 {
  --tw-shadow-color: #171717;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-neutral-950 {
  --tw-shadow-color: #0a0a0a;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-orange-100 {
  --tw-shadow-color: #ffedd5;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-orange-200 {
  --tw-shadow-color: #fed7aa;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-orange-300 {
  --tw-shadow-color: #fdba74;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-orange-400 {
  --tw-shadow-color: #fb923c;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-orange-50 {
  --tw-shadow-color: #fff7ed;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-orange-500 {
  --tw-shadow-color: #f97316;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-orange-600 {
  --tw-shadow-color: #ea580c;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-orange-700 {
  --tw-shadow-color: #c2410c;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-orange-800 {
  --tw-shadow-color: #9a3412;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-orange-900 {
  --tw-shadow-color: #7c2d12;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-orange-950 {
  --tw-shadow-color: #431407;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-pink-100 {
  --tw-shadow-color: #fce7f3;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-pink-200 {
  --tw-shadow-color: #fbcfe8;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-pink-300 {
  --tw-shadow-color: #f9a8d4;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-pink-400 {
  --tw-shadow-color: #f472b6;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-pink-50 {
  --tw-shadow-color: #fdf2f8;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-pink-500 {
  --tw-shadow-color: #ec4899;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-pink-600 {
  --tw-shadow-color: #db2777;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-pink-700 {
  --tw-shadow-color: #be185d;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-pink-800 {
  --tw-shadow-color: #9d174d;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-pink-900 {
  --tw-shadow-color: #831843;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-pink-950 {
  --tw-shadow-color: #500724;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-purple-100 {
  --tw-shadow-color: #f3e8ff;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-purple-200 {
  --tw-shadow-color: #e9d5ff;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-purple-300 {
  --tw-shadow-color: #d8b4fe;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-purple-400 {
  --tw-shadow-color: #c084fc;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-purple-50 {
  --tw-shadow-color: #faf5ff;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-purple-500 {
  --tw-shadow-color: #a855f7;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-purple-600 {
  --tw-shadow-color: #9333ea;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-purple-700 {
  --tw-shadow-color: #7e22ce;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-purple-800 {
  --tw-shadow-color: #6b21a8;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-purple-900 {
  --tw-shadow-color: #581c87;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-purple-950 {
  --tw-shadow-color: #3b0764;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-red-100 {
  --tw-shadow-color: #fee2e2;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-red-200 {
  --tw-shadow-color: #fecaca;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-red-300 {
  --tw-shadow-color: #fca5a5;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-red-400 {
  --tw-shadow-color: #f87171;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-red-50 {
  --tw-shadow-color: #fef2f2;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-red-500 {
  --tw-shadow-color: #ef4444;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-red-600 {
  --tw-shadow-color: #dc2626;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-red-700 {
  --tw-shadow-color: #b91c1c;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-red-800 {
  --tw-shadow-color: #991b1b;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-red-900 {
  --tw-shadow-color: #7f1d1d;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-red-950 {
  --tw-shadow-color: #450a0a;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-rose-100 {
  --tw-shadow-color: #ffe4e6;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-rose-200 {
  --tw-shadow-color: #fecdd3;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-rose-300 {
  --tw-shadow-color: #fda4af;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-rose-400 {
  --tw-shadow-color: #fb7185;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-rose-50 {
  --tw-shadow-color: #fff1f2;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-rose-500 {
  --tw-shadow-color: #f43f5e;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-rose-600 {
  --tw-shadow-color: #e11d48;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-rose-700 {
  --tw-shadow-color: #be123c;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-rose-800 {
  --tw-shadow-color: #9f1239;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-rose-900 {
  --tw-shadow-color: #881337;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-rose-950 {
  --tw-shadow-color: #4c0519;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-sky-100 {
  --tw-shadow-color: #e0f2fe;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-sky-200 {
  --tw-shadow-color: #bae6fd;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-sky-300 {
  --tw-shadow-color: #7dd3fc;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-sky-400 {
  --tw-shadow-color: #38bdf8;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-sky-50 {
  --tw-shadow-color: #f0f9ff;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-sky-500 {
  --tw-shadow-color: #0ea5e9;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-sky-600 {
  --tw-shadow-color: #0284c7;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-sky-700 {
  --tw-shadow-color: #0369a1;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-sky-800 {
  --tw-shadow-color: #075985;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-sky-900 {
  --tw-shadow-color: #0c4a6e;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-sky-950 {
  --tw-shadow-color: #082f49;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-slate-100 {
  --tw-shadow-color: #f1f5f9;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-slate-200 {
  --tw-shadow-color: #e2e8f0;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-slate-300 {
  --tw-shadow-color: #cbd5e1;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-slate-400 {
  --tw-shadow-color: #94a3b8;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-slate-50 {
  --tw-shadow-color: #f8fafc;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-slate-500 {
  --tw-shadow-color: #64748b;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-slate-600 {
  --tw-shadow-color: #475569;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-slate-700 {
  --tw-shadow-color: #334155;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-slate-800 {
  --tw-shadow-color: #1e293b;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-slate-900 {
  --tw-shadow-color: #0f172a;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-slate-950 {
  --tw-shadow-color: #020617;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-stone-100 {
  --tw-shadow-color: #f5f5f4;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-stone-200 {
  --tw-shadow-color: #e7e5e4;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-stone-300 {
  --tw-shadow-color: #d6d3d1;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-stone-400 {
  --tw-shadow-color: #a8a29e;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-stone-50 {
  --tw-shadow-color: #fafaf9;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-stone-500 {
  --tw-shadow-color: #78716c;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-stone-600 {
  --tw-shadow-color: #57534e;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-stone-700 {
  --tw-shadow-color: #44403c;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-stone-800 {
  --tw-shadow-color: #292524;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-stone-900 {
  --tw-shadow-color: #1c1917;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-stone-950 {
  --tw-shadow-color: #0c0a09;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-teal-100 {
  --tw-shadow-color: #ccfbf1;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-teal-200 {
  --tw-shadow-color: #99f6e4;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-teal-300 {
  --tw-shadow-color: #5eead4;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-teal-400 {
  --tw-shadow-color: #2dd4bf;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-teal-50 {
  --tw-shadow-color: #f0fdfa;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-teal-500 {
  --tw-shadow-color: #14b8a6;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-teal-600 {
  --tw-shadow-color: #0d9488;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-teal-700 {
  --tw-shadow-color: #0f766e;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-teal-800 {
  --tw-shadow-color: #115e59;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-teal-900 {
  --tw-shadow-color: #134e4a;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-teal-950 {
  --tw-shadow-color: #042f2e;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-transparent {
  --tw-shadow-color: transparent;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-violet-100 {
  --tw-shadow-color: #ede9fe;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-violet-200 {
  --tw-shadow-color: #ddd6fe;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-violet-300 {
  --tw-shadow-color: #c4b5fd;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-violet-400 {
  --tw-shadow-color: #a78bfa;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-violet-50 {
  --tw-shadow-color: #f5f3ff;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-violet-500 {
  --tw-shadow-color: #8b5cf6;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-violet-600 {
  --tw-shadow-color: #7c3aed;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-violet-700 {
  --tw-shadow-color: #6d28d9;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-violet-800 {
  --tw-shadow-color: #5b21b6;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-violet-900 {
  --tw-shadow-color: #4c1d95;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-violet-950 {
  --tw-shadow-color: #2e1065;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-white {
  --tw-shadow-color: #fff;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-yellow-100 {
  --tw-shadow-color: #fef9c3;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-yellow-200 {
  --tw-shadow-color: #fef08a;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-yellow-300 {
  --tw-shadow-color: #fde047;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-yellow-400 {
  --tw-shadow-color: #facc15;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-yellow-50 {
  --tw-shadow-color: #fefce8;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-yellow-500 {
  --tw-shadow-color: #eab308;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-yellow-600 {
  --tw-shadow-color: #ca8a04;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-yellow-700 {
  --tw-shadow-color: #a16207;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-yellow-800 {
  --tw-shadow-color: #854d0e;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-yellow-900 {
  --tw-shadow-color: #713f12;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-yellow-950 {
  --tw-shadow-color: #422006;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-zinc-100 {
  --tw-shadow-color: #f4f4f5;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-zinc-200 {
  --tw-shadow-color: #e4e4e7;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-zinc-300 {
  --tw-shadow-color: #d4d4d8;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-zinc-400 {
  --tw-shadow-color: #a1a1aa;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-zinc-50 {
  --tw-shadow-color: #fafafa;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-zinc-500 {
  --tw-shadow-color: #71717a;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-zinc-600 {
  --tw-shadow-color: #52525b;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-zinc-700 {
  --tw-shadow-color: #3f3f46;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-zinc-800 {
  --tw-shadow-color: #27272a;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-zinc-900 {
  --tw-shadow-color: #18181b;
  --tw-shadow: var(--tw-shadow-colored);
}

.shadow-zinc-950 {
  --tw-shadow-color: #09090b;
  --tw-shadow: var(--tw-shadow-colored);
}

.outline-none {
  outline: 2px solid transparent;
  outline-offset: 2px;
}

.outline {
  outline-style: solid;
}

.outline-dashed {
  outline-style: dashed;
}

.outline-dotted {
  outline-style: dotted;
}

.outline-double {
  outline-style: double;
}

.outline-0 {
  outline-width: 0px;
}

.outline-1 {
  outline-width: 1px;
}

.outline-2 {
  outline-width: 2px;
}

.outline-4 {
  outline-width: 4px;
}

.outline-8 {
  outline-width: 8px;
}

.-outline-offset-0 {
  outline-offset: -0px;
}

.-outline-offset-1 {
  outline-offset: -1px;
}

.-outline-offset-2 {
  outline-offset: -2px;
}

.-outline-offset-4 {
  outline-offset: -4px;
}

.-outline-offset-8 {
  outline-offset: -8px;
}

.outline-offset-0 {
  outline-offset: 0px;
}

.outline-offset-1 {
  outline-offset: 1px;
}

.outline-offset-2 {
  outline-offset: 2px;
}

.outline-offset-4 {
  outline-offset: 4px;
}

.outline-offset-8 {
  outline-offset: 8px;
}

.outline-amber-100 {
  outline-color: #fef3c7;
}

.outline-amber-200 {
  outline-color: #fde68a;
}

.outline-amber-300 {
  outline-color: #fcd34d;
}

.outline-amber-400 {
  outline-color: #fbbf24;
}

.outline-amber-50 {
  outline-color: #fffbeb;
}

.outline-amber-500 {
  outline-color: #f59e0b;
}

.outline-amber-600 {
  outline-color: #d97706;
}

.outline-amber-700 {
  outline-color: #b45309;
}

.outline-amber-800 {
  outline-color: #92400e;
}

.outline-amber-900 {
  outline-color: #78350f;
}

.outline-amber-950 {
  outline-color: #451a03;
}

.outline-black {
  outline-color: #000;
}

.outline-blue-100 {
  outline-color: #dbeafe;
}

.outline-blue-200 {
  outline-color: #bfdbfe;
}

.outline-blue-300 {
  outline-color: #93c5fd;
}

.outline-blue-400 {
  outline-color: #60a5fa;
}

.outline-blue-50 {
  outline-color: #eff6ff;
}

.outline-blue-500 {
  outline-color: #3b82f6;
}

.outline-blue-600 {
  outline-color: #2563eb;
}

.outline-blue-700 {
  outline-color: #1d4ed8;
}

.outline-blue-800 {
  outline-color: #1e40af;
}

.outline-blue-900 {
  outline-color: #1e3a8a;
}

.outline-blue-950 {
  outline-color: #172554;
}

.outline-current {
  outline-color: currentColor;
}

.outline-cyan-100 {
  outline-color: #cffafe;
}

.outline-cyan-200 {
  outline-color: #a5f3fc;
}

.outline-cyan-300 {
  outline-color: #67e8f9;
}

.outline-cyan-400 {
  outline-color: #22d3ee;
}

.outline-cyan-50 {
  outline-color: #ecfeff;
}

.outline-cyan-500 {
  outline-color: #06b6d4;
}

.outline-cyan-600 {
  outline-color: #0891b2;
}

.outline-cyan-700 {
  outline-color: #0e7490;
}

.outline-cyan-800 {
  outline-color: #155e75;
}

.outline-cyan-900 {
  outline-color: #164e63;
}

.outline-cyan-950 {
  outline-color: #083344;
}

.outline-emerald-100 {
  outline-color: #d1fae5;
}

.outline-emerald-200 {
  outline-color: #a7f3d0;
}

.outline-emerald-300 {
  outline-color: #6ee7b7;
}

.outline-emerald-400 {
  outline-color: #34d399;
}

.outline-emerald-50 {
  outline-color: #ecfdf5;
}

.outline-emerald-500 {
  outline-color: #10b981;
}

.outline-emerald-600 {
  outline-color: #059669;
}

.outline-emerald-700 {
  outline-color: #047857;
}

.outline-emerald-800 {
  outline-color: #065f46;
}

.outline-emerald-900 {
  outline-color: #064e3b;
}

.outline-emerald-950 {
  outline-color: #022c22;
}

.outline-fuchsia-100 {
  outline-color: #fae8ff;
}

.outline-fuchsia-200 {
  outline-color: #f5d0fe;
}

.outline-fuchsia-300 {
  outline-color: #f0abfc;
}

.outline-fuchsia-400 {
  outline-color: #e879f9;
}

.outline-fuchsia-50 {
  outline-color: #fdf4ff;
}

.outline-fuchsia-500 {
  outline-color: #d946ef;
}

.outline-fuchsia-600 {
  outline-color: #c026d3;
}

.outline-fuchsia-700 {
  outline-color: #a21caf;
}

.outline-fuchsia-800 {
  outline-color: #86198f;
}

.outline-fuchsia-900 {
  outline-color: #701a75;
}

.outline-fuchsia-950 {
  outline-color: #4a044e;
}

.outline-gray-100 {
  outline-color: #f3f4f6;
}

.outline-gray-200 {
  outline-color: #e5e7eb;
}

.outline-gray-300 {
  outline-color: #d1d5db;
}

.outline-gray-400 {
  outline-color: #9ca3af;
}

.outline-gray-50 {
  outline-color: #f9fafb;
}

.outline-gray-500 {
  outline-color: #6b7280;
}

.outline-gray-600 {
  outline-color: #4b5563;
}

.outline-gray-700 {
  outline-color: #374151;
}

.outline-gray-800 {
  outline-color: #1f2937;
}

.outline-gray-900 {
  outline-color: #111827;
}

.outline-gray-950 {
  outline-color: #030712;
}

.outline-green-100 {
  outline-color: #dcfce7;
}

.outline-green-200 {
  outline-color: #bbf7d0;
}

.outline-green-300 {
  outline-color: #86efac;
}

.outline-green-400 {
  outline-color: #4ade80;
}

.outline-green-50 {
  outline-color: #f0fdf4;
}

.outline-green-500 {
  outline-color: #22c55e;
}

.outline-green-600 {
  outline-color: #16a34a;
}

.outline-green-700 {
  outline-color: #15803d;
}

.outline-green-800 {
  outline-color: #166534;
}

.outline-green-900 {
  outline-color: #14532d;
}

.outline-green-950 {
  outline-color: #052e16;
}

.outline-indigo-100 {
  outline-color: #e0e7ff;
}

.outline-indigo-200 {
  outline-color: #c7d2fe;
}

.outline-indigo-300 {
  outline-color: #a5b4fc;
}

.outline-indigo-400 {
  outline-color: #818cf8;
}

.outline-indigo-50 {
  outline-color: #eef2ff;
}

.outline-indigo-500 {
  outline-color: #6366f1;
}

.outline-indigo-600 {
  outline-color: #4f46e5;
}

.outline-indigo-700 {
  outline-color: #4338ca;
}

.outline-indigo-800 {
  outline-color: #3730a3;
}

.outline-indigo-900 {
  outline-color: #312e81;
}

.outline-indigo-950 {
  outline-color: #1e1b4b;
}

.outline-inherit {
  outline-color: inherit;
}

.outline-lime-100 {
  outline-color: #ecfccb;
}

.outline-lime-200 {
  outline-color: #d9f99d;
}

.outline-lime-300 {
  outline-color: #bef264;
}

.outline-lime-400 {
  outline-color: #a3e635;
}

.outline-lime-50 {
  outline-color: #f7fee7;
}

.outline-lime-500 {
  outline-color: #84cc16;
}

.outline-lime-600 {
  outline-color: #65a30d;
}

.outline-lime-700 {
  outline-color: #4d7c0f;
}

.outline-lime-800 {
  outline-color: #3f6212;
}

.outline-lime-900 {
  outline-color: #365314;
}

.outline-lime-950 {
  outline-color: #1a2e05;
}

.outline-neutral-100 {
  outline-color: #f5f5f5;
}

.outline-neutral-200 {
  outline-color: #e5e5e5;
}

.outline-neutral-300 {
  outline-color: #d4d4d4;
}

.outline-neutral-400 {
  outline-color: #a3a3a3;
}

.outline-neutral-50 {
  outline-color: #fafafa;
}

.outline-neutral-500 {
  outline-color: #737373;
}

.outline-neutral-600 {
  outline-color: #525252;
}

.outline-neutral-700 {
  outline-color: #404040;
}

.outline-neutral-800 {
  outline-color: #262626;
}

.outline-neutral-900 {
  outline-color: #171717;
}

.outline-neutral-950 {
  outline-color: #0a0a0a;
}

.outline-orange-100 {
  outline-color: #ffedd5;
}

.outline-orange-200 {
  outline-color: #fed7aa;
}

.outline-orange-300 {
  outline-color: #fdba74;
}

.outline-orange-400 {
  outline-color: #fb923c;
}

.outline-orange-50 {
  outline-color: #fff7ed;
}

.outline-orange-500 {
  outline-color: #f97316;
}

.outline-orange-600 {
  outline-color: #ea580c;
}

.outline-orange-700 {
  outline-color: #c2410c;
}

.outline-orange-800 {
  outline-color: #9a3412;
}

.outline-orange-900 {
  outline-color: #7c2d12;
}

.outline-orange-950 {
  outline-color: #431407;
}

.outline-pink-100 {
  outline-color: #fce7f3;
}

.outline-pink-200 {
  outline-color: #fbcfe8;
}

.outline-pink-300 {
  outline-color: #f9a8d4;
}

.outline-pink-400 {
  outline-color: #f472b6;
}

.outline-pink-50 {
  outline-color: #fdf2f8;
}

.outline-pink-500 {
  outline-color: #ec4899;
}

.outline-pink-600 {
  outline-color: #db2777;
}

.outline-pink-700 {
  outline-color: #be185d;
}

.outline-pink-800 {
  outline-color: #9d174d;
}

.outline-pink-900 {
  outline-color: #831843;
}

.outline-pink-950 {
  outline-color: #500724;
}

.outline-purple-100 {
  outline-color: #f3e8ff;
}

.outline-purple-200 {
  outline-color: #e9d5ff;
}

.outline-purple-300 {
  outline-color: #d8b4fe;
}

.outline-purple-400 {
  outline-color: #c084fc;
}

.outline-purple-50 {
  outline-color: #faf5ff;
}

.outline-purple-500 {
  outline-color: #a855f7;
}

.outline-purple-600 {
  outline-color: #9333ea;
}

.outline-purple-700 {
  outline-color: #7e22ce;
}

.outline-purple-800 {
  outline-color: #6b21a8;
}

.outline-purple-900 {
  outline-color: #581c87;
}

.outline-purple-950 {
  outline-color: #3b0764;
}

.outline-red-100 {
  outline-color: #fee2e2;
}

.outline-red-200 {
  outline-color: #fecaca;
}

.outline-red-300 {
  outline-color: #fca5a5;
}

.outline-red-400 {
  outline-color: #f87171;
}

.outline-red-50 {
  outline-color: #fef2f2;
}

.outline-red-500 {
  outline-color: #ef4444;
}

.outline-red-600 {
  outline-color: #dc2626;
}

.outline-red-700 {
  outline-color: #b91c1c;
}

.outline-red-800 {
  outline-color: #991b1b;
}

.outline-red-900 {
  outline-color: #7f1d1d;
}

.outline-red-950 {
  outline-color: #450a0a;
}

.outline-rose-100 {
  outline-color: #ffe4e6;
}

.outline-rose-200 {
  outline-color: #fecdd3;
}

.outline-rose-300 {
  outline-color: #fda4af;
}

.outline-rose-400 {
  outline-color: #fb7185;
}

.outline-rose-50 {
  outline-color: #fff1f2;
}

.outline-rose-500 {
  outline-color: #f43f5e;
}

.outline-rose-600 {
  outline-color: #e11d48;
}

.outline-rose-700 {
  outline-color: #be123c;
}

.outline-rose-800 {
  outline-color: #9f1239;
}

.outline-rose-900 {
  outline-color: #881337;
}

.outline-rose-950 {
  outline-color: #4c0519;
}

.outline-sky-100 {
  outline-color: #e0f2fe;
}

.outline-sky-200 {
  outline-color: #bae6fd;
}

.outline-sky-300 {
  outline-color: #7dd3fc;
}

.outline-sky-400 {
  outline-color: #38bdf8;
}

.outline-sky-50 {
  outline-color: #f0f9ff;
}

.outline-sky-500 {
  outline-color: #0ea5e9;
}

.outline-sky-600 {
  outline-color: #0284c7;
}

.outline-sky-700 {
  outline-color: #0369a1;
}

.outline-sky-800 {
  outline-color: #075985;
}

.outline-sky-900 {
  outline-color: #0c4a6e;
}

.outline-sky-950 {
  outline-color: #082f49;
}

.outline-slate-100 {
  outline-color: #f1f5f9;
}

.outline-slate-200 {
  outline-color: #e2e8f0;
}

.outline-slate-300 {
  outline-color: #cbd5e1;
}

.outline-slate-400 {
  outline-color: #94a3b8;
}

.outline-slate-50 {
  outline-color: #f8fafc;
}

.outline-slate-500 {
  outline-color: #64748b;
}

.outline-slate-600 {
  outline-color: #475569;
}

.outline-slate-700 {
  outline-color: #334155;
}

.outline-slate-800 {
  outline-color: #1e293b;
}

.outline-slate-900 {
  outline-color: #0f172a;
}

.outline-slate-950 {
  outline-color: #020617;
}

.outline-stone-100 {
  outline-color: #f5f5f4;
}

.outline-stone-200 {
  outline-color: #e7e5e4;
}

.outline-stone-300 {
  outline-color: #d6d3d1;
}

.outline-stone-400 {
  outline-color: #a8a29e;
}

.outline-stone-50 {
  outline-color: #fafaf9;
}

.outline-stone-500 {
  outline-color: #78716c;
}

.outline-stone-600 {
  outline-color: #57534e;
}

.outline-stone-700 {
  outline-color: #44403c;
}

.outline-stone-800 {
  outline-color: #292524;
}

.outline-stone-900 {
  outline-color: #1c1917;
}

.outline-stone-950 {
  outline-color: #0c0a09;
}

.outline-teal-100 {
  outline-color: #ccfbf1;
}

.outline-teal-200 {
  outline-color: #99f6e4;
}

.outline-teal-300 {
  outline-color: #5eead4;
}

.outline-teal-400 {
  outline-color: #2dd4bf;
}

.outline-teal-50 {
  outline-color: #f0fdfa;
}

.outline-teal-500 {
  outline-color: #14b8a6;
}

.outline-teal-600 {
  outline-color: #0d9488;
}

.outline-teal-700 {
  outline-color: #0f766e;
}

.outline-teal-800 {
  outline-color: #115e59;
}

.outline-teal-900 {
  outline-color: #134e4a;
}

.outline-teal-950 {
  outline-color: #042f2e;
}

.outline-transparent {
  outline-color: transparent;
}

.outline-violet-100 {
  outline-color: #ede9fe;
}

.outline-violet-200 {
  outline-color: #ddd6fe;
}

.outline-violet-300 {
  outline-color: #c4b5fd;
}

.outline-violet-400 {
  outline-color: #a78bfa;
}

.outline-violet-50 {
  outline-color: #f5f3ff;
}

.outline-violet-500 {
  outline-color: #8b5cf6;
}

.outline-violet-600 {
  outline-color: #7c3aed;
}

.outline-violet-700 {
  outline-color: #6d28d9;
}

.outline-violet-800 {
  outline-color: #5b21b6;
}

.outline-violet-900 {
  outline-color: #4c1d95;
}

.outline-violet-950 {
  outline-color: #2e1065;
}

.outline-white {
  outline-color: #fff;
}

.outline-yellow-100 {
  outline-color: #fef9c3;
}

.outline-yellow-200 {
  outline-color: #fef08a;
}

.outline-yellow-300 {
  outline-color: #fde047;
}

.outline-yellow-400 {
  outline-color: #facc15;
}

.outline-yellow-50 {
  outline-color: #fefce8;
}

.outline-yellow-500 {
  outline-color: #eab308;
}

.outline-yellow-600 {
  outline-color: #ca8a04;
}

.outline-yellow-700 {
  outline-color: #a16207;
}

.outline-yellow-800 {
  outline-color: #854d0e;
}

.outline-yellow-900 {
  outline-color: #713f12;
}

.outline-yellow-950 {
  outline-color: #422006;
}

.outline-zinc-100 {
  outline-color: #f4f4f5;
}

.outline-zinc-200 {
  outline-color: #e4e4e7;
}

.outline-zinc-300 {
  outline-color: #d4d4d8;
}

.outline-zinc-400 {
  outline-color: #a1a1aa;
}

.outline-zinc-50 {
  outline-color: #fafafa;
}

.outline-zinc-500 {
  outline-color: #71717a;
}

.outline-zinc-600 {
  outline-color: #52525b;
}

.outline-zinc-700 {
  outline-color: #3f3f46;
}

.outline-zinc-800 {
  outline-color: #27272a;
}

.outline-zinc-900 {
  outline-color: #18181b;
}

.outline-zinc-950 {
  outline-color: #09090b;
}

.ring {
  --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);
  --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(3px + var(--tw-ring-offset-width)) var(--tw-ring-color);
  box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000);
}

.ring-0 {
  --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);
  --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(0px + var(--tw-ring-offset-width)) var(--tw-ring-color);
  box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000);
}

.ring-1 {
  --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);
  --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(1px + var(--tw-ring-offset-width)) var(--tw-ring-color);
  box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000);
}

.ring-2 {
  --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);
  --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color);
  box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000);
}

.ring-4 {
  --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);
  --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(4px + var(--tw-ring-offset-width)) var(--tw-ring-color);
  box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000);
}

.ring-8 {
  --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);
  --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(8px + var(--tw-ring-offset-width)) var(--tw-ring-color);
  box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000);
}

.ring-inset {
  --tw-ring-inset: inset;
}

.ring-amber-100 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(254 243 199 / var(--tw-ring-opacity));
}

.ring-amber-200 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(253 230 138 / var(--tw-ring-opacity));
}

.ring-amber-300 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(252 211 77 / var(--tw-ring-opacity));
}

.ring-amber-400 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(251 191 36 / var(--tw-ring-opacity));
}

.ring-amber-50 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(255 251 235 / var(--tw-ring-opacity));
}

.ring-amber-500 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(245 158 11 / var(--tw-ring-opacity));
}

.ring-amber-600 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(217 119 6 / var(--tw-ring-opacity));
}

.ring-amber-700 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(180 83 9 / var(--tw-ring-opacity));
}

.ring-amber-800 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(146 64 14 / var(--tw-ring-opacity));
}

.ring-amber-900 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(120 53 15 / var(--tw-ring-opacity));
}

.ring-amber-950 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(69 26 3 / var(--tw-ring-opacity));
}

.ring-black {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(0 0 0 / var(--tw-ring-opacity));
}

.ring-blue-100 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(219 234 254 / var(--tw-ring-opacity));
}

.ring-blue-200 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(191 219 254 / var(--tw-ring-opacity));
}

.ring-blue-300 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(147 197 253 / var(--tw-ring-opacity));
}

.ring-blue-400 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(96 165 250 / var(--tw-ring-opacity));
}

.ring-blue-50 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(239 246 255 / var(--tw-ring-opacity));
}

.ring-blue-500 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(59 130 246 / var(--tw-ring-opacity));
}

.ring-blue-600 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(37 99 235 / var(--tw-ring-opacity));
}

.ring-blue-700 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(29 78 216 / var(--tw-ring-opacity));
}

.ring-blue-800 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(30 64 175 / var(--tw-ring-opacity));
}

.ring-blue-900 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(30 58 138 / var(--tw-ring-opacity));
}

.ring-blue-950 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(23 37 84 / var(--tw-ring-opacity));
}

.ring-current {
  --tw-ring-color: currentColor;
}

.ring-cyan-100 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(207 250 254 / var(--tw-ring-opacity));
}

.ring-cyan-200 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(165 243 252 / var(--tw-ring-opacity));
}

.ring-cyan-300 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(103 232 249 / var(--tw-ring-opacity));
}

.ring-cyan-400 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(34 211 238 / var(--tw-ring-opacity));
}

.ring-cyan-50 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(236 254 255 / var(--tw-ring-opacity));
}

.ring-cyan-500 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(6 182 212 / var(--tw-ring-opacity));
}

.ring-cyan-600 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(8 145 178 / var(--tw-ring-opacity));
}

.ring-cyan-700 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(14 116 144 / var(--tw-ring-opacity));
}

.ring-cyan-800 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(21 94 117 / var(--tw-ring-opacity));
}

.ring-cyan-900 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(22 78 99 / var(--tw-ring-opacity));
}

.ring-cyan-950 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(8 51 68 / var(--tw-ring-opacity));
}

.ring-emerald-100 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(209 250 229 / var(--tw-ring-opacity));
}

.ring-emerald-200 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(167 243 208 / var(--tw-ring-opacity));
}

.ring-emerald-300 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(110 231 183 / var(--tw-ring-opacity));
}

.ring-emerald-400 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(52 211 153 / var(--tw-ring-opacity));
}

.ring-emerald-50 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(236 253 245 / var(--tw-ring-opacity));
}

.ring-emerald-500 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(16 185 129 / var(--tw-ring-opacity));
}

.ring-emerald-600 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(5 150 105 / var(--tw-ring-opacity));
}

.ring-emerald-700 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(4 120 87 / var(--tw-ring-opacity));
}

.ring-emerald-800 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(6 95 70 / var(--tw-ring-opacity));
}

.ring-emerald-900 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(6 78 59 / var(--tw-ring-opacity));
}

.ring-emerald-950 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(2 44 34 / var(--tw-ring-opacity));
}

.ring-fuchsia-100 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(250 232 255 / var(--tw-ring-opacity));
}

.ring-fuchsia-200 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(245 208 254 / var(--tw-ring-opacity));
}

.ring-fuchsia-300 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(240 171 252 / var(--tw-ring-opacity));
}

.ring-fuchsia-400 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(232 121 249 / var(--tw-ring-opacity));
}

.ring-fuchsia-50 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(253 244 255 / var(--tw-ring-opacity));
}

.ring-fuchsia-500 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(217 70 239 / var(--tw-ring-opacity));
}

.ring-fuchsia-600 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(192 38 211 / var(--tw-ring-opacity));
}

.ring-fuchsia-700 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(162 28 175 / var(--tw-ring-opacity));
}

.ring-fuchsia-800 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(134 25 143 / var(--tw-ring-opacity));
}

.ring-fuchsia-900 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(112 26 117 / var(--tw-ring-opacity));
}

.ring-fuchsia-950 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(74 4 78 / var(--tw-ring-opacity));
}

.ring-gray-100 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(243 244 246 / var(--tw-ring-opacity));
}

.ring-gray-200 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(229 231 235 / var(--tw-ring-opacity));
}

.ring-gray-300 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(209 213 219 / var(--tw-ring-opacity));
}

.ring-gray-400 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(156 163 175 / var(--tw-ring-opacity));
}

.ring-gray-50 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(249 250 251 / var(--tw-ring-opacity));
}

.ring-gray-500 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(107 114 128 / var(--tw-ring-opacity));
}

.ring-gray-600 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(75 85 99 / var(--tw-ring-opacity));
}

.ring-gray-700 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(55 65 81 / var(--tw-ring-opacity));
}

.ring-gray-800 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(31 41 55 / var(--tw-ring-opacity));
}

.ring-gray-900 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(17 24 39 / var(--tw-ring-opacity));
}

.ring-gray-950 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(3 7 18 / var(--tw-ring-opacity));
}

.ring-green-100 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(220 252 231 / var(--tw-ring-opacity));
}

.ring-green-200 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(187 247 208 / var(--tw-ring-opacity));
}

.ring-green-300 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(134 239 172 / var(--tw-ring-opacity));
}

.ring-green-400 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(74 222 128 / var(--tw-ring-opacity));
}

.ring-green-50 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(240 253 244 / var(--tw-ring-opacity));
}

.ring-green-500 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(34 197 94 / var(--tw-ring-opacity));
}

.ring-green-600 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(22 163 74 / var(--tw-ring-opacity));
}

.ring-green-700 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(21 128 61 / var(--tw-ring-opacity));
}

.ring-green-800 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(22 101 52 / var(--tw-ring-opacity));
}

.ring-green-900 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(20 83 45 / var(--tw-ring-opacity));
}

.ring-green-950 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(5 46 22 / var(--tw-ring-opacity));
}

.ring-indigo-100 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(224 231 255 / var(--tw-ring-opacity));
}

.ring-indigo-200 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(199 210 254 / var(--tw-ring-opacity));
}

.ring-indigo-300 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(165 180 252 / var(--tw-ring-opacity));
}

.ring-indigo-400 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(129 140 248 / var(--tw-ring-opacity));
}

.ring-indigo-50 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(238 242 255 / var(--tw-ring-opacity));
}

.ring-indigo-500 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(99 102 241 / var(--tw-ring-opacity));
}

.ring-indigo-600 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(79 70 229 / var(--tw-ring-opacity));
}

.ring-indigo-700 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(67 56 202 / var(--tw-ring-opacity));
}

.ring-indigo-800 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(55 48 163 / var(--tw-ring-opacity));
}

.ring-indigo-900 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(49 46 129 / var(--tw-ring-opacity));
}

.ring-indigo-950 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(30 27 75 / var(--tw-ring-opacity));
}

.ring-inherit {
  --tw-ring-color: inherit;
}

.ring-lime-100 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(236 252 203 / var(--tw-ring-opacity));
}

.ring-lime-200 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(217 249 157 / var(--tw-ring-opacity));
}

.ring-lime-300 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(190 242 100 / var(--tw-ring-opacity));
}

.ring-lime-400 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(163 230 53 / var(--tw-ring-opacity));
}

.ring-lime-50 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(247 254 231 / var(--tw-ring-opacity));
}

.ring-lime-500 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(132 204 22 / var(--tw-ring-opacity));
}

.ring-lime-600 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(101 163 13 / var(--tw-ring-opacity));
}

.ring-lime-700 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(77 124 15 / var(--tw-ring-opacity));
}

.ring-lime-800 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(63 98 18 / var(--tw-ring-opacity));
}

.ring-lime-900 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(54 83 20 / var(--tw-ring-opacity));
}

.ring-lime-950 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(26 46 5 / var(--tw-ring-opacity));
}

.ring-neutral-100 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(245 245 245 / var(--tw-ring-opacity));
}

.ring-neutral-200 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(229 229 229 / var(--tw-ring-opacity));
}

.ring-neutral-300 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(212 212 212 / var(--tw-ring-opacity));
}

.ring-neutral-400 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(163 163 163 / var(--tw-ring-opacity));
}

.ring-neutral-50 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(250 250 250 / var(--tw-ring-opacity));
}

.ring-neutral-500 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(115 115 115 / var(--tw-ring-opacity));
}

.ring-neutral-600 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(82 82 82 / var(--tw-ring-opacity));
}

.ring-neutral-700 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(64 64 64 / var(--tw-ring-opacity));
}

.ring-neutral-800 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(38 38 38 / var(--tw-ring-opacity));
}

.ring-neutral-900 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(23 23 23 / var(--tw-ring-opacity));
}

.ring-neutral-950 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(10 10 10 / var(--tw-ring-opacity));
}

.ring-orange-100 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(255 237 213 / var(--tw-ring-opacity));
}

.ring-orange-200 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(254 215 170 / var(--tw-ring-opacity));
}

.ring-orange-300 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(253 186 116 / var(--tw-ring-opacity));
}

.ring-orange-400 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(251 146 60 / var(--tw-ring-opacity));
}

.ring-orange-50 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(255 247 237 / var(--tw-ring-opacity));
}

.ring-orange-500 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(249 115 22 / var(--tw-ring-opacity));
}

.ring-orange-600 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(234 88 12 / var(--tw-ring-opacity));
}

.ring-orange-700 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(194 65 12 / var(--tw-ring-opacity));
}

.ring-orange-800 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(154 52 18 / var(--tw-ring-opacity));
}

.ring-orange-900 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(124 45 18 / var(--tw-ring-opacity));
}

.ring-orange-950 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(67 20 7 / var(--tw-ring-opacity));
}

.ring-pink-100 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(252 231 243 / var(--tw-ring-opacity));
}

.ring-pink-200 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(251 207 232 / var(--tw-ring-opacity));
}

.ring-pink-300 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(249 168 212 / var(--tw-ring-opacity));
}

.ring-pink-400 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(244 114 182 / var(--tw-ring-opacity));
}

.ring-pink-50 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(253 242 248 / var(--tw-ring-opacity));
}

.ring-pink-500 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(236 72 153 / var(--tw-ring-opacity));
}

.ring-pink-600 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(219 39 119 / var(--tw-ring-opacity));
}

.ring-pink-700 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(190 24 93 / var(--tw-ring-opacity));
}

.ring-pink-800 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(157 23 77 / var(--tw-ring-opacity));
}

.ring-pink-900 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(131 24 67 / var(--tw-ring-opacity));
}

.ring-pink-950 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(80 7 36 / var(--tw-ring-opacity));
}

.ring-purple-100 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(243 232 255 / var(--tw-ring-opacity));
}

.ring-purple-200 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(233 213 255 / var(--tw-ring-opacity));
}

.ring-purple-300 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(216 180 254 / var(--tw-ring-opacity));
}

.ring-purple-400 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(192 132 252 / var(--tw-ring-opacity));
}

.ring-purple-50 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(250 245 255 / var(--tw-ring-opacity));
}

.ring-purple-500 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(168 85 247 / var(--tw-ring-opacity));
}

.ring-purple-600 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(147 51 234 / var(--tw-ring-opacity));
}

.ring-purple-700 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(126 34 206 / var(--tw-ring-opacity));
}

.ring-purple-800 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(107 33 168 / var(--tw-ring-opacity));
}

.ring-purple-900 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(88 28 135 / var(--tw-ring-opacity));
}

.ring-purple-950 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(59 7 100 / var(--tw-ring-opacity));
}

.ring-red-100 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(254 226 226 / var(--tw-ring-opacity));
}

.ring-red-200 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(254 202 202 / var(--tw-ring-opacity));
}

.ring-red-300 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(252 165 165 / var(--tw-ring-opacity));
}

.ring-red-400 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(248 113 113 / var(--tw-ring-opacity));
}

.ring-red-50 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(254 242 242 / var(--tw-ring-opacity));
}

.ring-red-500 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(239 68 68 / var(--tw-ring-opacity));
}

.ring-red-600 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(220 38 38 / var(--tw-ring-opacity));
}

.ring-red-700 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(185 28 28 / var(--tw-ring-opacity));
}

.ring-red-800 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(153 27 27 / var(--tw-ring-opacity));
}

.ring-red-900 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(127 29 29 / var(--tw-ring-opacity));
}

.ring-red-950 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(69 10 10 / var(--tw-ring-opacity));
}

.ring-rose-100 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(255 228 230 / var(--tw-ring-opacity));
}

.ring-rose-200 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(254 205 211 / var(--tw-ring-opacity));
}

.ring-rose-300 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(253 164 175 / var(--tw-ring-opacity));
}

.ring-rose-400 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(251 113 133 / var(--tw-ring-opacity));
}

.ring-rose-50 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(255 241 242 / var(--tw-ring-opacity));
}

.ring-rose-500 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(244 63 94 / var(--tw-ring-opacity));
}

.ring-rose-600 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(225 29 72 / var(--tw-ring-opacity));
}

.ring-rose-700 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(190 18 60 / var(--tw-ring-opacity));
}

.ring-rose-800 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(159 18 57 / var(--tw-ring-opacity));
}

.ring-rose-900 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(136 19 55 / var(--tw-ring-opacity));
}

.ring-rose-950 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(76 5 25 / var(--tw-ring-opacity));
}

.ring-sky-100 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(224 242 254 / var(--tw-ring-opacity));
}

.ring-sky-200 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(186 230 253 / var(--tw-ring-opacity));
}

.ring-sky-300 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(125 211 252 / var(--tw-ring-opacity));
}

.ring-sky-400 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(56 189 248 / var(--tw-ring-opacity));
}

.ring-sky-50 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(240 249 255 / var(--tw-ring-opacity));
}

.ring-sky-500 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(14 165 233 / var(--tw-ring-opacity));
}

.ring-sky-600 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(2 132 199 / var(--tw-ring-opacity));
}

.ring-sky-700 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(3 105 161 / var(--tw-ring-opacity));
}

.ring-sky-800 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(7 89 133 / var(--tw-ring-opacity));
}

.ring-sky-900 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(12 74 110 / var(--tw-ring-opacity));
}

.ring-sky-950 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(8 47 73 / var(--tw-ring-opacity));
}

.ring-slate-100 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(241 245 249 / var(--tw-ring-opacity));
}

.ring-slate-200 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(226 232 240 / var(--tw-ring-opacity));
}

.ring-slate-300 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(203 213 225 / var(--tw-ring-opacity));
}

.ring-slate-400 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(148 163 184 / var(--tw-ring-opacity));
}

.ring-slate-50 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(248 250 252 / var(--tw-ring-opacity));
}

.ring-slate-500 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(100 116 139 / var(--tw-ring-opacity));
}

.ring-slate-600 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(71 85 105 / var(--tw-ring-opacity));
}

.ring-slate-700 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(51 65 85 / var(--tw-ring-opacity));
}

.ring-slate-800 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(30 41 59 / var(--tw-ring-opacity));
}

.ring-slate-900 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(15 23 42 / var(--tw-ring-opacity));
}

.ring-slate-950 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(2 6 23 / var(--tw-ring-opacity));
}

.ring-stone-100 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(245 245 244 / var(--tw-ring-opacity));
}

.ring-stone-200 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(231 229 228 / var(--tw-ring-opacity));
}

.ring-stone-300 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(214 211 209 / var(--tw-ring-opacity));
}

.ring-stone-400 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(168 162 158 / var(--tw-ring-opacity));
}

.ring-stone-50 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(250 250 249 / var(--tw-ring-opacity));
}

.ring-stone-500 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(120 113 108 / var(--tw-ring-opacity));
}

.ring-stone-600 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(87 83 78 / var(--tw-ring-opacity));
}

.ring-stone-700 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(68 64 60 / var(--tw-ring-opacity));
}

.ring-stone-800 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(41 37 36 / var(--tw-ring-opacity));
}

.ring-stone-900 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(28 25 23 / var(--tw-ring-opacity));
}

.ring-stone-950 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(12 10 9 / var(--tw-ring-opacity));
}

.ring-teal-100 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(204 251 241 / var(--tw-ring-opacity));
}

.ring-teal-200 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(153 246 228 / var(--tw-ring-opacity));
}

.ring-teal-300 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(94 234 212 / var(--tw-ring-opacity));
}

.ring-teal-400 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(45 212 191 / var(--tw-ring-opacity));
}

.ring-teal-50 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(240 253 250 / var(--tw-ring-opacity));
}

.ring-teal-500 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(20 184 166 / var(--tw-ring-opacity));
}

.ring-teal-600 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(13 148 136 / var(--tw-ring-opacity));
}

.ring-teal-700 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(15 118 110 / var(--tw-ring-opacity));
}

.ring-teal-800 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(17 94 89 / var(--tw-ring-opacity));
}

.ring-teal-900 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(19 78 74 / var(--tw-ring-opacity));
}

.ring-teal-950 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(4 47 46 / var(--tw-ring-opacity));
}

.ring-transparent {
  --tw-ring-color: transparent;
}

.ring-violet-100 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(237 233 254 / var(--tw-ring-opacity));
}

.ring-violet-200 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(221 214 254 / var(--tw-ring-opacity));
}

.ring-violet-300 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(196 181 253 / var(--tw-ring-opacity));
}

.ring-violet-400 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(167 139 250 / var(--tw-ring-opacity));
}

.ring-violet-50 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(245 243 255 / var(--tw-ring-opacity));
}

.ring-violet-500 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(139 92 246 / var(--tw-ring-opacity));
}

.ring-violet-600 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(124 58 237 / var(--tw-ring-opacity));
}

.ring-violet-700 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(109 40 217 / var(--tw-ring-opacity));
}

.ring-violet-800 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(91 33 182 / var(--tw-ring-opacity));
}

.ring-violet-900 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(76 29 149 / var(--tw-ring-opacity));
}

.ring-violet-950 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(46 16 101 / var(--tw-ring-opacity));
}

.ring-white {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(255 255 255 / var(--tw-ring-opacity));
}

.ring-yellow-100 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(254 249 195 / var(--tw-ring-opacity));
}

.ring-yellow-200 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(254 240 138 / var(--tw-ring-opacity));
}

.ring-yellow-300 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(253 224 71 / var(--tw-ring-opacity));
}

.ring-yellow-400 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(250 204 21 / var(--tw-ring-opacity));
}

.ring-yellow-50 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(254 252 232 / var(--tw-ring-opacity));
}

.ring-yellow-500 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(234 179 8 / var(--tw-ring-opacity));
}

.ring-yellow-600 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(202 138 4 / var(--tw-ring-opacity));
}

.ring-yellow-700 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(161 98 7 / var(--tw-ring-opacity));
}

.ring-yellow-800 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(133 77 14 / var(--tw-ring-opacity));
}

.ring-yellow-900 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(113 63 18 / var(--tw-ring-opacity));
}

.ring-yellow-950 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(66 32 6 / var(--tw-ring-opacity));
}

.ring-zinc-100 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(244 244 245 / var(--tw-ring-opacity));
}

.ring-zinc-200 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(228 228 231 / var(--tw-ring-opacity));
}

.ring-zinc-300 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(212 212 216 / var(--tw-ring-opacity));
}

.ring-zinc-400 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(161 161 170 / var(--tw-ring-opacity));
}

.ring-zinc-50 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(250 250 250 / var(--tw-ring-opacity));
}

.ring-zinc-500 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(113 113 122 / var(--tw-ring-opacity));
}

.ring-zinc-600 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(82 82 91 / var(--tw-ring-opacity));
}

.ring-zinc-700 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(63 63 70 / var(--tw-ring-opacity));
}

.ring-zinc-800 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(39 39 42 / var(--tw-ring-opacity));
}

.ring-zinc-900 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(24 24 27 / var(--tw-ring-opacity));
}

.ring-zinc-950 {
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(9 9 11 / var(--tw-ring-opacity));
}

.ring-offset-0 {
  --tw-ring-offset-width: 0px;
}

.ring-offset-1 {
  --tw-ring-offset-width: 1px;
}

.ring-offset-2 {
  --tw-ring-offset-width: 2px;
}

.ring-offset-4 {
  --tw-ring-offset-width: 4px;
}

.ring-offset-8 {
  --tw-ring-offset-width: 8px;
}

.ring-offset-amber-100 {
  --tw-ring-offset-color: #fef3c7;
}

.ring-offset-amber-200 {
  --tw-ring-offset-color: #fde68a;
}

.ring-offset-amber-300 {
  --tw-ring-offset-color: #fcd34d;
}

.ring-offset-amber-400 {
  --tw-ring-offset-color: #fbbf24;
}

.ring-offset-amber-50 {
  --tw-ring-offset-color: #fffbeb;
}

.ring-offset-amber-500 {
  --tw-ring-offset-color: #f59e0b;
}

.ring-offset-amber-600 {
  --tw-ring-offset-color: #d97706;
}

.ring-offset-amber-700 {
  --tw-ring-offset-color: #b45309;
}

.ring-offset-amber-800 {
  --tw-ring-offset-color: #92400e;
}

.ring-offset-amber-900 {
  --tw-ring-offset-color: #78350f;
}

.ring-offset-amber-950 {
  --tw-ring-offset-color: #451a03;
}

.ring-offset-black {
  --tw-ring-offset-color: #000;
}

.ring-offset-blue-100 {
  --tw-ring-offset-color: #dbeafe;
}

.ring-offset-blue-200 {
  --tw-ring-offset-color: #bfdbfe;
}

.ring-offset-blue-300 {
  --tw-ring-offset-color: #93c5fd;
}

.ring-offset-blue-400 {
  --tw-ring-offset-color: #60a5fa;
}

.ring-offset-blue-50 {
  --tw-ring-offset-color: #eff6ff;
}

.ring-offset-blue-500 {
  --tw-ring-offset-color: #3b82f6;
}

.ring-offset-blue-600 {
  --tw-ring-offset-color: #2563eb;
}

.ring-offset-blue-700 {
  --tw-ring-offset-color: #1d4ed8;
}

.ring-offset-blue-800 {
  --tw-ring-offset-color: #1e40af;
}

.ring-offset-blue-900 {
  --tw-ring-offset-color: #1e3a8a;
}

.ring-offset-blue-950 {
  --tw-ring-offset-color: #172554;
}

.ring-offset-current {
  --tw-ring-offset-color: currentColor;
}

.ring-offset-cyan-100 {
  --tw-ring-offset-color: #cffafe;
}

.ring-offset-cyan-200 {
  --tw-ring-offset-color: #a5f3fc;
}

.ring-offset-cyan-300 {
  --tw-ring-offset-color: #67e8f9;
}

.ring-offset-cyan-400 {
  --tw-ring-offset-color: #22d3ee;
}

.ring-offset-cyan-50 {
  --tw-ring-offset-color: #ecfeff;
}

.ring-offset-cyan-500 {
  --tw-ring-offset-color: #06b6d4;
}

.ring-offset-cyan-600 {
  --tw-ring-offset-color: #0891b2;
}

.ring-offset-cyan-700 {
  --tw-ring-offset-color: #0e7490;
}

.ring-offset-cyan-800 {
  --tw-ring-offset-color: #155e75;
}

.ring-offset-cyan-900 {
  --tw-ring-offset-color: #164e63;
}

.ring-offset-cyan-950 {
  --tw-ring-offset-color: #083344;
}

.ring-offset-emerald-100 {
  --tw-ring-offset-color: #d1fae5;
}

.ring-offset-emerald-200 {
  --tw-ring-offset-color: #a7f3d0;
}

.ring-offset-emerald-300 {
  --tw-ring-offset-color: #6ee7b7;
}

.ring-offset-emerald-400 {
  --tw-ring-offset-color: #34d399;
}

.ring-offset-emerald-50 {
  --tw-ring-offset-color: #ecfdf5;
}

.ring-offset-emerald-500 {
  --tw-ring-offset-color: #10b981;
}

.ring-offset-emerald-600 {
  --tw-ring-offset-color: #059669;
}

.ring-offset-emerald-700 {
  --tw-ring-offset-color: #047857;
}

.ring-offset-emerald-800 {
  --tw-ring-offset-color: #065f46;
}

.ring-offset-emerald-900 {
  --tw-ring-offset-color: #064e3b;
}

.ring-offset-emerald-950 {
  --tw-ring-offset-color: #022c22;
}

.ring-offset-fuchsia-100 {
  --tw-ring-offset-color: #fae8ff;
}

.ring-offset-fuchsia-200 {
  --tw-ring-offset-color: #f5d0fe;
}

.ring-offset-fuchsia-300 {
  --tw-ring-offset-color: #f0abfc;
}

.ring-offset-fuchsia-400 {
  --tw-ring-offset-color: #e879f9;
}

.ring-offset-fuchsia-50 {
  --tw-ring-offset-color: #fdf4ff;
}

.ring-offset-fuchsia-500 {
  --tw-ring-offset-color: #d946ef;
}

.ring-offset-fuchsia-600 {
  --tw-ring-offset-color: #c026d3;
}

.ring-offset-fuchsia-700 {
  --tw-ring-offset-color: #a21caf;
}

.ring-offset-fuchsia-800 {
  --tw-ring-offset-color: #86198f;
}

.ring-offset-fuchsia-900 {
  --tw-ring-offset-color: #701a75;
}

.ring-offset-fuchsia-950 {
  --tw-ring-offset-color: #4a044e;
}

.ring-offset-gray-100 {
  --tw-ring-offset-color: #f3f4f6;
}

.ring-offset-gray-200 {
  --tw-ring-offset-color: #e5e7eb;
}

.ring-offset-gray-300 {
  --tw-ring-offset-color: #d1d5db;
}

.ring-offset-gray-400 {
  --tw-ring-offset-color: #9ca3af;
}

.ring-offset-gray-50 {
  --tw-ring-offset-color: #f9fafb;
}

.ring-offset-gray-500 {
  --tw-ring-offset-color: #6b7280;
}

.ring-offset-gray-600 {
  --tw-ring-offset-color: #4b5563;
}

.ring-offset-gray-700 {
  --tw-ring-offset-color: #374151;
}

.ring-offset-gray-800 {
  --tw-ring-offset-color: #1f2937;
}

.ring-offset-gray-900 {
  --tw-ring-offset-color: #111827;
}

.ring-offset-gray-950 {
  --tw-ring-offset-color: #030712;
}

.ring-offset-green-100 {
  --tw-ring-offset-color: #dcfce7;
}

.ring-offset-green-200 {
  --tw-ring-offset-color: #bbf7d0;
}

.ring-offset-green-300 {
  --tw-ring-offset-color: #86efac;
}

.ring-offset-green-400 {
  --tw-ring-offset-color: #4ade80;
}

.ring-offset-green-50 {
  --tw-ring-offset-color: #f0fdf4;
}

.ring-offset-green-500 {
  --tw-ring-offset-color: #22c55e;
}

.ring-offset-green-600 {
  --tw-ring-offset-color: #16a34a;
}

.ring-offset-green-700 {
  --tw-ring-offset-color: #15803d;
}

.ring-offset-green-800 {
  --tw-ring-offset-color: #166534;
}

.ring-offset-green-900 {
  --tw-ring-offset-color: #14532d;
}

.ring-offset-green-950 {
  --tw-ring-offset-color: #052e16;
}

.ring-offset-indigo-100 {
  --tw-ring-offset-color: #e0e7ff;
}

.ring-offset-indigo-200 {
  --tw-ring-offset-color: #c7d2fe;
}

.ring-offset-indigo-300 {
  --tw-ring-offset-color: #a5b4fc;
}

.ring-offset-indigo-400 {
  --tw-ring-offset-color: #818cf8;
}

.ring-offset-indigo-50 {
  --tw-ring-offset-color: #eef2ff;
}

.ring-offset-indigo-500 {
  --tw-ring-offset-color: #6366f1;
}

.ring-offset-indigo-600 {
  --tw-ring-offset-color: #4f46e5;
}

.ring-offset-indigo-700 {
  --tw-ring-offset-color: #4338ca;
}

.ring-offset-indigo-800 {
  --tw-ring-offset-color: #3730a3;
}

.ring-offset-indigo-900 {
  --tw-ring-offset-color: #312e81;
}

.ring-offset-indigo-950 {
  --tw-ring-offset-color: #1e1b4b;
}

.ring-offset-inherit {
  --tw-ring-offset-color: inherit;
}

.ring-offset-lime-100 {
  --tw-ring-offset-color: #ecfccb;
}

.ring-offset-lime-200 {
  --tw-ring-offset-color: #d9f99d;
}

.ring-offset-lime-300 {
  --tw-ring-offset-color: #bef264;
}

.ring-offset-lime-400 {
  --tw-ring-offset-color: #a3e635;
}

.ring-offset-lime-50 {
  --tw-ring-offset-color: #f7fee7;
}

.ring-offset-lime-500 {
  --tw-ring-offset-color: #84cc16;
}

.ring-offset-lime-600 {
  --tw-ring-offset-color: #65a30d;
}

.ring-offset-lime-700 {
  --tw-ring-offset-color: #4d7c0f;
}

.ring-offset-lime-800 {
  --tw-ring-offset-color: #3f6212;
}

.ring-offset-lime-900 {
  --tw-ring-offset-color: #365314;
}

.ring-offset-lime-950 {
  --tw-ring-offset-color: #1a2e05;
}

.ring-offset-neutral-100 {
  --tw-ring-offset-color: #f5f5f5;
}

.ring-offset-neutral-200 {
  --tw-ring-offset-color: #e5e5e5;
}

.ring-offset-neutral-300 {
  --tw-ring-offset-color: #d4d4d4;
}

.ring-offset-neutral-400 {
  --tw-ring-offset-color: #a3a3a3;
}

.ring-offset-neutral-50 {
  --tw-ring-offset-color: #fafafa;
}

.ring-offset-neutral-500 {
  --tw-ring-offset-color: #737373;
}

.ring-offset-neutral-600 {
  --tw-ring-offset-color: #525252;
}

.ring-offset-neutral-700 {
  --tw-ring-offset-color: #404040;
}

.ring-offset-neutral-800 {
  --tw-ring-offset-color: #262626;
}

.ring-offset-neutral-900 {
  --tw-ring-offset-color: #171717;
}

.ring-offset-neutral-950 {
  --tw-ring-offset-color: #0a0a0a;
}

.ring-offset-orange-100 {
  --tw-ring-offset-color: #ffedd5;
}

.ring-offset-orange-200 {
  --tw-ring-offset-color: #fed7aa;
}

.ring-offset-orange-300 {
  --tw-ring-offset-color: #fdba74;
}

.ring-offset-orange-400 {
  --tw-ring-offset-color: #fb923c;
}

.ring-offset-orange-50 {
  --tw-ring-offset-color: #fff7ed;
}

.ring-offset-orange-500 {
  --tw-ring-offset-color: #f97316;
}

.ring-offset-orange-600 {
  --tw-ring-offset-color: #ea580c;
}

.ring-offset-orange-700 {
  --tw-ring-offset-color: #c2410c;
}

.ring-offset-orange-800 {
  --tw-ring-offset-color: #9a3412;
}

.ring-offset-orange-900 {
  --tw-ring-offset-color: #7c2d12;
}

.ring-offset-orange-950 {
  --tw-ring-offset-color: #431407;
}

.ring-offset-pink-100 {
  --tw-ring-offset-color: #fce7f3;
}

.ring-offset-pink-200 {
  --tw-ring-offset-color: #fbcfe8;
}

.ring-offset-pink-300 {
  --tw-ring-offset-color: #f9a8d4;
}

.ring-offset-pink-400 {
  --tw-ring-offset-color: #f472b6;
}

.ring-offset-pink-50 {
  --tw-ring-offset-color: #fdf2f8;
}

.ring-offset-pink-500 {
  --tw-ring-offset-color: #ec4899;
}

.ring-offset-pink-600 {
  --tw-ring-offset-color: #db2777;
}

.ring-offset-pink-700 {
  --tw-ring-offset-color: #be185d;
}

.ring-offset-pink-800 {
  --tw-ring-offset-color: #9d174d;
}

.ring-offset-pink-900 {
  --tw-ring-offset-color: #831843;
}

.ring-offset-pink-950 {
  --tw-ring-offset-color: #500724;
}

.ring-offset-purple-100 {
  --tw-ring-offset-color: #f3e8ff;
}

.ring-offset-purple-200 {
  --tw-ring-offset-color: #e9d5ff;
}

.ring-offset-purple-300 {
  --tw-ring-offset-color: #d8b4fe;
}

.ring-offset-purple-400 {
  --tw-ring-offset-color: #c084fc;
}

.ring-offset-purple-50 {
  --tw-ring-offset-color: #faf5ff;
}

.ring-offset-purple-500 {
  --tw-ring-offset-color: #a855f7;
}

.ring-offset-purple-600 {
  --tw-ring-offset-color: #9333ea;
}

.ring-offset-purple-700 {
  --tw-ring-offset-color: #7e22ce;
}

.ring-offset-purple-800 {
  --tw-ring-offset-color: #6b21a8;
}

.ring-offset-purple-900 {
  --tw-ring-offset-color: #581c87;
}

.ring-offset-purple-950 {
  --tw-ring-offset-color: #3b0764;
}

.ring-offset-red-100 {
  --tw-ring-offset-color: #fee2e2;
}

.ring-offset-red-200 {
  --tw-ring-offset-color: #fecaca;
}

.ring-offset-red-300 {
  --tw-ring-offset-color: #fca5a5;
}

.ring-offset-red-400 {
  --tw-ring-offset-color: #f87171;
}

.ring-offset-red-50 {
  --tw-ring-offset-color: #fef2f2;
}

.ring-offset-red-500 {
  --tw-ring-offset-color: #ef4444;
}

.ring-offset-red-600 {
  --tw-ring-offset-color: #dc2626;
}

.ring-offset-red-700 {
  --tw-ring-offset-color: #b91c1c;
}

.ring-offset-red-800 {
  --tw-ring-offset-color: #991b1b;
}

.ring-offset-red-900 {
  --tw-ring-offset-color: #7f1d1d;
}

.ring-offset-red-950 {
  --tw-ring-offset-color: #450a0a;
}

.ring-offset-rose-100 {
  --tw-ring-offset-color: #ffe4e6;
}

.ring-offset-rose-200 {
  --tw-ring-offset-color: #fecdd3;
}

.ring-offset-rose-300 {
  --tw-ring-offset-color: #fda4af;
}

.ring-offset-rose-400 {
  --tw-ring-offset-color: #fb7185;
}

.ring-offset-rose-50 {
  --tw-ring-offset-color: #fff1f2;
}

.ring-offset-rose-500 {
  --tw-ring-offset-color: #f43f5e;
}

.ring-offset-rose-600 {
  --tw-ring-offset-color: #e11d48;
}

.ring-offset-rose-700 {
  --tw-ring-offset-color: #be123c;
}

.ring-offset-rose-800 {
  --tw-ring-offset-color: #9f1239;
}

.ring-offset-rose-900 {
  --tw-ring-offset-color: #881337;
}

.ring-offset-rose-950 {
  --tw-ring-offset-color: #4c0519;
}

.ring-offset-sky-100 {
  --tw-ring-offset-color: #e0f2fe;
}

.ring-offset-sky-200 {
  --tw-ring-offset-color: #bae6fd;
}

.ring-offset-sky-300 {
  --tw-ring-offset-color: #7dd3fc;
}

.ring-offset-sky-400 {
  --tw-ring-offset-color: #38bdf8;
}

.ring-offset-sky-50 {
  --tw-ring-offset-color: #f0f9ff;
}

.ring-offset-sky-500 {
  --tw-ring-offset-color: #0ea5e9;
}

.ring-offset-sky-600 {
  --tw-ring-offset-color: #0284c7;
}

.ring-offset-sky-700 {
  --tw-ring-offset-color: #0369a1;
}

.ring-offset-sky-800 {
  --tw-ring-offset-color: #075985;
}

.ring-offset-sky-900 {
  --tw-ring-offset-color: #0c4a6e;
}

.ring-offset-sky-950 {
  --tw-ring-offset-color: #082f49;
}

.ring-offset-slate-100 {
  --tw-ring-offset-color: #f1f5f9;
}

.ring-offset-slate-200 {
  --tw-ring-offset-color: #e2e8f0;
}

.ring-offset-slate-300 {
  --tw-ring-offset-color: #cbd5e1;
}

.ring-offset-slate-400 {
  --tw-ring-offset-color: #94a3b8;
}

.ring-offset-slate-50 {
  --tw-ring-offset-color: #f8fafc;
}

.ring-offset-slate-500 {
  --tw-ring-offset-color: #64748b;
}

.ring-offset-slate-600 {
  --tw-ring-offset-color: #475569;
}

.ring-offset-slate-700 {
  --tw-ring-offset-color: #334155;
}

.ring-offset-slate-800 {
  --tw-ring-offset-color: #1e293b;
}

.ring-offset-slate-900 {
  --tw-ring-offset-color: #0f172a;
}

.ring-offset-slate-950 {
  --tw-ring-offset-color: #020617;
}

.ring-offset-stone-100 {
  --tw-ring-offset-color: #f5f5f4;
}

.ring-offset-stone-200 {
  --tw-ring-offset-color: #e7e5e4;
}

.ring-offset-stone-300 {
  --tw-ring-offset-color: #d6d3d1;
}

.ring-offset-stone-400 {
  --tw-ring-offset-color: #a8a29e;
}

.ring-offset-stone-50 {
  --tw-ring-offset-color: #fafaf9;
}

.ring-offset-stone-500 {
  --tw-ring-offset-color: #78716c;
}

.ring-offset-stone-600 {
  --tw-ring-offset-color: #57534e;
}

.ring-offset-stone-700 {
  --tw-ring-offset-color: #44403c;
}

.ring-offset-stone-800 {
  --tw-ring-offset-color: #292524;
}

.ring-offset-stone-900 {
  --tw-ring-offset-color: #1c1917;
}

.ring-offset-stone-950 {
  --tw-ring-offset-color: #0c0a09;
}

.ring-offset-teal-100 {
  --tw-ring-offset-color: #ccfbf1;
}

.ring-offset-teal-200 {
  --tw-ring-offset-color: #99f6e4;
}

.ring-offset-teal-300 {
  --tw-ring-offset-color: #5eead4;
}

.ring-offset-teal-400 {
  --tw-ring-offset-color: #2dd4bf;
}

.ring-offset-teal-50 {
  --tw-ring-offset-color: #f0fdfa;
}

.ring-offset-teal-500 {
  --tw-ring-offset-color: #14b8a6;
}

.ring-offset-teal-600 {
  --tw-ring-offset-color: #0d9488;
}

.ring-offset-teal-700 {
  --tw-ring-offset-color: #0f766e;
}

.ring-offset-teal-800 {
  --tw-ring-offset-color: #115e59;
}

.ring-offset-teal-900 {
  --tw-ring-offset-color: #134e4a;
}

.ring-offset-teal-950 {
  --tw-ring-offset-color: #042f2e;
}

.ring-offset-transparent {
  --tw-ring-offset-color: transparent;
}

.ring-offset-violet-100 {
  --tw-ring-offset-color: #ede9fe;
}

.ring-offset-violet-200 {
  --tw-ring-offset-color: #ddd6fe;
}

.ring-offset-violet-300 {
  --tw-ring-offset-color: #c4b5fd;
}

.ring-offset-violet-400 {
  --tw-ring-offset-color: #a78bfa;
}

.ring-offset-violet-50 {
  --tw-ring-offset-color: #f5f3ff;
}

.ring-offset-violet-500 {
  --tw-ring-offset-color: #8b5cf6;
}

.ring-offset-violet-600 {
  --tw-ring-offset-color: #7c3aed;
}

.ring-offset-violet-700 {
  --tw-ring-offset-color: #6d28d9;
}

.ring-offset-violet-800 {
  --tw-ring-offset-color: #5b21b6;
}

.ring-offset-violet-900 {
  --tw-ring-offset-color: #4c1d95;
}

.ring-offset-violet-950 {
  --tw-ring-offset-color: #2e1065;
}

.ring-offset-white {
  --tw-ring-offset-color: #fff;
}

.ring-offset-yellow-100 {
  --tw-ring-offset-color: #fef9c3;
}

.ring-offset-yellow-200 {
  --tw-ring-offset-color: #fef08a;
}

.ring-offset-yellow-300 {
  --tw-ring-offset-color: #fde047;
}

.ring-offset-yellow-400 {
  --tw-ring-offset-color: #facc15;
}

.ring-offset-yellow-50 {
  --tw-ring-offset-color: #fefce8;
}

.ring-offset-yellow-500 {
  --tw-ring-offset-color: #eab308;
}

.ring-offset-yellow-600 {
  --tw-ring-offset-color: #ca8a04;
}

.ring-offset-yellow-700 {
  --tw-ring-offset-color: #a16207;
}

.ring-offset-yellow-800 {
  --tw-ring-offset-color: #854d0e;
}

.ring-offset-yellow-900 {
  --tw-ring-offset-color: #713f12;
}

.ring-offset-yellow-950 {
  --tw-ring-offset-color: #422006;
}

.ring-offset-zinc-100 {
  --tw-ring-offset-color: #f4f4f5;
}

.ring-offset-zinc-200 {
  --tw-ring-offset-color: #e4e4e7;
}

.ring-offset-zinc-300 {
  --tw-ring-offset-color: #d4d4d8;
}

.ring-offset-zinc-400 {
  --tw-ring-offset-color: #a1a1aa;
}

.ring-offset-zinc-50 {
  --tw-ring-offset-color: #fafafa;
}

.ring-offset-zinc-500 {
  --tw-ring-offset-color: #71717a;
}

.ring-offset-zinc-600 {
  --tw-ring-offset-color: #52525b;
}

.ring-offset-zinc-700 {
  --tw-ring-offset-color: #3f3f46;
}

.ring-offset-zinc-800 {
  --tw-ring-offset-color: #27272a;
}

.ring-offset-zinc-900 {
  --tw-ring-offset-color: #18181b;
}

.ring-offset-zinc-950 {
  --tw-ring-offset-color: #09090b;
}

.blur {
  --tw-blur: blur(8px);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.blur-2xl {
  --tw-blur: blur(40px);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.blur-3xl {
  --tw-blur: blur(64px);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.blur-lg {
  --tw-blur: blur(16px);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.blur-md {
  --tw-blur: blur(12px);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.blur-none {
  --tw-blur: blur(0);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.blur-sm {
  --tw-blur: blur(4px);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.blur-xl {
  --tw-blur: blur(24px);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.brightness-0 {
  --tw-brightness: brightness(0);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.brightness-100 {
  --tw-brightness: brightness(1);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.brightness-105 {
  --tw-brightness: brightness(1.05);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.brightness-110 {
  --tw-brightness: brightness(1.1);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.brightness-125 {
  --tw-brightness: brightness(1.25);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.brightness-150 {
  --tw-brightness: brightness(1.5);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.brightness-200 {
  --tw-brightness: brightness(2);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.brightness-50 {
  --tw-brightness: brightness(.5);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.brightness-75 {
  --tw-brightness: brightness(.75);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.brightness-90 {
  --tw-brightness: brightness(.9);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.brightness-95 {
  --tw-brightness: brightness(.95);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.contrast-0 {
  --tw-contrast: contrast(0);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.contrast-100 {
  --tw-contrast: contrast(1);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.contrast-125 {
  --tw-contrast: contrast(1.25);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.contrast-150 {
  --tw-contrast: contrast(1.5);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.contrast-200 {
  --tw-contrast: contrast(2);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.contrast-50 {
  --tw-contrast: contrast(.5);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.contrast-75 {
  --tw-contrast: contrast(.75);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.drop-shadow {
  --tw-drop-shadow: drop-shadow(0 1px 2px rgb(0 0 0 / 0.1)) drop-shadow(0 1px 1px rgb(0 0 0 / 0.06));
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.drop-shadow-2xl {
  --tw-drop-shadow: drop-shadow(0 25px 25px rgb(0 0 0 / 0.15));
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.drop-shadow-lg {
  --tw-drop-shadow: drop-shadow(0 10px 8px rgb(0 0 0 / 0.04)) drop-shadow(0 4px 3px rgb(0 0 0 / 0.1));
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.drop-shadow-md {
  --tw-drop-shadow: drop-shadow(0 4px 3px rgb(0 0 0 / 0.07)) drop-shadow(0 2px 2px rgb(0 0 0 / 0.06));
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.drop-shadow-none {
  --tw-drop-shadow: drop-shadow(0 0 #0000);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.drop-shadow-sm {
  --tw-drop-shadow: drop-shadow(0 1px 1px rgb(0 0 0 / 0.05));
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.drop-shadow-xl {
  --tw-drop-shadow: drop-shadow(0 20px 13px rgb(0 0 0 / 0.03)) drop-shadow(0 8px 5px rgb(0 0 0 / 0.08));
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.grayscale {
  --tw-grayscale: grayscale(100%);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.grayscale-0 {
  --tw-grayscale: grayscale(0);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.-hue-rotate-0 {
  --tw-hue-rotate: hue-rotate(-0deg);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.-hue-rotate-15 {
  --tw-hue-rotate: hue-rotate(-15deg);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.-hue-rotate-180 {
  --tw-hue-rotate: hue-rotate(-180deg);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.-hue-rotate-30 {
  --tw-hue-rotate: hue-rotate(-30deg);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.-hue-rotate-60 {
  --tw-hue-rotate: hue-rotate(-60deg);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.-hue-rotate-90 {
  --tw-hue-rotate: hue-rotate(-90deg);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.hue-rotate-0 {
  --tw-hue-rotate: hue-rotate(0deg);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.hue-rotate-15 {
  --tw-hue-rotate: hue-rotate(15deg);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.hue-rotate-180 {
  --tw-hue-rotate: hue-rotate(180deg);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.hue-rotate-30 {
  --tw-hue-rotate: hue-rotate(30deg);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.hue-rotate-60 {
  --tw-hue-rotate: hue-rotate(60deg);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.hue-rotate-90 {
  --tw-hue-rotate: hue-rotate(90deg);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.invert {
  --tw-invert: invert(100%);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.invert-0 {
  --tw-invert: invert(0);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.saturate-0 {
  --tw-saturate: saturate(0);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.saturate-100 {
  --tw-saturate: saturate(1);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.saturate-150 {
  --tw-saturate: saturate(1.5);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.saturate-200 {
  --tw-saturate: saturate(2);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.saturate-50 {
  --tw-saturate: saturate(.5);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.sepia {
  --tw-sepia: sepia(100%);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.sepia-0 {
  --tw-sepia: sepia(0);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.backdrop-blur {
  --tw-backdrop-blur: blur(8px);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-blur-2xl {
  --tw-backdrop-blur: blur(40px);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-blur-3xl {
  --tw-backdrop-blur: blur(64px);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-blur-lg {
  --tw-backdrop-blur: blur(16px);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-blur-md {
  --tw-backdrop-blur: blur(12px);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-blur-none {
  --tw-backdrop-blur: blur(0);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-blur-sm {
  --tw-backdrop-blur: blur(4px);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-blur-xl {
  --tw-backdrop-blur: blur(24px);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-brightness-0 {
  --tw-backdrop-brightness: brightness(0);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-brightness-100 {
  --tw-backdrop-brightness: brightness(1);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-brightness-105 {
  --tw-backdrop-brightness: brightness(1.05);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-brightness-110 {
  --tw-backdrop-brightness: brightness(1.1);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-brightness-125 {
  --tw-backdrop-brightness: brightness(1.25);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-brightness-150 {
  --tw-backdrop-brightness: brightness(1.5);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-brightness-200 {
  --tw-backdrop-brightness: brightness(2);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-brightness-50 {
  --tw-backdrop-brightness: brightness(.5);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-brightness-75 {
  --tw-backdrop-brightness: brightness(.75);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-brightness-90 {
  --tw-backdrop-brightness: brightness(.9);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-brightness-95 {
  --tw-backdrop-brightness: brightness(.95);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-contrast-0 {
  --tw-backdrop-contrast: contrast(0);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-contrast-100 {
  --tw-backdrop-contrast: contrast(1);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-contrast-125 {
  --tw-backdrop-contrast: contrast(1.25);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-contrast-150 {
  --tw-backdrop-contrast: contrast(1.5);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-contrast-200 {
  --tw-backdrop-contrast: contrast(2);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-contrast-50 {
  --tw-backdrop-contrast: contrast(.5);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-contrast-75 {
  --tw-backdrop-contrast: contrast(.75);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-grayscale {
  --tw-backdrop-grayscale: grayscale(100%);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-grayscale-0 {
  --tw-backdrop-grayscale: grayscale(0);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.-backdrop-hue-rotate-0 {
  --tw-backdrop-hue-rotate: hue-rotate(-0deg);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.-backdrop-hue-rotate-15 {
  --tw-backdrop-hue-rotate: hue-rotate(-15deg);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.-backdrop-hue-rotate-180 {
  --tw-backdrop-hue-rotate: hue-rotate(-180deg);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.-backdrop-hue-rotate-30 {
  --tw-backdrop-hue-rotate: hue-rotate(-30deg);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.-backdrop-hue-rotate-60 {
  --tw-backdrop-hue-rotate: hue-rotate(-60deg);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.-backdrop-hue-rotate-90 {
  --tw-backdrop-hue-rotate: hue-rotate(-90deg);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-hue-rotate-0 {
  --tw-backdrop-hue-rotate: hue-rotate(0deg);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-hue-rotate-15 {
  --tw-backdrop-hue-rotate: hue-rotate(15deg);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-hue-rotate-180 {
  --tw-backdrop-hue-rotate: hue-rotate(180deg);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-hue-rotate-30 {
  --tw-backdrop-hue-rotate: hue-rotate(30deg);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-hue-rotate-60 {
  --tw-backdrop-hue-rotate: hue-rotate(60deg);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-hue-rotate-90 {
  --tw-backdrop-hue-rotate: hue-rotate(90deg);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-invert {
  --tw-backdrop-invert: invert(100%);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-invert-0 {
  --tw-backdrop-invert: invert(0);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-opacity-0 {
  --tw-backdrop-opacity: opacity(0);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-opacity-10 {
  --tw-backdrop-opacity: opacity(0.1);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-opacity-100 {
  --tw-backdrop-opacity: opacity(1);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-opacity-20 {
  --tw-backdrop-opacity: opacity(0.2);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-opacity-25 {
  --tw-backdrop-opacity: opacity(0.25);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-opacity-30 {
  --tw-backdrop-opacity: opacity(0.3);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-opacity-40 {
  --tw-backdrop-opacity: opacity(0.4);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-opacity-5 {
  --tw-backdrop-opacity: opacity(0.05);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-opacity-50 {
  --tw-backdrop-opacity: opacity(0.5);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-opacity-60 {
  --tw-backdrop-opacity: opacity(0.6);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-opacity-70 {
  --tw-backdrop-opacity: opacity(0.7);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-opacity-75 {
  --tw-backdrop-opacity: opacity(0.75);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-opacity-80 {
  --tw-backdrop-opacity: opacity(0.8);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-opacity-90 {
  --tw-backdrop-opacity: opacity(0.9);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-opacity-95 {
  --tw-backdrop-opacity: opacity(0.95);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-saturate-0 {
  --tw-backdrop-saturate: saturate(0);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-saturate-100 {
  --tw-backdrop-saturate: saturate(1);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-saturate-150 {
  --tw-backdrop-saturate: saturate(1.5);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-saturate-200 {
  --tw-backdrop-saturate: saturate(2);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-saturate-50 {
  --tw-backdrop-saturate: saturate(.5);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-sepia {
  --tw-backdrop-sepia: sepia(100%);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.backdrop-sepia-0 {
  --tw-backdrop-sepia: sepia(0);
  -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
          backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
}

.transition {
  transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, -webkit-backdrop-filter;
  transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter;
  transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter, -webkit-backdrop-filter;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}

.transition-all {
  transition-property: all;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}

.transition-colors {
  transition-property: color, background-color, border-color, text-decoration-color, fill, stroke;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}

.transition-none {
  transition-property: none;
}

.transition-opacity {
  transition-property: opacity;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}

.transition-shadow {
  transition-property: box-shadow;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}

.transition-transform {
  transition-property: transform;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}

.delay-0 {
  transition-delay: 0s;
}

.delay-100 {
  transition-delay: 100ms;
}

.delay-1000 {
  transition-delay: 1000ms;
}

.delay-150 {
  transition-delay: 150ms;
}

.delay-200 {
  transition-delay: 200ms;
}

.delay-300 {
  transition-delay: 300ms;
}

.delay-500 {
  transition-delay: 500ms;
}

.delay-700 {
  transition-delay: 700ms;
}

.delay-75 {
  transition-delay: 75ms;
}

.duration-0 {
  transition-duration: 0s;
}

.duration-100 {
  transition-duration: 100ms;
}

.duration-1000 {
  transition-duration: 1000ms;
}

.duration-150 {
  transition-duration: 150ms;
}

.duration-200 {
  transition-duration: 200ms;
}

.duration-300 {
  transition-duration: 300ms;
}

.duration-500 {
  transition-duration: 500ms;
}

.duration-700 {
  transition-duration: 700ms;
}

.duration-75 {
  transition-duration: 75ms;
}

.ease-in {
  transition-timing-function: cubic-bezier(0.4, 0, 1, 1);
}

.ease-in-out {
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
}

.ease-linear {
  transition-timing-function: linear;
}

.ease-out {
  transition-timing-function: cubic-bezier(0, 0, 0.2, 1);
}

.will-change-auto {
  will-change: auto;
}

.will-change-contents {
  will-change: contents;
}

.will-change-scroll {
  will-change: scroll-position;
}

.will-change-transform {
  will-change: transform;
}

.content-none {
  --tw-content: none;
  content: var(--tw-content);
}

"""
