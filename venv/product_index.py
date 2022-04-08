# product index

# imports
from openpyxl import load_workbook
from database import DataBase


# init the persistent memory of excel filename to be loaded
excel_file_storage = DataBase('excel_filename.txt')

# blank file structure for saving the loaded excel sheet
files = {
    'file_name': '',
    'status': '',
}

# get file name of the file marked as active
file = excel_file_storage.retrieve()

# load the excel sheet
wb = ''
try:
    wb = load_workbook(filename=file)
# if there is no product index reference excel file
except TypeError:
    print("\n\nERROR: no excel file set as active in excel_filename.txt\n")

# set the loaded sheet as active
sheet = wb.active


# test of crazy fast auto coding lmao [ success ]
# 000 - 099
product_000 = sheet['B2'].value
product_001 = sheet['B3'].value
product_002 = sheet['B4'].value
product_003 = sheet['B5'].value
product_004 = sheet['B6'].value
product_005 = sheet['B7'].value
product_006 = sheet['B8'].value
product_007 = sheet['B9'].value
product_008 = sheet['B10'].value
product_009 = sheet['B11'].value
product_010 = sheet['B12'].value
product_011 = sheet['B13'].value
product_012 = sheet['B14'].value
product_013 = sheet['B15'].value
product_014 = sheet['B16'].value
product_015 = sheet['B17'].value
product_016 = sheet['B18'].value
product_017 = sheet['B19'].value
product_018 = sheet['B20'].value
product_019 = sheet['B21'].value
product_020 = sheet['B22'].value
product_021 = sheet['B23'].value
product_022 = sheet['B24'].value
product_023 = sheet['B25'].value
product_024 = sheet['B26'].value
product_025 = sheet['B27'].value
product_026 = sheet['B28'].value
product_027 = sheet['B29'].value
product_028 = sheet['B30'].value
product_029 = sheet['B31'].value
product_030 = sheet['B32'].value
product_031 = sheet['B33'].value
product_032 = sheet['B34'].value
product_033 = sheet['B35'].value
product_034 = sheet['B36'].value
product_035 = sheet['B37'].value
product_036 = sheet['B38'].value
product_037 = sheet['B39'].value
product_038 = sheet['B40'].value
product_039 = sheet['B41'].value
product_040 = sheet['B42'].value
product_041 = sheet['B43'].value
product_042 = sheet['B44'].value
product_043 = sheet['B45'].value
product_044 = sheet['B46'].value
product_045 = sheet['B47'].value
product_046 = sheet['B48'].value
product_047 = sheet['B49'].value
product_048 = sheet['B50'].value
product_049 = sheet['B51'].value
product_050 = sheet['B52'].value
product_051 = sheet['B53'].value
product_052 = sheet['B54'].value
product_053 = sheet['B55'].value
product_054 = sheet['B56'].value
product_055 = sheet['B57'].value
product_056 = sheet['B58'].value
product_057 = sheet['B59'].value
product_058 = sheet['B60'].value
product_059 = sheet['B61'].value
product_060 = sheet['B62'].value
product_061 = sheet['B63'].value
product_062 = sheet['B64'].value
product_063 = sheet['B65'].value
product_064 = sheet['B66'].value
product_065 = sheet['B67'].value
product_066 = sheet['B68'].value
product_067 = sheet['B69'].value
product_068 = sheet['B70'].value
product_069 = sheet['B71'].value
product_070 = sheet['B72'].value
product_071 = sheet['B73'].value
product_072 = sheet['B74'].value
product_073 = sheet['B75'].value
product_074 = sheet['B76'].value
product_075 = sheet['B77'].value
product_076 = sheet['B78'].value
product_077 = sheet['B79'].value
product_078 = sheet['B80'].value
product_079 = sheet['B81'].value
product_080 = sheet['B82'].value
product_081 = sheet['B83'].value
product_082 = sheet['B84'].value
product_083 = sheet['B85'].value
product_084 = sheet['B86'].value
product_085 = sheet['B87'].value
product_086 = sheet['B88'].value
product_087 = sheet['B89'].value
product_088 = sheet['B90'].value
product_089 = sheet['B91'].value
product_090 = sheet['B92'].value
product_091 = sheet['B93'].value
product_092 = sheet['B94'].value
product_093 = sheet['B95'].value
product_094 = sheet['B96'].value
product_095 = sheet['B97'].value
product_096 = sheet['B98'].value
product_097 = sheet['B99'].value
product_098 = sheet['B100'].value
product_099 = sheet['B101'].value

# 100 - 199
product_100 = sheet['B102'].value
product_101 = sheet['B103'].value
product_102 = sheet['B104'].value
product_103 = sheet['B105'].value
product_104 = sheet['B106'].value
product_105 = sheet['B107'].value
product_106 = sheet['B108'].value
product_107 = sheet['B109'].value
product_108 = sheet['B110'].value
product_109 = sheet['B111'].value
product_110 = sheet['B112'].value
product_111 = sheet['B113'].value
product_112 = sheet['B114'].value
product_113 = sheet['B115'].value
product_114 = sheet['B116'].value
product_115 = sheet['B117'].value
product_116 = sheet['B118'].value
product_117 = sheet['B119'].value
product_118 = sheet['B120'].value
product_119 = sheet['B121'].value
product_120 = sheet['B122'].value
product_121 = sheet['B123'].value
product_122 = sheet['B124'].value
product_123 = sheet['B125'].value
product_124 = sheet['B126'].value
product_125 = sheet['B127'].value
product_126 = sheet['B128'].value
product_127 = sheet['B129'].value
product_128 = sheet['B130'].value
product_129 = sheet['B131'].value
product_130 = sheet['B132'].value
product_131 = sheet['B133'].value
product_132 = sheet['B134'].value
product_133 = sheet['B135'].value
product_134 = sheet['B136'].value
product_135 = sheet['B137'].value
product_136 = sheet['B138'].value
product_137 = sheet['B139'].value
product_138 = sheet['B140'].value
product_139 = sheet['B141'].value
product_140 = sheet['B142'].value
product_141 = sheet['B143'].value
product_142 = sheet['B144'].value
product_143 = sheet['B145'].value
product_144 = sheet['B146'].value
product_145 = sheet['B147'].value
product_146 = sheet['B148'].value
product_147 = sheet['B149'].value
product_148 = sheet['B150'].value
product_149 = sheet['B151'].value
product_150 = sheet['B152'].value
product_151 = sheet['B153'].value
product_152 = sheet['B154'].value
product_153 = sheet['B155'].value
product_154 = sheet['B156'].value
product_155 = sheet['B157'].value
product_156 = sheet['B158'].value
product_157 = sheet['B159'].value
product_158 = sheet['B160'].value
product_159 = sheet['B161'].value
product_160 = sheet['B162'].value
product_161 = sheet['B163'].value
product_162 = sheet['B164'].value
product_163 = sheet['B165'].value
product_164 = sheet['B166'].value
product_165 = sheet['B167'].value
product_166 = sheet['B168'].value
product_167 = sheet['B169'].value
product_168 = sheet['B170'].value
product_169 = sheet['B171'].value
product_170 = sheet['B172'].value
product_171 = sheet['B173'].value
product_172 = sheet['B174'].value
product_173 = sheet['B175'].value
product_174 = sheet['B176'].value
product_175 = sheet['B177'].value
product_176 = sheet['B178'].value
product_177 = sheet['B179'].value
product_178 = sheet['B180'].value
product_179 = sheet['B181'].value
product_180 = sheet['B182'].value
product_181 = sheet['B183'].value
product_182 = sheet['B184'].value
product_183 = sheet['B185'].value
product_184 = sheet['B186'].value
product_185 = sheet['B187'].value
product_186 = sheet['B188'].value
product_187 = sheet['B189'].value
product_188 = sheet['B190'].value
product_189 = sheet['B191'].value
product_190 = sheet['B192'].value
product_191 = sheet['B193'].value
product_192 = sheet['B194'].value
product_193 = sheet['B195'].value
product_194 = sheet['B196'].value
product_195 = sheet['B197'].value
product_196 = sheet['B198'].value
product_197 = sheet['B199'].value
product_198 = sheet['B200'].value
product_199 = sheet['B201'].value

# 200 - 299
product_200 = sheet['B202'].value
product_201 = sheet['B203'].value
product_202 = sheet['B204'].value
product_203 = sheet['B205'].value
product_204 = sheet['B206'].value
product_205 = sheet['B207'].value
product_206 = sheet['B208'].value
product_207 = sheet['B209'].value
product_208 = sheet['B210'].value
product_209 = sheet['B211'].value
product_210 = sheet['B212'].value
product_211 = sheet['B213'].value
product_212 = sheet['B214'].value
product_213 = sheet['B215'].value
product_214 = sheet['B216'].value
product_215 = sheet['B217'].value
product_216 = sheet['B218'].value
product_217 = sheet['B219'].value
product_218 = sheet['B220'].value
product_219 = sheet['B221'].value
product_220 = sheet['B222'].value
product_221 = sheet['B223'].value
product_222 = sheet['B224'].value
product_223 = sheet['B225'].value
product_224 = sheet['B226'].value
product_225 = sheet['B227'].value
product_226 = sheet['B228'].value
product_227 = sheet['B229'].value
product_228 = sheet['B230'].value
product_229 = sheet['B231'].value
product_230 = sheet['B232'].value
product_231 = sheet['B233'].value
product_232 = sheet['B234'].value
product_233 = sheet['B235'].value
product_234 = sheet['B236'].value
product_235 = sheet['B237'].value
product_236 = sheet['B238'].value
product_237 = sheet['B239'].value
product_238 = sheet['B240'].value
product_239 = sheet['B241'].value
product_240 = sheet['B242'].value
product_241 = sheet['B243'].value
product_242 = sheet['B244'].value
product_243 = sheet['B245'].value
product_244 = sheet['B246'].value
product_245 = sheet['B247'].value
product_246 = sheet['B248'].value
product_247 = sheet['B249'].value
product_248 = sheet['B250'].value
product_249 = sheet['B251'].value
product_250 = sheet['B252'].value
product_251 = sheet['B253'].value
product_252 = sheet['B254'].value
product_253 = sheet['B255'].value
product_254 = sheet['B256'].value
product_255 = sheet['B257'].value
product_256 = sheet['B258'].value
product_257 = sheet['B259'].value
product_258 = sheet['B260'].value
product_259 = sheet['B261'].value
product_260 = sheet['B262'].value
product_261 = sheet['B263'].value
product_262 = sheet['B264'].value
product_263 = sheet['B265'].value
product_264 = sheet['B266'].value
product_265 = sheet['B267'].value
product_266 = sheet['B268'].value
product_267 = sheet['B269'].value
product_268 = sheet['B270'].value
product_269 = sheet['B271'].value
product_270 = sheet['B272'].value
product_271 = sheet['B273'].value
product_272 = sheet['B274'].value
product_273 = sheet['B275'].value
product_274 = sheet['B276'].value
product_275 = sheet['B277'].value
product_276 = sheet['B278'].value
product_277 = sheet['B279'].value
product_278 = sheet['B280'].value
product_279 = sheet['B281'].value
product_280 = sheet['B282'].value
product_281 = sheet['B283'].value
product_282 = sheet['B284'].value
product_283 = sheet['B285'].value
product_284 = sheet['B286'].value
product_285 = sheet['B287'].value
product_286 = sheet['B288'].value
product_287 = sheet['B289'].value
product_288 = sheet['B290'].value
product_289 = sheet['B291'].value
product_290 = sheet['B292'].value
product_291 = sheet['B293'].value
product_292 = sheet['B294'].value
product_293 = sheet['B295'].value
product_294 = sheet['B296'].value
product_295 = sheet['B297'].value
product_296 = sheet['B298'].value
product_297 = sheet['B299'].value
product_298 = sheet['B300'].value
product_299 = sheet['B301'].value

