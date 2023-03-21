// Generated from c:\Users\Work\OneDrive\Desktop\Sem IV\ELSD\DSL-Fractals\src\grammar_fractals.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class grammar_fractalsParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, STRING=28, DIGIT=29, LETTER=30, EQ=31, DOT=32, 
		COMMA=33, LBRACK=34, RBRACK=35, SPACE=36, UNDERSCORE=37, ESC=38;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_size_statement = 2, RULE_color_statement = 3, 
		RULE_angle_statement = 4, RULE_iterations_statement = 5, RULE_shape_statement = 6, 
		RULE_move_statement = 7, RULE_scale_statement = 8, RULE_rotate_statement = 9, 
		RULE_mirror_statement = 10, RULE_axis = 11, RULE_draw_statement = 12, 
		RULE_save_statement = 13, RULE_shape = 14, RULE_digit = 15, RULE_string = 16, 
		RULE_filename = 17, RULE_value = 18, RULE_char = 19;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "size_statement", "color_statement", "angle_statement", 
			"iterations_statement", "shape_statement", "move_statement", "scale_statement", 
			"rotate_statement", "mirror_statement", "axis", "draw_statement", "save_statement", 
			"shape", "digit", "string", "filename", "value", "char"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'size'", "'color'", "'angle'", "'iterations'", "'shape'", "'move'", 
			"'scale'", "'rotate'", "'mirror'", "'x'", "'y'", "'draw'", "'save'", 
			"'circle'", "'square'", "'triangle'", "'polygon'", "'0'", "'1'", "'2'", 
			"'3'", "'4'", "'5'", "'6'", "'7'", "'8'", "'9'", null, null, null, "'='", 
			"'.'", "','", "'['", "']'", "' '", "'_'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, "STRING", "DIGIT", "LETTER", "EQ", "DOT", "COMMA", 
			"LBRACK", "RBRACK", "SPACE", "UNDERSCORE", "ESC"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "grammar_fractals.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public grammar_fractalsParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public ProgramContext program() {
			return getRuleContext(ProgramContext.class,0);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			setState(44);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(40);
				statement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(41);
				statement();
				setState(42);
				program();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public Size_statementContext size_statement() {
			return getRuleContext(Size_statementContext.class,0);
		}
		public Color_statementContext color_statement() {
			return getRuleContext(Color_statementContext.class,0);
		}
		public Angle_statementContext angle_statement() {
			return getRuleContext(Angle_statementContext.class,0);
		}
		public Iterations_statementContext iterations_statement() {
			return getRuleContext(Iterations_statementContext.class,0);
		}
		public Shape_statementContext shape_statement() {
			return getRuleContext(Shape_statementContext.class,0);
		}
		public Move_statementContext move_statement() {
			return getRuleContext(Move_statementContext.class,0);
		}
		public Scale_statementContext scale_statement() {
			return getRuleContext(Scale_statementContext.class,0);
		}
		public Rotate_statementContext rotate_statement() {
			return getRuleContext(Rotate_statementContext.class,0);
		}
		public Mirror_statementContext mirror_statement() {
			return getRuleContext(Mirror_statementContext.class,0);
		}
		public Draw_statementContext draw_statement() {
			return getRuleContext(Draw_statementContext.class,0);
		}
		public Save_statementContext save_statement() {
			return getRuleContext(Save_statementContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(57);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				enterOuterAlt(_localctx, 1);
				{
				setState(46);
				size_statement();
				}
				break;
			case T__1:
				enterOuterAlt(_localctx, 2);
				{
				setState(47);
				color_statement();
				}
				break;
			case T__2:
				enterOuterAlt(_localctx, 3);
				{
				setState(48);
				angle_statement();
				}
				break;
			case T__3:
				enterOuterAlt(_localctx, 4);
				{
				setState(49);
				iterations_statement();
				}
				break;
			case T__4:
				enterOuterAlt(_localctx, 5);
				{
				setState(50);
				shape_statement();
				}
				break;
			case T__5:
				enterOuterAlt(_localctx, 6);
				{
				setState(51);
				move_statement();
				}
				break;
			case T__6:
				enterOuterAlt(_localctx, 7);
				{
				setState(52);
				scale_statement();
				}
				break;
			case T__7:
				enterOuterAlt(_localctx, 8);
				{
				setState(53);
				rotate_statement();
				}
				break;
			case T__8:
				enterOuterAlt(_localctx, 9);
				{
				setState(54);
				mirror_statement();
				}
				break;
			case T__11:
				enterOuterAlt(_localctx, 10);
				{
				setState(55);
				draw_statement();
				}
				break;
			case T__12:
				enterOuterAlt(_localctx, 11);
				{
				setState(56);
				save_statement();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Size_statementContext extends ParserRuleContext {
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public Size_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_size_statement; }
	}

	public final Size_statementContext size_statement() throws RecognitionException {
		Size_statementContext _localctx = new Size_statementContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_size_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			match(T__0);
			setState(60);
			value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Color_statementContext extends ParserRuleContext {
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public Color_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_color_statement; }
	}

	public final Color_statementContext color_statement() throws RecognitionException {
		Color_statementContext _localctx = new Color_statementContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_color_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(62);
			match(T__1);
			setState(63);
			value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Angle_statementContext extends ParserRuleContext {
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public Angle_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_angle_statement; }
	}

	public final Angle_statementContext angle_statement() throws RecognitionException {
		Angle_statementContext _localctx = new Angle_statementContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_angle_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(65);
			match(T__2);
			setState(66);
			value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Iterations_statementContext extends ParserRuleContext {
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public Iterations_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_iterations_statement; }
	}

	public final Iterations_statementContext iterations_statement() throws RecognitionException {
		Iterations_statementContext _localctx = new Iterations_statementContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_iterations_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			match(T__3);
			setState(69);
			value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Shape_statementContext extends ParserRuleContext {
		public ShapeContext shape() {
			return getRuleContext(ShapeContext.class,0);
		}
		public Shape_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_shape_statement; }
	}

	public final Shape_statementContext shape_statement() throws RecognitionException {
		Shape_statementContext _localctx = new Shape_statementContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_shape_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			match(T__4);
			setState(72);
			shape();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Move_statementContext extends ParserRuleContext {
		public List<ValueContext> value() {
			return getRuleContexts(ValueContext.class);
		}
		public ValueContext value(int i) {
			return getRuleContext(ValueContext.class,i);
		}
		public Move_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_move_statement; }
	}

	public final Move_statementContext move_statement() throws RecognitionException {
		Move_statementContext _localctx = new Move_statementContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_move_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(74);
			match(T__5);
			setState(75);
			value();
			setState(76);
			value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Scale_statementContext extends ParserRuleContext {
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public Scale_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scale_statement; }
	}

	public final Scale_statementContext scale_statement() throws RecognitionException {
		Scale_statementContext _localctx = new Scale_statementContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_scale_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(78);
			match(T__6);
			setState(79);
			value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Rotate_statementContext extends ParserRuleContext {
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public Rotate_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rotate_statement; }
	}

	public final Rotate_statementContext rotate_statement() throws RecognitionException {
		Rotate_statementContext _localctx = new Rotate_statementContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_rotate_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(81);
			match(T__7);
			setState(82);
			value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Mirror_statementContext extends ParserRuleContext {
		public AxisContext axis() {
			return getRuleContext(AxisContext.class,0);
		}
		public Mirror_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mirror_statement; }
	}

	public final Mirror_statementContext mirror_statement() throws RecognitionException {
		Mirror_statementContext _localctx = new Mirror_statementContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_mirror_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(84);
			match(T__8);
			setState(85);
			axis();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AxisContext extends ParserRuleContext {
		public AxisContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_axis; }
	}

	public final AxisContext axis() throws RecognitionException {
		AxisContext _localctx = new AxisContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_axis);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			_la = _input.LA(1);
			if ( !(_la==T__9 || _la==T__10) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Draw_statementContext extends ParserRuleContext {
		public Draw_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_draw_statement; }
	}

	public final Draw_statementContext draw_statement() throws RecognitionException {
		Draw_statementContext _localctx = new Draw_statementContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_draw_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(89);
			match(T__11);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Save_statementContext extends ParserRuleContext {
		public FilenameContext filename() {
			return getRuleContext(FilenameContext.class,0);
		}
		public Save_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_save_statement; }
	}

	public final Save_statementContext save_statement() throws RecognitionException {
		Save_statementContext _localctx = new Save_statementContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_save_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			match(T__12);
			setState(92);
			filename();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ShapeContext extends ParserRuleContext {
		public ShapeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_shape; }
	}

	public final ShapeContext shape() throws RecognitionException {
		ShapeContext _localctx = new ShapeContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_shape);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DigitContext extends ParserRuleContext {
		public DigitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_digit; }
	}

	public final DigitContext digit() throws RecognitionException {
		DigitContext _localctx = new DigitContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_digit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(96);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__17) | (1L << T__18) | (1L << T__19) | (1L << T__20) | (1L << T__21) | (1L << T__22) | (1L << T__23) | (1L << T__24) | (1L << T__25) | (1L << T__26))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StringContext extends ParserRuleContext {
		public CharContext char() {
			return getRuleContext(CharContext.class,0);
		}
		public StringContext string() {
			return getRuleContext(StringContext.class,0);
		}
		public StringContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_string; }
	}

	public final StringContext string() throws RecognitionException {
		StringContext _localctx = new StringContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_string);
		try {
			setState(102);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(98);
				char();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(99);
				char();
				setState(100);
				string();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FilenameContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(grammar_fractalsParser.STRING, 0); }
		public FilenameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_filename; }
	}

	public final FilenameContext filename() throws RecognitionException {
		FilenameContext _localctx = new FilenameContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_filename);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(104);
			match(STRING);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ValueContext extends ParserRuleContext {
		public List<TerminalNode> DIGIT() { return getTokens(grammar_fractalsParser.DIGIT); }
		public TerminalNode DIGIT(int i) {
			return getToken(grammar_fractalsParser.DIGIT, i);
		}
		public List<TerminalNode> STRING() { return getTokens(grammar_fractalsParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(grammar_fractalsParser.STRING, i);
		}
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_value);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(109);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(106);
					_la = _input.LA(1);
					if ( !(_la==STRING || _la==DIGIT) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
					} 
				}
				setState(111);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CharContext extends ParserRuleContext {
		public TerminalNode LETTER() { return getToken(grammar_fractalsParser.LETTER, 0); }
		public TerminalNode DIGIT() { return getToken(grammar_fractalsParser.DIGIT, 0); }
		public TerminalNode EQ() { return getToken(grammar_fractalsParser.EQ, 0); }
		public TerminalNode DOT() { return getToken(grammar_fractalsParser.DOT, 0); }
		public TerminalNode COMMA() { return getToken(grammar_fractalsParser.COMMA, 0); }
		public TerminalNode LBRACK() { return getToken(grammar_fractalsParser.LBRACK, 0); }
		public TerminalNode RBRACK() { return getToken(grammar_fractalsParser.RBRACK, 0); }
		public TerminalNode SPACE() { return getToken(grammar_fractalsParser.SPACE, 0); }
		public TerminalNode UNDERSCORE() { return getToken(grammar_fractalsParser.UNDERSCORE, 0); }
		public CharContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_char; }
	}

	public final CharContext char() throws RecognitionException {
		CharContext _localctx = new CharContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_char);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(112);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << DIGIT) | (1L << LETTER) | (1L << EQ) | (1L << DOT) | (1L << COMMA) | (1L << LBRACK) | (1L << RBRACK) | (1L << SPACE) | (1L << UNDERSCORE))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3(u\4\2\t\2\4\3\t\3"+
		"\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f"+
		"\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t"+
		"\23\4\24\t\24\4\25\t\25\3\2\3\2\3\2\3\2\5\2/\n\2\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\5\3<\n\3\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3"+
		"\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\f"+
		"\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22"+
		"\3\22\3\22\5\22i\n\22\3\23\3\23\3\24\7\24n\n\24\f\24\16\24q\13\24\3\25"+
		"\3\25\3\25\2\2\26\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(\2\7\3\2"+
		"\f\r\3\2\20\23\3\2\24\35\3\2\36\37\3\2\37\'\2m\2.\3\2\2\2\4;\3\2\2\2\6"+
		"=\3\2\2\2\b@\3\2\2\2\nC\3\2\2\2\fF\3\2\2\2\16I\3\2\2\2\20L\3\2\2\2\22"+
		"P\3\2\2\2\24S\3\2\2\2\26V\3\2\2\2\30Y\3\2\2\2\32[\3\2\2\2\34]\3\2\2\2"+
		"\36`\3\2\2\2 b\3\2\2\2\"h\3\2\2\2$j\3\2\2\2&o\3\2\2\2(r\3\2\2\2*/\5\4"+
		"\3\2+,\5\4\3\2,-\5\2\2\2-/\3\2\2\2.*\3\2\2\2.+\3\2\2\2/\3\3\2\2\2\60<"+
		"\5\6\4\2\61<\5\b\5\2\62<\5\n\6\2\63<\5\f\7\2\64<\5\16\b\2\65<\5\20\t\2"+
		"\66<\5\22\n\2\67<\5\24\13\28<\5\26\f\29<\5\32\16\2:<\5\34\17\2;\60\3\2"+
		"\2\2;\61\3\2\2\2;\62\3\2\2\2;\63\3\2\2\2;\64\3\2\2\2;\65\3\2\2\2;\66\3"+
		"\2\2\2;\67\3\2\2\2;8\3\2\2\2;9\3\2\2\2;:\3\2\2\2<\5\3\2\2\2=>\7\3\2\2"+
		">?\5&\24\2?\7\3\2\2\2@A\7\4\2\2AB\5&\24\2B\t\3\2\2\2CD\7\5\2\2DE\5&\24"+
		"\2E\13\3\2\2\2FG\7\6\2\2GH\5&\24\2H\r\3\2\2\2IJ\7\7\2\2JK\5\36\20\2K\17"+
		"\3\2\2\2LM\7\b\2\2MN\5&\24\2NO\5&\24\2O\21\3\2\2\2PQ\7\t\2\2QR\5&\24\2"+
		"R\23\3\2\2\2ST\7\n\2\2TU\5&\24\2U\25\3\2\2\2VW\7\13\2\2WX\5\30\r\2X\27"+
		"\3\2\2\2YZ\t\2\2\2Z\31\3\2\2\2[\\\7\16\2\2\\\33\3\2\2\2]^\7\17\2\2^_\5"+
		"$\23\2_\35\3\2\2\2`a\t\3\2\2a\37\3\2\2\2bc\t\4\2\2c!\3\2\2\2di\5(\25\2"+
		"ef\5(\25\2fg\5\"\22\2gi\3\2\2\2hd\3\2\2\2he\3\2\2\2i#\3\2\2\2jk\7\36\2"+
		"\2k%\3\2\2\2ln\t\5\2\2ml\3\2\2\2nq\3\2\2\2om\3\2\2\2op\3\2\2\2p\'\3\2"+
		"\2\2qo\3\2\2\2rs\t\6\2\2s)\3\2\2\2\6.;ho";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}