# 300 - 399
product_300 = sheet['B302'].value
product_301 = sheet['B303'].value
product_302 = sheet['B304'].value
product_303 = sheet['B305'].value
product_304 = sheet['B306'].value
product_305 = sheet['B307'].value
product_306 = sheet['B308'].value
product_307 = sheet['B309'].value
product_308 = sheet['B310'].value
product_309 = sheet['B311'].value
product_310 = sheet['B312'].value
product_311 = sheet['B313'].value
product_312 = sheet['B314'].value
product_313 = sheet['B315'].value
product_314 = sheet['B316'].value
product_315 = sheet['B317'].value
product_316 = sheet['B318'].value
product_317 = sheet['B319'].value
product_318 = sheet['B320'].value
product_319 = sheet['B321'].value
product_320 = sheet['B322'].value
product_321 = sheet['B323'].value
product_322 = sheet['B324'].value
product_323 = sheet['B325'].value
product_324 = sheet['B326'].value
product_325 = sheet['B327'].value
product_326 = sheet['B328'].value
product_327 = sheet['B329'].value
product_328 = sheet['B330'].value
product_329 = sheet['B331'].value
product_330 = sheet['B332'].value
product_331 = sheet['B333'].value
product_332 = sheet['B334'].value
product_333 = sheet['B335'].value
product_334 = sheet['B336'].value
product_335 = sheet['B337'].value
product_336 = sheet['B338'].value
product_337 = sheet['B339'].value
product_338 = sheet['B340'].value
product_339 = sheet['B341'].value
product_340 = sheet['B342'].value
product_341 = sheet['B343'].value
product_342 = sheet['B344'].value
product_343 = sheet['B345'].value
product_344 = sheet['B346'].value
product_345 = sheet['B347'].value
product_346 = sheet['B348'].value
product_347 = sheet['B349'].value
product_348 = sheet['B350'].value
product_349 = sheet['B351'].value
product_350 = sheet['B352'].value
product_351 = sheet['B353'].value
product_352 = sheet['B354'].value
product_353 = sheet['B355'].value
product_354 = sheet['B356'].value
product_355 = sheet['B357'].value
product_356 = sheet['B358'].value
product_357 = sheet['B359'].value
product_358 = sheet['B360'].value
product_359 = sheet['B361'].value
product_360 = sheet['B362'].value
product_361 = sheet['B363'].value
product_362 = sheet['B364'].value
product_363 = sheet['B365'].value
product_364 = sheet['B366'].value
product_365 = sheet['B367'].value
product_366 = sheet['B368'].value
product_367 = sheet['B369'].value
product_368 = sheet['B370'].value
product_369 = sheet['B371'].value
product_370 = sheet['B372'].value
product_371 = sheet['B373'].value
product_372 = sheet['B374'].value
product_373 = sheet['B375'].value
product_374 = sheet['B376'].value
product_375 = sheet['B377'].value
product_376 = sheet['B378'].value
product_377 = sheet['B379'].value
product_378 = sheet['B380'].value
product_379 = sheet['B381'].value
product_380 = sheet['B382'].value
product_381 = sheet['B383'].value
product_382 = sheet['B384'].value
product_383 = sheet['B385'].value
product_384 = sheet['B386'].value
product_385 = sheet['B387'].value
product_386 = sheet['B388'].value
product_387 = sheet['B389'].value
product_388 = sheet['B390'].value
product_389 = sheet['B391'].value
product_390 = sheet['B392'].value
product_391 = sheet['B393'].value
product_392 = sheet['B394'].value
product_393 = sheet['B395'].value
product_394 = sheet['B396'].value
product_395 = sheet['B397'].value
product_396 = sheet['B398'].value
product_397 = sheet['B399'].value
product_398 = sheet['B400'].value
product_399 = sheet['B401'].value

# 400 - 499
product_400 = sheet['B402'].value
product_401 = sheet['B403'].value
product_402 = sheet['B404'].value
product_403 = sheet['B405'].value
product_404 = sheet['B406'].value
product_405 = sheet['B407'].value
product_406 = sheet['B408'].value
product_407 = sheet['B409'].value
product_408 = sheet['B410'].value
product_409 = sheet['B411'].value
product_410 = sheet['B412'].value
product_411 = sheet['B413'].value
product_412 = sheet['B414'].value
product_413 = sheet['B415'].value
product_414 = sheet['B416'].value
product_415 = sheet['B417'].value
product_416 = sheet['B418'].value
product_417 = sheet['B419'].value
product_418 = sheet['B420'].value
product_419 = sheet['B421'].value
product_420 = sheet['B422'].value
product_421 = sheet['B423'].value
product_422 = sheet['B424'].value
product_423 = sheet['B425'].value
product_424 = sheet['B426'].value
product_425 = sheet['B427'].value
product_426 = sheet['B428'].value
product_427 = sheet['B429'].value
product_428 = sheet['B430'].value
product_429 = sheet['B431'].value
product_430 = sheet['B432'].value
product_431 = sheet['B433'].value
product_432 = sheet['B434'].value
product_433 = sheet['B435'].value
product_434 = sheet['B436'].value
product_435 = sheet['B437'].value
product_436 = sheet['B438'].value
product_437 = sheet['B439'].value
product_438 = sheet['B440'].value
product_439 = sheet['B441'].value
product_440 = sheet['B442'].value
product_441 = sheet['B443'].value
product_442 = sheet['B444'].value
product_443 = sheet['B445'].value
product_444 = sheet['B446'].value
product_445 = sheet['B447'].value
product_446 = sheet['B448'].value
product_447 = sheet['B449'].value
product_448 = sheet['B450'].value
product_449 = sheet['B451'].value
product_450 = sheet['B452'].value
product_451 = sheet['B453'].value
product_452 = sheet['B454'].value
product_453 = sheet['B455'].value
product_454 = sheet['B456'].value
product_455 = sheet['B457'].value
product_456 = sheet['B458'].value
product_457 = sheet['B459'].value
product_458 = sheet['B460'].value
product_459 = sheet['B461'].value
product_460 = sheet['B462'].value
product_461 = sheet['B463'].value
product_462 = sheet['B464'].value
product_463 = sheet['B465'].value
product_464 = sheet['B466'].value
product_465 = sheet['B467'].value
product_466 = sheet['B468'].value
product_467 = sheet['B469'].value
product_468 = sheet['B470'].value
product_469 = sheet['B471'].value
product_470 = sheet['B472'].value
product_471 = sheet['B473'].value
product_472 = sheet['B474'].value
product_473 = sheet['B475'].value
product_474 = sheet['B476'].value
product_475 = sheet['B477'].value
product_476 = sheet['B478'].value
product_477 = sheet['B479'].value
product_478 = sheet['B480'].value
product_479 = sheet['B481'].value
product_480 = sheet['B482'].value
product_481 = sheet['B483'].value
product_482 = sheet['B484'].value
product_483 = sheet['B485'].value
product_484 = sheet['B486'].value
product_485 = sheet['B487'].value
product_486 = sheet['B488'].value
product_487 = sheet['B489'].value
product_488 = sheet['B490'].value
product_489 = sheet['B491'].value
product_490 = sheet['B492'].value
product_491 = sheet['B493'].value
product_492 = sheet['B494'].value
product_493 = sheet['B495'].value
product_494 = sheet['B496'].value
product_495 = sheet['B497'].value
product_496 = sheet['B498'].value
product_497 = sheet['B499'].value
product_498 = sheet['B500'].value
product_499 = sheet['B501'].value

# 500 - 599
product_500 = sheet['B502'].value
product_501 = sheet['B503'].value
product_502 = sheet['B504'].value
product_503 = sheet['B505'].value
product_504 = sheet['B506'].value
product_505 = sheet['B507'].value
product_506 = sheet['B508'].value
product_507 = sheet['B509'].value
product_508 = sheet['B510'].value
product_509 = sheet['B511'].value
product_510 = sheet['B512'].value
product_511 = sheet['B513'].value
product_512 = sheet['B514'].value
product_513 = sheet['B515'].value
product_514 = sheet['B516'].value
product_515 = sheet['B517'].value
product_516 = sheet['B518'].value
product_517 = sheet['B519'].value
product_518 = sheet['B520'].value
product_519 = sheet['B521'].value
product_520 = sheet['B522'].value
product_521 = sheet['B523'].value
product_522 = sheet['B524'].value
product_523 = sheet['B525'].value
product_524 = sheet['B526'].value
product_525 = sheet['B527'].value
product_526 = sheet['B528'].value
product_527 = sheet['B529'].value
product_528 = sheet['B530'].value
product_529 = sheet['B531'].value
product_530 = sheet['B532'].value
product_531 = sheet['B533'].value
product_532 = sheet['B534'].value
product_533 = sheet['B535'].value
product_534 = sheet['B536'].value
product_535 = sheet['B537'].value
product_536 = sheet['B538'].value
product_537 = sheet['B539'].value
product_538 = sheet['B540'].value
product_539 = sheet['B541'].value
product_540 = sheet['B542'].value
product_541 = sheet['B543'].value
product_542 = sheet['B544'].value
product_543 = sheet['B545'].value
product_544 = sheet['B546'].value
product_545 = sheet['B547'].value
product_546 = sheet['B548'].value
product_547 = sheet['B549'].value
product_548 = sheet['B550'].value
product_549 = sheet['B551'].value
product_550 = sheet['B552'].value
product_551 = sheet['B553'].value
product_552 = sheet['B554'].value
product_553 = sheet['B555'].value
product_554 = sheet['B556'].value
product_555 = sheet['B557'].value
product_556 = sheet['B558'].value
product_557 = sheet['B559'].value
product_558 = sheet['B560'].value
product_559 = sheet['B561'].value
product_560 = sheet['B562'].value
product_561 = sheet['B563'].value
product_562 = sheet['B564'].value
product_563 = sheet['B565'].value
product_564 = sheet['B566'].value
product_565 = sheet['B567'].value
product_566 = sheet['B568'].value
product_567 = sheet['B569'].value
product_568 = sheet['B570'].value
product_569 = sheet['B571'].value
product_570 = sheet['B572'].value
product_571 = sheet['B573'].value
product_572 = sheet['B574'].value
product_573 = sheet['B575'].value
product_574 = sheet['B576'].value
product_575 = sheet['B577'].value
product_576 = sheet['B578'].value
product_577 = sheet['B579'].value
product_578 = sheet['B580'].value
product_579 = sheet['B581'].value
product_580 = sheet['B582'].value
product_581 = sheet['B583'].value
product_582 = sheet['B584'].value
product_583 = sheet['B585'].value
product_584 = sheet['B586'].value
product_585 = sheet['B587'].value
product_586 = sheet['B588'].value
product_587 = sheet['B589'].value
product_588 = sheet['B590'].value
product_589 = sheet['B591'].value
product_590 = sheet['B592'].value
product_591 = sheet['B593'].value
product_592 = sheet['B594'].value
product_593 = sheet['B595'].value
product_594 = sheet['B596'].value
product_595 = sheet['B597'].value
product_596 = sheet['B598'].value
product_597 = sheet['B599'].value
product_598 = sheet['B600'].value
product_599 = sheet['B601'].value

# 600 - 699
product_600 = sheet['B602'].value
product_601 = sheet['B603'].value
product_602 = sheet['B604'].value
product_603 = sheet['B605'].value
product_604 = sheet['B606'].value
product_605 = sheet['B607'].value
product_606 = sheet['B608'].value
product_607 = sheet['B609'].value
product_608 = sheet['B610'].value
product_609 = sheet['B611'].value
product_610 = sheet['B612'].value
product_611 = sheet['B613'].value
product_612 = sheet['B614'].value
product_613 = sheet['B615'].value
product_614 = sheet['B616'].value
product_615 = sheet['B617'].value
product_616 = sheet['B618'].value
product_617 = sheet['B619'].value
product_618 = sheet['B620'].value
product_619 = sheet['B621'].value
product_620 = sheet['B622'].value
product_621 = sheet['B623'].value
product_622 = sheet['B624'].value
product_623 = sheet['B625'].value
product_624 = sheet['B626'].value
product_625 = sheet['B627'].value
product_626 = sheet['B628'].value
product_627 = sheet['B629'].value
product_628 = sheet['B630'].value
product_629 = sheet['B631'].value
product_630 = sheet['B632'].value
product_631 = sheet['B633'].value
product_632 = sheet['B634'].value
product_633 = sheet['B635'].value
product_634 = sheet['B636'].value
product_635 = sheet['B637'].value
product_636 = sheet['B638'].value
product_637 = sheet['B639'].value
product_638 = sheet['B640'].value
product_639 = sheet['B641'].value
product_640 = sheet['B642'].value
product_641 = sheet['B643'].value
product_642 = sheet['B644'].value
product_643 = sheet['B645'].value
product_644 = sheet['B646'].value
product_645 = sheet['B647'].value
product_646 = sheet['B648'].value
product_647 = sheet['B649'].value
product_648 = sheet['B650'].value
product_649 = sheet['B651'].value
product_650 = sheet['B652'].value
product_651 = sheet['B653'].value
product_652 = sheet['B654'].value
product_653 = sheet['B655'].value
product_654 = sheet['B656'].value
product_655 = sheet['B657'].value
product_656 = sheet['B658'].value
product_657 = sheet['B659'].value
product_658 = sheet['B660'].value
product_659 = sheet['B661'].value
product_660 = sheet['B662'].value
product_661 = sheet['B663'].value
product_662 = sheet['B664'].value
product_663 = sheet['B665'].value
product_664 = sheet['B666'].value
product_665 = sheet['B667'].value
product_666 = sheet['B668'].value
product_667 = sheet['B669'].value
product_668 = sheet['B670'].value
product_669 = sheet['B671'].value
product_670 = sheet['B672'].value
product_671 = sheet['B673'].value
product_672 = sheet['B674'].value
product_673 = sheet['B675'].value
product_674 = sheet['B676'].value
product_675 = sheet['B677'].value
product_676 = sheet['B678'].value
product_677 = sheet['B679'].value
product_678 = sheet['B680'].value
product_679 = sheet['B681'].value
product_680 = sheet['B682'].value
product_681 = sheet['B683'].value
product_682 = sheet['B684'].value
product_683 = sheet['B685'].value
product_684 = sheet['B686'].value
product_685 = sheet['B687'].value
product_686 = sheet['B688'].value
product_687 = sheet['B689'].value
product_688 = sheet['B690'].value
product_689 = sheet['B691'].value
product_690 = sheet['B692'].value
product_691 = sheet['B693'].value
product_692 = sheet['B694'].value
product_693 = sheet['B695'].value
product_694 = sheet['B696'].value
product_695 = sheet['B697'].value
product_696 = sheet['B698'].value
product_697 = sheet['B699'].value
product_698 = sheet['B700'].value
product_699 = sheet['B701'].value

# 700 - 799
product_700 = sheet['B702'].value
product_701 = sheet['B703'].value
product_702 = sheet['B704'].value
product_703 = sheet['B705'].value
product_704 = sheet['B706'].value
product_705 = sheet['B707'].value
product_706 = sheet['B708'].value
product_707 = sheet['B709'].value
product_708 = sheet['B710'].value
product_709 = sheet['B711'].value
product_710 = sheet['B712'].value
product_711 = sheet['B713'].value
product_712 = sheet['B714'].value
product_713 = sheet['B715'].value
product_714 = sheet['B716'].value
product_715 = sheet['B717'].value
product_716 = sheet['B718'].value
product_717 = sheet['B719'].value
product_718 = sheet['B720'].value
product_719 = sheet['B721'].value
product_720 = sheet['B722'].value
product_721 = sheet['B723'].value
product_722 = sheet['B724'].value
product_723 = sheet['B725'].value
product_724 = sheet['B726'].value
product_725 = sheet['B727'].value
product_726 = sheet['B728'].value
product_727 = sheet['B729'].value
product_728 = sheet['B730'].value
product_729 = sheet['B731'].value
product_730 = sheet['B732'].value
product_731 = sheet['B733'].value
product_732 = sheet['B734'].value
product_733 = sheet['B735'].value
product_734 = sheet['B736'].value
product_735 = sheet['B737'].value
product_736 = sheet['B738'].value
product_737 = sheet['B739'].value
product_738 = sheet['B740'].value
product_739 = sheet['B741'].value
product_740 = sheet['B742'].value
product_741 = sheet['B743'].value
product_742 = sheet['B744'].value
product_743 = sheet['B745'].value
product_744 = sheet['B746'].value
product_745 = sheet['B747'].value
product_746 = sheet['B748'].value
product_747 = sheet['B749'].value
product_748 = sheet['B750'].value
product_749 = sheet['B751'].value
product_750 = sheet['B752'].value
product_751 = sheet['B753'].value
product_752 = sheet['B754'].value
product_753 = sheet['B755'].value
product_754 = sheet['B756'].value
product_755 = sheet['B757'].value
product_756 = sheet['B758'].value
product_757 = sheet['B759'].value
product_758 = sheet['B760'].value
product_759 = sheet['B761'].value
product_760 = sheet['B762'].value
product_761 = sheet['B763'].value
product_762 = sheet['B764'].value
product_763 = sheet['B765'].value
product_764 = sheet['B766'].value
product_765 = sheet['B767'].value
product_766 = sheet['B768'].value
product_767 = sheet['B769'].value
product_768 = sheet['B770'].value
product_769 = sheet['B771'].value
product_770 = sheet['B772'].value
product_771 = sheet['B773'].value
product_772 = sheet['B774'].value
product_773 = sheet['B775'].value
product_774 = sheet['B776'].value
product_775 = sheet['B777'].value
product_776 = sheet['B778'].value
product_777 = sheet['B779'].value
product_778 = sheet['B780'].value
product_779 = sheet['B781'].value
product_780 = sheet['B782'].value
product_781 = sheet['B783'].value
product_782 = sheet['B784'].value
product_783 = sheet['B785'].value
product_784 = sheet['B786'].value
product_785 = sheet['B787'].value
product_786 = sheet['B788'].value
product_787 = sheet['B789'].value
product_788 = sheet['B790'].value
product_789 = sheet['B791'].value
product_790 = sheet['B792'].value
product_791 = sheet['B793'].value
product_792 = sheet['B794'].value
product_793 = sheet['B795'].value
product_794 = sheet['B796'].value
product_795 = sheet['B797'].value
product_796 = sheet['B798'].value
product_797 = sheet['B799'].value
product_798 = sheet['B800'].value
product_799 = sheet['B801'].value

# 800 - 899
product_800 = sheet['B802'].value
product_801 = sheet['B803'].value
product_802 = sheet['B804'].value
product_803 = sheet['B805'].value
product_804 = sheet['B806'].value
product_805 = sheet['B807'].value
product_806 = sheet['B808'].value
product_807 = sheet['B809'].value
product_808 = sheet['B810'].value
product_809 = sheet['B811'].value
product_810 = sheet['B812'].value
product_811 = sheet['B813'].value
product_812 = sheet['B814'].value
product_813 = sheet['B815'].value
product_814 = sheet['B816'].value
product_815 = sheet['B817'].value
product_816 = sheet['B818'].value
product_817 = sheet['B819'].value
product_818 = sheet['B820'].value
product_819 = sheet['B821'].value
product_820 = sheet['B822'].value
product_821 = sheet['B823'].value
product_822 = sheet['B824'].value
product_823 = sheet['B825'].value
product_824 = sheet['B826'].value
product_825 = sheet['B827'].value
product_826 = sheet['B828'].value
product_827 = sheet['B829'].value
product_828 = sheet['B830'].value
product_829 = sheet['B831'].value
product_830 = sheet['B832'].value
product_831 = sheet['B833'].value
product_832 = sheet['B834'].value
product_833 = sheet['B835'].value
product_834 = sheet['B836'].value
product_835 = sheet['B837'].value
product_836 = sheet['B838'].value
product_837 = sheet['B839'].value
product_838 = sheet['B840'].value
product_839 = sheet['B841'].value
product_840 = sheet['B842'].value
product_841 = sheet['B843'].value
product_842 = sheet['B844'].value
product_843 = sheet['B845'].value
product_844 = sheet['B846'].value
product_845 = sheet['B847'].value
product_846 = sheet['B848'].value
product_847 = sheet['B849'].value
product_848 = sheet['B850'].value
product_849 = sheet['B851'].value
product_850 = sheet['B852'].value
product_851 = sheet['B853'].value
product_852 = sheet['B854'].value
product_853 = sheet['B855'].value
product_854 = sheet['B856'].value
product_855 = sheet['B857'].value
product_856 = sheet['B858'].value
product_857 = sheet['B859'].value
product_858 = sheet['B860'].value
product_859 = sheet['B861'].value
product_860 = sheet['B862'].value
product_861 = sheet['B863'].value
product_862 = sheet['B864'].value
product_863 = sheet['B865'].value
product_864 = sheet['B866'].value
product_865 = sheet['B867'].value
product_866 = sheet['B868'].value
product_867 = sheet['B869'].value
product_868 = sheet['B870'].value
product_869 = sheet['B871'].value
product_870 = sheet['B872'].value
product_871 = sheet['B873'].value
product_872 = sheet['B874'].value
product_873 = sheet['B875'].value
product_874 = sheet['B876'].value
product_875 = sheet['B877'].value
product_876 = sheet['B878'].value
product_877 = sheet['B879'].value
product_878 = sheet['B880'].value
product_879 = sheet['B881'].value
product_880 = sheet['B882'].value
product_881 = sheet['B883'].value
product_882 = sheet['B884'].value
product_883 = sheet['B885'].value
product_884 = sheet['B886'].value
product_885 = sheet['B887'].value
product_886 = sheet['B888'].value
product_887 = sheet['B889'].value
product_888 = sheet['B890'].value
product_889 = sheet['B891'].value
product_890 = sheet['B892'].value
product_891 = sheet['B893'].value
product_892 = sheet['B894'].value
product_893 = sheet['B895'].value
product_894 = sheet['B896'].value
product_895 = sheet['B897'].value
product_896 = sheet['B898'].value
product_897 = sheet['B899'].value
product_898 = sheet['B900'].value
product_899 = sheet['B901'].value

# 900 - 999
product_900 = sheet['B902'].value
product_901 = sheet['B903'].value
product_902 = sheet['B904'].value
product_903 = sheet['B905'].value
product_904 = sheet['B906'].value
product_905 = sheet['B907'].value
product_906 = sheet['B908'].value
product_907 = sheet['B909'].value
product_908 = sheet['B910'].value
product_909 = sheet['B911'].value
product_910 = sheet['B912'].value
product_911 = sheet['B913'].value
product_912 = sheet['B914'].value
product_913 = sheet['B915'].value
product_914 = sheet['B916'].value
product_915 = sheet['B917'].value
product_916 = sheet['B918'].value
product_917 = sheet['B919'].value
product_918 = sheet['B920'].value
product_919 = sheet['B921'].value
product_920 = sheet['B922'].value
product_921 = sheet['B923'].value
product_922 = sheet['B924'].value
product_923 = sheet['B925'].value
product_924 = sheet['B926'].value
product_925 = sheet['B927'].value
product_926 = sheet['B928'].value
product_927 = sheet['B929'].value
product_928 = sheet['B930'].value
product_929 = sheet['B931'].value
product_930 = sheet['B932'].value
product_931 = sheet['B933'].value
product_932 = sheet['B934'].value
product_933 = sheet['B935'].value
product_934 = sheet['B936'].value
product_935 = sheet['B937'].value
product_936 = sheet['B938'].value
product_937 = sheet['B939'].value
product_938 = sheet['B940'].value
product_939 = sheet['B941'].value
product_940 = sheet['B942'].value
product_941 = sheet['B943'].value
product_942 = sheet['B944'].value
product_943 = sheet['B945'].value
product_944 = sheet['B946'].value
product_945 = sheet['B947'].value
product_946 = sheet['B948'].value
product_947 = sheet['B949'].value
product_948 = sheet['B950'].value
product_949 = sheet['B951'].value
product_950 = sheet['B952'].value
product_951 = sheet['B953'].value
product_952 = sheet['B954'].value
product_953 = sheet['B955'].value
product_954 = sheet['B956'].value
product_955 = sheet['B957'].value
product_956 = sheet['B958'].value
product_957 = sheet['B959'].value
product_958 = sheet['B960'].value
product_959 = sheet['B961'].value
product_960 = sheet['B962'].value
product_961 = sheet['B963'].value
product_962 = sheet['B964'].value
product_963 = sheet['B965'].value
product_964 = sheet['B966'].value
product_965 = sheet['B967'].value
product_966 = sheet['B968'].value
product_967 = sheet['B969'].value
product_968 = sheet['B970'].value
product_969 = sheet['B971'].value
product_970 = sheet['B972'].value
product_971 = sheet['B973'].value
product_972 = sheet['B974'].value
product_973 = sheet['B975'].value
product_974 = sheet['B976'].value
product_975 = sheet['B977'].value
product_976 = sheet['B978'].value
product_977 = sheet['B979'].value
product_978 = sheet['B980'].value
product_979 = sheet['B981'].value
product_980 = sheet['B982'].value
product_981 = sheet['B983'].value
product_982 = sheet['B984'].value
product_983 = sheet['B985'].value
product_984 = sheet['B986'].value
product_985 = sheet['B987'].value
product_986 = sheet['B988'].value
product_987 = sheet['B989'].value
product_988 = sheet['B990'].value
product_989 = sheet['B991'].value
product_990 = sheet['B992'].value
product_991 = sheet['B993'].value
product_992 = sheet['B994'].value
product_993 = sheet['B995'].value
product_994 = sheet['B996'].value
product_995 = sheet['B997'].value
product_996 = sheet['B998'].value
product_997 = sheet['B999'].value
product_998 = sheet['B1000'].value
product_999 = sheet['B1001'].value

# it's 1000 more lines lmao
product_index = {

    # 000 - 009
    "000": product_000,
    "001": product_001,
    "002": product_002,
    "003": product_003,
    "004": product_004,
    "005": product_005,
    "006": product_006,
    "007": product_007,
    "008": product_008,
    "009": product_009,

    # 010 - 019
    "010": product_010,
    "011": product_011,
    "012": product_012,
    "013": product_013,
    "014": product_014,
    "015": product_015,
    "016": product_016,
    "017": product_017,
    "018": product_018,
    "019": product_019,

    # 020 - 029
    "020": product_020,
    "021": product_021,
    "022": product_022,
    "023": product_023,
    "024": product_024,
    "025": product_025,
    "026": product_026,
    "027": product_027,
    "028": product_028,
    "029": product_029,

    # 030 - 039
    "030": product_030,
    "031": product_031,
    "032": product_032,
    "033": product_033,
    "034": product_034,
    "035": product_035,
    "036": product_036,
    "037": product_037,
    "038": product_038,
    "039": product_039,

    # 040 - 049
    "040": product_040,
    "041": product_041,
    "042": product_042,
    "043": product_043,
    "044": product_044,
    "045": product_045,
    "046": product_046,
    "047": product_047,
    "048": product_048,
    "049": product_049,

    # 050 - 059
    "050": product_050,
    "051": product_051,
    "052": product_052,
    "053": product_053,
    "054": product_054,
    "055": product_055,
    "056": product_056,
    "057": product_057,
    "058": product_058,
    "059": product_059,

    # 060 - 069
    "060": product_060,
    "061": product_061,
    "062": product_062,
    "063": product_063,
    "064": product_064,
    "065": product_065,
    "066": product_066,
    "067": product_067,
    "068": product_068,
    "069": product_069,

    # 070 - 079
    "070": product_070,
    "071": product_071,
    "072": product_072,
    "073": product_073,
    "074": product_074,
    "075": product_075,
    "076": product_076,
    "077": product_077,
    "078": product_078,
    "079": product_079,

    # 080 - 089
    "080": product_080,
    "081": product_081,
    "082": product_082,
    "083": product_083,
    "084": product_084,
    "085": product_085,
    "086": product_086,
    "087": product_087,
    "088": product_088,
    "089": product_089,

    # 090 - 099
    "090": product_090,
    "091": product_091,
    "092": product_092,
    "093": product_093,
    "094": product_094,
    "095": product_095,
    "096": product_096,
    "097": product_097,
    "098": product_098,
    "099": product_099,

    # 100 - 109
    "100": product_100,
    "101": product_101,
    "102": product_102,
    "103": product_103,
    "104": product_104,
    "105": product_105,
    "106": product_106,
    "107": product_107,
    "108": product_108,
    "109": product_109,

    # 110 - 119
    "110": product_110,
    "111": product_111,
    "112": product_112,
    "113": product_113,
    "114": product_114,
    "115": product_115,
    "116": product_116,
    "117": product_117,
    "118": product_118,
    "119": product_119,

    # 120 - 129
    "120": product_120,
    "121": product_121,
    "122": product_122,
    "123": product_123,
    "124": product_124,
    "125": product_125,
    "126": product_126,
    "127": product_127,
    "128": product_128,
    "129": product_129,

    # 130 - 139
    "130": product_130,
    "131": product_131,
    "132": product_132,
    "133": product_133,
    "134": product_134,
    "135": product_135,
    "136": product_136,
    "137": product_137,
    "138": product_138,
    "139": product_139,

    # 140 - 149
    "140": product_140,
    "141": product_141,
    "142": product_142,
    "143": product_143,
    "144": product_144,
    "145": product_145,
    "146": product_146,
    "147": product_147,
    "148": product_148,
    "149": product_149,

    # 150 - 159
    "150": product_150,
    "151": product_151,
    "152": product_152,
    "153": product_153,
    "154": product_154,
    "155": product_155,
    "156": product_156,
    "157": product_157,
    "158": product_158,
    "159": product_159,

    # 160 - 169
    "160": product_160,
    "161": product_161,
    "162": product_162,
    "163": product_163,
    "164": product_164,
    "165": product_165,
    "166": product_166,
    "167": product_167,
    "168": product_168,
    "169": product_169,

    # 170 - 179
    "170": product_170,
    "171": product_171,
    "172": product_172,
    "173": product_173,
    "174": product_174,
    "175": product_175,
    "176": product_176,
    "177": product_177,
    "178": product_178,
    "179": product_179,

    # 180 - 189
    "180": product_180,
    "181": product_181,
    "182": product_182,
    "183": product_183,
    "184": product_184,
    "185": product_185,
    "186": product_186,
    "187": product_187,
    "188": product_188,
    "189": product_189,

    # 190 - 199
    "190": product_190,
    "191": product_191,
    "192": product_192,
    "193": product_193,
    "194": product_194,
    "195": product_195,
    "196": product_196,
    "197": product_197,
    "198": product_198,
    "199": product_199,

    # 200 - 209
    "200": product_200,
    "201": product_201,
    "202": product_202,
    "203": product_203,
    "204": product_204,
    "205": product_205,
    "206": product_206,
    "207": product_207,
    "208": product_208,
    "209": product_209,

    # 210 - 219
    "210": product_210,
    "211": product_211,
    "212": product_212,
    "213": product_213,
    "214": product_214,
    "215": product_215,
    "216": product_216,
    "217": product_217,
    "218": product_218,
    "219": product_219,

    # 220 - 229
    "220": product_220,
    "221": product_221,
    "222": product_222,
    "223": product_223,
    "224": product_224,
    "225": product_225,
    "226": product_226,
    "227": product_227,
    "228": product_228,
    "229": product_229,

    # 230 - 239
    "230": product_230,
    "231": product_231,
    "232": product_232,
    "233": product_233,
    "234": product_234,
    "235": product_235,
    "236": product_236,
    "237": product_237,
    "238": product_238,
    "239": product_239,

    # 240 - 249
    "240": product_240,
    "241": product_241,
    "242": product_242,
    "243": product_243,
    "244": product_244,
    "245": product_245,
    "246": product_246,
    "247": product_247,
    "248": product_248,
    "249": product_249,

    # 050 - 059
    "250": product_250,
    "251": product_251,
    "252": product_252,
    "253": product_253,
    "254": product_254,
    "255": product_255,
    "256": product_256,
    "257": product_257,
    "258": product_258,
    "259": product_259,

    # 260 - 269
    "260": product_260,
    "261": product_261,
    "262": product_262,
    "263": product_263,
    "264": product_264,
    "265": product_265,
    "266": product_266,
    "267": product_267,
    "268": product_268,
    "269": product_269,

    # 270 - 279
    "270": product_270,
    "271": product_271,
    "272": product_272,
    "273": product_273,
    "274": product_274,
    "275": product_275,
    "276": product_276,
    "277": product_277,
    "278": product_278,
    "279": product_279,

    # 280 - 289
    "280": product_280,
    "281": product_281,
    "282": product_282,
    "283": product_283,
    "284": product_284,
    "285": product_285,
    "286": product_286,
    "287": product_287,
    "288": product_288,
    "289": product_289,

    # 290 - 299
    "290": product_290,
    "291": product_291,
    "292": product_292,
    "293": product_293,
    "294": product_294,
    "295": product_295,
    "296": product_296,
    "297": product_297,
    "298": product_298,
    "299": product_299,

    # 300 - 309
    "300": product_300,
    "301": product_301,
    "302": product_302,
    "303": product_303,
    "304": product_304,
    "305": product_305,
    "306": product_306,
    "307": product_307,
    "308": product_308,
    "309": product_309,

    # 310 - 319
    "310": product_310,
    "311": product_311,
    "312": product_312,
    "313": product_313,
    "314": product_314,
    "315": product_315,
    "316": product_316,
    "317": product_317,
    "318": product_318,
    "319": product_319,

    # 320 - 329
    "320": product_320,
    "321": product_321,
    "322": product_322,
    "323": product_323,
    "324": product_324,
    "325": product_325,
    "326": product_326,
    "327": product_327,
    "328": product_328,
    "329": product_329,

    # 330 - 339
    "330": product_330,
    "331": product_331,
    "332": product_332,
    "333": product_333,
    "334": product_334,
    "335": product_335,
    "336": product_336,
    "337": product_337,
    "338": product_338,
    "339": product_339,

    # 340 - 349
    "340": product_340,
    "341": product_341,
    "342": product_342,
    "343": product_343,
    "344": product_344,
    "345": product_345,
    "346": product_346,
    "347": product_347,
    "348": product_348,
    "349": product_349,

    # 350 - 359
    "350": product_350,
    "351": product_351,
    "352": product_352,
    "353": product_353,
    "354": product_354,
    "355": product_355,
    "356": product_356,
    "357": product_357,
    "358": product_358,
    "359": product_359,

    # 360 - 369
    "360": product_360,
    "361": product_361,
    "362": product_362,
    "363": product_363,
    "364": product_364,
    "365": product_365,
    "366": product_366,
    "367": product_367,
    "368": product_368,
    "369": product_369,

    # 370 - 379
    "370": product_370,
    "371": product_371,
    "372": product_372,
    "373": product_373,
    "374": product_374,
    "375": product_375,
    "376": product_376,
    "377": product_377,
    "378": product_378,
    "379": product_379,

    # 380 - 389
    "380": product_380,
    "381": product_381,
    "382": product_382,
    "383": product_383,
    "384": product_384,
    "385": product_385,
    "386": product_386,
    "387": product_387,
    "388": product_388,
    "389": product_389,

    # 390 - 399
    "390": product_390,
    "391": product_391,
    "392": product_392,
    "393": product_393,
    "394": product_394,
    "395": product_395,
    "396": product_396,
    "397": product_397,
    "398": product_398,
    "399": product_399,

    # 400 - 409
    "400": product_400,
    "401": product_401,
    "402": product_402,
    "403": product_403,
    "404": product_404,
    "405": product_405,
    "406": product_406,
    "407": product_407,
    "408": product_408,
    "409": product_409,
    "410": product_410,
    "411": product_411,
    "412": product_412,
    "413": product_413,
    "414": product_414,
    "415": product_415,
    "416": product_416,
    "417": product_417,
    "418": product_418,
    "419": product_419,
    "420": product_420,
    "421": product_421,
    "422": product_422,
    "423": product_423,
    "424": product_424,
    "425": product_425,
    "426": product_426,
    "427": product_427,
    "428": product_428,
    "429": product_429,
    "430": product_430,
    "431": product_431,
    "432": product_432,
    "433": product_433,
    "434": product_434,
    "435": product_435,
    "436": product_436,
    "437": product_437,
    "438": product_438,
    "439": product_439,
    "440": product_440,
    "441": product_441,
    "442": product_442,
    "443": product_443,
    "444": product_444,
    "445": product_445,
    "446": product_446,
    "447": product_447,
    "448": product_448,
    "449": product_449,
    "450": product_450,
    "451": product_451,
    "452": product_452,
    "453": product_453,
    "454": product_454,
    "455": product_455,
    "456": product_456,
    "457": product_457,
    "458": product_458,
    "459": product_459,
    "460": product_460,
    "461": product_461,
    "462": product_462,
    "463": product_463,
    "464": product_464,
    "465": product_465,
    "466": product_466,
    "467": product_467,
    "468": product_468,
    "469": product_469,
    "470": product_470,
    "471": product_471,
    "472": product_472,
    "473": product_473,
    "474": product_474,
    "475": product_475,
    "476": product_476,
    "477": product_477,
    "478": product_478,
    "479": product_479,
    "480": product_480,
    "481": product_481,
    "482": product_482,
    "483": product_483,
    "484": product_484,
    "485": product_485,
    "486": product_486,
    "487": product_487,
    "488": product_488,
    "489": product_489,
    "490": product_490,
    "491": product_491,
    "492": product_492,
    "493": product_493,
    "494": product_494,
    "495": product_495,
    "496": product_496,
    "497": product_497,
    "498": product_498,
    "499": product_499,
    "500": product_500,
    "501": product_501,
    "502": product_502,
    "503": product_503,
    "504": product_504,
    "505": product_505,
    "506": product_506,
    "507": product_507,
    "508": product_508,
    "509": product_509,
    "510": product_510,
    "511": product_511,
    "512": product_512,
    "513": product_513,
    "514": product_514,
    "515": product_515,
    "516": product_516,
    "517": product_517,
    "518": product_518,
    "519": product_519,
    "520": product_520,
    "521": product_521,
    "522": product_522,
    "523": product_523,
    "524": product_524,
    "525": product_525,
    "526": product_526,
    "527": product_527,
    "528": product_528,
    "529": product_529,
    "530": product_530,
    "531": product_531,
    "532": product_532,
    "533": product_533,
    "534": product_534,
    "535": product_535,
    "536": product_536,
    "537": product_537,
    "538": product_538,
    "539": product_539,
    "540": product_540,
    "541": product_541,
    "542": product_542,
    "543": product_543,
    "544": product_544,
    "545": product_545,
    "546": product_546,
    "547": product_547,
    "548": product_548,
    "549": product_549,
    "550": product_550,
    "551": product_551,
    "552": product_552,
    "553": product_553,
    "554": product_554,
    "555": product_555,
    "556": product_556,
    "557": product_557,
    "558": product_558,
    "559": product_559,
    "560": product_560,
    "561": product_561,
    "562": product_562,
    "563": product_563,
    "564": product_564,
    "565": product_565,
    "566": product_566,
    "567": product_567,
    "568": product_568,
    "569": product_569,
    "570": product_570,
    "571": product_571,
    "572": product_572,
    "573": product_573,
    "574": product_574,
    "575": product_575,
    "576": product_576,
    "577": product_577,
    "578": product_578,
    "579": product_579,
    "580": product_580,
    "581": product_581,
    "582": product_582,
    "583": product_583,
    "584": product_584,
    "585": product_585,
    "586": product_586,
    "587": product_587,
    "588": product_588,
    "589": product_589,
    "590": product_590,
    "591": product_591,
    "592": product_592,
    "593": product_593,
    "594": product_594,
    "595": product_595,
    "596": product_596,
    "597": product_597,
    "598": product_598,
    "599": product_599,
    "600": product_600,
    "601": product_601,
    "602": product_602,
    "603": product_603,
    "604": product_604,
    "605": product_605,
    "606": product_606,
    "607": product_607,
    "608": product_608,
    "609": product_609,
    "610": product_610,
    "611": product_611,
    "612": product_612,
    "613": product_613,
    "614": product_614,
    "615": product_615,
    "616": product_616,
    "617": product_617,
    "618": product_618,
    "619": product_619,
    "620": product_620,
    "621": product_621,
    "622": product_622,
    "623": product_623,
    "624": product_624,
    "625": product_625,
    "626": product_626,
    "627": product_627,
    "628": product_628,
    "629": product_629,
    "630": product_630,
    "631": product_631,
    "632": product_632,
    "633": product_633,
    "634": product_634,
    "635": product_635,
    "636": product_636,
    "637": product_637,
    "638": product_638,
    "639": product_639,
    "640": product_640,
    "641": product_641,
    "642": product_642,
    "643": product_643,
    "644": product_644,
    "645": product_645,
    "646": product_646,
    "647": product_647,
    "648": product_648,
    "649": product_649,
    "650": product_650,
    "651": product_651,
    "652": product_652,
    "653": product_653,
    "654": product_654,
    "655": product_655,
    "656": product_656,
    "657": product_657,
    "658": product_658,
    "659": product_659,
    "660": product_660,
    "661": product_661,
    "662": product_662,
    "663": product_663,
    "664": product_664,
    "665": product_665,
    "666": product_666,
    "667": product_667,
    "668": product_668,
    "669": product_669,
    "670": product_670,
    "671": product_671,
    "672": product_672,
    "673": product_673,
    "674": product_674,
    "675": product_675,
    "676": product_676,
    "677": product_677,
    "678": product_678,
    "679": product_679,
    "680": product_680,
    "681": product_681,
    "682": product_682,
    "683": product_683,
    "684": product_684,
    "685": product_685,
    "686": product_686,
    "687": product_687,
    "688": product_688,
    "689": product_689,
    "690": product_690,
    "691": product_691,
    "692": product_692,
    "693": product_693,
    "694": product_694,
    "695": product_695,
    "696": product_696,
    "697": product_697,
    "698": product_698,
    "699": product_699,
    "700": product_700,
    "701": product_701,
    "702": product_702,
    "703": product_703,
    "704": product_704,
    "705": product_705,
    "706": product_706,
    "707": product_707,
    "708": product_708,
    "709": product_709,
    "710": product_710,
    "711": product_711,
    "712": product_712,
    "713": product_713,
    "714": product_714,
    "715": product_715,
    "716": product_716,
    "717": product_717,
    "718": product_718,
    "719": product_719,
    "720": product_720,
    "721": product_721,
    "722": product_722,
    "723": product_723,
    "724": product_724,
    "725": product_725,
    "726": product_726,
    "727": product_727,
    "728": product_728,
    "729": product_729,
    "730": product_730,
    "731": product_731,
    "732": product_732,
    "733": product_733,
    "734": product_734,
    "735": product_735,
    "736": product_736,
    "737": product_737,
    "738": product_738,
    "739": product_739,
    "740": product_740,
    "741": product_741,
    "742": product_742,
    "743": product_743,
    "744": product_744,
    "745": product_745,
    "746": product_746,
    "747": product_747,
    "748": product_748,
    "749": product_749,
    "750": product_750,
    "751": product_751,
    "752": product_752,
    "753": product_753,
    "754": product_754,
    "755": product_755,
    "756": product_756,
    "757": product_757,
    "758": product_758,
    "759": product_759,
    "760": product_760,
    "761": product_761,
    "762": product_762,
    "763": product_763,
    "764": product_764,
    "765": product_765,
    "766": product_766,
    "767": product_767,
    "768": product_768,
    "769": product_769,
    "770": product_770,
    "771": product_771,
    "772": product_772,
    "773": product_773,
    "774": product_774,
    "775": product_775,
    "776": product_776,
    "777": product_777,
    "778": product_778,
    "779": product_779,
    "780": product_780,
    "781": product_781,
    "782": product_782,
    "783": product_783,
    "784": product_784,
    "785": product_785,
    "786": product_786,
    "787": product_787,
    "788": product_788,
    "789": product_789,
    "790": product_790,
    "791": product_791,
    "792": product_792,
    "793": product_793,
    "794": product_794,
    "795": product_795,
    "796": product_796,
    "797": product_797,
    "798": product_798,
    "799": product_799,
    "800": product_800,
    "801": product_801,
    "802": product_802,
    "803": product_803,
    "804": product_804,
    "805": product_805,
    "806": product_806,
    "807": product_807,
    "808": product_808,
    "809": product_809,
    "810": product_810,
    "811": product_811,
    "812": product_812,
    "813": product_813,
    "814": product_814,
    "815": product_815,
    "816": product_816,
    "817": product_817,
    "818": product_818,
    "819": product_819,
    "820": product_820,
    "821": product_821,
    "822": product_822,
    "823": product_823,
    "824": product_824,
    "825": product_825,
    "826": product_826,
    "827": product_827,
    "828": product_828,
    "829": product_829,
    "830": product_830,
    "831": product_831,
    "832": product_832,
    "833": product_833,
    "834": product_834,
    "835": product_835,
    "836": product_836,
    "837": product_837,
    "838": product_838,
    "839": product_839,
    "840": product_840,
    "841": product_841,
    "842": product_842,
    "843": product_843,
    "844": product_844,
    "845": product_845,
    "846": product_846,
    "847": product_847,
    "848": product_848,
    "849": product_849,
    "850": product_850,
    "851": product_851,
    "852": product_852,
    "853": product_853,
    "854": product_854,
    "855": product_855,
    "856": product_856,
    "857": product_857,
    "858": product_858,
    "859": product_859,
    "860": product_860,
    "861": product_861,
    "862": product_862,
    "863": product_863,
    "864": product_864,
    "865": product_865,
    "866": product_866,
    "867": product_867,
    "868": product_868,
    "869": product_869,
    "870": product_870,
    "871": product_871,
    "872": product_872,
    "873": product_873,
    "874": product_874,
    "875": product_875,
    "876": product_876,
    "877": product_877,
    "878": product_878,
    "879": product_879,
    "880": product_880,
    "881": product_881,
    "882": product_882,
    "883": product_883,
    "884": product_884,
    "885": product_885,
    "886": product_886,
    "887": product_887,
    "888": product_888,
    "889": product_889,
    "890": product_890,
    "891": product_891,
    "892": product_892,
    "893": product_893,
    "894": product_894,
    "895": product_895,
    "896": product_896,
    "897": product_897,
    "898": product_898,
    "899": product_899,

    # 900 - 999
    "900": product_900,
    "901": product_901,
    "902": product_902,
    "903": product_903,
    "904": product_904,
    "905": product_905,
    "906": product_906,
    "907": product_907,
    "908": product_908,
    "909": product_909,
    "910": product_910,
    "911": product_911,
    "912": product_912,
    "913": product_913,
    "914": product_914,
    "915": product_915,
    "916": product_916,
    "917": product_917,
    "918": product_918,
    "919": product_919,
    "920": product_920,
    "921": product_921,
    "922": product_922,
    "923": product_923,
    "924": product_924,
    "925": product_925,
    "926": product_926,
    "927": product_927,
    "928": product_928,
    "929": product_929,
    "930": product_930,
    "931": product_931,
    "932": product_932,
    "933": product_933,
    "934": product_934,
    "935": product_935,
    "936": product_936,
    "937": product_937,
    "938": product_938,
    "939": product_939,
    "940": product_940,
    "941": product_941,
    "942": product_942,
    "943": product_943,
    "944": product_944,
    "945": product_945,
    "946": product_946,
    "947": product_947,
    "948": product_948,
    "949": product_949,
    "950": product_950,
    "951": product_951,
    "952": product_952,
    "953": product_953,
    "954": product_954,
    "955": product_955,
    "956": product_956,
    "957": product_957,
    "958": product_958,
    "959": product_959,
    "960": product_960,
    "961": product_961,
    "962": product_962,
    "963": product_963,
    "964": product_964,
    "965": product_965,
    "966": product_966,
    "967": product_967,
    "968": product_968,
    "969": product_969,
    "970": product_970,
    "971": product_971,
    "972": product_972,
    "973": product_973,
    "974": product_974,
    "975": product_975,
    "976": product_976,
    "977": product_977,
    "978": product_978,
    "979": product_979,
    "980": product_980,
    "981": product_981,
    "982": product_982,
    "983": product_983,
    "984": product_984,
    "985": product_985,
    "986": product_986,
    "987": product_987,
    "988": product_988,
    "989": product_989,
    "990": product_990,
    "991": product_991,
    "992": product_992,
    "993": product_993,
    "994": product_994,
    "995": product_995,
    "996": product_996,
    "997": product_997,
    "998": product_998,
    "999": product_999

}


# blank customer information dict
info = {
    'name': '',
    'email': '',
    'phone_number': '',
    product_index['000']: 0,
    product_index['001']: 0,
    product_index['002']: 0,
    product_index['003']: 0,
    product_index['004']: 0,
    product_index['005']: 0,
    product_index['006']: 0,
    product_index['007']: 0,
    product_index['008']: 0,
    product_index['009']: 0,
    product_index['010']: 0,
    product_index['011']: 0,
    product_index['012']: 0,
    product_index['013']: 0,
    product_index['014']: 0,
    product_index['015']: 0,
    product_index['016']: 0,
    product_index['017']: 0,
    product_index['018']: 0,
    product_index['019']: 0,
    product_index['020']: 0,
    product_index['021']: 0,
    product_index['022']: 0,
    product_index['023']: 0,
    product_index['024']: 0,
    product_index['025']: 0,
    product_index['026']: 0,
    product_index['027']: 0,
    product_index['028']: 0,
    product_index['029']: 0,
    product_index['030']: 0,
    product_index['031']: 0,
    product_index['032']: 0,
    product_index['033']: 0,
    product_index['034']: 0,
    product_index['035']: 0,
    product_index['036']: 0,
    product_index['037']: 0,
    product_index['038']: 0,
    product_index['039']: 0,
    product_index['040']: 0,
    product_index['041']: 0,
    product_index['042']: 0,
    product_index['043']: 0,
    product_index['044']: 0,
    product_index['045']: 0,
    product_index['046']: 0,
    product_index['047']: 0,
    product_index['048']: 0,
    product_index['049']: 0,
    product_index['050']: 0,
    product_index['051']: 0,
    product_index['052']: 0,
    product_index['053']: 0,
    product_index['054']: 0,
    product_index['055']: 0,
    product_index['056']: 0,
    product_index['057']: 0,
    product_index['058']: 0,
    product_index['059']: 0,
    product_index['060']: 0,
    product_index['061']: 0,
    product_index['062']: 0,
    product_index['063']: 0,
    product_index['064']: 0,
    product_index['065']: 0,
    product_index['066']: 0,
    product_index['067']: 0,
    product_index['068']: 0,
    product_index['069']: 0,
    product_index['070']: 0,
    product_index['071']: 0,
    product_index['072']: 0,
    product_index['073']: 0,
    product_index['074']: 0,
    product_index['075']: 0,
    product_index['076']: 0,
    product_index['077']: 0,
    product_index['078']: 0,
    product_index['079']: 0,
    product_index['080']: 0,
    product_index['081']: 0,
    product_index['082']: 0,
    product_index['083']: 0,
    product_index['084']: 0,
    product_index['085']: 0,
    product_index['086']: 0,
    product_index['087']: 0,
    product_index['088']: 0,
    product_index['089']: 0,
    product_index['090']: 0,
    product_index['091']: 0,
    product_index['092']: 0,
    product_index['093']: 0,
    product_index['094']: 0,
    product_index['095']: 0,
    product_index['096']: 0,
    product_index['097']: 0,
    product_index['098']: 0,
    product_index['099']: 0,
    product_index['100']: 0,
    product_index['101']: 0,
    product_index['102']: 0,
    product_index['103']: 0,
    product_index['104']: 0,
    product_index['105']: 0,
    product_index['106']: 0,
    product_index['107']: 0,
    product_index['108']: 0,
    product_index['109']: 0,
    product_index['110']: 0,
    product_index['111']: 0,
    product_index['112']: 0,
    product_index['113']: 0,
    product_index['114']: 0,
    product_index['115']: 0,
    product_index['116']: 0,
    product_index['117']: 0,
    product_index['118']: 0,
    product_index['119']: 0,
    product_index['120']: 0,
    product_index['121']: 0,
    product_index['122']: 0,
    product_index['123']: 0,
    product_index['124']: 0,
    product_index['125']: 0,
    product_index['126']: 0,
    product_index['127']: 0,
    product_index['128']: 0,
    product_index['129']: 0,
    product_index['130']: 0,
    product_index['131']: 0,
    product_index['132']: 0,
    product_index['133']: 0,
    product_index['134']: 0,
    product_index['135']: 0,
    product_index['136']: 0,
    product_index['137']: 0,
    product_index['138']: 0,
    product_index['139']: 0,
    product_index['140']: 0,
    product_index['141']: 0,
    product_index['142']: 0,
    product_index['143']: 0,
    product_index['144']: 0,
    product_index['145']: 0,
    product_index['146']: 0,
    product_index['147']: 0,
    product_index['148']: 0,
    product_index['149']: 0,
    product_index['150']: 0,
    product_index['151']: 0,
    product_index['152']: 0,
    product_index['153']: 0,
    product_index['154']: 0,
    product_index['155']: 0,
    product_index['156']: 0,
    product_index['157']: 0,
    product_index['158']: 0,
    product_index['159']: 0,
    product_index['160']: 0,
    product_index['161']: 0,
    product_index['162']: 0,
    product_index['163']: 0,
    product_index['164']: 0,
    product_index['165']: 0,
    product_index['166']: 0,
    product_index['167']: 0,
    product_index['168']: 0,
    product_index['169']: 0,
    product_index['170']: 0,
    product_index['171']: 0,
    product_index['172']: 0,
    product_index['173']: 0,
    product_index['174']: 0,
    product_index['175']: 0,
    product_index['176']: 0,
    product_index['177']: 0,
    product_index['178']: 0,
    product_index['179']: 0,
    product_index['180']: 0,
    product_index['181']: 0,
    product_index['182']: 0,
    product_index['183']: 0,
    product_index['184']: 0,
    product_index['185']: 0,
    product_index['186']: 0,
    product_index['187']: 0,
    product_index['188']: 0,
    product_index['189']: 0,
    product_index['190']: 0,
    product_index['191']: 0,
    product_index['192']: 0,
    product_index['193']: 0,
    product_index['194']: 0,
    product_index['195']: 0,
    product_index['196']: 0,
    product_index['197']: 0,
    product_index['198']: 0,
    product_index['199']: 0,
    product_index['200']: 0,
    product_index['201']: 0,
    product_index['202']: 0,
    product_index['203']: 0,
    product_index['204']: 0,
    product_index['205']: 0,
    product_index['206']: 0,
    product_index['207']: 0,
    product_index['208']: 0,
    product_index['209']: 0,
    product_index['210']: 0,
    product_index['211']: 0,
    product_index['212']: 0,
    product_index['213']: 0,
    product_index['214']: 0,
    product_index['215']: 0,
    product_index['216']: 0,
    product_index['217']: 0,
    product_index['218']: 0,
    product_index['219']: 0,
    product_index['220']: 0,
    product_index['221']: 0,
    product_index['222']: 0,
    product_index['223']: 0,
    product_index['224']: 0,
    product_index['225']: 0,
    product_index['226']: 0,
    product_index['227']: 0,
    product_index['228']: 0,
    product_index['229']: 0,
    product_index['230']: 0,
    product_index['231']: 0,
    product_index['232']: 0,
    product_index['233']: 0,
    product_index['234']: 0,
    product_index['235']: 0,
    product_index['236']: 0,
    product_index['237']: 0,
    product_index['238']: 0,
    product_index['239']: 0,
    product_index['240']: 0,
    product_index['241']: 0,
    product_index['242']: 0,
    product_index['243']: 0,
    product_index['244']: 0,
    product_index['245']: 0,
    product_index['246']: 0,
    product_index['247']: 0,
    product_index['248']: 0,
    product_index['249']: 0,
    product_index['250']: 0,
    product_index['251']: 0,
    product_index['252']: 0,
    product_index['253']: 0,
    product_index['254']: 0,
    product_index['255']: 0,
    product_index['256']: 0,
    product_index['257']: 0,
    product_index['258']: 0,
    product_index['259']: 0,
    product_index['260']: 0,
    product_index['261']: 0,
    product_index['262']: 0,
    product_index['263']: 0,
    product_index['264']: 0,
    product_index['265']: 0,
    product_index['266']: 0,
    product_index['267']: 0,
    product_index['268']: 0,
    product_index['269']: 0,
    product_index['270']: 0,
    product_index['271']: 0,
    product_index['272']: 0,
    product_index['273']: 0,
    product_index['274']: 0,
    product_index['275']: 0,
    product_index['276']: 0,
    product_index['277']: 0,
    product_index['278']: 0,
    product_index['279']: 0,
    product_index['280']: 0,
    product_index['281']: 0,
    product_index['282']: 0,
    product_index['283']: 0,
    product_index['284']: 0,
    product_index['285']: 0,
    product_index['286']: 0,
    product_index['287']: 0,
    product_index['288']: 0,
    product_index['289']: 0,
    product_index['290']: 0,
    product_index['291']: 0,
    product_index['292']: 0,
    product_index['293']: 0,
    product_index['294']: 0,
    product_index['295']: 0,
    product_index['296']: 0,
    product_index['297']: 0,
    product_index['298']: 0,
    product_index['299']: 0,
    product_index['300']: 0,
    product_index['301']: 0,
    product_index['302']: 0,
    product_index['303']: 0,
    product_index['304']: 0,
    product_index['305']: 0,
    product_index['306']: 0,
    product_index['307']: 0,
    product_index['308']: 0,
    product_index['309']: 0,
    product_index['310']: 0,
    product_index['311']: 0,
    product_index['312']: 0,
    product_index['313']: 0,
    product_index['314']: 0,
    product_index['315']: 0,
    product_index['316']: 0,
    product_index['317']: 0,
    product_index['318']: 0,
    product_index['319']: 0,
    product_index['320']: 0,
    product_index['321']: 0,
    product_index['322']: 0,
    product_index['323']: 0,
    product_index['324']: 0,
    product_index['325']: 0,
    product_index['326']: 0,
    product_index['327']: 0,
    product_index['328']: 0,
    product_index['329']: 0,
    product_index['330']: 0,
    product_index['331']: 0,
    product_index['332']: 0,
    product_index['333']: 0,
    product_index['334']: 0,
    product_index['335']: 0,
    product_index['336']: 0,
    product_index['337']: 0,
    product_index['338']: 0,
    product_index['339']: 0,
    product_index['340']: 0,
    product_index['341']: 0,
    product_index['342']: 0,
    product_index['343']: 0,
    product_index['344']: 0,
    product_index['345']: 0,
    product_index['346']: 0,
    product_index['347']: 0,
    product_index['348']: 0,
    product_index['349']: 0,
    product_index['350']: 0,
    product_index['351']: 0,
    product_index['352']: 0,
    product_index['353']: 0,
    product_index['354']: 0,
    product_index['355']: 0,
    product_index['356']: 0,
    product_index['357']: 0,
    product_index['358']: 0,
    product_index['359']: 0,
    product_index['360']: 0,
    product_index['361']: 0,
    product_index['362']: 0,
    product_index['363']: 0,
    product_index['364']: 0,
    product_index['365']: 0,
    product_index['366']: 0,
    product_index['367']: 0,
    product_index['368']: 0,
    product_index['369']: 0,
    product_index['370']: 0,
    product_index['371']: 0,
    product_index['372']: 0,
    product_index['373']: 0,
    product_index['374']: 0,
    product_index['375']: 0,
    product_index['376']: 0,
    product_index['377']: 0,
    product_index['378']: 0,
    product_index['379']: 0,
    product_index['380']: 0,
    product_index['381']: 0,
    product_index['382']: 0,
    product_index['383']: 0,
    product_index['384']: 0,
    product_index['385']: 0,
    product_index['386']: 0,
    product_index['387']: 0,
    product_index['388']: 0,
    product_index['389']: 0,
    product_index['390']: 0,
    product_index['391']: 0,
    product_index['392']: 0,
    product_index['393']: 0,
    product_index['394']: 0,
    product_index['395']: 0,
    product_index['396']: 0,
    product_index['397']: 0,
    product_index['398']: 0,
    product_index['399']: 0,
    product_index['400']: 0,
    product_index['401']: 0,
    product_index['402']: 0,
    product_index['403']: 0,
    product_index['404']: 0,
    product_index['405']: 0,
    product_index['406']: 0,
    product_index['407']: 0,
    product_index['408']: 0,
    product_index['409']: 0,
    product_index['410']: 0,
    product_index['411']: 0,
    product_index['412']: 0,
    product_index['413']: 0,
    product_index['414']: 0,
    product_index['415']: 0,
    product_index['416']: 0,
    product_index['417']: 0,
    product_index['418']: 0,
    product_index['419']: 0,
    product_index['420']: 0,
    product_index['421']: 0,
    product_index['422']: 0,
    product_index['423']: 0,
    product_index['424']: 0,
    product_index['425']: 0,
    product_index['426']: 0,
    product_index['427']: 0,
    product_index['428']: 0,
    product_index['429']: 0,
    product_index['430']: 0,
    product_index['431']: 0,
    product_index['432']: 0,
    product_index['433']: 0,
    product_index['434']: 0,
    product_index['435']: 0,
    product_index['436']: 0,
    product_index['437']: 0,
    product_index['438']: 0,
    product_index['439']: 0,
    product_index['440']: 0,
    product_index['441']: 0,
    product_index['442']: 0,
    product_index['443']: 0,
    product_index['444']: 0,
    product_index['445']: 0,
    product_index['446']: 0,
    product_index['447']: 0,
    product_index['448']: 0,
    product_index['449']: 0,
    product_index['450']: 0,
    product_index['451']: 0,
    product_index['452']: 0,
    product_index['453']: 0,
    product_index['454']: 0,
    product_index['455']: 0,
    product_index['456']: 0,
    product_index['457']: 0,
    product_index['458']: 0,
    product_index['459']: 0,
    product_index['460']: 0,
    product_index['461']: 0,
    product_index['462']: 0,
    product_index['463']: 0,
    product_index['464']: 0,
    product_index['465']: 0,
    product_index['466']: 0,
    product_index['467']: 0,
    product_index['468']: 0,
    product_index['469']: 0,
    product_index['470']: 0,
    product_index['471']: 0,
    product_index['472']: 0,
    product_index['473']: 0,
    product_index['474']: 0,
    product_index['475']: 0,
    product_index['476']: 0,
    product_index['477']: 0,
    product_index['478']: 0,
    product_index['479']: 0,
    product_index['480']: 0,
    product_index['481']: 0,
    product_index['482']: 0,
    product_index['483']: 0,
    product_index['484']: 0,
    product_index['485']: 0,
    product_index['486']: 0,
    product_index['487']: 0,
    product_index['488']: 0,
    product_index['489']: 0,
    product_index['490']: 0,
    product_index['491']: 0,
    product_index['492']: 0,
    product_index['493']: 0,
    product_index['494']: 0,
    product_index['495']: 0,
    product_index['496']: 0,
    product_index['497']: 0,
    product_index['498']: 0,
    product_index['499']: 0,
    product_index['500']: 0,
    product_index['501']: 0,
    product_index['502']: 0,
    product_index['503']: 0,
    product_index['504']: 0,
    product_index['505']: 0,
    product_index['506']: 0,
    product_index['507']: 0,
    product_index['508']: 0,
    product_index['509']: 0,
    product_index['510']: 0,
    product_index['511']: 0,
    product_index['512']: 0,
    product_index['513']: 0,
    product_index['514']: 0,
    product_index['515']: 0,
    product_index['516']: 0,
    product_index['517']: 0,
    product_index['518']: 0,
    product_index['519']: 0,
    product_index['520']: 0,
    product_index['521']: 0,
    product_index['522']: 0,
    product_index['523']: 0,
    product_index['524']: 0,
    product_index['525']: 0,
    product_index['526']: 0,
    product_index['527']: 0,
    product_index['528']: 0,
    product_index['529']: 0,
    product_index['530']: 0,
    product_index['531']: 0,
    product_index['532']: 0,
    product_index['533']: 0,
    product_index['534']: 0,
    product_index['535']: 0,
    product_index['536']: 0,
    product_index['537']: 0,
    product_index['538']: 0,
    product_index['539']: 0,
    product_index['540']: 0,
    product_index['541']: 0,
    product_index['542']: 0,
    product_index['543']: 0,
    product_index['544']: 0,
    product_index['545']: 0,
    product_index['546']: 0,
    product_index['547']: 0,
    product_index['548']: 0,
    product_index['549']: 0,
    product_index['550']: 0,
    product_index['551']: 0,
    product_index['552']: 0,
    product_index['553']: 0,
    product_index['554']: 0,
    product_index['555']: 0,
    product_index['556']: 0,
    product_index['557']: 0,
    product_index['558']: 0,
    product_index['559']: 0,
    product_index['560']: 0,
    product_index['561']: 0,
    product_index['562']: 0,
    product_index['563']: 0,
    product_index['564']: 0,
    product_index['565']: 0,
    product_index['566']: 0,
    product_index['567']: 0,
    product_index['568']: 0,
    product_index['569']: 0,
    product_index['570']: 0,
    product_index['571']: 0,
    product_index['572']: 0,
    product_index['573']: 0,
    product_index['574']: 0,
    product_index['575']: 0,
    product_index['576']: 0,
    product_index['577']: 0,
    product_index['578']: 0,
    product_index['579']: 0,
    product_index['580']: 0,
    product_index['581']: 0,
    product_index['582']: 0,
    product_index['583']: 0,
    product_index['584']: 0,
    product_index['585']: 0,
    product_index['586']: 0,
    product_index['587']: 0,
    product_index['588']: 0,
    product_index['589']: 0,
    product_index['590']: 0,
    product_index['591']: 0,
    product_index['592']: 0,
    product_index['593']: 0,
    product_index['594']: 0,
    product_index['595']: 0,
    product_index['596']: 0,
    product_index['597']: 0,
    product_index['598']: 0,
    product_index['599']: 0,
    product_index['600']: 0,
    product_index['601']: 0,
    product_index['602']: 0,
    product_index['603']: 0,
    product_index['604']: 0,
    product_index['605']: 0,
    product_index['606']: 0,
    product_index['607']: 0,
    product_index['608']: 0,
    product_index['609']: 0,
    product_index['610']: 0,
    product_index['611']: 0,
    product_index['612']: 0,
    product_index['613']: 0,
    product_index['614']: 0,
    product_index['615']: 0,
    product_index['616']: 0,
    product_index['617']: 0,
    product_index['618']: 0,
    product_index['619']: 0,
    product_index['620']: 0,
    product_index['621']: 0,
    product_index['622']: 0,
    product_index['623']: 0,
    product_index['624']: 0,
    product_index['625']: 0,
    product_index['626']: 0,
    product_index['627']: 0,
    product_index['628']: 0,
    product_index['629']: 0,
    product_index['630']: 0,
    product_index['631']: 0,
    product_index['632']: 0,
    product_index['633']: 0,
    product_index['634']: 0,
    product_index['635']: 0,
    product_index['636']: 0,
    product_index['637']: 0,
    product_index['638']: 0,
    product_index['639']: 0,
    product_index['640']: 0,
    product_index['641']: 0,
    product_index['642']: 0,
    product_index['643']: 0,
    product_index['644']: 0,
    product_index['645']: 0,
    product_index['646']: 0,
    product_index['647']: 0,
    product_index['648']: 0,
    product_index['649']: 0,
    product_index['650']: 0,
    product_index['651']: 0,
    product_index['652']: 0,
    product_index['653']: 0,
    product_index['654']: 0,
    product_index['655']: 0,
    product_index['656']: 0,
    product_index['657']: 0,
    product_index['658']: 0,
    product_index['659']: 0,
    product_index['660']: 0,
    product_index['661']: 0,
    product_index['662']: 0,
    product_index['663']: 0,
    product_index['664']: 0,
    product_index['665']: 0,
    product_index['666']: 0,
    product_index['667']: 0,
    product_index['668']: 0,
    product_index['669']: 0,
    product_index['670']: 0,
    product_index['671']: 0,
    product_index['672']: 0,
    product_index['673']: 0,
    product_index['674']: 0,
    product_index['675']: 0,
    product_index['676']: 0,
    product_index['677']: 0,
    product_index['678']: 0,
    product_index['679']: 0,
    product_index['680']: 0,
    product_index['681']: 0,
    product_index['682']: 0,
    product_index['683']: 0,
    product_index['684']: 0,
    product_index['685']: 0,
    product_index['686']: 0,
    product_index['687']: 0,
    product_index['688']: 0,
    product_index['689']: 0,
    product_index['690']: 0,
    product_index['691']: 0,
    product_index['692']: 0,
    product_index['693']: 0,
    product_index['694']: 0,
    product_index['695']: 0,
    product_index['696']: 0,
    product_index['697']: 0,
    product_index['698']: 0,
    product_index['699']: 0,
    product_index['700']: 0,
    product_index['701']: 0,
    product_index['702']: 0,
    product_index['703']: 0,
    product_index['704']: 0,
    product_index['705']: 0,
    product_index['706']: 0,
    product_index['707']: 0,
    product_index['708']: 0,
    product_index['709']: 0,
    product_index['710']: 0,
    product_index['711']: 0,
    product_index['712']: 0,
    product_index['713']: 0,
    product_index['714']: 0,
    product_index['715']: 0,
    product_index['716']: 0,
    product_index['717']: 0,
    product_index['718']: 0,
    product_index['719']: 0,
    product_index['720']: 0,
    product_index['721']: 0,
    product_index['722']: 0,
    product_index['723']: 0,
    product_index['724']: 0,
    product_index['725']: 0,
    product_index['726']: 0,
    product_index['727']: 0,
    product_index['728']: 0,
    product_index['729']: 0,
    product_index['730']: 0,
    product_index['731']: 0,
    product_index['732']: 0,
    product_index['733']: 0,
    product_index['734']: 0,
    product_index['735']: 0,
    product_index['736']: 0,
    product_index['737']: 0,
    product_index['738']: 0,
    product_index['739']: 0,
    product_index['740']: 0,
    product_index['741']: 0,
    product_index['742']: 0,
    product_index['743']: 0,
    product_index['744']: 0,
    product_index['745']: 0,
    product_index['746']: 0,
    product_index['747']: 0,
    product_index['748']: 0,
    product_index['749']: 0,
    product_index['750']: 0,
    product_index['751']: 0,
    product_index['752']: 0,
    product_index['753']: 0,
    product_index['754']: 0,
    product_index['755']: 0,
    product_index['756']: 0,
    product_index['757']: 0,
    product_index['758']: 0,
    product_index['759']: 0,
    product_index['760']: 0,
    product_index['761']: 0,
    product_index['762']: 0,
    product_index['763']: 0,
    product_index['764']: 0,
    product_index['765']: 0,
    product_index['766']: 0,
    product_index['767']: 0,
    product_index['768']: 0,
    product_index['769']: 0,
    product_index['770']: 0,
    product_index['771']: 0,
    product_index['772']: 0,
    product_index['773']: 0,
    product_index['774']: 0,
    product_index['775']: 0,
    product_index['776']: 0,
    product_index['777']: 0,
    product_index['778']: 0,
    product_index['779']: 0,
    product_index['780']: 0,
    product_index['781']: 0,
    product_index['782']: 0,
    product_index['783']: 0,
    product_index['784']: 0,
    product_index['785']: 0,
    product_index['786']: 0,
    product_index['787']: 0,
    product_index['788']: 0,
    product_index['789']: 0,
    product_index['790']: 0,
    product_index['791']: 0,
    product_index['792']: 0,
    product_index['793']: 0,
    product_index['794']: 0,
    product_index['795']: 0,
    product_index['796']: 0,
    product_index['797']: 0,
    product_index['798']: 0,
    product_index['799']: 0,
    product_index['800']: 0,
    product_index['801']: 0,
    product_index['802']: 0,
    product_index['803']: 0,
    product_index['804']: 0,
    product_index['805']: 0,
    product_index['806']: 0,
    product_index['807']: 0,
    product_index['808']: 0,
    product_index['809']: 0,
    product_index['810']: 0,
    product_index['811']: 0,
    product_index['812']: 0,
    product_index['813']: 0,
    product_index['814']: 0,
    product_index['815']: 0,
    product_index['816']: 0,
    product_index['817']: 0,
    product_index['818']: 0,
    product_index['819']: 0,
    product_index['820']: 0,
    product_index['821']: 0,
    product_index['822']: 0,
    product_index['823']: 0,
    product_index['824']: 0,
    product_index['825']: 0,
    product_index['826']: 0,
    product_index['827']: 0,
    product_index['828']: 0,
    product_index['829']: 0,
    product_index['830']: 0,
    product_index['831']: 0,
    product_index['832']: 0,
    product_index['833']: 0,
    product_index['834']: 0,
    product_index['835']: 0,
    product_index['836']: 0,
    product_index['837']: 0,
    product_index['838']: 0,
    product_index['839']: 0,
    product_index['840']: 0,
    product_index['841']: 0,
    product_index['842']: 0,
    product_index['843']: 0,
    product_index['844']: 0,
    product_index['845']: 0,
    product_index['846']: 0,
    product_index['847']: 0,
    product_index['848']: 0,
    product_index['849']: 0,
    product_index['850']: 0,
    product_index['851']: 0,
    product_index['852']: 0,
    product_index['853']: 0,
    product_index['854']: 0,
    product_index['855']: 0,
    product_index['856']: 0,
    product_index['857']: 0,
    product_index['858']: 0,
    product_index['859']: 0,
    product_index['860']: 0,
    product_index['861']: 0,
    product_index['862']: 0,
    product_index['863']: 0,
    product_index['864']: 0,
    product_index['865']: 0,
    product_index['866']: 0,
    product_index['867']: 0,
    product_index['868']: 0,
    product_index['869']: 0,
    product_index['870']: 0,
    product_index['871']: 0,
    product_index['872']: 0,
    product_index['873']: 0,
    product_index['874']: 0,
    product_index['875']: 0,
    product_index['876']: 0,
    product_index['877']: 0,
    product_index['878']: 0,
    product_index['879']: 0,
    product_index['880']: 0,
    product_index['881']: 0,
    product_index['882']: 0,
    product_index['883']: 0,
    product_index['884']: 0,
    product_index['885']: 0,
    product_index['886']: 0,
    product_index['887']: 0,
    product_index['888']: 0,
    product_index['889']: 0,
    product_index['890']: 0,
    product_index['891']: 0,
    product_index['892']: 0,
    product_index['893']: 0,
    product_index['894']: 0,
    product_index['895']: 0,
    product_index['896']: 0,
    product_index['897']: 0,
    product_index['898']: 0,
    product_index['899']: 0,
    product_index['900']: 0,
    product_index['901']: 0,
    product_index['902']: 0,
    product_index['903']: 0,
    product_index['904']: 0,
    product_index['905']: 0,
    product_index['906']: 0,
    product_index['907']: 0,
    product_index['908']: 0,
    product_index['909']: 0,
    product_index['910']: 0,
    product_index['911']: 0,
    product_index['912']: 0,
    product_index['913']: 0,
    product_index['914']: 0,
    product_index['915']: 0,
    product_index['916']: 0,
    product_index['917']: 0,
    product_index['918']: 0,
    product_index['919']: 0,
    product_index['920']: 0,
    product_index['921']: 0,
    product_index['922']: 0,
    product_index['923']: 0,
    product_index['924']: 0,
    product_index['925']: 0,
    product_index['926']: 0,
    product_index['927']: 0,
    product_index['928']: 0,
    product_index['929']: 0,
    product_index['930']: 0,
    product_index['931']: 0,
    product_index['932']: 0,
    product_index['933']: 0,
    product_index['934']: 0,
    product_index['935']: 0,
    product_index['936']: 0,
    product_index['937']: 0,
    product_index['938']: 0,
    product_index['939']: 0,
    product_index['940']: 0,
    product_index['941']: 0,
    product_index['942']: 0,
    product_index['943']: 0,
    product_index['944']: 0,
    product_index['945']: 0,
    product_index['946']: 0,
    product_index['947']: 0,
    product_index['948']: 0,
    product_index['949']: 0,
    product_index['950']: 0,
    product_index['951']: 0,
    product_index['952']: 0,
    product_index['953']: 0,
    product_index['954']: 0,
    product_index['955']: 0,
    product_index['956']: 0,
    product_index['957']: 0,
    product_index['958']: 0,
    product_index['959']: 0,
    product_index['960']: 0,
    product_index['961']: 0,
    product_index['962']: 0,
    product_index['963']: 0,
    product_index['964']: 0,
    product_index['965']: 0,
    product_index['966']: 0,
    product_index['967']: 0,
    product_index['968']: 0,
    product_index['969']: 0,
    product_index['970']: 0,
    product_index['971']: 0,
    product_index['972']: 0,
    product_index['973']: 0,
    product_index['974']: 0,
    product_index['975']: 0,
    product_index['976']: 0,
    product_index['977']: 0,
    product_index['978']: 0,
    product_index['979']: 0,
    product_index['980']: 0,
    product_index['981']: 0,
    product_index['982']: 0,
    product_index['983']: 0,
    product_index['984']: 0,
    product_index['985']: 0,
    product_index['986']: 0,
    product_index['987']: 0,
    product_index['988']: 0,
    product_index['989']: 0,
    product_index['990']: 0,
    product_index['991']: 0,
    product_index['992']: 0,
    product_index['993']: 0,
    product_index['994']: 0,
    product_index['995']: 0,
    product_index['996']: 0,
    product_index['997']: 0,
    product_index['998']: 0,
    product_index['999']: 0,
}
